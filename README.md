# design-patterns-practice
my design patterns practices

## Creational Patterns

### [Abstract Factory](creational-patterns/abstract_factory.py)
- 有一個類別負責執行類別的介面方法，未來每新增一個類別只要記得實作該介面方法就好。雖然可以運用繼承關係來定義介面，但看起來古今中外累積的經驗告訴我們： ***Favor object composition over inheritance***

### [Singleton](creational-patterns/singleton.py)
- 有時候我們的application對於某一個類別僅需要唯一一個實體，且有時候以lazy mode(需要時)才去生成他。例如連接database，提供唯一的進入點給apllication。 ***Ensure a class only has one instance, and provide a global point of access to it.***
- 各種實作singleton的方法
    - [stackoverflow討論](https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python)
    - [繼承type及運用__call__來達成](https://sourcemaking.com/design_patterns/singleton/python/1)
- [__init__與__call__的差異](https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call-in-python)
    - __init__只能用在初始化時，但有時我們可能想要重新定義此物件
- what is metaclass?
    - 從object與type對照講起，告訴你object背後運作的機制其實是type，若你也想要創造自己的metaclass就用type...太多了看不完 [stackoverflow](https://stackoverflow.com/a/6581949/8694937)
- 先記得我們有方法可以創造singleton class就好



## Structural Patterns

## Behavioral Patterns

## Design for Testability Patterns

## Fundamental Patterns

## Others


# reference
- [github.com/faif/python-patterns](https://github.com/faif/python-patterns)
- https://www.toptal.com/python/python-design-patterns
- https://sourcemaking.com/design_patterns