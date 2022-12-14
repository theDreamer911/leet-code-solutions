/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let result = new ListNode(0);
    let currentNode = result;
    let previousNode = null;

    while(l1 != null || l2 != null){
        if(l1 === null){
            currentNode.val += l2.val;
        } else if (l2 === null){
            currentNode.val += l1.val;
        } else {
            currentNode.val += l1.val + l2.val;
        }

        currentNode.next = new ListNode(0);

        if(currentNode.val >= 10){
            currentNode.val = currentNode.val % 10;
            currentNode.next.val += 1;
        }
        
        previousNode = currentNode;
        currentNode = currentNode.next;

        if(l1 != null){
            l1 = l1.next;
        }
        if(l2 != null){
            l2 = l2.next;
        }
    }

    if(currentNode.val === 0){
        previousNode.next = null;
    }

    return result;
};