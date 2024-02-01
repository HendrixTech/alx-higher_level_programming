#!/usr/bin/node
/**
 * Validate parameters
 */
class Rectangle {
    constructor(w, h) {
        if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
            this.width = w;
            this.height = h;
        }
        // Instead of printing undefined, you can set a default value or message here
        // else {
        //     this.width = w;
        //     this.height = h;
        //     console.log("one or more arguments undefined")
        // }
    }
}
module.exports = Rectangle;