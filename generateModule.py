import jinja2
import os

data = {
    "module_name": "MyModule",
    "friendly_name": "MyMod"
}

def renderTemplate(TEMPLATE_FILE):
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(TEMPLATE_FILE)
    return template.render(data)

def getTemplates(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return(paths)

templates = getTemplates('TemplateModule', '1')

for template in templates:
     outputText = renderTemplate(template)
     print(outputText)