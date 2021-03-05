import config
from jira import JIRA

project_url = ''
source_ticket = ''
parent_ticket = ''
assignee_id = ''


def copy(src, assignee, name=''):
    copy_fields = ['project', 'components', 'labels', 'description']

    src_fields = src.raw['fields']

    old_fields = {f: src_fields[f] for f in copy_fields}

    if name:
        summary = 'CLONE - ' + src.fields.summary.split()[0] + name
    else:
        summary = 'CLONE - ' + src.fields.summary

    new_fields = dict(
        summary=summary, assignee=dict(name=assignee),
        issuetype=dict(id='5'), parent=dict(key=parent_ticket)
    )

    return {**old_fields, **new_fields}

jira = JIRA(project_url, auth=(config.USER, config.PASSWD))

ticket = jira.issue(source_ticket)

fields = copy(ticket, assignee_name)

new_ticket = jira.create_issue(fields=fields)
print(new_ticket)
