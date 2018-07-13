<template>
  <div>
    <div v-if="introStage">
      <slot name="intro" :title="title">
        <h1>Quizz {{title}}</h1>
      </slot>
      <button @click="startQuiz" class="bg-blue hover:bg-blue-dark text-white font-bold py-2 px-4 rounded mt-10" type="button">Démarrer !</button>
    </div>

    <div v-if="questionStage">
      <Question
        :question="questions[currentQuestion]"
        v-on:answer="handleAnswer"
        :question-number="currentQuestion+1"
        :nb-questions="questions.length"
      ></Question>
    </div>

    <div v-if="resultsStage">
      <slot name="results" :length="questions.length" :perc="perc" :correct="correct">
      Tu as bien répondu à {{correct}} questions sur {{questions.length}}, soit {{perc}}%. Merci !
      </slot>
    </div>
  </div>
</template>

<script>
import Question from './Question'

export default {
  name: 'Quiz',
  components: {
    Question
  },
  props: ['url'],
  data () {
    return {
      introStage: false,
      questionStage: false,
      resultsStage: false,
      title: '',
      questions: [],
      currentQuestion: 0,
      answers: [],
      correct: 0,
      perc: null
    }
  },
  created () {
    fetch(this.url)
      .then(res => res.json())
      .then(res => {
        this.title = res.title
        this.questions = res.questions
        this.introStage = true
      })
  },
  methods: {
    startQuiz () {
      this.introStage = false
      this.questionStage = true
    },
    handleAnswer (e) {
      this.answers[this.currentQuestion] = e.answer
      if ((this.currentQuestion + 1) === this.questions.length) {
        this.handleResults()
        this.questionStage = false
        this.resultsStage = true
      } else {
        this.currentQuestion++
      }
    },
    handleResults () {
      this.questions.forEach((a, index) => {
        if (this.answers[index] === a.answer) this.correct++
      })
      this.perc = ((this.correct / this.questions.length) * 100).toFixed(2)
    }
  }
}
</script>
