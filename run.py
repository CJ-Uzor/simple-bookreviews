from app import create_app

app = create_app()

# list all routes, similar to ruby on rails 'rake routes'
@app.cli.command()
def routes():
    #Display registered routes
    rules = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))

    sort_by_rule = operator.itemgetter(2)
    for endpoint, methods, rule in sorted(rules, key=sort_by_rule):
        route = '{:50s} {:25s} {}'.format(endpoint, methods, rule)
        print(route)

