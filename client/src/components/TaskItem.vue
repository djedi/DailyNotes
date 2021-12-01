<template>
  <div class="field">
    <b-checkbox v-model="completed" @input="updateTask">
      {{ this.task.name }}
    </b-checkbox>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

import SidebarInst from "../services/sidebar";

@Component({
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
})
export default class TaskItem extends Vue {
  public task: any;
  public sidebar = SidebarInst;
  public completed: Boolean = false;

  mounted() {
    this.completed = this.task.completed;
  }

  public async updateTask() {
    this.task.completed = this.completed;
  }
}
</script>

<style>
.level-item > .dropdown > .dropdown-menu {
  width: 300px;
}

.level-item > .dropdown > .dropdown-menu > .dropdown-content {
  max-height: 400px;
  overflow-y: auto;
}
</style>
