<template>
  <div class="mt-5">
    <Listbox class="w-32" as="div" v-model="selected">
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
            <ListboxOption as="template" v-for="person in people" :key="person.id" :value="person"
              v-slot="{ active, selected }">
              <li
                :class="[active ? 'bg-indigo-600 text-white' : 'text-gray-900', 'relative cursor-default select-none py-2 pl-3 pr-9']">
                <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">{{ person.name }}</span>

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

    <dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-2">
      <div v-for="item in stats" :key="item.id"
        class="relative overflow-hidden rounded-lg bg-white px-4 pb-12 pt-5 shadow sm:px-6 sm:pt-6">
        <dt>
          <div class="absolute rounded-md bg-indigo-500 p-3">
            <component :is="item.icon" class="h-6 w-6 text-white" aria-hidden="true" />
          </div>
          <p class="ml-16 truncate text-sm font-medium text-gray-500">{{ item.name }}</p>
        </dt>
        <dd class="ml-16 flex items-baseline pb-6 sm:pb-7">
          <p class="text-2xl font-semibold text-gray-900">{{ item.stat }}</p>
          <div class="absolute inset-x-0 bottom-0 bg-gray-50 px-4 py-4 sm:px-6">
            <div class="text-sm">
              <a :href="item.link" class="font-medium text-indigo-600 hover:text-indigo-500">View all<span
                  class="sr-only"> {{
                  item.name }} stats</span></a>
            </div>
          </div>
        </dd>
      </div>
    </dl>
  </div>
</template>

<script>
import { ArrowDownIcon, ArrowUpIcon } from '@heroicons/vue/20/solid'
import { Listbox, ListboxButton, ListboxLabel, ListboxOption, ListboxOptions } from '@headlessui/vue'
import { CursorArrowRaysIcon, ClockIcon, UsersIcon, EnvelopeOpenIcon } from '@heroicons/vue/24/outline'
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/vue/20/solid'

export default {
  name: "StatsComponent",
  components: {
    Listbox,
    ListboxButton,
    ListboxOption,
    ListboxOptions,
    ListboxLabel,
    CheckIcon,
    ChevronUpDownIcon
  },
  data() {
    return {
      stats: [
        { id: 1, name: 'Attendance', stat: '97%', icon: ClockIcon },
        { id: 2, name: 'Tardies', stat: '5', icon: ClockIcon },
        { id: 3, name: 'Weighted GPA', stat: '4.21', icon: EnvelopeOpenIcon, link: "/grades" },
        { id: 4, name: 'Unweighted GPA', stat: '3.97', icon: EnvelopeOpenIcon, link: "/grades" },
      ],
      people: [
        { id: 1, name: 'Quarter 1' },
        { id: 2, name: 'Quarter 2' },
        { id: 3, name: 'Quarter 3' },
        { id: 4, name: 'Quarter 4' },
        { id: 5, name: 'Semester 1' },
        { id: 6, name: 'Semester 2' },
        { id: 7, name: 'School year' },
      ],
      selected: null,
    }
  },
  beforeMount() {
    this.selected = this.people[3];
  }
}
</script>