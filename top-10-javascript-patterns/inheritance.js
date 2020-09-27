function Person (first, last, age, gender, interests) {
  console.log('[Person] call constructor')
  this.name = {
    first,
    last
  }
  this.age = age
  this.gender = gender
  this.interests = interests
}

// 我們在 Person.prototype 中擴充方法
// 利用此方法擴充的方法才不會因創建多個 Person 而重複佔用記憶體
Person.prototype.greeting = function () {
  console.log('Hi! I\'m ' + this.name.first + '.')
}

const p = new Person(
  'Max', 'Cian', 30, 'male', ['Javascript', 'Python', 'Golang'])
p.greeting()

// ============================================================
// ============================================================
// ============================================================

function Teacher (first, last, age, gender, interests, subject) {
  console.log('[Teacher] call constructor')
  Person.call(this, first, last, age, gender, interests)
  this.subject = subject
}

// 此舉才能「繼承」 Person.prototype 中的方法
Teacher.prototype = Object.create(Person.prototype)

const teacher = new Teacher(
  'Max', 'Cian', 30, 'male', ['Javascript', 'Python', 'Golang'],
  'Object-Oriented Programming of Javascript')

teacher.greeting() // Person's greeting()

// 「子類別」通常會有需求是「覆寫 (overriding)」掉父類別的方法，以符合子類別的使用情境
Teacher.prototype.greeting = function () {
  let prefix

  if (this.gender === 'male' || this.gender === 'Male' || this.gender === 'm' || this.gender === 'M') {
    prefix = 'Mr.'
  } else if (this.gender === 'female' || this.gender === 'Female' || this.gender === 'f' || this.gender === 'F') {
    prefix = 'Ms.'
  } else {
    prefix = 'Mx.'
  }

  console.log('Hello. My name is ' + prefix + ' ' + this.name.last + ', and I teach ' + this.subject + '.')
}

teacher.greeting()
