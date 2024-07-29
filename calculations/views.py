from django.shortcuts import render
from .forms import CalculationForm
import math
import plotly.graph_objs as go
import plotly.offline as opy

def calculate_view(request):
    result = None
    graph = None
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            Q1 = form.cleaned_data['Q1']
            Q2 = form.cleaned_data['Q2']
            Q3 = form.cleaned_data['Q3']
            Q4 = form.cleaned_data['Q4']
            Q5 = form.cleaned_data['Q5']
            Q6 = form.cleaned_data['Q6']
            Q7 = form.cleaned_data['Q7']
            Q8 = form.cleaned_data['Q8']
            Q9 = form.cleaned_data['Q9']
            Q10 = form.cleaned_data['Q10']
            Q11 = form.cleaned_data['Q11']

            # 現行の値
            current_measurement_interval = Q9
            current_adjustment_limit = Q11
            current_adjustment_interval = Q10

            # 最適の値の計算
            optimal_measurement_interval = round(math.sqrt((2 * Q10 * Q5) / Q4) * (Q3 / Q11), 2)
            optimal_adjustment_limit = round(((3 * Q6 / Q4) * (Q11**2 / Q10) * Q3**2)**(1/4), 2)
            optimal_adjustment_interval = round(Q10 * (optimal_adjustment_limit**2 / Q11**2), 2)

            # 現行のコスト計算
            current_measurement_cost = round(Q5 / current_measurement_interval, 2)
            current_adjustment_cost = round(Q6 / current_adjustment_interval, 2)
            current_loss_within_limit = round((Q4 / Q3**2) * (current_adjustment_limit**2 / 3), 2)
            current_loss_beyond_limit = round((Q4 / Q3**2) * ((current_measurement_interval + 1) / 2 + Q7) * (current_adjustment_limit**2 / current_adjustment_interval), 2)
            current_measurement_error = round((Q4 / Q3**2) * Q8, 2)
            current_total_cost = round(current_measurement_cost + current_adjustment_cost + current_loss_within_limit + current_loss_beyond_limit + current_measurement_error, 2)

            # 最適のコスト計算
            optimal_measurement_cost = round(Q5 / optimal_measurement_interval, 2)
            optimal_adjustment_cost = round(Q6 / optimal_adjustment_interval, 2)
            optimal_loss_within_limit = round((Q4 / Q3**2) * (optimal_adjustment_limit**2 / 3), 2)
            optimal_loss_beyond_limit = round((Q4 / Q3**2) * ((optimal_measurement_interval + 1) / 2 + Q7) * (optimal_adjustment_limit**2 / optimal_adjustment_interval), 2)
            optimal_measurement_error = round((Q4 / Q3**2) * Q8, 2)
            optimal_total_cost = round(optimal_measurement_cost + optimal_adjustment_cost + optimal_loss_within_limit + optimal_loss_beyond_limit + optimal_measurement_error, 2)

            result = {
                'current_measurement_interval': f"{current_measurement_interval} {Q2}",
                'current_adjustment_limit': f"{current_adjustment_limit} {Q1}",
                'current_adjustment_interval': f"{current_adjustment_interval} {Q2}",
                'optimal_measurement_interval': f"{optimal_measurement_interval} {Q2}",
                'optimal_adjustment_limit': f"{optimal_adjustment_limit} {Q1}",
                'optimal_adjustment_interval': f"{optimal_adjustment_interval} {Q2}",
                'current_measurement_cost': current_measurement_cost,
                'current_adjustment_cost': current_adjustment_cost,
                'current_loss_within_limit': current_loss_within_limit,
                'current_loss_beyond_limit': current_loss_beyond_limit,
                'current_measurement_error': current_measurement_error,
                'current_total_cost': current_total_cost,
                'optimal_measurement_cost': optimal_measurement_cost,
                'optimal_adjustment_cost': optimal_adjustment_cost,
                'optimal_loss_within_limit': optimal_loss_within_limit,
                'optimal_loss_beyond_limit': optimal_loss_beyond_limit,
                'optimal_measurement_error': optimal_measurement_error,
                'optimal_total_cost': optimal_total_cost,
            }

            # グラフの作成
            categories = ['計測コスト', '調整コスト', '調整限界内損失', '調整限界外損失', '計測誤差', '総損失コスト']
            current_values = [current_measurement_cost, current_adjustment_cost, current_loss_within_limit, current_loss_beyond_limit, current_measurement_error, current_total_cost]
            optimal_values = [optimal_measurement_cost, optimal_adjustment_cost, optimal_loss_within_limit, optimal_loss_beyond_limit, optimal_measurement_error, optimal_total_cost]

            fig = go.Figure(data=[
                go.Bar(name='現行', x=categories, y=current_values),
                go.Bar(name='最適', x=categories, y=optimal_values)
            ])
            fig.update_layout(barmode='group', title='現行 vs 最適 損失コスト比較', xaxis_title='要素', yaxis_title='損失コスト [円]')

            graph = opy.plot(fig, auto_open=False, output_type='div')

    else:
        form = CalculationForm()
    
    return render(request, 'calculate.html', {'form': form, 'result': result, 'graph': graph})
