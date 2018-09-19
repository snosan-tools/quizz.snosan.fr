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

    <div v-for="question in questions" :key="question.text" class="hidden">
      <img :src="question.image" alt="preload" v-if="question.image">
    </div>
  </div>
</template>

<script>
import Question from './Question'
import axios from 'axios'
import qs from 'qs'

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
      slug: '',
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
        this.slug = res.slug
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
      this.saveAnswers()
    },
    saveAnswers () {
      const url = process.env.GOOGLE_SHEETS_WEBHOOK_URL
      const data = {}

      this.questions.forEach((a, index) => {
        data[`question_${index + 1}_reponse`] = this.answers[index]
        data[`question_${index + 1}_valide`] = (this.answers[index] === a.answer)
      })

      data['slug'] = this.slug
      data['score'] = this.correct
      data['total'] = this.questions.length

      axios.post(url, qs.stringify(data))
    }
  }
}
</script>
