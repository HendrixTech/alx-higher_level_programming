#!/usr/bin/node
/**
 * Define square class that inherits from Rectangle class
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
