import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "Install-Module.ps1"
template = templateEnv.get_template(TEMPLATE_FILE)


data = {
    "module_name" = "MyModule"
}

outputText = template.render(data)

# maybe i can functionize the above and loop through module files to render?
# need to research more jinja2 capabilities.