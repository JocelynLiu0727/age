driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit   #程式終止
age = input('請問您的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了!')
	else:
		print('奇怪 你怎麼會開過車???')
elif driving == '沒有':
	if age >= 18:
		print('可以考駕照囉!')
	else: 
		print('很好，18歲就可以考駕照了!')
else:
	print('只能輸入 有/沒有')