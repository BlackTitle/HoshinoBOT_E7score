import random
import hoshino
from hoshino import Service, priv
from hoshino.typing import CQEvent


sv = Service('E7分数', manage_priv=priv.SUPERUSER, help_='请输入：分数 名1 值1 名2 值2 名3 值3 名4 值4\n如：分数 攻击 1 攻击 2 攻击 3 攻击 4\n')

@sv.on_prefix('分数')
async def feedback(bot, ev: CQEvent):
    vaule = ev.raw_message
    ge = vaule.split()
    #不知道为什么总是出错误，搞个字典设置禁止
    ciku = ['生命','防御','攻击','暴击','爆伤','速度','命中','抗性','分数']
    #各类总分
    atk = 0
    rou = 0
    ob = 0
    score = 0

    #适用人群 这一块不知道该咋写了 等有机会再写吧XD
    #大概的思路就是结合某几种的分 去计算适合哪个角色   比如生命+暴击+爆伤>x 那就是适合暗萝 就输出banrou=1
    banrou = 0 #半肉 暗萝等
    huotui = 0 #特指火腿
    tongc = 0 #普通c 比如暗法？
    tongob = 0 #普通辅助 比如光ll
    tongrou = 0 #普通肉 拉斯 暗盾等

    #整几句骚话
    laji = ['你这装备垃圾桶捡来的？', '这么点分...你尽力了', '在某种层面上讲,兄弟你很欧洲'] #总分<50
    yiban  = ['中规中矩,还算不错', '一人之下,万人之上的利器', '不是KFC疯狂星期四出来的鸡腿一般的普通'] #70 > 总分 >50
    niubi = ['尚方宝剑,先斩后奏。男中龙，女中风。', '传说是由女娲石打造而成的利器...', '牛逼']
    wudi = ['无敌'] #>70

    #杂项
    jiancha = 0


    for i in range(0, len(ge)):
        if len(ge[i]) == 2 and i % 2 != 0 or len(ge[i]) == 2 and i == 0 :
            jiancha = jiancha + 1
    #检查词条数量
    if len(ge) % 2 == 0:
        cuowu = '指令格式有误.\n指令例:分数 攻击 1 攻击 2 攻击 3 攻击 4'
        await bot.send(ev, cuowu)
        return
    #检查格式防止出现错误
    elif jiancha / 2 == 0 :
        cuowu = '指令格式有误。\n暴击伤害→爆伤、暴击率→暴击、效果命中→命中、效果抗性→抗性\n攻击、防御、生命如是百分比请在前面加"." 如:生命 .12'
        await bot.send(ev, cuowu)
        return
    else:
    #开始循环
        for i in range(0, len(ge)):
            #判断是否为百分比
            if '.' in ge[i]:
                ge[i] = ge[i].replace('.', '')

            #计算
            elif '%' not in ge[i] and ge[i] not in ciku:
                if ge[i-1] == "攻击":
                    ge[i] = round(float(ge[i]) /  11.27 , 2)
                elif ge[i-1] == "防御":
                    ge[i] = round(float(ge[i]) / 6.21 , 2)
                elif ge[i-1] == "生命":
                    ge[i] = round(float(ge[i]) / 56.31 , 2)

            #计算百分比特殊数值
            if ge[i-1] == "暴击":
                ge[i] = float(ge[i])  * 1.5
            elif ge[i-1] == "爆伤":
                ge[i] = float(ge[i])  * 1.125
            elif ge[i-1] == "速度":
                ge[i] = float(ge[i])  * 2

            #计算合体分值
            if ge[i-1] == "攻击" or ge[i-1] == "速度" or ge[i-1] == "暴击" or ge[i-1] == "爆伤" and ge[i] not in ciku :
                atk = atk + float(ge[i])
            if ge[i-1] == "生命" or ge[i-1] == "速度" or ge[i-1] == "防御" and ge[i] not in ciku:
                rou = rou + float(ge[i])
            if ge[i - 1] == "生命" or ge[i - 1] == "速度" or ge[i - 1] == "命中" or ge[i - 1] == "抗性" and ge[i] not in ciku:
                ob = ob + float(ge[i])

            #总分
            if ge[i] not in ciku:
                score = score + float(ge[i])

        #判断总分
        if score < 50:
            talk4 = random.choice(laji)
        elif score < 70:
            talk4 = random.choice(yiban)
        elif score < 80:
            talk4 = random.choice(niubi)
        elif score < 999999:
            talk4 = random.choice(wudi)


        #打印
        talk1 = f'您的这件装备分数为\n'
        if len(ge) == 9:
            talk2 = f'{ge[1]}:{ge[2]}分\n{ge[3]}:{ge[4]}分\n{ge[5]}:{ge[6]}分\n{ge[7]}:{ge[8]}分\n'
        elif len(ge) == 7:
            talk2 = f'{ge[1]}:{ge[2]}分\n{ge[3]}:{ge[4]}分\n{ge[5]}:{ge[6]}分\n'
        elif len(ge) == 5:
            talk2 = f'{ge[1]}:{ge[2]}分\n{ge[3]}:{ge[4]}分\n'
        elif len(ge) == 3:
            talk2 = f'{ge[1]}:{ge[2]}分\n'

        talk3 = f'攻击分为{atk}分,\n防御分为{rou}分,\n辅助分为{ob}分,\n总分为{score}分.\n'
        talk = f'{talk1}{talk2}{talk3}一眼丁真:{talk4}'

    await bot.send(ev, talk)


