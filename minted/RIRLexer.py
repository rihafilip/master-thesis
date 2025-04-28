from pygments.lexer import RegexLexer
import pygments.token as T


class CustomLexer(RegexLexer):
    name = "RIR"
    aliases = ["Rir", "rir"]
    filenames = ["*.rir"]

    tokens = {
        "root": [
            (r";.*$", T.Comment.Single),
            (r"^\s+\d+", T.Name.Variable),
            (r"\d+:", T.Name.Namespace),
            (r"\[Prom[^\]]*\]", T.Name.Namespace),
            (
                r"\b(\S*)_\b",
                T.Name.Function,
            ),
            (r"\[[^\[]*\] (Test|Type|Call)#\d+", T.Name.Tag),
            (r"[0-9]+L?", T.Number),
            (r".", T.Text),
        ]
    }
