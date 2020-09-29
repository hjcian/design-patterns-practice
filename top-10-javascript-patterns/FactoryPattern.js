function FullTime () {
  this.hourly = '$12'
}

function PartTime () {
  this.hourly = '$10'
}

function Contractor () {
  this.hourly = '$15'
}

function JobTypeFactory () {
  this.createEmployee = function (name, type) {
    let employee

    if (type === 'fulltime') {
      employee = new FullTime()
    } else if (type === 'parttime') {
      employee = new PartTime()
    } else if (type === 'contractor') {
      employee = new Contractor()
    } else {
      throw new Error(`Company does not offer ${type} type job now`)
    }

    employee.name = name
    employee.type = type

    employee.say = function () {
      console.log(`${employee.name} is a ${employee.type}-type employee, wage is ${employee.hourly}/hr`)
    }

    return employee
  }
}

const employees = []
const hr = new JobTypeFactory()
employees.push(hr.createEmployee('Max', 'fulltime'))
employees.push(hr.createEmployee('John', 'parttime'))
employees.push(hr.createEmployee('HH', 'contractor'))

employees.forEach((employee) => { employee.say() })
// Max is a fulltime-type employee, wage is $12/hr
// John is a parttime-type employee, wage is $10/hr
// HH is a contractor-type employee, wage is $15/hr
