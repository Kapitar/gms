<template>
  <main class="lg:pl-72">
    <div class="px-4 sm:px-6 lg:px-8">
    <main>
        <!-- Settings forms -->
        <div class="divide-y divide-grey-500">
          <div class="grid max-w-7xl grid-cols-1 gap-x-8 gap-y-10 px-4 py-16 sm:px-6 md:grid-cols-3 lg:px-8">
            <div>
              <h2 class="text-base font-semibold leading-7 text-black">Personal Information</h2>
              <p class="mt-1 text-sm leading-6 text-gray-500">Request a change if information is misleading</p>
            </div>

            <form class="md:col-span-2">
              <div class="grid grid-cols-1 gap-x-6 gap-y-8 sm:max-w-xl sm:grid-cols-6">
                <div class="col-span-full flex items-center gap-x-8">
                  <img src="https://www.rainforest-alliance.org/wp-content/uploads/2021/06/capybara-square-1.jpg.optimal.jpg" alt="" class="h-24 w-24 flex-none rounded-lg bg-gray-800 object-cover" />
                  <div>
                    <button type="button" class="rounded-md bg-indigo-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Change photo</button>
                    <p class="mt-2 text-xs leading-5 text-gray-500">JPG, GIF or PNG. 1MB max.</p>
                  </div>
                </div>

                <div class="sm:col-span-3">
                  <label for="first-name" class="block text-sm font-medium leading-6 text-black">First name</label>
                  <div class="mt-2">
                    <input type="text" value="Artem" name="first-name" id="first-name" autocomplete="given-name" class="block w-full rounded-md border-0 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>
                </div>

                <div class="sm:col-span-3">
                  <label for="last-name" class="block text-sm font-medium leading-6 text-black">Last name</label>
                  <div class="mt-2">
                    <input type="text" value="Kim" name="last-name" id="last-name" autocomplete="family-name" class="block w-full rounded-md border-0 px-3 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>
                </div>

                <div class="col-span-full">
                  <label for="email" class="block text-sm font-medium leading-6 text-black">Email address</label>
                  <div class="mt-2">
                    <input id="email" value="2025kimat@bfs.or.kr" name="email" type="email" autocomplete="email" class="block w-full rounded-md border-0 px-3 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>
                </div>
              </div>

              <div class="mt-8 flex">
                <button type="submit" class="rounded-md bg-indigo-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Request</button>
              </div>
            </form>
          </div>

          <div class="grid max-w-7xl grid-cols-1 gap-x-8 gap-y-10 px-4 py-16 sm:px-6 md:grid-cols-3 lg:px-8">
            <div>
              <h2 class="text-base font-semibold leading-7 text-black">Change password</h2>
              <p class="mt-1 text-sm leading-6 text-gray-500">Update your password associated with your account.</p>
            </div>

            <form class="md:col-span-2">
              <div class="grid grid-cols-1 gap-x-6 gap-y-8 sm:max-w-xl sm:grid-cols-6">
                <div class="col-span-full">
                  <label for="current-password" class="block text-sm font-medium leading-6 text-black">Current password</label>
                  <div class="mt-2">
                    <input id="current-password" name="current_password" type="password" autocomplete="current-password" class="block w-full rounded-md border-0 px-3 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>
                </div>

                <div class="col-span-full">
                  <label for="new-password" class="block text-sm font-medium leading-6 text-black">New password</label>
                  <div class="mt-2">
                    <input id="new-password" name="new_password" type="password" autocomplete="new-password" class="block w-full rounded-md border-0 px-3 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>
                </div>

                <div class="col-span-full">
                  <label for="confirm-password" class="block text-sm font-medium leading-6 text-black">Confirm password</label>
                  <div class="mt-2">
                    <input id="confirm-password" name="confirm_password" type="password" autocomplete="new-password" class="block w-full rounded-md border-0 px-3 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>
                </div>
              </div>

              <div class="mt-8 flex">
                <button type="submit" class="rounded-md bg-indigo-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Save</button>
              </div>
            </form>
          </div>

          <div class="grid max-w-7xl grid-cols-1 gap-x-8 gap-y-10 px-4 py-16 sm:px-6 md:grid-cols-3 lg:px-8">
            <div>
              <h2 class="text-base font-semibold leading-7 text-black">Log out</h2>
              <p class="mt-1 text-sm leading-6 text-gray-500">Log out of your other sessions across all of your devices.</p>
            </div>

            <form class="md:col-span-2">
              <div class="grid grid-cols-1 gap-x-6 gap-y-8 sm:max-w-xl sm:grid-cols-6">
                <div class="col-span-full">
                  <label for="logout-password" class="block text-sm font-medium leading-6 text-black">Your password</label>
                  <div class="mt-2">
                    <input id="logout-password" name="password" type="password" autocomplete="current-password" class="block w-full rounded-md border-0 px-3 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>
                </div>
              </div>

              <div class="mt-8 flex">
                <button type="submit" class="rounded-md bg-red-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-400">Log out</button>
              </div>
            </form>
          </div>
        </div>
      </main>
    </div>
  </main>
</template>

<script>
export default {
  name: "ProfileView",
  components: {

  }
}
</script>