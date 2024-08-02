from django import forms

class CalculationForm(forms.Form):
    Q1 = forms.CharField(label='測定単位を記入してください。', max_length=100)
    Q2 = forms.CharField(label='製品あるいは部品の数量の単位を記入してください。', max_length=100)
    Q3 = forms.FloatField(label='許容差を目標値からの差として記入して下さい。（両側公差の場合は厳しいほうを記入）')
    Q4 = forms.FloatField(label='不合格になったときに発生する単位数あたりの損失額[円]を記入して下さい。')
    Q5 = forms.FloatField(label='１回の計測にかかる平均コスト[円]を記入して下さい。')
    Q6 = forms.FloatField(label='１回の調整にかかる平均コスト[円]を記入して下さい。')
    Q7 = forms.FloatField(label='計測をしている間にいくつの単位数（何個，何枚など）の品物が流れてしまうかを記入して下さい。')
    Q8 = forms.FloatField(label='計測誤差を標準偏差で記入してください。')
    Q9 = forms.FloatField(label='平均して単位数として何個（枚）ごとにチェックのための計測がなされているか記入して下さい。')
    Q10 = forms.FloatField(label='平均して単位数として何個（枚）ごとに調整が入っているか記入して下さい。')
    Q11 = forms.FloatField(label='工程での調整限界を記入してください。')


    # 新しい診断コスト計算用のフォーム
class DiagnosticForm(forms.Form):
    Q1 = forms.FloatField(label='単位生産量', min_value=0)
    Q2 = forms.FloatField(label='異常時の損失額', min_value=0)
    Q3 = forms.FloatField(label='診断コスト', min_value=0)
    Q4 = forms.FloatField(label='工程調整損失', min_value=0)
    Q5 = forms.FloatField(label='異常時の生産数', min_value=0)
    Q6 = forms.FloatField(label='診断間隔', min_value=0)
    Q7 = forms.FloatField(label='平均故障間隔', min_value=0)
