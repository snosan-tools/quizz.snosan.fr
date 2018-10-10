<template>
  <div id="app">
    <div v-if="hasQuizz">
      <Quiz :url="quizzURL">
        <div slot="intro" slot-scope="props">
          {{props.title}}
        </div>

        <div slot="results" slot-scope="props">
          <h2 class="text-orange mb-3">Félicitations !</h2>
            Tu as bien répondu à {{props.correct}} questions sur {{props.length}}, soit {{props.perc}}%. À bientôt en mer !
        </div>
      </Quiz>
    </div>

    <div v-if="!hasQuizz">
      <div v-for="item in quizzes" :key="item.slug">
        <a :href="`/?quizz=${item.slug}`" class="no-underline text-white">
          <div class="bg-blue hover:bg-blue-dark py-2 px-4 mt-4">
            {{ item.title }}
          </div>
        </a>
      </div>
    </div>

  </div>
</template>

<script>
import Quiz from './components/Quiz'

export default {
  name: 'App',
  components: {
    Quiz
  },
  data () {
    return {
      quizzes: []
    }
  },
  created () {
    fetch('/static/liste-quizz.json')
      .then(res => res.json())
      .then(res => {
        this.quizzes = res
      })
  },
  computed: {
    hasQuizz: function () {
      return this.quizzValue !== null
    },
    quizzValue: function () {
      return new URL(window.location.href).searchParams.get('quizz')
    },
    quizzURL: function () {
      if (this.quizzValue === null) {
        return null
      }
      return `static/${this.quizzValue}.json`
    }
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
