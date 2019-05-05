# design-patterns-practice
My design patterns practices and notes

## Creational Patterns

### [Abstract Factory](creational-patterns/abstract_factory.py)
有一個類別負責執行類別的介面方法，未來每新增一個類別只要記得實作該介面方法就好。雖然可以運用繼承關係來定義介面，但看起來古今中外累積的經驗告訴我們： ***Favor object composition over inheritance***

### [Singleton](creational-patterns/singleton.py)
有時候我們的application對於某一個類別僅需要唯一一個實體，且有時候以lazy mode(需要時)才去生成他。例如連接database，提供唯一的進入點給apllication。 ***Ensure a class only has one instance, and provide a global point of access to it.***
- 各種實作singleton的方法
    - [stackoverflow討論](https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python)
    - [繼承type及運用__call__來達成](https://sourcemaking.com/design_patterns/singleton/python/1)
- [__init__與__call__的差異](https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call-in-python)
    - __init__只能用在初始化時，但有時我們可能想要重新定義此物件
- what is metaclass?
    - 從object與type對照講起，告訴你object背後運作的機制其實是type，若你也想要創造自己的metaclass就用type...太多了看不完 [stackoverflow](https://stackoverflow.com/a/6581949/8694937)
- 先記得我們有方法可以創造singleton class就好
### [Builder](creational-patterns/builder.py)
有時候某些類別的constructor很不靠普，不如另外寫一個class或function去執行它的construction process，如此一般就能重複利用此過程來建造類似功能的class。

例如，此例中Building的__init__可能不好用，所以當有一個ComplexBuilding的介面及ComplexHouse的類別，有更複雜的建造過程，另外用一個function來執行它，同時也要符合原本Building的interface
- 另外[sourcemaking](https://sourcemaking.com/design_patterns/builder/python/1)的例子中，則是想像成有一個執行者(Director)負責統一執行construction的過程、執行Builder的interfaces，最後再交由Builder class遞交product
- 在[tutorial point](https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_builder.htm)的例子裡，一樣是由Director負責執行建造的過程，而builder另外透過function給予。概念與sourcemaking相同，但譬喻更完整一點
### [Factory Method](creational-patterns/factory_method.py)
由一個類別或方法負責創立實體，該類別或方法中會有一個dictionary提供"類別名稱"(str)及class object的映射表，呼叫該類別或方法時給予欲產生的類別的名稱，該類別或方法即回傳該類別的實體
- 未來新增類別時要記得實作應有的interface
- [sourcemaking](https://sourcemaking.com/design_patterns/factory_method/python/1)的例子有點繞，上述的"映射表"變成另一組Creator類別家族，負責創建他們時，也產生相對應的product class為其屬性(`self.product = self._factory_method()`)，並在呼叫Creator.some_operation()時能使用到該product的interface()
### [Object Pool](creational-patterns/object_pool.py)
一個簡單的概念demo，由一個class將你要用的資源預先初始化並持有，接著提供獲取及回收的interfaces給外部取用/回收

#### ***Object Pool in practical***: [ThreadPool](complex-practice/thread_pool.py)
將 *`thread.py`* 中的 *`ThreadPoolExecutor`* 及相關的class看完，取出必要的部分，練習寫一個能夠將job submit到背景、且由另外一條thread執行的code snippets

*`ThreadPoolExecutor`* 的作法是lazy instantiation，若thread pool還沒滿則create一條new thread，create出來之後讓該thread執行一個做while loop的function，該while loop不斷地從work queue中試圖取出item並執行。關鍵在於，python的queue class在get item時指定`block=True`，則會等待直到有item為止，避免此while loop不斷的運作造成CPU資源消耗
- 另外精闢的解釋[link](https://www.metachris.com/2016/04/python-threadpool/)，試圖解釋ThreadPoolExecutor()怎麼做的。但他的作法是事先create threads出來
- 一個 *`flask`* 與 *`ThreadPoolExecutor`* 搭配的[demo](https://gist.github.com/arshpreetsingh/006f4fafc7e20e94ad5be99b830a08c7)，或另參考[service.py](complex-practice/service.py)

### [Prototype](creational-patterns/prototype.py)
run-time時生成需要的class，利用如同template般的prototype class來生成小型的class

在用Register來統一管理每個run-time生成的object

## Structural Patterns
### [Adapter](structural-patterns/adapter.py)
實作一個新的interface去包裝舊的interface

### [Bridge](structural-patterns/bridge.py)
將interface與implementation分開的pattern

low-level的包裝為用另外的方法名稱呼叫實作體的方法

high-level為抽象層特有的方法，目的可能是改變屬性的值

### [Composite](structural-patterns/composite.py)
***Key points***:
- 有一個base class(component)作為composites的最大公因數method
- containee要繼承component，並且override基底的方法提供實作
- container也要繼承component、並提供add以及del等方法讓此composite架構可以添加containee
- 因container也繼承了component，所以container的add可以將其他的container也加進去視為containee
- 上述的關係就稱作composite pattern

### **Decorator**
> 用重新實作介面的方式來提供情境的需求，可能是擴充或改或原始介面方法的輸出
1. 首先會實作一個抽象介面，具有最少共通性的方法作為未來子類別繼承時的interface，python的話可能可以用abc module來製作。
2. 接著你實際上的應用會繼承此abc，並重新實作該共通性方法，符合各種情境的應用
- [faif example](https://github.com/faif/python-patterns/blob/master/patterns/structural/decorator.py)
- [sourcemaking example](https://sourcemaking.com/design_patterns/decorator/python/1)

### **Facade**
> 替你許多複雜的端口、subsystem實作一個統一且簡單的entry point，供客戶端方便操作數據資源
> 與Adapter不同的是，Adapter使用的是舊介面、而Facade實作一組新的


## Behavioral Patterns

## Design for Testability Patterns

## Fundamental Patterns

## Others


# reference
- [github.com/faif/python-patterns](https://github.com/faif/python-patterns)
- [sourcemaking](https://sourcemaking.com/design_patterns)
- [tutorial point](https://www.tutorialspoint.com/python_design_patterns/index.htm)
- https://www.toptal.com/python/python-design-patterns
