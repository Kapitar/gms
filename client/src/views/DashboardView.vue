<template>
  <main class="lg:pl-72">
    <div class="xl:pl-96">
      <div class="px-4 py-10 sm:px-6 lg:px-8 lg:py-6">
        <RecentActivity/>
        <Stats/>
      </div>
    </div>
  </main>

  <aside class="fixed inset-y-0 left-72 hidden w-96 overflow-y-auto border-r border-gray-200 px-4 py-6 sm:px-6 lg:px-8 xl:block">
    <div class="pb-5">
      <div class="-ml-2 -mt-2 flex flex-wrap items-baseline">
        <h3 class="ml-2 mt-2 text-base font-semibold leading-6 text-gray-900">Schedule</h3>
        <p class="ml-2 mt-1 truncate text-sm text-gray-500">Wednesday</p>
      </div>
    </div>
    
    <ul role="list" class="grid grid-cols-1 gap-6 sm:grid-cols-1 lg:grid-cols-1">
      <li v-for="period in classes" :key="period.name" class="col-span-1 divide-y divide-gray-200 rounded-lg bg-white shadow" :class="{'opacity-35': period.finished}">
        <div class="flex w-full items-center justify-between space-x-6 p-6">
          <div class="flex-1 truncate">
            <div class="flex items-center space-x-3">
              <h3 class="truncate text-sm font-medium text-gray-900">{{ period.name }}</h3>
              <span class="inline-flex flex-shrink-0 items-center rounded-full bg-blue-50 px-1.5 py-0.5 text-xs font-medium text-blue-700 ring-1 ring-inset ring-blue-600/20">{{ period.room }}</span>
            </div>
            <p class="mt-2 truncate text-sm text-gray-500 inline-flex gap-x-1 flex-1"><ClockIcon class="h-5 w-5 text-gray-400" aria-hidden="true"/>{{ period.time }}</p>
          </div>
          <img class="h-10 w-10 flex-shrink-0 rounded-full bg-gray-300" :src="period.teacherImg" alt="" />
        </div>
      </li>
    </ul>
  </aside>
</template>


<script>
import {
  ClockIcon
} from '@heroicons/vue/24/outline'

// import TodaySchedule from '../components/TodayScheduleComponent.vue';
import RecentActivity from '../components/dashboard/RecentActivityComponent.vue';
import Stats from '../components/dashboard/StatsComponent.vue';

export default {
  name: "DashboardView",
  components: {
    ClockIcon, 
    RecentActivity,
    Stats
  },
  data() {
    return {
      classes: [
        {
          name: 'APCSP',
          teacher: 'Dr. Barnes',
          room: 'Room 201',
          finished: true,
          teacherImg: 'https://busanforeignschool.org/wp-content/uploads/2024/02/Dylan.png',
          time: "8:30 AM - 9:20 AM"
        },
        {
          name: 'APCSA',
          teacher: 'Dr. Barnes',
          room: 'Room 201',
          finished: false,
          teacherImg: 'https://busanforeignschool.org/wp-content/uploads/2024/02/Dylan.png',
          time: "9:24 AM - 10:14 AM"
        },
        {
          name: 'Pre-Calculus',
          teacher: 'Mr. Hanawalt',
          room: 'Room B103',
          finished: false,
          teacherImg: 'https://busanforeignschool.org/wp-content/uploads/2024/02/Matthew.png',
          time: "10:31 AM - 11:21 AM"
        },
        {
          name: 'English 11',
          teacher: 'Mr. Bishop',
          room: 'Room 112',
          finished: false,
          teacherImg: 'https://busanforeignschool.org/wp-content/uploads/2024/02/Alec.png',
          time: "11:25 AM - 12:15 PM"
        },
        {
          name: 'Music History',
          teacher: 'Ms. Harris',
          room: 'Room 333',
          finished: false,
          teacherImg: 'https://busanforeignschool.org/wp-content/uploads/2024/02/Nikki.png',
          time: "12:51 PM - 01:41 PM"
        },
        {
          name: 'Environmental Science',
          teacher: 'Ms. Tempest',
          room: 'Room 105',
          finished: false,
          teacherImg: 'https://busanforeignschool.org/wp-content/uploads/2024/02/Kyla.png',
          time: "01:45 PM - 02:35 PM"
        },
        {
          name: 'Korean',
          teacher: 'Ms. Lee',
          room: 'Room 401',
          finished: false,
          teacherImg: 'https://busanforeignschool.org/wp-content/uploads/2024/02/Heejin.png',
          time: "02:39 PM - 03:30 PM"
        },
      ]
    }
  }
}
</script>