const Alligator = function (speed, direction) {
  this.speed = speed
  this.direction = direction
}

// The swim property here is the "mixin"
const swim = {
  location () {
    console.log(`Heading ${this.direction} at ${this.speed}`)
  }
}

// 許多 mixin 文章的解說，會直接使用 Object.assign 來達成同樣的目的
Object.assign(Alligator.prototype, swim)

const alligator = new Alligator('10 mph', 'East')

alligator.location()

const bbb = new Alligator('20 mph', 'North')

bbb.location()

// test the function is the same
console.log(alligator.location === bbb.location)
