import UIKit

var str = "Hello, playground"

// MARK: - Array
// Liniear : O(n) // Linear Time
func findMinMaxValue(of arr: [Int]) -> (min : Int, max: Int) {
    var min: Int = Int.max
    var max: Int = 0
    for value in arr {
        if value < min {
            min = value
        }
        if value > max {
            max = value
        }
    }
    return (min, max)
}

print("Find Min Max Value: \(findMinMaxValue(of: [2,3,4,5,6,7,8,9,10]))")
