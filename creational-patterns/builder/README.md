## Builder pattern
### 目的
- 將複雜的物件創建過程與使用者隔離
- 建造過程是 step-by-step
- 在不同的 objects 間 reuse 創建邏輯 (creation algorithm)


### 自我解釋
- 有一個中心化的過程，所有物件都得實作並滿足該流程所需的 method
- 最後取得該物件的實體
- `BuildProcess` 是所有新的物件需要實作的介面，滿足介面、就滿足 construction process

### Anti-patterns
- `SetWheels()` `SetSeats()` `SetStructure()` 需要 stable，任何 method 的更動都會嚴重影響每個物件
- 如果不同物件需要的 method 不一樣，會很怪
