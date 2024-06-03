<template>
  <div>
    <button
      class="hs-accordion-toggle hs-accordion-active:text-indigo-500 inline-flex justify-between items-center gap-x-3 w-full font-semibold text-start text-gray-800 py-5 px-8 hover:text-gray-500 disabled:opacity-50 disabled:pointer-events-none"
      aria-controls="hs-basic-active-bordered-collapse-one">
      <div class="accordion-class">
        <div class="accordion-class-name text-xl">
          {{ course.name }}
        </div>
        <div class="accordion-class-teacher text-sm font-normal">
          {{ course.teacher }}
        </div>
      </div>
      <div class="block rounded-md bg-indigo-500 p-3 text-white text-xl font-semibold">
        {{ course.average }}
      </div>
    </button>
    <div id="hs-basic-active-bordered-collapse-one"
      class="hs-accordion-content hidden w-full overflow-hidden transition-[height] duration-300"
      aria-labelledby="hs-active-bordered-heading-one">
      <div class="pb-5 px-6 sm:px-6 lg:px-6">
        <div class="flow-root">
          <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
              <table class="min-w-full table-fixed">
                <thead class="bg-white">
                  <tr>
                    <th scope="col"
                      class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-3 break-all">
                      Assignment</th>
                    <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">
                      Points
                    </th>
                    <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">
                      Average
                    </th>
                    <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">
                      Status
                    </th>
                    <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-3">
                      <span class="sr-only">Details</span>
                    </th>
                  </tr>
                </thead>
                <tbody class="bg-white">
                  <template v-for="section in course.sections" :key="section.name">
                    <tr class="border-t border-gray-200">
                      <th colspan="5" scope="colgroup"
                        class="bg-gray-50 py-2 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-3 break-all">
                        {{ section.name }}</th>
                    </tr>
                    <tr v-for="(assignment, assignmentId) in section.assignments" :key="assignment.email"
                      :class="[assignmentId === 0 ? 'border-gray-300' : 'border-gray-200', 'border-t']">
                      <td class="py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-3">{{
                        assignment.name }}
                      </td>
                      <td class="whitespace-nowrap text-center px-3 py-4 text-sm text-gray-500">{{
                        assignment.grade }}</td>
                      <td class="whitespace-nowrap text-center px-3 py-4 text-sm text-gray-500">{{
                        assignment.avg }}</td>
                      <td class="whitespace-nowrap text-center px-3 py-4 text-sm text-gray-500">{{
                        assignment.status
                        }}</td>
                      <td class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-3">
                        <a href="#" @click.prevent="openModal(assignment)"
                          class="text-indigo-600 hover:text-indigo-900">Details<span class="sr-only">, {{
                            assignment.name }}</span></a>
                      </td>
                    </tr>
                    <tr class="border-t border-gray-200">
                      <th colspan="5" scope="colgroup"
                        class="py-4 pl-4 pr-3 text-right text-sm font-semibold text-gray-900 sm:pl-3">
                        Category
                        Average: {{ section.average }}</th>
                    </tr>
                  </template>
                </tbody>
              </table>
              <div class="final-grade text-center text-l font-semibold text-gray-900">
                Term Grade: {{ course.grade }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <DetailsModal :open="open" :assignment="selectedAssignment" @close="closeModal" />
  </div>
</template>

<script>
import { ref } from 'vue'
import DetailsModal from './DetailsModalComponent.vue'

export default {
  name: "ClassComponent",
  components: {
    DetailsModal
  },
  props: ["course"],
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
