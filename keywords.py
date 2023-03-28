from multi_rake import Rake

# https://github.com/vgrabovets/multi_rake

# Работает в Google Colab и с Cloud Functions Яндекс Облака - в т.ч. с русским языком
# Не работает на Mac M1 =(


def extract(text, lim=10):
    rake = Rake()
    keywords = rake.apply(text)
    return keywords[:lim]
