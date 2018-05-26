---
Description: The installer stores all information about the user interface in the tables of the installation database.
ms.assetid: 56d8ecb4-6c95-46c6-98dc-3118d2061101
title: Previewing the User Interface
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Previewing the User Interface

The installer stores all information about the [user interface](user-interface.md) in the tables of the installation database. To facilitate the design of the UI the installer also provides a preview mode for viewing this information. The following procedure describes how to enable the UI preview mode and display the current appearance of dialog boxes and billboards.

**To view the user interface in the preview mode**

1.  Enable the preview mode by calling the [**MsiEnableUIPreview**](/windows/win32/Msiquery/nf-msiquery-msienableuipreview?branch=master) function.
2.  Display the particular dialog boxes by calling the [**MsiPreviewDialog**](/windows/win32/Msiquery/nf-msiquery-msipreviewdialoga?branch=master) function.
3.  Display particular billboards by calling the [**MsiPreviewBillboard**](/windows/win32/Msiquery/nf-msiquery-msipreviewbillboarda?branch=master) function.

 

 



