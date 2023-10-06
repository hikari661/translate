## Ansible Collection - hikari661.argostranslate

This collection contains 1 x very simple module which interfaces with the argos-translate offline translation engine. 

The module allows you to translate some text between any of the supported argos-translate language models.

For the translate module to work, you must have argos-translate installed in your environment. It should be as simple as:

```
pip install argostranslate # Install the argos-translate engine
argospm install translate  # Install all the language models.
argospm install translate-en_ja # Save space by only installing the language model you need
```

See https://github.com/argosopentech/argos-translate/ for other installation options.   

Here is an example:

```
- name: Translate from English to Japanese
  hikari661.argostranslate.translate:
    text: 'My dog is very muddy.'
    source: 'en'
    target: 'ja'
```

The module would output the following:

```
localhost | CHANGED => {
    "changed": true,
    "translated_text": "私の犬は非常に泥だめです",
    "original_text": "My dog is very muddy"
}
```

## ansible-builder

Under the /docs folder of the collection is a sample ansible-builder definition which configures this colleciton and all python dependencies in a custom execution environment. You can use this as a starting point to build your custom EE.
