<template>
  <div>
    <h3 class="mb-5">
      <span class="text-orange-dark">Question {{ questionNumber }}</span><span class="text-grey text-sm">/{{ nbQuestions }}</span>
    </h3>

    <template v-if="question.image">
      <div class="bg-white rounded sm:p-1 shadow mb-8">
        <img class="w-full rounded" :src="question.image">
      </div>
    </template>

    <strong>{{ question.text }}</strong>

    <div class="mt-5">
      <template v-if="!resultStage">
        <template v-if="question.type === 'tf'">
          <input type="radio" name="currentQuestion" id="trueAnswer" v-model="answer" value="t" class="mb-4"><label for="trueAnswer" class="mx-2">Vrai</label><br/>
          <input type="radio" name="currentQuestion" id="falseAnswer" v-model="answer" value="f"><label for="falseAnswer" class="mx-2">Faux</label><br/>
        </template>

        <template v-if="question.type === 'mc'">
          <div v-for="(mcanswer, index) in question.answers" :key='index'>
          <input type="radio" :id="'answer'+index" name="currentQuestion" v-model="answer" :value="mcanswer" class="mb-4"><label :for="'answer'+index" class="mx-2">{{mcanswer}}</label><br/>
          </div>
        </template>

        <button
          @click="checkAnswer"
          class="bg-blue hover:bg-blue-dark text-white font-bold py-2 px-4 rounded mt-8">
          Continuer
        </button>
      </template>

      <template v-if="resultStage">
        <div v-if="answerIsGood" class="text-green">
          Bonne réponse !
        </div>
        <div v-else class="text-red">
          Oups, pas tout à fait.
        </div>

        <div class="my-5">
          La bonne réponse est : {{ presentedAnswer }}.
        </div>

        <div class="border-l-2 border-grey sm:ml-2 ml-1 sm:p-2 p-1 pl-3 text-sm">
          {{ question.explanations }}
        </div>

        <button
          @click="submitAnswer"
          class="bg-blue hover:bg-blue-dark text-white font-bold py-2 px-4 rounded mt-8">
          Continuer
        </button>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Question',
  props: ['question', 'question-number', 'nbQuestions'],
  data () {
    return {
      answer: '',
      resultStage: false
    }
  },
  methods: {
    submitAnswer: function () {
      this.$emit('answer', {answer: this.answer})
      this.answer = null
      this.resultStage = false
    },
    checkAnswer: function () {
      this.resultStage = true
    }
  },
  computed: {
    answerIsGood: function () {
      return this.answer === this.question.answer
    },
    presentedAnswer: function () {
      if (this.question.type === 'tf') {
        return (this.question.answer === 't') ? 'Vrai' : 'Faux'
      }
      return this.question.answer
    }
  }
}
</script>
