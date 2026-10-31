'''mermaid 
flowchart TD
    Start ([Начало]) --› InputQ[/Ввод Q* и W/]
    Input --> CheckValid{Qx в 0. 1000И W в 0..100?)
    CheckValid -- Het →> Inpute
    CheckValid - Да --› CalcVol[Расчёт объёма нефти: Он = Q* * 1 - w/100]
    CalcVol --› CalcMass [Расчёт массы нефти: Мн - н * 850 / 1000]
    CalMass --> Cond1{Mн < M_min?)
    Cond1 -- Да -→› Status1[Статус: Убыточна - стоп]
    Cond1 -- Het --> Cond2(Mн < 3 * M_min?)
    Cond2 - - Да --› Status2[Статус: Рентабельна - база]
    Cond2 -- Нет --› Status3[Статус: Высокодебитная - приоритет)
   Status1 --> Output[/Вывод: Он, Мн, Статус/1
   Status --> Output
   Status3 --› Output
   Output --> End([Конец])
'''
