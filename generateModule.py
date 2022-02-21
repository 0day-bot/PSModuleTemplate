import jinja2

data = {
    "module_name" = "MyModule"
}

def renderTemplate(TEMPLATE_FILE)
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(TEMPLATE_FILE)
    return template.render(data)


TEMPLATE_FILE = "Install-Module.ps1"
renderTemplate(TEMPLATE_FILE)

outputText = template.render(data)

# maybe i can functionize the above and loop through module files to render?
# need to research more jinja2 capabilities.