package main

import "fmt"


// Definition for singly-linked list.
type ListNode struct {
	Val int
   	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {

	currentNode := ListNode{}
	var head ListNode = currentNode

	for list1.Next != nil || list2.Next != nil {

		// if list1 != nil && list2 != nil{
		if list1.Val < list2.Val{
			fmt.Println(list1.Val)
			currentNode.Val = list1.Val
			list1 = list1.Next

		} else {
			
			fmt.Println(list2.Val)
			currentNode.Val = list2.Val
			list2 = list2.Next
		}

		currentNode.Next = &ListNode{}
		currentNode = *currentNode.Next

		// } else if list1 != nil{
		// 	currentNode.Val = list1.Val
		// 	list1 = list1.Next

		// } else {
		// 	currentNode.Val = list2.Val
		// 	list2 = list2.Next
		// }
		

	}


	return &head	
    
}

func printList(list1 *ListNode){

	currentNode := list1

	for currentNode != nil {

		fmt.Println(currentNode.Val)
		currentNode = currentNode.Next
	}
}

func main(){

	var list1 ListNode = ListNode{1,&ListNode{2,&ListNode{4,nil}}}
	var list2 ListNode = ListNode{3,&ListNode{5,nil}}

	list3 := mergeTwoLists(&list1,&list2)

	printList(list3)


}