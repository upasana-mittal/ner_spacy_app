from flask import Flask, Response, request
import json
from src.NamedEntity import *

app = Flask(__name__)

@app.route("/health", methods=['GET'])
def get_status():
    return Response(json.dumps({"status":"UP"}), status=200, mimetype='application/json')

@app.route("/", methods=['GET'])
def get_help():
    return Response(json.dumps(
        {"languages supported": ["English"],
         "models": {"en_core_web_sm": {"Language": "English",
                                       "Description": "This model is multi-task CNN trained on OntoNotes. "
                                                      "Assigns context-specific token vectors, POS tags, "
                                                      "dependency parse and named entities.",
                                       "Accuracy Metrics": {"F-Score": 85.86,
                                                            "Precision": 86.33,
                                                            "Recall": 85.39}},

                    "en_core_web_md": {"Language": "English",
                                       "Description": "This model is multi-task CNN trained on OntoNotes, "
                                                      "with GloVe vectors trained on Common Crawl. Assigns word vectors, "
                                                      "context-specific token vectors, POS tags, dependency parse and named entities.",
                                       "Accuracy Metrics": {"F-Score": 85.56,
                                                            "Precision": 86.88,
                                                            "Recall": 86.25}},
                    "en_core_web_lg": {"Language": "English",
                                       "Description": "This model is multi-task CNN trained on OntoNotes, with GloVe vectors"
                                                      " trained on Common Crawl. Assigns word vectors, context-specific token vectors,"
                                                      " POS tags, dependency parse and named entities.",
                                       "Accuracy Metrics": {"F-Score": 85.56,
                                                            "Precision": 86.88,
                                                            "Recall": 86.25}}
                    },
         "sample input body": {
             "text": "i will fire you raman prasad. Return my hyundai verna and hyundai creta",
             "model": "en_core_web_sm"
         }
         }
    ), status=200, mimetype='application/json')

@app.route("/predict_entity", methods=["POST"])
def predict_entity_sm():
    text = request.json["text"]
    model = request.json["model"]
    entity_dict = NamedEntityService.get_entities(text, model)
    return Response(json.dumps(entity_dict), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(port = 5000, debug=True, threaded=True)
