# -*- coding: utf-8 -*-
def move(n,a='A',b='B',c='C'):

    #如果n=1,直接a到c

    if n == 1:

        print(a, '-->', c)

    #n＞1,视为1个最大的圆盘和剩余n-1个圆盘当一个整体移动,

    #那n-1个移到b,最大那个移到c,即可实现递归

    else:

        move(n-1,a,c,b)#n-1个以整体移到b

        print(a,'-->',c)#剩下那个最大的移到c

        move(n-1,b,a,c)#n-1个变成新的问题:如何将n-1个从b移到c.(递归即可)