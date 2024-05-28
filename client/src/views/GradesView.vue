<template>
  <main class="py-10 lg:pl-72">
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="hs-accordion-group">
        <div v-for="course in classes" :key="course.name" class="hs-accordion hs-accordion-active:border-gray-200 bg-white border border-transparent rounded-xl mb-4 shadow" id="hs-active-bordered-heading-one">
          <button class="hs-accordion-toggle hs-accordion-active:text-indigo-500 inline-flex justify-between items-center gap-x-3 w-full font-semibold text-start text-gray-800 py-5 px-8 hover:text-gray-500 disabled:opacity-50 disabled:pointer-events-none" aria-controls="hs-basic-active-bordered-collapse-one">
            <div class="accordion-class">
              <div class="accordion-class-name text-xl">
                {{ course.name }}
              </div>
              <div class="accordion-class-teacher text-sm font-normal">
                {{ course.teacher }}
              </div>
            </div>
            <div class="block rounded-md bg-indigo-500 p-3 text-white text-xl font-semibold">
              97
              <!-- <component :is="item.icon" class="h-6 w-6 text-white" aria-hidden="true" /> -->
            </div>

            <!-- <svg class="hs-accordion-active:hidden block size-3.5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14"></path>
              <path d="M12 5v14"></path>
            </svg>
            <svg class="hs-accordion-active:block hidden size-3.5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14"></path>
            </svg> -->
          </button>
          <div id="hs-basic-active-bordered-collapse-one" class="hs-accordion-content hidden w-full overflow-hidden transition-[height] duration-300" aria-labelledby="hs-active-bordered-heading-one">
            <div class="pb-5 px-6 sm:px-6 lg:px-6">
              <div class="flow-root">
                <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                  <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
                    <table class="min-w-full table-fixed">
                      <thead class="bg-white">
                        <tr>
                          <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-3 break-all">Assigment</th>
                          <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">Points</th>
                          <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">Average</th>
                          <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold text-gray-900">Status</th>
                          <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-3">
                            <span class="sr-only">Details</span>
                          </th>
                        </tr>
                      </thead>
                      <tbody class="bg-white">
                        <template v-for="section in course.sections" :key="section.name">
                          <tr class="border-t border-gray-200">
                            <th colspan="5" scope="colgroup" class="bg-gray-50 py-2 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-3 break-all">{{ section.name }}</th>
                          </tr> 
                          <tr v-for="(assignment, assignmentId) in section.assignments" :key="assignment.email" :class="[assignmentId === 0 ? 'border-gray-300' : 'border-gray-200', 'border-t']">
                            <td class="py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-3">{{ assignment.name }}</td>
                            <td class="whitespace-nowrap text-center px-3 py-4 text-sm text-gray-500">{{ assignment.title }}</td>
                            <td class="whitespace-nowrap text-center px-3 py-4 text-sm text-gray-500">{{ assignment.email }}</td>
                            <td class="whitespace-nowrap text-center px-3 py-4 text-sm text-gray-500">{{ assignment.role }}</td>
                            <td class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-3">
                              <a href="#" @click="open=true" class="text-indigo-600 hover:text-indigo-900"
                                >Details<span class="sr-only">, {{ assignment.name }}</span></a
                              >
                            </td>
                          </tr>
                          <tr class="border-t border-gray-200">
                            <th colspan="5" scope="colgroup" class="py-4 pl-4 pr-3 text-right text-sm font-semibold text-gray-900 sm:pl-3">Category Average: 72</th>
                          </tr>
                        </template>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>

  <TransitionRoot class="z-50" as="template" :show="open">
    <Dialog as="div" class="relative z-10" @close="open = false">
      <TransitionChild as="template" enter="ease-in-out duration-500" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in-out duration-500" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-hidden">
        <div class="absolute inset-0 overflow-hidden">
          <div class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10">
            <TransitionChild as="template" enter="transform transition ease-in-out duration-500 sm:duration-700" enter-from="translate-x-full" enter-to="translate-x-0" leave="transform transition ease-in-out duration-500 sm:duration-700" leave-from="translate-x-0" leave-to="translate-x-full">
              <DialogPanel class="pointer-events-auto relative w-96">
                <TransitionChild as="template" enter="ease-in-out duration-500" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in-out duration-500" leave-from="opacity-100" leave-to="opacity-0">
                  <div class="absolute left-0 top-0 -ml-8 flex pr-2 pt-4 sm:-ml-10 sm:pr-4">
                    <button type="button" class="relative rounded-md text-gray-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-white" @click="open = false">
                      <span class="absolute -inset-2.5" />
                      <span class="sr-only">Close panel</span>
                      <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                    </button>
                  </div>
                </TransitionChild>
                <div class="h-full overflow-y-auto bg-white p-8">
                  <div class="space-y-6 pb-16">
                    <div>
                      <div class="mt-4 flex items-start justify-between">
                        <div>
                          <h2 class="text-base font-semibold leading-6 text-gray-900"><span class="sr-only">Details for </span>Quiz 7.4 - 7.8</h2>
                          <p class="text-sm font-medium text-gray-500">Formative</p>
                        </div>
                      </div>
                    </div>
                    <div>
                      <h3 class="font-medium text-gray-900">Information</h3>
                      <dl class="mt-2 divide-y divide-gray-200 border-b border-t border-gray-200">
                        <div class="flex justify-between py-3 text-sm font-medium">
                          <dt class="text-gray-500">Points</dt>
                          <dd class="text-gray-900">70/100</dd>
                        </div>
                        <div class="flex justify-between py-3 text-sm font-medium">
                          <dt class="text-gray-500">Average</dt>
                          <dd class="text-gray-900">70</dd>
                        </div>
                        <div class="flex justify-between py-3 text-sm font-medium">
                          <dt class="text-gray-500">Status</dt>
                          <dd class="text-gray-900">Graded</dd>
                        </div>
                        <div class="flex justify-between py-3 text-sm font-medium">
                          <dt class="text-gray-500">Date</dt>
                          <dd class="text-gray-900">March 20, 2024</dd>
                        </div>
                      </dl>
                    </div>
                    <div>
                      <h3 class="font-medium text-gray-900">Notes</h3>
                      <div class="mt-2 flex items-center justify-between">
                        <p class="text-sm italic text-gray-500">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus, rem, doloribus necessitatibus perferendis quidem assumenda dolores, deleniti a aspernatur consequuntur corporis delectus odit numquam. Nemo aliquid sunt soluta deleniti quasi!</p>
                      </div>
                    </div>
                    <div>
                      <h3 class="font-medium text-gray-900">Teacher</h3>
                      <ul role="list" class="mt-2 divide-y divide-gray-200 border-b border-t border-gray-200">
                        <li class="flex items-center justify-between py-3">
                          <div class="flex items-center">
                            <img src="https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg" alt="" class="h-8 w-8 rounded-full" />
                            <p class="ml-4 text-sm font-medium text-gray-900">Dr. Barnes</p>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { HeartIcon, XMarkIcon } from '@heroicons/vue/24/outline'
import { PencilIcon, PlusIcon } from '@heroicons/vue/20/solid'

const open = ref(false)

const classes = [
  {
    name: "AP Computer Science A",
    teacher: "Dr. Barnes",
    sections: [
      {
        name: 'Formative 40%',
        assignments: [
          { name: 'Quiz 7.4-7.8 really long assignment name bluh bluh bluh', title: '70/100', email: '70', role: 'Graded' },
          { name: 'Quiz 7.4-7.8', title: '70/100', email: '70', role: 'Graded' },
          { name: 'Quiz 7.4-7.8', title: '70/100', email: '70', role: 'Graded' },
        ],
      },
      {
        name: 'Summative 60%',
        assignments: [
          { name: 'Unit 7 Test', title: '70/100', email: '70', role: 'Graded' },
        ],
      }
    ]
  },
  {
    name: "AP Computer Science Principles",
    teacher: "Dr. Barnes",
    sections: [
      {
        name: 'Formative 40%',
        assignments: [
          { name: 'Quiz 7.4-7.8', title: '70/100', email: '70', role: 'Graded' },
          { name: 'Quiz 7.4-7.8', title: '70/100', email: '70', role: 'Graded' },
          { name: 'Quiz 7.4-7.8', title: '70/100', email: '70', role: 'Graded' },
        ],
      },
      {
        name: 'Summative 60%',
        assignments: [
          { name: 'Unit 7 Test', title: '70/100', email: '70', role: 'Graded' },
        ],
      }
    ]
  }
]
 
</script>

<script>
export default {
  name: "GradesView",
  components: {

  }
}
</script>