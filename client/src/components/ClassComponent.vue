<template>
  <div class="course-period" v-for="period in classes" :key="period.period">
    <div class="divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow">
    <div class="p-4">
      <div class="period-number text-sm text-gray-500 flex">
        <span class="inline-flex items-center rounded-md bg-blue-100 px-1.5 py-0.5 text-xs font-medium text-blue-600">Period {{ period.period }}</span>
        <div class="period-time pl-2">
          {{ period.time }}
        </div>
      </div>
      <div class="mt-2 period-name font-medium text-xl">
        {{ period.name }}
        <span class="ml-1 align-middle	inline-flex flex-shrink-0 items-center rounded-full bg-blue-50 px-1.5 py-0.5 text-xs font-medium text-blue-700 ring-1 ring-inset ring-blue-600/20">{{ period.room }}</span>
      </div>
      <div class="teacher mt-0.5 text-sm">
        {{ period.teacher }}
      </div> 
    </div>
  </div>

  <div class="relative mt-3 mb-3" v-if="period.break !== null">
    <div class="absolute inset-0 flex items-center" aria-hidden="true">
      <div class="w-full border-t border-gray-300" />
    </div>
    <div class="relative flex justify-center">
      <span class="bg-gray-50 px-2 text-sm text-gray-500">{{ period.break }}</span>
    </div>
  </div>
  </div>
</template>

<script setup>
let classes = [
  {
    period: 1,
    name: "Free period",
    time: "8:30 AM - 9:20 AM",
    room: "Room 201",
    teacher: "Dr. Barnes",
    break: "Break 9:20 AM - 9:24 AM",
  },
  {
    period: 2,
    name: "Senior English",
    time: "9:24 AM - 10:14 AM",
    room: "Room 192",
    teacher: "Mr. Bishop",
    break: "Break 10:14 AM - 10:29 AM",
  },
  {
    period: 3,
    name: "Free period",
    time: "10:31 AM - 11:21 AM",
    room: "Room 192",
    teacher: "Mr. Bishop",
    break: "Break 11:21 AM - 11:25 AM",
  },
  {
    period: 4,
    name: "AP Calculus BC",
    time: "11:25 AM - 12:15 PM",
    room: "Room B102",
    teacher: "Mr. Gates",
    break: "Lunch 12:15 PM - 12:47 PM",
  },
  {
    period: 5,
    name: "AP Statistics",
    time: "12:51 PM - 01:41 PM",
    room: "Room B102",
    teacher: "Mr. Gates",
    break: "Break 01:41 PM - 01:45 PM",
  },
  {
    period: 6,
    name: "AP Macroeconomics",
    time: "01:45 PM - 02:35 PM",
    room: "Room B101",
    teacher: "Mr. Van Genderen",
    break: "Break 02:35 PM - 02:39 PM",
  },
  {
    period: 7,
    name: "Korean 1",
    time: "02:39 PM - 03:30 PM",
    room: "Room B101",
    teacher: "Ms. Lee",
    break: null
  }
]

</script>

<script>
import ClassSeperatorComponent from "./ClassSeperatorComponent.vue"


export default {
  name: "ClassComponent",
  components: {
    ClassSeperatorComponent
  }
}
</script>