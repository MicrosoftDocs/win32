---
title: Loading a Character
description: Loading a Character
ms.assetid: 973de75b-b530-40c6-896d-e2ab0755ae2c
ms.topic: article
ms.date: 05/31/2018
---

# Loading a Character

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

To animate a character, you must first load the character. Use the [**Load**](load-method.md) method to load the character's data. Microsoft Agent supports two formats for character and animation data: a single structured file and separate files. Typically, you use the single file format (.ACS) when the data is stored locally. The multiple file format (.ACF, .ACA) works best when you want to download animations individually, such as when accessing animations from an HTTP server.

A client application can load only a single instance of the same character. Any attempt to load the same character more than once will fail. However, an application can have multiple instances of the same character loaded by providing separate connections to Microsoft Agent. For example, an application could load the same character from two copies of the Microsoft Agent control.

You can also define your own characters for use with Microsoft Agent. You may use any rendering tool you prefer to create the images, provided that you end up with Windows bitmap format files. To assemble and compile a character's images into animations for use with Microsoft Agent, use the Microsoft Agent Character Editor. This tool enables you to define a character's default properties as well as define animations for the character. The Microsoft Agent Character Editor also enables you to select the appropriate file format when you create a character.

 

 




