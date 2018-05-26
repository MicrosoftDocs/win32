---
title: Common Dialog Box Initialization Flags
description: Flags are used to modify the behavior and appearance of a common dialog box.
ms.assetid: 072cdcab-00d1-4a09-97fb-a6de2d51392e
keywords:
- Common Dialog Box Library,initializing
- common dialog boxes,initializing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Common Dialog Box Initialization Flags

Flags are used to modify the behavior and appearance of a common dialog box. Initialization flags are the values that you set in the **Flags** member of the structure that is used to create the dialog box. You use the flags to specify which controls in a dialog box receive initial values, to disable selected controls, and to modify the range of values that the user can set with the controls. You also use the flags to enable hook procedures and custom templates for the dialog boxes.

For example, you can set the **CF\_EFFECTS** value in the **Flags** member of the [**CHOOSEFONT**](/windows/win32/Commdlg/ns-commdlg-tagchoosefonta?branch=master) structure to direct the **Font** dialog box to display the effects controls. These controls let the user choose a font color as well as strikethrough and underline effects.

The initialization flag values are unique to each common dialog box and are described in detail by the **Flags** members of the following structures that correspond to them:

-   [**CHOOSECOLOR**](/windows/win32/Commdlg/ns-commdlg-tagchoosecolora?branch=master)
-   [**CHOOSEFONT**](/windows/win32/Commdlg/ns-commdlg-tagchoosefonta?branch=master)
-   [**FINDREPLACE**](/windows/win32/Commdlg/ns-commdlg-tagfindreplacea?branch=master)
-   [**OPENFILENAME**](/windows/win32/Commdlg/ns-commdlg-tagofna?branch=master)
-   [**PAGESETUPDLG**](/windows/win32/Commdlg/ns-commdlg-tagpsda?branch=master)
-   [**PRINTDLG**](/windows/win32/Commdlg/ns-commdlg-tagpda?branch=master)
-   [**PRINTDLGEX**](/windows/win32/Commdlg/ns-commdlg-tagpdexa?branch=master)

 

 




