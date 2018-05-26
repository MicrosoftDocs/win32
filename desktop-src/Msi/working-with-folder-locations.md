---
Description: Use these functions to find the source or target of a specified folder in the Directory table of a Windows Installer database.
ms.assetid: 8f9971da-cca8-4623-bdd2-079c4f4859f9
title: Working with Folder Locations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Working with Folder Locations

Use the following functions to find the source or target of a specified folder in the [Directory table](directory-table.md):

-   Obtain the path of the specified source folder by calling the [**MsiGetSourcePath**](/windows/win32/Msiquery/nf-msiquery-msigetsourcepatha?branch=master) function.
-   Obtain the path of the specified target folder by calling the [**MsiGetTargetPath**](/windows/win32/Msiquery/nf-msiquery-msigettargetpatha?branch=master) function.
-   Change the target location for a folder with the [**MsiSetTargetPath**](/windows/win32/Msiquery/nf-msiquery-msisettargetpatha?branch=master) function.

 

 



