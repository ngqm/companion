from dash import Dash, html, dcc, Input, Output
from dash.exceptions import PreventUpdate
from main import get_updated_plan

# example data
with open('description.txt', 'r') as f:
    description = f.read()
with open('schedule.txt', 'r') as f:
    schedule = f.read()
with open('preferences.txt', 'r') as f:
    preferences = f.read()
with open('notice.txt', 'r') as f:
    notice = f.read()
with open('feedback.txt', 'r') as f:
    feedback = f.read()
with open('first.txt', 'r') as f:
    first = f.read()
with open('chat.txt', 'r') as f:
    chat = f.read()

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        children="COMPANION: Facilitating EFL Learners’ Individual Differences Through Natural Language Interactions",
        style = {'textAlign': 'center'}
    ),
    html.Div(
        children=[
            html.H2(
                children='Step 1: Initialization',
                style = {'textAlign': 'center'}
            ),
            html.Div(
                children=[
                    html.Label("Course description/learning goals"),
                    html.Br(),
                    dcc.Textarea(
                        id = 'description',
                        value=description,
                        style={'width': '90%', 'height': 150}
                    ),
                    html.Label("Course schedule"),
                    html.Br(),
                    dcc.Textarea(
                        id = 'schedule',
                        value=schedule,
                        style={'width': '90%', 'height': 150}
                    ),
                    html.Label("Individual preferences"),
                    html.Br(),
                    dcc.Textarea(
                        id = 'preferences',
                        value=preferences,
                        style={'width': '90%', 'height': 150}
                ),
                ],
                style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'}
            ),
            html.Div(
                children=[
                    html.Label("Generated study schedule"),
                    html.Br(),
                    dcc.Textarea(
                        id = 'first_plan',
                        value=first,
                        style={'width': '90%', 'height': 520}
                    ),
                ],
                style={'width': '50%', 'display': 'inline-block'}
            )
        ],
        style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'},
    ),
    html.Div(
        children=[
            html.H2(
                children='Step 2: Continual Update',
                style = {'textAlign': 'center'}
            ),
            html.Div(
                children=[
                    html.Label("Course notice"),
                    html.Br(),
                    dcc.Textarea(
                        id = 'notice',
                        value=notice,
                        style={'width': '90%', 'height': 150}
                    ),
                    html.Label("Feedback"),
                    html.Br(),
                    dcc.Textarea(
                        id = 'feedback',
                        value=feedback,
                        style={'width': '90%', 'height': 150}
                    ),
                    html.Label("Chat"),
                    html.Br(),
                    dcc.Textarea(
                        id = 'chat',
                        value=chat,
                        style={'width': '90%', 'height': 150}
                    ),
                ],
                style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'}
            ),
            html.Div(
                children=[
                    html.Label("Updated study schedule"),
                    html.Br(),
                    dcc.Textarea(
                        id = 'updated_plan',
                        value='E.g., ',
                        style={'width': '90%', 'height': 520}
                    ),
                ],
                style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'}
            )
        ],
        style={'width': '50%', 'display': 'inline-block'},
    ),
    ],)


@app.callback(
    Output('updated_plan', 'value'),
    Input('description', 'value'),
    Input('schedule', 'value'),
    Input('preferences', 'value'),
    Input('first_plan', 'value'),
    Input('notice', 'value'),
    Input('feedback', 'value'),
    Input('feedback', 'n_clicks')
)
def update_output(description, schedule, preferences, first_plan, notice, feedback, n_clicks):
    if n_clicks:
        raise PreventUpdate
    else:
        return get_updated_plan(description, schedule, preferences, first_plan, notice, feedback)


if __name__ == '__main__':
    app.run_server(debug=True)