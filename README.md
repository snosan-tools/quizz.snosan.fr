# Quizz SNOSAN
Ce répertoire contient le code utilisé par le site https://quizz.snosan.fr, utilisé par le SNOSAN pour des quizzs relatifs à la sécurité en mer.

## Installation
Il faut installer les dépendances en JavaScript et lancer le serveur local
```sh
npm install
HOST=127.0.0.1 npm run dev
```

Puis visiter http://127.0.0.1:8080.

## Stockage des quizzs
Les quizzs sont définis à l'aide de fichiers JSON. Un quizz est défini par :
- Un titre, présenté au début du quizz
- Un slug, identifiant du quizz
- Un ensemble de questions, et pour chaque question :
  - La question
  - Un lien vers une image, optionnelle (idéalement de taille 1000x300 pixels)
  - Le type de question : vrai-faux / bonne réponse unique parmi un ensemble de choix
  - La bonne réponse
  - Des explications complémentaires pour justifier la bonne réponse

Les quizzs sont stockés dans le dossier [static](`static`). Il y a un fichier JSON unique par quizz.

Le site est prévu pour pouvoir avoir plusieurs quizzs. Il est possible de choisir un quizz spécifique grâce à l'URL et le nom du fichier JSON du quizz. Si le quizz est stocké dans le fichier `foo.json`, le quizz est accessible à l'adresse https://quizz.snosan.fr/?quizz=foo.

### Format pour une question vrai-faux
Une question de type vrai-faux à un `type` à la valeur `tf` (true / false). La bonne réponse est indiquée par la valeur de `answer` : `t` pour vrai et `f` pour faux.
```json
{
  "text":"La terre est-elle ronde ?",
  "image": "https://placeimg.com/500/150/nature",
  "type":"tf",
  "answer":"t",
  "explanations": "Lorem ipsum, consectetur adipiscing elit."
}
```

### Format pour une question à choix multiples
Une question de type vrai-faux à un `type` à la valeur `mc`. La bonne réponse est indiquée par la valeur de `answer`.
```json
{
  "text":"Quel est le plus grand chiffre ?",
  "image": "https://placeimg.com/500/150/nature",
  "type":"mc",
  "answers":[
    "1",
    "2",
    "3"
  ],
  "answer":"3",
  "explanations": "Lorem ipsum, consectetur adipiscing elit."
}
```
