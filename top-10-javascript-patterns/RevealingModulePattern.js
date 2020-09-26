const CarController = (() => {
  let carSpeed = 0
  function NitrogenAcceleration (speed) {
    carSpeed += speed
  }

  function LockFrontWheel (speed) {
    carSpeed -= speed
  }
  function LockReerWheel (speed) {
    carSpeed -= speed
  }
  function LockWheels (speed) {
    LockFrontWheel(speed * 0.6)
    LockReerWheel(speed * 0.4)
  }

  return {
    speedUp: NitrogenAcceleration,
    slowDown: LockWheels,
    checkSpeed: () => carSpeed
  }
})()

console.log(CarController.checkSpeed())
CarController.speedUp(100)
console.log(CarController.checkSpeed())
CarController.slowDown(33)
console.log(CarController.checkSpeed())
