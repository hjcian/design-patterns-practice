function iMac () {
  this.cost = function () {
    return 51100
  }
  this.screenSize = function () {
    return 21.5
  }
}

// Decorator 1
function LinePointDiscount (imac) {
  const v = imac.cost()
  imac.cost = function () {
    return v - 5110
  }
}

// Decorator 2
function SellAirPods (imac) {
  const v = imac.cost()
  imac.cost = function () {
    return v - 3600
  }
}

// Decorator 3
function SellKeyboardMouse (imac) {
  const v = imac.cost()
  imac.cost = function () {
    return v - 4000
  }
}

const imac = new iMac()
console.log('Original cost:', imac.cost())
// Original cost: 51100

LinePointDiscount(imac)
SellAirPods(imac)
SellKeyboardMouse(imac)

console.log('Final cost:', imac.cost())
// Final cost: 38390
