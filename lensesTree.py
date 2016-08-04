#!/usr/bin/python
#-*-coding:utf-8-*-

import trees
import treePlotter

def main():
    '''
    使用决策树对话者需要佩戴的隐形眼镜类型进行预测
    隐形眼镜的类型包括硬材质、软材质以及不适合佩戴隐形眼镜
    '''
    fr = open('lenses.txt')
    lenses = [linst.strip().split('\t') for linst in fr.readlines()]
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    lensesTree = trees.createTree(lenses, lensesLabels)
    print lensesTree
    treePlotter.createPlot(lensesTree)

if __name__ == "__main__":
    main()
