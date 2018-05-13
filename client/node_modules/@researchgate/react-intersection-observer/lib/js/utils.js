'use strict';

exports.__esModule = true;
exports.isDOMTypeElement = isDOMTypeElement;
exports.parseRootMargin = parseRootMargin;
exports.shallowCompareOptions = shallowCompareOptions;

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function isDOMTypeElement(element) {
    return _react2.default.isValidElement(element) && typeof element.type === 'string';
}

var marginRE = /^-?\d*\.?\d+(px|%)$/;

function parseRootMargin(rootMargin) {
    var marginString = rootMargin ? rootMargin.trim() : '0px';

    var _marginString$split$m = marginString.split(/\s+/).map(function (margin) {
        if (!marginRE.test(margin)) {
            throw new Error('rootMargin must be a string literal containing pixels and/or percent values');
        }
        return margin;
    }),
        _marginString$split$m2 = _marginString$split$m[0],
        m0 = _marginString$split$m2 === undefined ? '0px' : _marginString$split$m2,
        _marginString$split$m3 = _marginString$split$m[1],
        m1 = _marginString$split$m3 === undefined ? m0 : _marginString$split$m3,
        _marginString$split$m4 = _marginString$split$m[2],
        m2 = _marginString$split$m4 === undefined ? m0 : _marginString$split$m4,
        _marginString$split$m5 = _marginString$split$m[3],
        m3 = _marginString$split$m5 === undefined ? m1 : _marginString$split$m5;

    return m0 + ' ' + m1 + ' ' + m2 + ' ' + m3;
}

function shallowCompareOptions(next, prev) {
    if (Array.isArray(next) && Array.isArray(prev)) {
        if (next.length === prev.length) {
            return next.some(function (_, index) {
                return shallowCompareOptions(next[index], prev[index]);
            });
        }
    }
    return next !== prev;
}