---
title: Common Dialog Box Initialization Flags
description: Flags are used to modify the behavior and appearance of a common dialog box.
ms.assetid: '072cdcab-00d1-4a09-97fb-a6de2d51392e'
keywords: ["Common Dialog Box Library,initializing", "common dialog boxes,initializing"]
---

# Common Dialog Box Initialization Flags

Flags are used to modify the behavior and appearance of a common dialog box. Initialization flags are the values that you set in the **Flags** member of the structure that is used to create the dialog box. You use the flags to specify which controls in a dialog box receive initial values, to disable selected controls, and to modify the range of values that the user can set with the controls. You also use the flags to enable hook procedures and custom templates for the dialog boxes.

For example, you can set the **CF\_EFFECTS** value in the **Flags** member of the [**CHOOSEFONT**](choosefont-str.md) structure to direct the **Font** dialog box to display the effects controls. These controls let the user choose a font color as well as strikethrough and underline effects.

The initialization flag values are unique to each common dialog box and are described in detail by the **Flags** members of the following structures that correspond to them:

-   [**CHOOSECOLOR**](choosecolor-str.md)
-   [**CHOOSEFONT**](choosefont-str.md)
-   [**FINDREPLACE**](findreplace-str.md)
-   [**OPENFILENAME**](openfilename-str.md)
-   [**PAGESETUPDLG**](pagesetupdlg-str.md)
-   [**PRINTDLG**](printdlg-str.md)
-   [**PRINTDLGEX**](printdlgex-str.md)

 

 




