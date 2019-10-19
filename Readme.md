= Named Entity Recognition using spacy


== Getting started

=== Pre-requisites
You must have Python 3.6 installed on your system.

.Install the virtual environment

    $ pip install virtualenv

.Create the virtual environment

    $ virtualenv -p python3.6 venv

.Activate virtual environment

    $ source venv/bin/activate

.Install the requirements by using the below command:

    $ pip install -r requirements.txt

.Afterwards, install spaCy packages using below commands:

[source, bash]
----
$ python -m spacy download en
$ python -m spacy download en_core_web_md
$ python -m spacy download en_core_web_lg
----


.Run program

    $ python src/main.py
