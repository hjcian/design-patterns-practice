function Participant (name) {
  this.name = name
  this.chatroom = null
}

Participant.prototype = {
  send: function (message, to) {
    this.chatroom.send(message, this, to)
  },
  receive: function (message, from) {
    console.log(`[${from.name}]->[${this.name}]: ${message}`)
  }
}

function Chatroom () {
  const participants = {}

  return {

    register: function (participant) {
      participants[participant.name] = participant
      participant.chatroom = this
    },

    send: function (message, from, to) {
      if (to) { // single message
        to.receive(message, from)
      } else { // broadcast message
        for (const key in participants) {
          if (participants[key] !== from) {
            participants[key].receive(message, from)
          }
        }
      }
    }
  }
}

const chatroom = new Chatroom()
const maxcian = new Participant('Max Cian')
const johnlee = new Participant('John Lee')
const hhtu = new Participant('HH Tu')
chatroom.register(maxcian)
chatroom.register(johnlee)
chatroom.register(hhtu)

maxcian.send('要不要吃肥宅快樂餐', johnlee)
console.log()
johnlee.send('我就怕被罵咩', hhtu)
console.log()
hhtu.send('開會囉')
