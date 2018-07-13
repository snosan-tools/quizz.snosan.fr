<template>
  <div id="app">
    <Quiz url="/static/data.json">
      <div slot="intro" slot-scope="props">
        This is my custom quiz header for {{props.title}}.
      </div>

      <div slot="results" slot-scope="props">
        <h2 class="text-orange mb-3">WOWOWOW!</h2>
          You got {{props.correct}} right out of
          {{props.length}} questions.
        Your percentage is {{props.perc}}%.
      </div>
    </Quiz>
  </div>
</template>

<script>
import Quiz from './components/Quiz'

export default {
  name: 'App',
  components: {
    Quiz
  }
}
</script>

<style lang="postcss">
/**
 * This injects Tailwind's base styles, which is a combination of Normalize.css
 * and some additional base styles.
 */
@import 'tailwindcss/preflight';

/**
 * This injects any component classes registered by plugins.
 */
@import 'tailwindcss/components';

/**
 * This injects all of Tailwind's utility classes, based on its config file.
 */
@import 'tailwindcss/utilities';
</style>
