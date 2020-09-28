function ClickSubject () {
  this.handlers = [] // observers
}

ClickSubject.prototype = {

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

function onClick (args) {
  console.log(`clicked by: ${args}`)
}

const click = new ClickSubject()

click.subscribe(onClick)
click.notify('event #1')
console.log('='.repeat(30))
click.unsubscribe(onClick)
click.notify('event #2') // no handler catch this event
console.log('='.repeat(30))
click.subscribe(onClick)
click.notify('event #3')
