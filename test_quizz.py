# -*- coding: utf-8 -*-
import unittest
import glob
import json


class TestQuizz(unittest.TestCase):
    MAX_QUESTIONS_QUIZZ = 15

    def __init__(self, *args, **kwargs):
        super(TestQuizz, self).__init__(*args, **kwargs)
        self.slugs = []

    def test_for_each_quizz(self):
        files = glob.glob("static/*.json")
        files = [f for f in files if 'liste-quizz' not in f]

        for file in files:
            content = json.load(open(file))
            self.general_structure(content)
            self.check_questions(content['questions'])

    def general_structure(self, content):
        self.assertEquals(
            set(content.keys()),
            set(['title', 'slug', 'questions'])
        )

        # Slug is unique accross quizzes
        self.assertNotIn(content['slug'], self.slugs)
        self.slugs.append(content['slug'])

    def check_questions(self, questions):
        self.assertLessEqual(len(questions), self.MAX_QUESTIONS_QUIZZ)

        for question in questions:
            self.assertIn(question['type'], ['mc', 'tf'])

            # Image is not required for now
            question.pop('image', None)

            if question['type'] == 'tf':
                self.assertEquals(
                    set(question.keys()),
                    set(['text', 'type', 'answer', 'explanations'])
                )
                self.assertIn(question['answer'], ['t', 'f'])
            elif question['type'] == 'mc':
                self.assertEquals(
                    set(question.keys()),
                    set(['text', 'type', 'answer', 'explanations', 'answers'])
                )
                self.assertIn(question['answer'], question['answers'])
                self.assertEquals(type(question['answer']), str)
            else:
                raise NotImplementedError
