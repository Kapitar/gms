<template>
  <div class="divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow">
    <div class="p-4">
      <div class="period-number text-sm text-gray-500 flex">
        <span
          class="inline-flex items-center rounded-md bg-blue-100 px-1.5 py-0.5 text-xs font-medium text-blue-600">Period
          {{ period.period }}</span>
        <div class="period-time pl-2">
          {{ period.time }}
        </div>
      </div>
      <div class="mt-2 period-name font-medium text-xl">
        {{ period.name }}
        <span
          class="ml-1 align-middle	inline-flex flex-shrink-0 items-center rounded-full bg-blue-50 px-1.5 py-0.5 text-xs font-medium text-blue-700 ring-1 ring-inset ring-blue-600/20">{{
          period.room }}</span>
      </div>
      <div class="teacher mt-0.5 text-sm">
        {{ period.teacher }}
      </div>
    </div>
  </div>

  <ClassSeperator v-if="period.break" :time='period.break' />
</template>

<script>
import ClassSeperator from './ClassSeperatorComponent.vue';

export default {
  name: 'ClassComponent',
  props: ['period'],
  components: {
    ClassSeperator
  }
}
</script>