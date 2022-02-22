import jinja2
import os
import pathlib
import argparse

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

def renameModuleFiles(templateFilePath):
    if 'module_name' in templateFilePath:
        return templateFilePath.replace('module_name', data['module_name'])
    elif 'friendly_name' in templateFilePath:
        return templateFilePath.replace('friendly_name', data['friendly_name'])
    else:
        return templateFilePath


# main
if __name__ == '__main__':

    # cli arguments for module and friendly names
    parser = argparse.ArgumentParser(description="Pass names for module name for folders and friendly name for cmdlets e.g. --mName WidgetCorp --fName WC")
    parser.add_argument('--mName', '-m', required=True, help='Module name for directories and import-module.')
    parser.add_argument('--fName', '-f', required=True, help='Friendly name for cmdlets e.g. WC gives Set-WCConfiguration.')

    args = parser.parse_args()
    data['module_name'] = args.mName 
    data['friendly_name'] = args.fName 

    os.rename('./TemplateModule/module_name', f'./TemplateModule/{data["module_name"]}')

    templates = getTemplates('TemplateModule', '1')

    for template in templates:
        p = pathlib.PureWindowsPath(template)
        outputText = renderTemplate(p.as_posix())
        with open(template, 'w') as outputFile:
            outputFile.write(outputText)
        os.rename(template, renameModuleFiles(template))
         # print(outputText)