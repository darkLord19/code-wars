package main

import "fmt"

// List is struct representation of doubly linked list
type List struct {
	head *node
	tail *node
	size int
}

type node struct {
	data int
	prev *node
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
	tmp.prev = last
	l.size++
	l.tail = tmp
}

func (l *List) prepend(data int) {
	tmp := &node{data: data}
	l.head.prev = tmp
	tmp.next = l.head
	l.head = tmp
	l.size++
}

func (l *List) remove(data int) {
	tmp := l.head
	for tmp != nil {
		if tmp.data == data {
			prev := tmp.prev
			next := tmp.next
			if prev != nil {
				prev.next = next
			} else {
				l.head = next
			}
			if next != nil {
				next.prev = prev
			} else {
				l.tail = prev
			}
			l.size--
			return
		}
		tmp = tmp.next
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
