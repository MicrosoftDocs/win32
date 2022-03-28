---
description: Most namespace extensions are a subset of the Shell namespace.
ms.assetid: 00b6b281-b157-4a61-9852-8aafd9ba68d3
title: Displaying a Self-Contained View of a Namespace Extension
ms.topic: article
ms.date: 05/31/2018
---

# Displaying a Self-Contained View of a Namespace Extension

Most namespace extensions are a subset of the Shell namespace. When you create a junction point, as described in [Specifying a Namespace Extension's Location](nse-junction.md), Windows Explorer allows users to navigate into and out of your namespace extension just like any other folder. However, it is also possible to use Windows Explorer to display only the contents of your namespace extension. This display option is sometimes referred to as a *rooted view*. Although not commonly used, rooted views might be preferable to normal views for some types of extensions.

With a rooted view, a new instance of Windows Explorer is created that displays the contents of the extension as a separate namespace. The tree view of a rooted view shows only those folders that are part of the extension. Users cannot navigate from a rooted view to other parts of the Shell namespace.

Extensions are implemented in the same way for rooted views as they are for normal views. The only difference is in the way the contents of the extension are displayed by Windows Explorer. It is even possible to have normal and rooted views of the same extension.

To open a view of an extension, you must launch an instance of Explorer.exe with a /root flag. There are several different ways to launch a rooted view, depending on the nature of your extension.

- [How To Use a Junction Point to Open a Rooted View](how-to-use-a-junction-point-to-open-a-rooted-view.md)
- [How To Use a Shortcut File to Open a Rooted View](how-to-use-a-shortcut-file-to-open-a-rooted-view.md)
- [How To Display a Rooted View of a File](how-to-display-a-rooted-view-of-a-file.md)

 

 



