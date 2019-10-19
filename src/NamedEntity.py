import en_core_web_lg, en_core_web_sm, en_core_web_md

class NamedEntityService(object):
    model1 = None  # Where we keep the model when it's loaded
    model2 = None  # Where we keep the model when it's loaded
    model3 = None  # Where we keep the model when it's loaded

    @classmethod
    def get_model1(cls):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model1 is None:
            cls.model1 = en_core_web_sm.load()
        return cls.model1

    @classmethod
    def get_model2(cls):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model2 is None:
            cls.model2 = en_core_web_md.load()
        return cls.model2

    @classmethod
    def get_model3(cls):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model3 is None:
            cls.model3 = en_core_web_lg.load()
        return cls.model3

    @classmethod
    def get_entities(cls, input, mod):
        """For the input, get entities and return them."""
        switcher = {
            "en_core_web_sm": cls.get_model1(),
            "en_core_web_md": cls.get_model2(),
            "en_core_web_lg": cls.get_model3()
        }
        clf = switcher.get(mod, cls.get_model1())
        return dict([(str(x), x.label_) for x in clf(input).ents])
