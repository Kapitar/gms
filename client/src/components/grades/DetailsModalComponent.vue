<template>
  <TransitionRoot class="z-50" as="template" :show="open">
    <Dialog as="div" class="relative z-10" @close="emitClose">
      <TransitionChild as="template" enter="ease-in-out duration-500" enter-from="opacity-0" enter-to="opacity-100"
        leave="ease-in-out duration-500" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-hidden">
        <div class="absolute inset-0 overflow-hidden">
          <div class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10">
            <TransitionChild as="template" enter="transform transition ease-in-out duration-500 sm:duration-700"
              enter-from="translate-x-full" enter-to="translate-x-0"
              leave="transform transition ease-in-out duration-500 sm:duration-700" leave-from="translate-x-0"
              leave-to="translate-x-full">
              <DialogPanel class="pointer-events-auto relative w-96">
                <TransitionChild as="template" enter="ease-in-out duration-500" enter-from="opacity-0"
                  enter-to="opacity-100" leave="ease-in-out duration-500" leave-from="opacity-100" leave-to="opacity-0">
                  <div class="absolute left-0 top-0 -ml-8 flex pr-2 pt-4 sm:-ml-10 sm:pr-4">
                    <button type="button"
                      class="relative rounded-md text-gray-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-white"
                      @click="emitClose">
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
                          <h2 class="text-base font-semibold leading-6 text-gray-900"><span class="sr-only">Details for
                            </span>{{ assignment.name }}</h2>
                          <p class="text-sm font-medium text-gray-500">{{assignment.section}}</p>
                        </div>
                      </div>
                    </div>
                    <div>
                      <h3 class="font-medium text-gray-900">Information</h3>
                      <dl class="mt-2 divide-y divide-gray-200 border-b border-t border-gray-200">
                        <div class="flex justify-between py-3 text-sm font-medium">
                          <dt class="text-gray-500">Points</dt>
                          <dd class="text-gray-900">{{ assignment.grade }}</dd>
                        </div>
                        <div class="flex justify-between py-3 text-sm font-medium">
                          <dt class="text-gray-500">Average</dt>
                          <dd class="text-gray-900">{{ assignment.avg }}</dd>
                        </div>
                        <div class="flex justify-between py-3 text-sm font-medium">
                          <dt class="text-gray-500">Status</dt>
                          <dd class="text-gray-900">{{ assignment.status }}</dd>
                        </div>
                        <div class="flex justify-between py-3 text-sm font-medium">
                          <dt class="text-gray-500">Date</dt>
                          <dd class="text-gray-900">{{ assignment.date }}</dd>
                        </div>
                      </dl>
                    </div>
                    <div>
                      <h3 class="font-medium text-gray-900">Notes</h3>
                      <div class="mt-2 flex items-center justify-between">
                        <p class="text-sm italic text-gray-500">{{ assignment.notes }}
                        </p>
                      </div>
                    </div>
                    <div>
                      <h3 class="font-medium text-gray-900">Teacher</h3>
                      <ul role="list" class="mt-2 divide-y divide-gray-200 border-b border-t border-gray-200">
                        <li class="flex items-center justify-between py-3">
                          <div class="flex items-center">
                            <img
                              src="https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg"
                              alt="" class="h-8 w-8 rounded-full" />
                            <p class="ml-4 text-sm font-medium text-gray-900">{{ assignment.teacher }}</p>
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

<script>
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XMarkIcon } from '@heroicons/vue/24/outline'

export default {
  name: "DetailsModalComponent",
  props: ["open", "assignment"],
  components: {
    Dialog,
    DialogPanel,
    TransitionChild,
    TransitionRoot,
    XMarkIcon
  },
  methods: {
    emitClose() {
      this.$emit('close');
    }
  }
}
</script>