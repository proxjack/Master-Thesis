"""Fusion 360 script: import the rectifiers board OBJ and prep it for rendering.

How to run:
  1. Open Fusion 360.
  2. Utilities tab -> Scripts and Add-Ins (or Shift+S).
  3. "Scripts" tab -> green "+" -> browse to this file -> Run.

What it does:
  1. Creates a new empty design.
  2. Imports Rectifiers_Board_V1.0.pdf.obj (Fusion reads the sibling .mtl
     automatically since both files live in the same folder).
  3. Walks the imported mesh bodies and assigns a plausible appearance to
     each one, based on keywords found in its name (copper / silkscreen /
     solder mask / generic component). Bodies that don't match anything
     are left untouched so you can assign them by hand.
  4. Switches to the Render workspace and frames the model in an
     isometric view so you're ready to pick a scene/lighting and render.

Adjust OBJ_PATH below if you move the file, and tweak APPEARANCE_MAP to
match the actual body names Fusion gives you (check the Bodies folder in
the browser tree after import -- Altium's group/object names don't always
survive the OBJ import 1:1).
"""

import adsk.core
import adsk.fusion
import traceback

OBJ_PATH = r"C:\UNIPD\Magistrale\Master Thesis\Manuscript\Circuits\3Dmodel\Rectifiers_Board_V1.0.pdf.obj"

# keyword (lowercase, matched anywhere in the body name) -> appearance name
# in the stock "Fusion Appearance Library"
APPEARANCE_MAP = {
    'copper': 'Copper - Polished',
    'pad': 'Copper - Polished',
    'via': 'Copper - Polished',
    'trace': 'Copper - Polished',
    'silk': 'Paint - Enamel Glossy (White)',
    'mask': 'Paint - Enamel Glossy (Green)',
    'solder': 'Paint - Enamel Glossy (Green)',
    'component': 'Plastic - Matte (Black)',
    'body': 'Plastic - Matte (Black)',
    'pin': 'Steel - Satin',
    'lead': 'Steel - Satin',
}


def find_appearance_library(app):
    for lib in app.materialLibraries:
        if lib.name == 'Fusion Appearance Library':
            return lib
    return None


def assign_appearances(root_comp, appearance_lib):
    assigned, skipped = 0, 0
    for body in root_comp.meshBodies:
        name = body.name.lower()
        appearance_name = next((v for k, v in APPEARANCE_MAP.items() if k in name), None)
        if appearance_name and appearance_lib:
            appearance = appearance_lib.appearances.itemByName(appearance_name)
            if appearance:
                body.appearance = appearance
                assigned += 1
                continue
        skipped += 1
    return assigned, skipped


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = adsk.fusion.Design.cast(app.activeProduct)
        root_comp = design.rootComponent

        import_manager = app.importManager
        obj_options = import_manager.createOBJImportOptions(OBJ_PATH)
        import_manager.importToTarget(obj_options, root_comp)

        appearance_lib = find_appearance_library(app)
        assigned, skipped = assign_appearances(root_comp, appearance_lib)

        viewport = app.activeViewport
        viewport.camera.viewOrientation = adsk.core.ViewOrientations.IsoTopRightViewOrientation
        viewport.fit()
        viewport.refresh()

        render_workspace = ui.workspaces.itemById('FusionRenderEnvironment')
        if render_workspace:
            render_workspace.activate()

        ui.messageBox(
            'Import completato.\n'
            'Mesh bodies: {}\n'
            'Materiali assegnati automaticamente: {}\n'
            'Da assegnare a mano: {}'.format(
                root_comp.meshBodies.count, assigned, skipped
            )
        )

    except Exception:
        if ui:
            ui.messageBox('Errore:\n{}'.format(traceback.format_exc()))


def stop(context):
    pass
