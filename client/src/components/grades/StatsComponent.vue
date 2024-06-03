<template>
  <div class="pb-5">
    <dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-2">
      <div v-for="item in stats" :key="item.id"
        class="relative overflow-hidden rounded-lg bg-white px-4 pt-5 shadow sm:px-6 sm:pt-6">
        <dt>
          <div class="absolute rounded-md bg-indigo-500 p-3">
            <component :is="item.icon" class="h-6 w-6 text-white" aria-hidden="true" />
          </div>
          <p class="ml-16 truncate text-sm font-medium text-gray-500">{{ item.name }}</p>
        </dt>
        <dd class="ml-16 flex items-baseline pb-6 sm:pb-7">
          <p class="text-2xl font-semibold text-gray-900">{{ item.stat }}</p>
        </dd>
      </div>
    </dl>
  </div>
</template>

<script>
import { HeartIcon, XMarkIcon, StarIcon, SparklesIcon } from '@heroicons/vue/24/outline'

export default {
  name: "StatsComponent",
  data() {
    return {
      stats: [
        { id: 1, name: 'Weighted GPA', stat: '4.17', icon: StarIcon },
        { id: 2, name: 'Unweighted GPA', stat: '3.97', icon: SparklesIcon },
      ]
    }
  }
}
</script>
