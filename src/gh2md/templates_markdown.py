BASE = r"""Export of Github issues for [{repo_name}]({repo_url}).{datestring}

{issues}
"""

ISSUE = r"""# [\#{number}]({url}) `{state}`: {title}
{labels}
#### [{author}]({author_url}) opened issue at [{date}]({url}):

{body}

{comments}
<div style="page-break-after: always;"></div>
"""

COMMENT = r"""#### [{author}]({author_url}) commented at [{date}]({url}):

{body}
"""

ISSUE_FILE_FOOTNOTE = r"""

[Export of Github issue for [{repo_name}]({repo_url}).{datestring}]
"""
