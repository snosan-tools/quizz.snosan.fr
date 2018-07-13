<template>
  <div id="app">
    <Quiz url="/static/data.json">
      <div slot="intro" slot-scope="props">
        {{props.title}}
      </div>

      <div slot="results" slot-scope="props">
        <h2 class="text-orange mb-3">Félicitations !</h2>
          Tu as bien répondu à {{props.correct}} questions sur {{props.length}}, soit {{props.perc}}%. À bientôt en mer !
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
