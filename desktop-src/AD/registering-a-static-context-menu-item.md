---
title: Registering a Static Context Menu Item
description: This topic describes registering a static context menu item displayed for Active Directory objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ed945812-3adb-4058-bdb6-8d9d34468265
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Registering a Static Context Menu Item AD
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Static Context Menu Item

The administrative MMC snap-ins of Active Directory Domain Services and the Windows shell provide a mechanism to add an item to the context menu displayed for objects in Active Directory Domain Services. The context menu can invoke any file that can be started with the [**ShellExecute**](https://msdn.microsoft.com/library/Bb762153(v=VS.85).aspx) API, such as an application or webpage URL.

## Registering with Active Directory Domain Services

Context menu extension registration is specific to one locale. If the context menu extension applies to all locales, it must be registered in the object class [**displaySpecifier**](https://msdn.microsoft.com/library/ms682163) object in all of the locale subcontainers in the Display Specifiers container. If the context menu extension is localized for a certain locale, it must be registered in the **displaySpecifier** object in that locale subcontainer. For more information about the Display Specifiers container and locales, see [Display Specifiers](display-specifiers.md) and [DisplaySpecifiers Container](displayspecifiers-container.md).

There are two display specifier attributes that a static context menu item can be registered under, [**adminContextMenu**](https://msdn.microsoft.com/library/ms675211) and [**shellContextMenu**](https://msdn.microsoft.com/library/ms679807).

The [**adminContextMenu**](https://msdn.microsoft.com/library/ms675211) attribute identifies administrative context menus to display in the administrative snap-ins of Active Directory Domain Services. The context menu appears when the user displays the context menu for objects of the appropriate class in one of the administrative MMC snap-ins.

The [**shellContextMenu**](https://msdn.microsoft.com/library/ms679807) attribute identifies end-user context menus to display in the Windows shell. The context menu appears when the user views the context menu for objects of the appropriate class in the Windows Explorer. Beginning with Windows Server 2003, the Windows shell no longer displays objects that are from Active Directory Domain Services.

All of these attributes are multi-valued.

When registering a static context menu item, the values for the [**adminContextMenu**](https://msdn.microsoft.com/library/ms675211) and [**shellContextMenu**](https://msdn.microsoft.com/library/ms679807) attributes require the following format.


```C++
<order number>,<menu text>,<command>
```



The "<order number>" is an unsigned number that represents the item's position in the context menu. When a context menu is displayed, the values are sorted using a comparison of each value's "<order number>". If more than one value has the same "<order number>", those context menu extensions are loaded in the order they are read from the Active Directory server. If possible, use a non-existing "<order number>", that is, one that has not been used by other values in the property. There is no prescribed starting position, and gaps are allowed in the "<order number>" sequence.

The "<menu text>" is the string displayed in the context menu. The "<menu text>" can include one "&" character that precedes the keyboard shortcut character for the menu item. This will cause the preceded character to be underlined. For example, if the "<menu text>" is "&File", the menu text will be displayed as "File", the "F" will be underlined and "F" will be the keyboard shortcut for the menu item.

The "<command>" is the program or file executed by the snap-in. Either the full path must be specified or the file must exist in the computer path environment variable. The file is invoked using the [**ShellExecute**](https://msdn.microsoft.com/library/Bb762153(v=VS.85).aspx) function. The "<command>" cannot contain additional parameters, for example, Notepad.exe Myfile.txt. Because **ShellExecute** is used, any file or address that can be passed to **ShellExecute** can be used for "<command>". For example, if "<command>" contains "d:\\file.txt", d:\\file.txt will be opened with the application associated with the .txt extension. Likewise, if "<command>" contains "http://www.fabrikam.com", the default web browser is opened and will display the specified webpage. Paths and application names with spaces are allowed. If "<command>" is an application, the selected object's ADsPath and class are passed as command line arguments, separated by a space.

In the Windows shell, multiple-selection context menu items are supported. In this case, the "<command>" is invoked for each selected object. In Active Directory Domain Services' administrative snap-ins, multiple-selection static context menu items are not supported.

> \[!Important\]  
> For the Windows shell, display specifier data is retrieved at user logon and cached for the user's session. For the administrative snap-ins, the display specifier data is retrieved when the snap-in is loaded and is cached for the duration of the process. For the Windows shell, this means changes to display specifiers take effect after a user logs off and back on again. For the administrative snap-ins, changes take effect when the snap-in or console file is reloaded; that is, if you start a new instance of the console file or new Mmc.exe instance and add the snap-in, the latest display specifier data is retrieved.

 

For more information, and a code example, see [Example Code for Installing a Static Context Menu Item](example-code-for-installing-a-static-context-menu-item.md).

 

 




