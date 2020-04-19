def input_work():
    work = []
    work_name = str(input('作業名を入力してください'))
    work_time = int(input('作業時間を入力してください'))
    work.append(work_name)
    work.append(work_time)
    return work

def push_estimate(work):
    estimate.append(work)

def check_continue(flg):
    if(flg == 'y'):
        work = input_work()
        push_estimate(work)
        check_continue(input('まだ作業はありますか？[y/n]'))
    elif(flg == 'n'):
        print('見積もった作業は以下の通りです')
        total = 0
        for work in estimate:
            print('作業名:{}\n工数:{}h'.format(work[0], work[1]))
            total += work[1]
        print('\n総工数:{}h'.format(total))
    else:
        raise ValueError

try:
    estimate = []
    work = input_work()
    push_estimate(work)
    print('作業名:{}\n工数:{}h'.format(work[0], work[1]))
    check_continue(input('まだ作業はありますか？[y/n]'))
except(ValueError):
    print('予期せぬ値が入力されました')