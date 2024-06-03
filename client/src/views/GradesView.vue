<template>
  <main class="py-10 lg:pl-72">
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between">
        <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">Gradebook</h2>
        <div class="ml-4 w-32">
          <Listbox as="div" v-model="selected">
            <div class="relative mt-2">
              <ListboxButton
                class="relative w-full cursor-default rounded-md bg-white py-1.5 pl-3 pr-10 text-left text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-600 sm:text-sm sm:leading-6">
                <span class="block truncate">{{ selected.name }}</span>
                <span class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2">
                  <ChevronUpDownIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
                </span>
              </ListboxButton>

              <transition leave-active-class="transition ease-in duration-100" leave-from-class="opacity-100"
                leave-to-class="opacity-0">
                <ListboxOptions
                  class="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
                  <ListboxOption as="template" v-for="term in terms" :key="term.id" :value="term"
                    v-slot="{ active, selected }">
                    <li
                      :class="[active ? 'bg-indigo-600 text-white' : 'text-gray-900', 'relative cursor-default select-none py-2 pl-3 pr-9']">
                      <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">{{
                        term.name
                        }}</span>

                      <span v-if="selected"
                        :class="[active ? 'text-white' : 'text-indigo-600', 'absolute inset-y-0 right-0 flex items-center pr-4']">
                        <CheckIcon class="h-5 w-5" aria-hidden="true" />
                      </span>
                    </li>
                  </ListboxOption>
                </ListboxOptions>
              </transition>
            </div>
          </Listbox>
        </div>
      </div>

      <Stats />

      <div class="hs-accordion-group">
        <div v-for="course in classes" :key="course.name"
          class="hs-accordion hs-accordion-active:border-gray-200 bg-white border border-transparent rounded-xl mb-4 shadow"
          id="hs-active-bordered-heading-one">
          <Class :course="course" />
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { HeartIcon, XMarkIcon, StarIcon, SparklesIcon } from '@heroicons/vue/24/outline'
import { PencilIcon, PlusIcon } from '@heroicons/vue/20/solid'
import { Listbox, ListboxButton, ListboxLabel, ListboxOption, ListboxOptions } from '@headlessui/vue'
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/vue/20/solid'

const open = ref(false);

const terms = [
  { id: 1, name: 'Quarter 1' },
  { id: 2, name: 'Quarter 2' },
  { id: 3, name: 'Quarter 3' },
  { id: 4, name: 'Quarter 4' }
]

const selected = ref(terms[3])

const classes = [
  {
    name: "AP Computer Science A",
    teacher: "Dr. Barnes",
    sections: [
      {
        name: 'Formative 40%',
        assignments: [
          { name: 'Quiz 7.4-7.8', grade: '96/100', avg: '96', status: 'Graded', section: "Formative 40%", teacher: "Dr. Barnes", notes: "No description.", date: "May 20, 2024" },
          { name: 'Quiz 8.1-8.3', grade: '98/100', avg: '98', status: 'Changed', section: "Formative 40%", teacher: "Dr. Barnes", notes: "No description.", date: "May 28, 2024" },
          { name: 'Quiz 8.4-8.6', grade: '0/100', avg: '0', status: 'Missing', section: "Formative 40%", teacher: "Dr. Barnes", notes: "No description.", date: "May 28, 2024" },
        ],
        average: 65
      },
      {
        name: 'Summative 60%',
        assignments: [
          { name: 'Unit 7 Test', grade: '100/100', avg: '100', status: 'Graded', section: "Summative 60%", teacher: "Dr. Barnes", notes: "Correction due to June 4", date: "May 30, 2024" },
        ],
        average: 100
      }
    ],
    average: 84,
    grade: "B+"
  },
  {
    name: "AP Computer Science Principles",
    teacher: "Dr. Barnes",
    sections: [
      {
        name: 'Formative 40%',
        assignments: [
          { name: 'Quiz 7.4-7.8', grade: '96/100', avg: '96', status: 'Graded', section: "Formative 40%", teacher: "Dr. Barnes", notes: "No description.", date: "May 20, 2024" },
          { name: 'Quiz 8.1-8.3', grade: '98/100', avg: '98', status: 'Changed', section: "Formative 40%", teacher: "Dr. Barnes", notes: "No description.", date: "May 28, 2024" },
          { name: 'Quiz 8.4-8.6', grade: '0/100', avg: '0', status: 'Missing', section: "Formative 40%", teacher: "Dr. Barnes", notes: "No description.", date: "May 28, 2024" },
        ],
        average: 65
      },
      {
        name: 'Summative 60%',
        assignments: [
          { name: 'Unit 7 Test', grade: '100/100', avg: '100', status: 'Graded', section: "Summative 60%", teacher: "Dr. Barnes", notes: "Correction due to June 4", date: "May 30, 2024" },
        ],
        average: 100
      }
    ],
    average: 84,
    grade: "B+"
  },
  {
    name: "Pre-Calculus",
    teacher: "Mr. Hanawalt",
    sections: [
      {
        name: 'Formative 40%',
        assignments: [
          { name: 'Quiz 7.4-7.8', grade: '96/100', avg: '96', status: 'Graded', section: "Formative 40%", teacher: "Mr. Hanawalt", notes: "No description.", date: "May 20, 2024" },
          { name: 'Quiz 8.1-8.3', grade: '98/100', avg: '98', status: 'Changed', section: "Formative 40%", teacher: "Mr. Hanawalt", notes: "No description.", date: "May 28, 2024" },
          { name: 'Quiz 8.4-8.6', grade: '0/100', avg: '0', status: 'Missing', section: "Formative 40%", teacher: "Mr. Hanawalt", notes: "No description.", date: "May 28, 2024" },
        ],
        average: 65
      },
      {
        name: 'Summative 60%',
        assignments: [
          { name: 'Unit 7 Test', grade: '100/100', avg: '100', status: 'Graded', section: "Summative 60%", teacher: "Mr. Hanawalt", notes: "Correction due to June 4", date: "May 30, 2024" },
        ],
        average: 100
      }
    ],
    average: 84,
    grade: "B+"
  },
]

</script>

<script>

import Stats from '../components/grades/StatsComponent.vue'
import Class from '../components/grades/ClassComponent.vue'

export default {
  name: "GradesView",
  components: {
    Stats,
    Class
  }
}
</script>