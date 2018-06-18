from __future__ import print_function
from __future__ import unicode_literals

from builtins import str, bytes, dict, int

import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from pattern.fr import article, referenced
from pattern.fr import pluralize, singularize
from pattern.fr import comparative, superlative
from pattern.fr import conjugate, lemma, lexeme, tenses
from pattern.fr import NOUN, VERB, ADJECTIVE

# The fr module has a range of tools for word inflection:
# guessing the indefinite article of a word (a/an?),
# pluralization and singularization, comparative and superlative adjectives, verb conjugation.

# INDEFINITE ARTICLE
# ------------------
# The article() function returns the indefinite article (a/an) for a given noun.
# The definitive article is always "the". The plural indefinite is "some".
print(article("oiseau") + " oiseau")
print("")

print(article("mouche") + " mouche")
print("")

# The referenced() function returns a string with article() prepended to the given word.
# The referenced() funtion is non-trivial, as demonstrated with the exception words below:
for word in ["heure", "ligne", "Européen", "université", "hibou", "yclept", "année"]:
    print(referenced(word))
print("")

# PLURALIZATION
# -------------
# The pluralize() function returns the plural form of a singular noun (or adjective).
# The algorithm is robust and handles about 98% of exceptions correctly:
for word in ["pain", "enfant", "cheval", "hibou", "ours", "couteau"]:
    print(pluralize(word))
print(pluralize("bijou", classical=True))
print(pluralize("merveille", classical=True))
print(pluralize("test", classical=False))
print(pluralize("ma", pos=ADJECTIVE))
print("")

# SINGULARIZATION
# ---------------
# The singularize() function returns the singular form of a plural noun (or adjective).
# It is slightly less robust than the pluralize() function.
for word in ["enfants", "chiens", "chevaux", "banals", "tests", "couteaux", 
             "bijoux", "avares", "grilles"]:
    print(singularize(word))
print(singularize("nos", pos=ADJECTIVE))
print("")

# COMPARATIVE & SUPERLATIVE ADJECTIVES
# ------------------------------------
# The comparative() and superlative() functions give the comparative/superlative form of an adjective.
# Words with three or more syllables are simply preceded by "more" or "most".
for word in ["gentil", "gros", "joli", "blessé", "important", "mauvais"]:
    print("%s => %s => %s" % (word, comparative(word), superlative(word)))
print("")

# VERB CONJUGATION
# ----------------
# The lexeme() function returns a list of all possible verb inflections.
# The lemma() function returns the base form (infinitive) of a verb.
print("lexeme: %s" % lexeme("être"))
print("lemma: %s" % lemma("était"))
print("")

# The conjugate() function inflects a verb to another tense.
# You can supply: 
# - tense : INFINITIVE, PRESENT, PAST, 
# - person: 1, 2, 3 or None, 
# - number: SINGULAR, PLURAL,
# - mood  : INDICATIVE, IMPERATIVE,
# - aspect: IMPERFECTIVE, PROGRESSIVE.
# The tense can also be given as an abbreviated alias, e.g., 
# inf, 1sg, 2sg, 3sg, pl, part, 1sgp, 2sgp, 3sgp, ppl, ppart.
from pattern.fr import PRESENT, SINGULAR
print(conjugate("étant", tense=PRESENT, person=1, number=SINGULAR, negated=False))
print(conjugate("étant", tense="1sg", negated=False))
print("")

# Prefer the full constants for code that will be reused/shared.

# The tenses() function returns a list of all tenses for the given verb form.
# Each tense is a tuple of (tense, person, number, mood, aspect).
# For example: tenses("are") => [('present', 2, 'plural', 'indicative', 'imperfective'), ...]
# You can then check if a tense constant is in the list.
# This will also work with aliases, even though they are not explicitly in the list.
from pattern.fr import PRESENT, PLURAL
print(tenses("sommes"))
print((PRESENT, 1, PLURAL) in tenses("sommes"))
print("pl" in tenses("êtes"))