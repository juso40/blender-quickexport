# quickexport
Quickexport is a simple blender addon that allows quick batch export of selected meshes.

## Installation
1. Click on `Releases` on the right side of this page and download the latest release `quickexport.zip`.
2. In Blender, go to `Edit > Preferences > Add-ons > Install...` and select the downloaded zip file.
3. Enable the addon by clicking on the checkbox next to it.
   
## Usage
With the addon enabled, you can now right click in the outliner on selected objects and use any of the added export options in the ``Quick Export`` submenu.

## FAQ
- What file formats are supported?
  - Currently only ``.obj`` is supported.
- Where can I find the exported files?
  - The files will be exported to the same directory as the blend file. You can also find the directory by pressing the ``Quick Export > Reveal in File Explorer`` button.
- What objects will be exported?
  - Only selected objects will be exported. Objects that are not of type mesh will be skipped.
- How can I change the export directory?
  - You can't.
