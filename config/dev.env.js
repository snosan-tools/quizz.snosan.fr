'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  GOOGLE_SHEETS_WEBHOOK_URL: '"https://script.google.com/macros/s/AKfycbxJczXb08trioEJwaYN8_hIkyJIuDr2Yfwh9_84pmySJJoo1q4G/exec"'
})
