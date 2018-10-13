# design-patterns-practice
My design patterns practices and notes

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
### [Builder](creational-patterns/builder.py)
- 有時候某些類別的constructor很不靠普，不如另外寫一個class或function去執行它的construction process，如此一般就能重複利用此過程來建造類似功能的class
- 例如，此例中Building的__init__可能不好用，所以當有一個ComplexBuilding的介面及ComplexHouse的類別，有更複雜的建造過程，另外用一個function來執行它，同時也要符合原本Building的interface
- 另外[sourcemaking](https://sourcemaking.com/design_patterns/builder/python/1)的例子中，則是想像成有一個執行者(Director)負責統一執行construction的過程、執行Builder的interfaces，最後再交由Builder class遞交product
- 在[tutorial point](https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_builder.htm)的例子裡，一樣是由Director負責執行建造的過程，而builder另外透過function給予。概念與sourcemaking相同，但譬喻更完整一點

## Structural Patterns

## Behavioral Patterns

## Design for Testability Patterns

## Fundamental Patterns

## Others


# reference
- [github.com/faif/python-patterns](https://github.com/faif/python-patterns)
- [sourcemaking](https://sourcemaking.com/design_patterns)
- [tutorial point](https://www.tutorialspoint.com/python_design_patterns/index.htm)
- https://www.toptal.com/python/python-design-patterns
