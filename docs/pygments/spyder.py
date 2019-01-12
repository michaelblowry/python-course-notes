# -*- coding: utf-8 -*-
"""
    pygments.styles.spyder
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A modern style based on Spyder.

    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class SpyderStyle(Style):
    """
    A modern style based on Spyder.
    """

    background_color = "#ffffff"
    default_style = ""

    styles = {
        Whitespace:                "#bbbbbb",
        Comment:                   "italic #adadad",
        Comment.Preproc:           "noitalic #007020",
        Comment.Special:           "noitalic bg:#fff0f0",

        Number:                    "#800000",

        Keyword:                   "#0000ff",

        Operator:                  "#000000",
        Operator.Word:             "bold #000000",

        Name:                      "#000000", 
        Name.Builtin:              "#900090",
        Name.Builtin.Pseudo:       "italic #924900",
        Name.Function:             "bold #000000",
        Name.Class:                "bold #000000",
        Name.Namespace:            "#000000",
        Name.Exception:            "#007020",
        Name.Variable:             "#bb60d5",
        Name.Constant:             "#60add5",
        Name.Label:                "bold #002070",
        Name.Entity:               "bold #d55537",
        Name.Attribute:            "#4070a0",
        Name.Tag:                  "bold #062873",
        Name.Decorator:            "bold #555555",

        String:                    "#00aa00",
        String.Interpol:           "italic #70a0d0",
        String.Escape:             "bold #4070a0",
        String.Regex:              "#235388",
        String.Symbol:             "#517918",
        String.Other:              "#c65d09",

        Number:                    "#800000",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#00A000",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #c65d09",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }
