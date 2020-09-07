package main

import "fmt"

// List is struct representation of doubly linked list
type List struct {
	head *node
	size int
}

type node struct {
	data int
	next *node
}

func newList() List {
	return List{size: 0, head: nil}
}

func (l *List) append(data int) {
	if l.head == nil {
		l.head = &node{data: data}
		l.size++
		return
	}
	tmp := &node{data: data, next: nil}
	last := l.head
	for last.next != nil {
		last = last.next
	}
	last.next = tmp
	l.size++
}

func (l *List) prepend(data int) {
	tmp := &node{data: data}
	tmp.next = l.head
	l.head = tmp
	l.size++
}

func (l *List) remove(data int) {
	tmp := l.head
	cnt := 0
	if l.head.data == data {
		l.head = tmp
		tmp = nil
		return
	}
	prev := &node{}
	for tmp != nil {
		cnt++
		if tmp.data == data {
			break
		}
		prev = tmp
		tmp = tmp.next
	}
	if tmp != nil {
		prev.next = tmp.next
		tmp = nil
	}
}

func (l *List) find(data int) *node {
	for i := l.head; i != nil; i = i.next {
		if i.data == data {
			return i
		}
	}
	return nil
}

func (l *List) print() {
	tmp := l.head
	for tmp != nil {
		fmt.Print(tmp.data, " ")
		tmp = tmp.next
	}
	fmt.Println()
}

func main() {
	l := newList()
	l.append(1)
	l.append(2)
	l.append(3)
	l.prepend(4)
	l.prepend(5)
	l.print()
	l.remove(3)
	l.print()
	l.append(9)
	l.print()
	t := l.find(2)
	fmt.Println(t)
	t = l.find(3)
	fmt.Println(t)
	fmt.Println(l.size)
}
