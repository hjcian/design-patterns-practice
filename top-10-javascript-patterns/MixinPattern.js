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

const aaa = new Alligator('10 mph', 'East')

aaa.location()
// Heading East at 10 mph

const bbb = new Alligator('20 mph', 'North')

bbb.location()
// Heading North at 20 mph

console.log(aaa.location === bbb.location)
// true
