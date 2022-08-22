import hoshino
from hoshino import Service, priv
from hoshino.typing import CQEvent

sv = Service('E7分数', manage_priv=priv.SUPERUSER, help_='请输入:分数 属性名 属性数值 属性名 属性数值 属性名 属性数值 属性名 属性数值\n例:分数 爆伤 1 暴击 2 生命 3 攻击 4')

@sv.on_prefix('分数')
async def feedback(bot, ev: CQEvent):
    code = ev.raw_message
    code = code.replace('%','')
    qiege = code.split()
    tx = 0
    shuchu=0

    if len(qiege)>9 or len(qiege)%2 == 0:
        tixing="您的指令输入的有问题,请检查后输入\n格式为:分数 爆伤 1 暴击 2 生命 3 攻击 4"
        await bot.send(ev, tixing)
        return

#无限套娃的开始
    if len(qiege) == 9:
        score1 = float(qiege[2]) #第一个数据
        score2 = float(qiege[4]) #第二个数据
        score3 = float(qiege[6]) #第三个数据
        score4 = float(qiege[8]) #第四个数据
        name1 = str(qiege[1])  # 第一个数据名
        name2 = str(qiege[3])  # 第二个数据名
        name3 = str(qiege[5])  # 第三个数据名
        name4 = str(qiege[7])  # 第四个数据名
        #判断数据名格式
        if len(name1) != 2 or len(name2) != 2 or len(name3) != 2 or len(name4) != 2:
            tx = 1
            return
#寻找暴击
        if name1 == "暴击":
            score1 = score1 * 1.5
        elif name2 == "暴击":
            score2 = score2 * 1.5
        elif name3 == "暴击":
            score3 = score3 * 1.5
        elif name4 == "暴击":
            score4 = score4 * 1.5

#寻找爆伤
        if name1 == "爆伤":
            score1 = score1 * 1.125
        elif name2 == "爆伤":
            score2 = score2 * 1.125
        elif name3 == "爆伤":
            score3 = score3 * 1.125
        elif name4 == "爆伤":
            score4 = score4 * 1.125

#寻找速度
        if name1 == "速度":
            score1 = score1 * 2
        elif name2 == "速度":
            score2 = score2 * 2
        elif name3 == "速度":
            score3 = score3 * 2
        elif name4 == "速度":
            score4 = score4 * 2

        scorehe = score1 + score2 + score3 + score4
        shuchu = f'您这件装备的分数为:\n{name1}:{score1}分\n{name2}:{score2}分\n{name3}:{score3}分\n{name4}:{score4}分\n总分为 {scorehe}分.'

#无限套娃2
    if len(qiege) == 7:
        score1 = float(qiege[2]) #第一个数据
        score2 = float(qiege[4]) #第二个数据
        score3 = float(qiege[6]) #第三个数据
        name1 = str(qiege[1])  # 第一个数据名
        name2 = str(qiege[3])  # 第二个数据名
        name3 = str(qiege[5])  # 第三个数据名

        #判断数据名格式
        if len(name1) != 2 or len(name2) != 2 or len(name3) != 2:
            tx = 1
            return
#寻找暴击
        if name1 == "暴击":
            score1 = score1 * 1.5
        elif name2 == "暴击":
            score2 = score2 * 1.5
        elif name3 == "暴击":
            score3 = score3 * 1.5

#寻找爆伤
        if name1 == "爆伤":
            score1 = score1 * 1.125
        elif name2 == "爆伤":
            score2 = score2 * 1.125
        elif name3 == "爆伤":
            score3 = score3 * 1.125

#寻找速度
        if name1 == "速度":
            score1 = score1 * 2
        elif name2 == "速度":
            score2 = score2 * 2
        elif name3 == "速度":
            score3 = score3 * 2

        scorehe = score1 + score2 + score3
        shuchu = f'您这件装备的分数为:\n{name1}:{score1}分\n{name2}:{score2}分\n{name3}:{score3}分\n总分为 {scorehe}分.'


#无限套娃2
    if len(qiege) == 5:
        score1 = float(qiege[2]) #第一个数据
        score2 = float(qiege[4]) #第二个数据
        name1 = str(qiege[1])  # 第一个数据名
        name2 = str(qiege[3])  # 第二个数据名


        #判断数据名格式
        if len(name1) != 2 or len(name2) != 2:
            tx = 1
            return
#寻找暴击
        if name1 == "暴击":
            score1 = score1 * 1.5
        elif name2 == "暴击":
            score2 = score2 * 1.5

#寻找爆伤
        if name1 == "爆伤":
            score1 = score1 * 1.125
        elif name2 == "爆伤":
            score2 = score2 * 1.125

#寻找速度
        if name1 == "速度":
            score1 = score1 * 2
        elif name2 == "速度":
            score2 = score2 * 2

        scorehe = score1 + score2
        shuchu = f'您这件装备的分数为:\n{name1}:{score1}分\n{name2}:{score2}分\n总分为 {scorehe}分.'


#无限套娃2
    if len(qiege) == 3:
        score1 = float(qiege[2]) #第一个数据
        name1 = str(qiege[1])  # 第一个数据名

        #判断数据名格式
        if len(name1) != 2:
            tx = 1
            return
#寻找暴击
        if name1 == "暴击":
            score1 = score1 * 1.5

#寻找爆伤
        if name1 == "爆伤":
            score1 = score1 * 1.125

#寻找速度
        if name1 == "速度":
            score1 = score1 * 2

        scorehe = score1
        shuchu = f'您这件装备的分数为:\n{name1}:{score1}分\n总分为 {scorehe}分.'

    if tx == 1:
        tixing = "您输入的数据名称有问题,请检查后重新输入\n提醒:暴击伤害输入爆伤,暴击率输入暴击"
        await bot.send(ev, tixing)
        return
    else:
        await bot.send(ev, shuchu)



