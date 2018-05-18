---
Description: 'The installer stores all information about the user interface in the tables of the installation database.'
ms.assetid: '56d8ecb4-6c95-46c6-98dc-3118d2061101'
title: Previewing the User Interface
---

# Previewing the User Interface

The installer stores all information about the [user interface](user-interface.md) in the tables of the installation database. To facilitate the design of the UI the installer also provides a preview mode for viewing this information. The following procedure describes how to enable the UI preview mode and display the current appearance of dialog boxes and billboards.

**To view the user interface in the preview mode**

1.  Enable the preview mode by calling the [**MsiEnableUIPreview**](msienableuipreview.md) function.
2.  Display the particular dialog boxes by calling the [**MsiPreviewDialog**](msipreviewdialog.md) function.
3.  Display particular billboards by calling the [**MsiPreviewBillboard**](msipreviewbillboard.md) function.

 

 



