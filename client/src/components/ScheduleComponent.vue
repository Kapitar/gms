<template>
  <ul role="list" class="grid grid-cols-1 gap-6 sm:grid-cols-1 lg:grid-cols-1">
    <li v-for="person in people" :key="person.email" class="col-span-1 divide-y divide-gray-200 rounded-lg bg-white shadow" :class="{'opacity-35': person.finished}">
      <div class="flex w-full items-center justify-between space-x-6 p-6">
        <div class="flex-1 truncate">
          <div class="flex items-center space-x-3">
            <h3 class="truncate text-sm font-medium text-gray-900">{{ person.name }}</h3>
            <span class="inline-flex flex-shrink-0 items-center rounded-full bg-blue-50 px-1.5 py-0.5 text-xs font-medium text-blue-700 ring-1 ring-inset ring-blue-600/20">{{ person.role }}</span>
          </div>
          <p class="mt-2 truncate text-sm text-gray-500 inline-flex gap-x-1 flex-1"><ClockIcon class="h-5 w-5 text-gray-400" aria-hidden="true"/> 8:30 AM - 9:20 AM</p>
        </div>
        <img class="h-10 w-10 flex-shrink-0 rounded-full bg-gray-300" :src="person.imageUrl" alt="" />
      </div>
    </li>
  </ul>
</template>

<script setup>
import {
  ClockIcon
} from '@heroicons/vue/24/outline'

const people = [
  {
    name: 'APCSP',
    title: 'Dr. Barnes',
    role: 'Room 201',
    finished: true,
    imageUrl:
      'https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg',
  },
  {
    name: 'APCSP',
    title: 'Dr. Barnes',
    role: 'Room 201',
    finished: true,
    imageUrl:
      'https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg',
  },
  {
    name: 'APCSP',
    title: 'Dr. Barnes',
    role: 'Room 201',
    imageUrl:
      'https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg',
  },
  {
    name: 'APCSP',
    title: 'Dr. Barnes',
    role: 'Room 201',
    imageUrl:
      'https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg',
  },
  {
    name: 'APCSP',
    title: 'Dr. Barnes',
    role: 'Room 201',
    imageUrl:
      'https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg',
  },
  {
    name: 'APCSP',
    title: 'Dr. Barnes',
    role: 'Room 201',
    imageUrl:
      'https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg',
  },

  {
    name: 'APCSP',
    title: 'Dr. Barnes',
    role: 'Room 201',
    imageUrl:
      'https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg',
  },
]
</script>

<script>
export default {
    name: "ScheduleComponent",
}
</script>