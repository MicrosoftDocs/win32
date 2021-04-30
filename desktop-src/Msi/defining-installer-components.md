---
description: The following outlines how to organize your application into Windows Installer components.
ms.assetid: 981a3def-1e59-4703-ad97-c8cd5431375d
title: Defining Installer Components
ms.topic: article
ms.date: 05/31/2018
---

# Defining Installer Components

The following outlines how to organize your application into Windows Installer components.

**To organize an application into components**

1.  Begin by obtaining a directory and file tree for all of the files and other resources used in your application.
2.  Identify any files, registry keys, shortcuts, or other resources that are shared across applications and can be provided by existing components available as [merge modules](merge-modules.md). You must not include any of these resources in the components you author. Instead obtain these components by merging the merge modules into your installation package. The following steps describe how to organize the remaining resources of the application into components.
3.  Define a new component for every .exe, .dll, and .ocx file. Designate these files as the key path files of their components. Assign each component a component code GUID.
4.  Define a new component for every .hlp or .chm help file. Designate these files as the key path files of their components. Add the .cnt or .chi files to the components holding their associated .hlp and .chm files. Assign each component a component code GUID.
5.  Define a new component for every file that serves as a target of a shortcut. Designate these files as the key path files of their components. Assign each component a component code GUID.
6.  Group all of the remaining resources into folders. All resources in each folder must ship together. If there is a possibility that a pair of resources may ship separately in the future, put these in separate folders. Define a new component for every folder. Try to keep the total number of components low to improve performance. Divide the application into many components when it is necessary to have the installer check the validity of the installation thoroughly. Designate any file in the component as the key path file. Assign each component a component code GUID.
7.  Add registry keys to the components. Any registry key that points to a file should be included in that file's component. Other registry keys should be logically grouped with the files that require them.

 

 



