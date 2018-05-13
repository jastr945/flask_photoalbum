function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

import { parseRootMargin, shallowCompareOptions } from './utils';

export function getPooled() {
    var options = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};

    var root = options.root || null;
    var rootMargin = parseRootMargin(options.rootMargin);
    var threshold = Array.isArray(options.threshold) ? options.threshold : [typeof options.threshold !== 'undefined' ? options.threshold : 0];
    // eslint-disable-next-line no-restricted-syntax
    for (var _iterator = storage.keys(), _isArray = Array.isArray(_iterator), _i = 0, _iterator = _isArray ? _iterator : _iterator[Symbol.iterator]();;) {
        var _ref;

        if (_isArray) {
            if (_i >= _iterator.length) break;
            _ref = _iterator[_i++];
        } else {
            _i = _iterator.next();
            if (_i.done) break;
            _ref = _i.value;
        }

        var observer = _ref;

        var unmatched = [[root, observer.root], [rootMargin, observer.rootMargin], [threshold, observer.thresholds]].some(function (option) {
            return shallowCompareOptions.apply(undefined, option);
        });

        if (!unmatched) {
            return observer;
        }
    }
    return null;
}

export var storage = new Map();

/**
 * If instances of a class can be reused because the options map,
 * we avoid creating instances of Intersection Observer by reusing them.
 */

var IntersectionObserverContainer = function () {
    function IntersectionObserverContainer() {
        _classCallCheck(this, IntersectionObserverContainer);
    }

    IntersectionObserverContainer.create = function create(callback, options) {
        return getPooled(options) || new IntersectionObserver(callback, options);
    };

    IntersectionObserverContainer.findElement = function findElement(entry, observer) {
        var elements = storage.get(observer);
        if (elements) {
            // eslint-disable-next-line no-restricted-syntax
            for (var _iterator2 = elements.values(), _isArray2 = Array.isArray(_iterator2), _i2 = 0, _iterator2 = _isArray2 ? _iterator2 : _iterator2[Symbol.iterator]();;) {
                var _ref2;

                if (_isArray2) {
                    if (_i2 >= _iterator2.length) break;
                    _ref2 = _iterator2[_i2++];
                } else {
                    _i2 = _iterator2.next();
                    if (_i2.done) break;
                    _ref2 = _i2.value;
                }

                var element = _ref2;

                if (element.target === entry.target) {
                    return element;
                }
            }
        }
        return null;
    };

    IntersectionObserverContainer.observe = function observe(element) {
        var targets = void 0;
        if (storage.has(element.observer)) {
            targets = storage.get(element.observer);
        } else {
            targets = new Set();
            storage.set(element.observer, targets);
        }
        targets.add(element);
        element.observer.observe(element.target);
    };

    IntersectionObserverContainer.unobserve = function unobserve(element) {
        if (storage.has(element.observer)) {
            var targets = storage.get(element.observer);
            if (targets.delete(element)) {
                if (targets.size > 0) {
                    element.observer.unobserve(element.target);
                } else {
                    element.observer.disconnect();
                    storage.delete(element.observer);
                }
            }
        }
    };

    IntersectionObserverContainer.clear = function clear() {
        storage.clear();
    };

    IntersectionObserverContainer.count = function count() {
        return storage.size;
    };

    return IntersectionObserverContainer;
}();

export default IntersectionObserverContainer;