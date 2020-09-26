const CarController = (() => {
  let carSpeed = 0
  return {
    speedUp: (speed) => { carSpeed += speed },
    slowDown: (speed) => { carSpeed -= speed },
    checkSpeed: () => carSpeed
  }
})()

console.log(CarController.checkSpeed())
CarController.speedUp(100)
console.log(CarController.checkSpeed())
CarController.slowDown(33)
console.log(CarController.checkSpeed())
