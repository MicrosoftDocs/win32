---
description: If this bit is set, the dialog box is modal, other dialogs of the same application cannot be put on top of it, and the dialog keeps the control while it is running.
ms.assetid: 14871dc7-c928-4381-a043-6beb06d25214
title: Modal Dialog Style Bit
ms.topic: article
ms.date: 05/31/2018
---

# Modal Dialog Style Bit

If this bit is set, the dialog box is modal, other dialogs of the same application cannot be put on top of it, and the dialog keeps the control while it is running. If this bit is not set, the dialog is modeless, other dialogs of the same application may be moved on top of it. After a modeless dialog is created and displayed, the user interface returns control to the installer. The installer then calls the user interface periodically to update the dialog and to give it a chance to process the messages. As soon as this is done, the control is returned to the installer.

> [!Note]  
> There should be no modeless dialogs in a wizard sequence, since this would return control to the installer, ending the wizard sequence prematurely.

 

## Value



| Decimal | Hexadecimal | Constant                          |
|---------|-------------|-----------------------------------|
| 2       | 0x00000002  | **msidbDialogAttributesSysModal** |



 

 

 



