#!/usr/bin/python
#-*-coding:utf-8-*-


from trees import *
from treePlotter import start_plot

def main1():
    '''
    构造收据并计算香农熵
    '''
    myDat, labels = createDataSet()
    print myDat
    print calcShannonEnt(myDat)
    myDat[0][-1] = 'maybe'
    print calcShannonEnt(myDat)
    

def main2():
    '''
    划分数据集
    '''
    myDat, labels = createDataSet()
    print splitDataSet(myDat, 0, 0)
    
def main3():
    '''
    选择最好的划分方式
    '''
    myDat, labels = createDataSet()
    print chooseBestFeatureToSplit(myDat)
    
def main4():
    '''
    构建决策树并打印
    观察生成树的结构
    '''
    myDat, labels = createDataSet()
    myTree = createTree(myDat, labels)
    print myTree
    
def main5():
    '''
    根据生成的决策树绘图显示
    工具：matplot
    '''
    start_plot()
    
def main6():
    '''
    执行决策树进行分类
    '''
    myDat, labels = createDataSet()
    myTree = createTree(myDat, labels)
    print classify(myTree, labels, [1,0])
    print classify(myTree, labels, [1,1])
    
def main7():
    '''
    生成决策树并存储为.txt
    从.txt文件导入决策树
    '''
    import treePlotter
    myDat, labels = createDataSet()
    myTree = treePlotter.retrieveTree (0)
    print classify(myTree, labels, [1,0])
    storeTree(myTree, 'classifierStorage.txt')
    print grabTree('classifierStorage.txt')
    
    
if __name__ == "__main__":
    main5()