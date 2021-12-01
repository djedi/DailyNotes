<template>
  <div class="level-item alt-button">
    <b-dropdown aria-role="list">
      <b-tooltip
        label="Tasks"
        position="is-bottom"
        slot="trigger"
        role="button"
      >
        <b-icon icon="tasks"></b-icon>
      </b-tooltip>
      <b-dropdown-item custom v-for="task of tasks" v-bind:key="task.uuid">
        <task-item :task="task"></task-item>
      </b-dropdown-item>
      <div class="no-tasks" v-if="!tasks.length">No tasks found</div>
    </b-dropdown>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import _ from "lodash";

import TaskItem from "./TaskItem.vue";

@Component({
  components: { TaskItem },
  props: {
    tasks: {
      type: Array,
      required: true,
    },
  },
})
export default class Tasks extends Vue {
  public tasks: Array<object> = [];
}
</script>

<style scoped>
.no-tasks {
  margin-left: 1em;
  color: black;
}
</style>
