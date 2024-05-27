<template>
  <RadioGroup v-model="selectedMailingLists">
    <div class="mt-4 grid grid-cols-2 gap-x-2 gap-y-6 sm:grid-cols-5 sm:gap-x-4">
      <RadioGroupOption as="template" v-for="mailingList in mailingLists" :key="mailingList.id" :value="mailingList" v-slot="{ active, checked }">
        <div :class="[active ? 'border-indigo-600 ring-2 ring-indigo-600' : 'border-gray-300', 'relative flex cursor-pointer rounded-lg border bg-white p-4 shadow-sm focus:outline-none']">
          <span class="flex flex-1">
            <span class="flex flex-col">
              <RadioGroupLabel as="span" class="block text-sm font-medium text-gray-900">{{ mailingList.title }}</RadioGroupLabel>
              <RadioGroupDescription as="span" class="mt-1 flex items-center text-sm text-gray-500">{{ mailingList.description }}</RadioGroupDescription>
              <!-- <RadioGroupDescription as="span" class="mt-6 text-sm font-medium text-gray-900">{{ mailingList.users }}</RadioGroupDescription> -->
            </span>
          </span>
          <CheckCircleIcon :class="[!checked ? 'invisible' : '', 'h-5 w-5 text-indigo-600']" aria-hidden="true" />
          <span :class="[active ? 'border' : 'border-2', checked ? 'border-indigo-600' : 'border-transparent', 'pointer-events-none absolute -inset-px rounded-lg']" aria-hidden="true" />
        </div>
      </RadioGroupOption>
    </div>
  </RadioGroup>
</template>

<script setup>
import { ref } from 'vue'
import { RadioGroup, RadioGroupDescription, RadioGroupLabel, RadioGroupOption } from '@headlessui/vue'
import { CheckCircleIcon } from '@heroicons/vue/20/solid'

const mailingLists = [
  { id: 1, title: 'Monday', description: 'May 20, 2024', users: '621 users' },
  { id: 2, title: 'Tuesday', description: 'May 21, 2024', users: '621 users' },
  { id: 3, title: 'Wednesday', description: 'May 22, 2024', users: '621 users' },
  { id: 4, title: 'Thursday', description: 'May 23, 2024', users: '621 users' },
  { id: 5, title: 'Friday', description: 'May 24, 2024', users: '621 users' },
]

const selectedMailingLists = ref(mailingLists[0])
</script>

<script>
export default {
  name: "DayPickerComponent"
}
</script>