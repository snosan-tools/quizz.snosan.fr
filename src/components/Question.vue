<template>
  <div>
    <h3 class="text-orange-dark">Question {{ questionNumber }}</h3><br/>
    <strong>{{ question.text }} </strong>

    <div class="mt-5">
      <div v-if="question.type === 'tf'">
        <input type="radio" name="currentQuestion" id="trueAnswer" v-model="answer" value="t" class="mb-4"><label for="trueAnswer" class="mx-2">Vrai</label><br/>
        <input type="radio" name="currentQuestion" id="falseAnswer" v-model="answer" value="f"><label for="falseAnswer" class="mx-2">Faux</label><br/>
      </div>

      <div v-if="question.type === 'mc'">
        <div v-for="(mcanswer, index) in question.answers" :key='index'>
        <input type="radio" :id="'answer'+index" name="currentQuestion" v-model="answer" :value="mcanswer" class="mb-4"><label :for="'answer'+index" class="mx-2">{{mcanswer}}</label><br/>
        </div>
      </div>

      <button @click="submitAnswer" class="bg-blue hover:bg-blue-dark text-white font-bold py-2 px-4 rounded mt-10">Répondre</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Question',
  props: ['question', 'question-number'],
  data () {
    return {
      answer: ''
    }
  },
  methods: {
    submitAnswer: function () {
      this.$emit('answer', {answer: this.answer})
      this.answer = null
    }
  }
}
</script>
