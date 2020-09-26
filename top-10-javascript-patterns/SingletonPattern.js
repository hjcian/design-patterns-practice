let car

function Car (model, year, miles) {
  this.model = model
  this.year = year
  this.miles = miles
}

car = new Car('M4', '2019', '1000')
console.log(car)
car = new Car('M4', '2030', '12345')
console.log(car)

const SingletonCar = (() => {
  let car
  const init = (model, year, miles) => new Car(model, year, miles)
  return {
    getCar: (model, year, miles) => {
      if (car) {
        console.log('Car was created, return the old')
        return car
      }
      console.log('Lazy create a new car')
      car = init(model, year, miles)
      return car
    }
  }
})()

car = SingletonCar.getCar('M4', '2019', '1000')
console.log(car)
car = SingletonCar.getCar('M4', '2030', '12345')
console.log(car)
