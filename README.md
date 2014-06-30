Abduction-based Discourse Processing System
===========================================

This is a repository of the ISI metaphor project team, in which we store
all the resources and tools constituting our natural language
understanding system based on abductive reasoning, implemented for four
languages:

- English
- Spanish
- Russian
- Farsi

The system is largely based on ideas summarized in [[Hobbs, 1993]](http://www.isi.edu/~hobbs/interp-abduct-ai.pdf).

Our abductive Natural Language Understanding pipeline is shown below.

![Fig.](https://raw.github.com/metaphor-adp/Metaphor-ADP/master/docs/pics/pipeline-pic.png)

Text fragments are given as input to the pipeline. The text fragments are
parsed. For Russian and Spanish tagging, we use
[TreeTagger](http://www.ims.uni-stuttgart.de/projekte/corplex/TreeTagger/).
For Farsi tagging, we use the [Stanford NLP
tagger](http://nlp.stanford.edu/software/tagger.shtml). For parsing, we
use the dependency parser [Malt](http://www.maltparser.org) for Spanish,
Russian, and Farsi. For English, the whole processing is performed by
the [Boxer](http://svn.ask.it.usyd.edu.au/trac/candc/wiki/boxer)
semantic parser.

The parses are input to the module converting them into logical forms. A
logical form (LF) is a conjunction of propositions, which have
generalized eventuality arguments that can be used for showing
relationships among the propositions. We use logical representations of
natural language texts as described in [[Hobbs,
1995]](http://www.isi.edu/~hobbs/op-acl85.pdf). For Spanish, Russian,
and Farsi, we have developed logical form converters. For English, we
use the LF converter built in the Boxer semantic parser.

Logical forms and a knowledge base are input to the [abductive
reasoner](http://code.google.com/p/henry-n700/) based on Integer Linear
Programming [[Inoue et al.,
2012]](http://www.cl.ecei.tohoku.ac.jp/~naoya-i/resources/jelia2012_paper.pdf).
The reasoner produces flat first order logic interpretations in the
textual format and proof graphs in the PDF format.

More details about each component can be found
[here](https://github.com/metaphor-adp/Metaphor-ADP/blob/master/pipelines/README.md).

---

**Installation and running**

- Clone Metaphor-ADP repository

```
git clone https://github.com/metaphor-adp/Metaphor-ADP
```

- Install external packages and software; see instructions [here](https://github.com/metaphor-adp/Metaphor-ADP/tree/master/installation)

- Run the system; see instructions [here](https://github.com/metaphor-adp/Metaphor-ADP/blob/master/pipelines/common/README.md)

---

**System requirements**

- Linux or Mac
- at least 4 cores CPU
- at least 8GB RAM

---

**Contact**

- Katya Ovchinnikova (e.ovchinnikova@gmail.com)

---

**Publications**

Inoue, N., E. Ovchinnikova, K. Inui and J. R. Hobbs (2014). Weighted
Abduction for Discourse Processing Based on Integer Linear Programming.
In Sukthankar, G., Goldman, R. P., Geib, S., Pynadath, D. V., Hung, H.
B. (eds.) : Plan, Activity, and Intent Recognition, pp. 33-55.
[[Link]](http://store.elsevier.com/Plan-Activity-and-Intent-Recognition/isbn-9780123985323/)

Ovchinnikova, E., Israel, R., Wertheim, S., Zaytsev, V., Montazeri, N,
and Hobbs, J. (2014). Abductive Inference for Interpretation of
Metaphors. In Proc. of ACL 2014 Workshop on Metaphor in NLP. Baltimore,
MD., to appear.

Ovchinnikova, E., N. Montazeri, T. Alexandrov, J. R. Hobbs, M. C.
McCord and R. Mulkar-Mehta (2013). Abductive Reasoning with a Large
Knowledge Base for Discourse Processing. In Hunt, H., Bos, J. and
Pulman, S. (eds.) : Computing Meaning, vol. 4, pp. 104-124.
[[PDF]](http://ovchinnikova.me/papers/IWCS-bookchap-final3.pdf)

Ovchinnikova, E. (2012). Integration of World Knowledge for Natural
Language Understanding, Atlantis Press,
Springer.[[Link]](http://www.springer.com/computer/ai/book/978-94-91216-52-7)

Inoue, N., E. Ovchinnikova, K. Inui, and J. R. Hobbs (2012).
Coreference Resolution with ILP-based Weighted Abduction. In Proceedings
of COLING 2012, pp.1291-1308.
[[PDF]](http://ovchinnikova.me/papers/coling2012_final.pdf)

Ovchinnikova, E., N. Montazeri, T. Alexandrov, J. R. Hobbs, M. C.
McCord and R. Mulkar-Mehta (2011). Abductive Reasoning with a Large
Knowledge Base for Discourse Processing. In Proceedings the 9th
International Conference on Computational Semantics (IWCS'11), pp.
225-234. [[Link]](http://www.aclweb.org/anthology/W/W11/W11-0124.pdf)
