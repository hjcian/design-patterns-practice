function CelloNews () {
  this.handlers = [] // observers
}

CelloNews.prototype = {

  subscribe: function (fn) {
    this.handlers.push(fn)
  },

  unsubscribe: function (fn) {
    this.handlers = this.handlers.filter(item => item !== fn)
  },

  notify: function (args) {
    this.handlers.forEach(fn => fn(args))
  }
}

function MaxCian (args) {
  console.log(`[MaxCian] got message: ${args}`)
}

function JohnLee (args) {
  console.log(`[JohnLee] got message: ${args}`)
}

function HHTu (args) {
  console.log(`[HHTu] got message: ${args}`)
}

const cello = new CelloNews()

cello.subscribe(MaxCian)
cello.subscribe(JohnLee)
cello.notify('台塑家教專案上課啦')
console.log()

cello.unsubscribe(JohnLee)

cello.notify('吃飯啦')
console.log()

cello.subscribe(HHTu)
cello.notify('爬山啦')
