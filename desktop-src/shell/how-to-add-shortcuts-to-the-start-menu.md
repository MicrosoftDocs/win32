---
Description: To add an item to the Programs submenu, follow these steps.
ms.assetid: F8793C33-2281-4E4A-9659-4189E1C8279A
title: How to Add Shortcuts to the Start Menu
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Add Shortcuts to the Start Menu

To add an item to the **Programs** submenu, follow these steps.

## Instructions

### Step 1:

Create a [shell link](shell.Links) by using the [**IShellLink**](/windows/win32/Shobjidl_core/nn-shobjidl_core-ishelllinka?branch=master) interface.

### Step 2:

Obtain the location of the Programs folder by using the [**SHGetKnownFolderPath**](/windows/win32/shlobj_core/nf-shlobj_core-shgetknownfolderpath?branch=master) function, passing [**FOLDERID\_Programs**](knownfolderid.md).

### Step 3:

Add the Shell link to the Programs folder. You can also create a folder in the Programs folder and add the link to that folder.

 

 



