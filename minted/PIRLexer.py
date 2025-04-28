from pygments.lexer import RegexLexer
import pygments.token as T


class CustomLexer(RegexLexer):
    name = "PIR"
    aliases = ["Pir", "pir"]
    filenames = ["*.pir"]

    tokens = {
        "root": [
            (r"^#.*$", T.Comment.Single),

            (r"%\d+(\.\d+)?", T.Name.Variable),
            (r"e\d+(\.\d+)?", T.Name.Namespace),
            (r"BB\d+", T.Name.Namespace),
            (r"R_GlobalEnv", T.Name.Namespace),

            (
                r"\b("
                r"StArg|StVar|MkEnv|\(MkEnv\)|Assume|AssumeNot|"
                r"Force!?<[^>]+>|"
                r"Force!?|"
                r"Add|"
                r"LdFun|"
                r"LdVar|"
                r"LdArg|"
                r"LdDots|"
                r"StVarSuper|"
                r"LdVarSuper|"
                r"Branch|"
                r"Phi|"
                r"DotsList|"
                r"ExpandDots|"
                r"AsLogical|"
                r"AsSwitchIdx|"
                r"CheckTrueFalse|"
                r"ColonInputEffects|"
                r"ColonCastLhs|"
                r"ColonCastRhs|"
                r"IsEnvStub|"
                r"Unreachable|"
                r"Return|"
                r"NonLocalReturn|"
                r"MkArg|"
                r"UpdatePromise|"
                r"MkCls|"
                r"ChkMissing|"
                r"ChkFunction|"
                r"Call|"
                r"NamedCall|"
                r"StaticCall|"
                r"CallBuiltin|"
                r"CallSafeBuiltin|"
                r"MaterializeEnv|"
                r"PushContext|"
                r"PopContext|"
                r"DropContext|"
                r"LdFunctionEnv|"
                r"Inc|"
                r"IsType|"
                r"Is|"
                r"Identical|"
                r"ToForSeq|"
                r"Length|"
                r"FrameState|"
                r"Checkpoint|"
                r"Deopt|"
                r"CastType|"
                r"Missing|"
                r"Visible|"
                r"Invisible|"
                r"Names|"
                r"SetNames|"
                r"PirCopy|"
                r"Nop"
                r")\b",
                T.Name.Function,
            ),

            (
                r"\b("
                r"void|"
                r"ct|cp|fs|dr|"
                r"ast|raw|vec|char|real|complex|str|env|code|expression|list|prim|nul|cls|spec|blt|sym|int|lgl|miss|dots|\*dots|other|"
                r"missing|val|num"
                r")\b",
                T.Keyword.Type
            ),

            (r"isA|goto", T.Keyword),

            (r"0x[a-fA-F0-9]+", T.Number.Hex),
            (r"[0-9]+", T.Number),

            (r"(true|false)", T.Keyword.Constant),

            (r"\s+", T.Text),
            (r".", T.Text),
        ]
    }

