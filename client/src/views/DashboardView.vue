<template>
  <main class="lg:pl-72">
    <div class="xl:pl-96">
      <div class="px-4 py-10 sm:px-6 lg:px-8 lg:py-6">
        <RecentActivityComponent />
        <StatsComponent/>
      </div>
    </div>
  </main>

  <aside class="fixed inset-y-0 left-72 hidden w-96 overflow-y-auto border-r border-gray-200 px-4 py-6 sm:px-6 lg:px-8 xl:block">
    <div class="pb-5">
      <div class="-ml-2 -mt-2 flex flex-wrap items-baseline">
        <h3 class="ml-2 mt-2 text-base font-semibold leading-6 text-gray-900">Schedule</h3>
        <p class="ml-2 mt-1 truncate text-sm text-gray-500">Wednesday</p>
      </div>
    </div>
    <ScheduleComponent/>
  </aside>
</template>

<script>
import ScheduleComponent from '../components/ScheduleComponent.vue';
import RecentActivityComponent from '../components/RecentActivityComponent.vue';
import StatsComponent from '../components/StatsComponent.vue';

export default {
  name: "DashboardView",
  components: {
    ScheduleComponent,
    RecentActivityComponent,
    StatsComponent
  }
}
</script>