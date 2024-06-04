<template>
  <main class="py-10 lg:pl-72">
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="lg:flex lg:items-center lg:justify-between">
        <div class="min-w-0 flex-1">
          <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">Schedule</h2>
          <div class="mt-1 flex flex-col sm:mt-0 sm:flex-row sm:flex-wrap sm:space-x-6">
            <div class="mt-2 flex items-center text-sm text-gray-500">
              <CalendarIcon class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400" aria-hidden="true" />
              June 3 - June 7, 2024
            </div>
          </div>
        </div>
        <div class="mt-5 flex lg:ml-4 lg:mt-0">
          <span class="sm:ml-3">
            <button type="button"
              class="inline-flex items-center rounded-md bg-indigo-600 px-5 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
              <PrinterIcon class="-ml-0.5 mr-1.5 h-5 w-5" aria-hidden="true" />
              Print
            </button>
          </span>
        </div>
      </div>

      <RadioGroup v-model="selectedDay">
        <div class="mt-4 grid grid-cols-2 gap-x-2 gap-y-6 sm:grid-cols-5 sm:gap-x-4">
          <RadioGroupOption as="template" v-for="day in days" :key="day.id" :value="day" v-slot="{ active, checked }">
            <div
              :class="[active ? 'border-indigo-600 ring-2 ring-indigo-600' : 'border-gray-300', 'relative flex cursor-pointer rounded-lg border bg-white p-4 shadow-sm focus:outline-none']">
              <span class="flex flex-1">
                <span class="flex flex-col">
                  <RadioGroupLabel as="span" class="block text-sm font-medium text-gray-900">{{ day.name }}
                  </RadioGroupLabel>
                  <RadioGroupDescription as="span" class="mt-1 flex items-center text-sm text-gray-500">{{
                    day.date }}</RadioGroupDescription>
                  <!-- <RadioGroupDescription as="span" class="mt-6 text-sm font-medium text-gray-900">{{ mailingList.users }}</RadioGroupDescription> -->
                </span>
              </span>
              <CheckCircleIcon :class="[!checked ? 'invisible' : '', 'h-5 w-5 text-indigo-600']" aria-hidden="true" />
              <span
                :class="[active ? 'border' : 'border-2', checked ? 'border-indigo-600' : 'border-transparent', 'pointer-events-none absolute -inset-px rounded-lg']"
                aria-hidden="true" />
            </div>
          </RadioGroupOption>
        </div>
      </RadioGroup>


      <div class="schedule mt-5">
        <div class="course-period" v-for="period in classes" :key="period.period">
          <Class :period="period" />
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import ClassSeperatorComponent from "../components/schedule/ClassSeperatorComponent.vue"
import { CalendarIcon, PrinterIcon, CheckCircleIcon } from '@heroicons/vue/20/solid'
import { RadioGroup, RadioGroupDescription, RadioGroupLabel, RadioGroupOption } from '@headlessui/vue'
import Class from "../components/schedule/ClassComponent.vue"

export default {
  name: "DashboardView",
  components: {
    ClassSeperatorComponent,
    PrinterIcon,
    CalendarIcon,
    RadioGroup,
    RadioGroupDescription,
    RadioGroupLabel,
    RadioGroupOption,
    CheckCircleIcon,
    Class
  },
  data() {
    return {
      days: [
        { id: 1, name: 'Monday', date: 'June 3, 2024' },
        { id: 2, name: 'Tuesday', date: 'June 4, 2024' },
        { id: 3, name: 'Wednesday', date: 'June 5, 2024' },
        { id: 4, name: 'Thursday', date: 'June 6, 2024', },
        { id: 5, name: 'Friday', date: 'June 7, 2024' },
      ],
      selectedDay: null,
      classes: [
        {
          period: 1,
          name: "APCSP",
          time: "8:30 AM - 9:20 AM",
          room: "Room 201",
          teacher: "Dr. Barnes",
          break: "Break 9:20 AM - 9:24 AM",
        },
        {
          period: 2,
          name: "APCSA",
          time: "9:24 AM - 10:14 AM",
          room: "Room 192",
          teacher: "Dr. Barnes",
          break: "Break 10:14 AM - 10:29 AM",
        },
        {
          period: 3,
          name: "Pre-Calculus",
          time: "10:31 AM - 11:21 AM",
          room: "Room 192",
          teacher: "Mr. Hanawalt",
          break: "Break 11:21 AM - 11:25 AM",
        },
        {
          period: 4,
          name: "English 11",
          time: "11:25 AM - 12:15 PM",
          room: "Room B102",
          teacher: "Mr. Bishop",
          break: "Lunch 12:15 PM - 12:47 PM",
        },
        {
          period: 5,
          name: "Music History",
          time: "12:51 PM - 01:41 PM",
          room: "Room B102",
          teacher: "Ms. Harris",
          break: "Break 01:41 PM - 01:45 PM",
        },
        {
          period: 6,
          name: "Environmental Science",
          time: "01:45 PM - 02:35 PM",
          room: "Room B101",
          teacher: "Ms. Tempest",
          break: "Break 02:35 PM - 02:39 PM",
        },
        {
          period: 7,
          name: "Korean",
          time: "02:39 PM - 03:30 PM",
          room: "Room B101",
          teacher: "Ms. Lee",
          break: null
        }
      ]
    }
  },
  beforeMount() {
    this.selectedDay = this.days[1];
  }
}
</script>