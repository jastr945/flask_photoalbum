'use strict';

exports.__esModule = true;

var _IntersectionObserver = require('./IntersectionObserver');

Object.defineProperty(exports, 'default', {
  enumerable: true,
  get: function get() {
    return _interopRequireDefault(_IntersectionObserver).default;
  }
});

var _utils = require('./utils');

Object.defineProperty(exports, 'parseRootMargin', {
  enumerable: true,
  get: function get() {
    return _utils.parseRootMargin;
  }
});

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }