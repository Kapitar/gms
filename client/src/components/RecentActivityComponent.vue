<template>
  <div>
    <div class="mx-auto max-w-7xl">
        <h2 class="mx-auto max-w-2xl text-base font-semibold leading-6 text-gray-900 lg:mx-0 lg:max-w-none">Recent activity</h2>
    </div>
    <div class="mt-3 overflow-hidden">
        <div class="mx-auto max-w-7xl">
        <div class="mx-auto max-w-2xl lg:mx-0 lg:max-w-none">
            <table class="w-full text-left">
            <thead class="sr-only">
                <tr>
                <th>Amount</th>
                <th class="hidden sm:table-cell">Client</th>
                <th>More details</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="action in actions" :key="action.id">
                    <td class="relative py-5 pr-6">
                    <div class="flex gap-x-6">
                        <component :is="action.icon" class="hidden h-6 w-5 flex-none text-gray-400 sm:block" aria-hidden="true" />
                        <div class="flex-auto">
                        <div class="flex items-start gap-x-3">
                            <div class="text-sm font-medium leading-6 text-gray-900">{{ action.amount }}</div>
                            <div :class="[statuses[action.status], 'rounded-md py-1 px-2 text-xs font-medium ring-1 ring-inset']">{{ action.status }}</div>
                        </div>
                        <div v-if="action.tax" class="mt-1 text-xs leading-5 text-gray-500">{{ action.tax }}</div>
                        </div>
                    </div>
                    <div class="absolute bottom-0 right-full h-px w-screen bg-gray-100" />
                    <div class="absolute bottom-0 left-0 h-px w-screen bg-gray-100" />
                    </td>
                    <td class="hidden py-5 pr-6 sm:table-cell">
                    <div class="text-sm leading-6 text-gray-900">{{ action.client }}</div>
                    <div class="mt-1 text-xs leading-5 text-gray-500">{{ action.description }}</div>
                    </td>
                    <td class="py-5 text-right">
                    <div class="flex justify-end">
                        <a :href="action.href" class="text-sm font-medium leading-6 text-indigo-600 hover:text-indigo-500"
                        >View<span class="hidden sm:inline"> grade</span><span class="sr-only">, invoice #{{ action.invoiceNumber }}, {{ action.client }}</span></a
                        >
                    </div>
                    <!-- <div class="mt-1 text-xs leading-5 text-gray-500">
                        Invoice <span class="text-gray-900">#{{ action.invoiceNumber }}</span>
                    </div> -->
                    </td>
                </tr>
            </tbody>
            </table>
        </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import {
  ArrowDownCircleIcon,
  ArrowPathIcon,
  ArrowUpCircleIcon,
  Bars3Icon,
  EllipsisHorizontalIcon,
  PlusSmallIcon,
} from '@heroicons/vue/20/solid'
import { BellIcon, XMarkIcon } from '@heroicons/vue/24/outline'

const statuses = {
  Graded: 'text-green-700 bg-green-50 ring-green-600/20',
  Changed: 'text-gray-600 bg-gray-50 ring-gray-500/10',
  Missing: 'text-red-700 bg-red-50 ring-red-600/10',
}
const actions = [
  {
    id: 1,
    href: '#',
    amount: 'APCSP Unit 10 Test',
    tax: 'Grade: 20/100',
    status: 'Graded',
    client: 'March 21, 2024',
    icon: ArrowUpCircleIcon,
  },
  {
    id: 2,
    href: '#',
    amount: 'AP Macroeconomics Unit 5 Test',
    tax: 'Grade: 30/100 -> 50/100',
    status: 'Changed',
    client: 'March 20, 2024',
    icon: ArrowPathIcon,
  },
  {
    id: 3,
    href: '#',
    amount: 'AP Calculus BC Homework 4.2',
    tax: 'Missing',
    status: 'Missing',
    client: 'March 19, 2024',
    icon: XMarkIcon,
  },
  {
    id: 3,
    href: '#',
    amount: 'AP Calculus BC Homework 4.2',
    tax: 'Missing',
    status: 'Missing',
    client: 'March 19, 2024',
    icon: XMarkIcon,
  },
]

const mobileMenuOpen = ref(false)
</script>

<script>
export default {
  name: "RecentActivityComponent"
}
</script>
