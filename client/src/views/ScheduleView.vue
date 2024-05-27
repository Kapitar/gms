<template>
  <main class="py-10 lg:pl-72">
    <div class="px-4 sm:px-6 lg:px-8">
        <ScheduleHeadingComponent/>
        <DayPickerComponent/>

        <div class="schedule mt-5">
          <ClassComponent/>
        </div>
    </div>
  </main>


</template>

<script>
import DayPickerComponent from "../components/DayPickerComponent.vue";
import ScheduleHeadingComponent from "../components/ScheduleHeadingComponent.vue"
import ClassComponent from "../components/ClassComponent.vue"
import ClassSeperatorComponent from "../components/ClassSeperatorComponent.vue"

export default {
  name: "DashboardView",
  components: {
    ScheduleHeadingComponent,
    DayPickerComponent,
    ClassComponent,
    ClassSeperatorComponent
  }
}
</script>