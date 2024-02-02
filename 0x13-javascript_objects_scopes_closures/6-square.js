#!/usr/bin/node
/**
 * Defines class Square and create an instance method
 */
const PrevSquare = require('./5-square.js');

class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += myChar;
        y++;
      }
      console.log(myVar);
    }
  }
}
module.exports = Square;
