<template>
  <div id="app">
    <TodoList :todos="todos" @delete-todo="deleteTodo"/>
    <TodoForm
      @create-todo="createTodo"
    />
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      todos: []
    }
  },
  methods: {
    createTodo: function (todoTitle) {
      const todo = {
        title: todoTitle
      }
      this.todos.push(todo)
    },
    deleteTodo: function (todo) {
      const index = this.todos.indexOf(todo)
      this.todos.splice(index, 1) // index 하나 삭제하고 새로 배열 생성
    }
  }
}
</script>

<style>
</style>
