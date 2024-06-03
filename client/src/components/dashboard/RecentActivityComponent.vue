<template>
  <div>
    <div class="mx-auto max-w-7xl">
      <h2 class="mx-auto max-w-2xl text-base font-semibold leading-6 text-gray-900 lg:mx-0 lg:max-w-none">Recent
        activity</h2>
    </div>
    <div class="mt-3 overflow-hidden">
      <div class="mx-auto max-w-7xl">
        <div class="mx-auto max-w-2xl lg:mx-0 lg:max-w-none">
          <table class="w-full text-left">
            <thead class="sr-only">
              <tr>
                <th>Name</th>
                <th class="hidden sm:table-cell">Client</th>
                <th>More details</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="action in actions" :key="action.id">
                <td class="relative py-5 pr-6">
                  <div class="flex gap-x-6">
                    <component :is="action.icon" class="hidden h-6 w-5 flex-none text-gray-400 sm:block"
                      aria-hidden="true" />
                    <div class="flex-auto">
                      <div class="flex items-start gap-x-3">
                        <div class="text-sm font-medium leading-6 text-gray-900">{{ action.name }}</div>
                        <div
                          :class="[statuses[action.status], 'rounded-md py-1 px-2 text-xs font-medium ring-1 ring-inset']">
                          {{ action.status }}</div>
                      </div>
                      <div v-if="action.description" class="mt-1 text-xs leading-5 text-gray-500">{{ action.description
                        }}</div>
                    </div>
                  </div>
                  <div class="absolute bottom-0 right-full h-px w-screen bg-gray-100" />
                  <div class="absolute bottom-0 left-0 h-px w-screen bg-gray-100" />
                </td>
                <td class="hidden py-5 pr-6 sm:table-cell">
                  <div class="text-sm leading-6 text-gray-900">{{ action.date }}</div>
                </td>
                <td class="py-5 text-right">
                  <div class="flex justify-end">
                    <a href="#" @click.prevent="openModal(action)"
                      class="text-sm font-medium leading-6 text-indigo-600 hover:text-indigo-500">View<span
                        class="hidden sm:inline"> grade</span><span class="sr-only">, invoice #{{ action.invoiceNumber
                        }}, {{ action.client }}</span></a>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <DetailsModal :open="open" :assignment="selectedAssignment" @close="closeModal" />
  </div>
</template>

<script>
import { ref } from 'vue'
import {
  ArrowDownCircleIcon,
  ArrowPathIcon,
  ArrowUpCircleIcon,
} from '@heroicons/vue/20/solid'
import DetailsModal from '../grades/DetailsModalComponent.vue'

export default {
  name: "RecentActivityComponent",
  components: {
    DetailsModal
  },
  data() {
    return {
      statuses: {
        Graded: 'text-green-700 bg-green-50 ring-green-600/20',
        Changed: 'text-gray-600 bg-gray-50 ring-gray-500/10',
        Missing: 'text-red-700 bg-red-50 ring-red-600/10',
      },
      actions: [
        {
          id: 1,
          href: '#',
          name: 'APCSP Unit 10 Test',
          section: "Summative 60%",
          description: 'Grade: 20/100',
          notes: "Corrections due to March 31",
          grade: "20/100",
          avg: 20,
          status: 'Graded',
          date: 'March 21, 2024',
          teacher: "Dr. Barnes",
          icon: ArrowUpCircleIcon,
        },
        {
          id: 2,
          href: '#',
          name: 'Pre-Calculus Homework',
          section: "Formative 40%",
          notes: "No description",
          grade: "0/100",
          teacher: "Mr. Hanawalt",
          avg: 0,
          description: 'Missing',
          status: 'Missing',
          date: 'March 21, 2024',
          icon: ArrowDownCircleIcon,
        },
        {
          id: 3,
          href: '#',
          name: 'APCSA Unit 9 Test',
          section: "Summative 60%",
          description: 'Grade: 20/100 -> 60/100',
          notes: "No description",
          grade: "60/100",
          teacher: "Dr. Barnes",
          avg: 60,
          status: 'Changed',
          date: 'March 21, 2024',
          icon: ArrowPathIcon,
        },
      ]
    }
  },
  setup() {
    const open = ref(false);
    const selectedAssignment = ref(null);

    const openModal = (assignment) => {
      selectedAssignment.value = assignment;
      open.value = true;
    };

    const closeModal = () => {
      open.value = false;
      // selectedAssignment.value = null;
    };

    return {
      open,
      selectedAssignment,
      openModal,
      closeModal
    };
  }
}
</script>
