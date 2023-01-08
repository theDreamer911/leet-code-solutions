const isSigned32bit = (ints) => {
    return (ints > Math.pow(2, 31) * -1) && (ints < Math.pow(2,31) -1);
}

var reverse = function(x) {
    const isNegative = x < 0;
    const unsignedInput = Math.abs(x);
    const inputString = unsignedInput.toString().split("");
    const reversedString = inputString.reverse().join("");
    const reversedUnsignedInt = parseInt(reversedString);
    const result = isNegative ? -reversedUnsignedInt : reversedUnsignedInt;

    return isSigned32bit(result) ? result : 0
};
