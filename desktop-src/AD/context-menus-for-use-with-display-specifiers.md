---
title: Context Menus for Use with Display Specifiers
description: The Active Directory administrative MMC snap-ins and Windows 2000 shell provide a mechanism to add an item to the context menu displayed for objects in Active Directory Domain Services.
ms.assetid: 0b0691f5-321d-4f22-b39c-bc528db9e707
ms.tgt_platform: multiple
keywords:
- display specifiers AD ,context menus for
ms.topic: article
ms.date: 05/31/2018
---

# Context Menus for Use with Display Specifiers

The Active Directory administrative MMC snap-ins and Windows 2000 shell provide a mechanism to add an item to the context menu displayed for objects in Active Directory Domain Services. A context menu item can be added by implementing an COM in-proc server known as a *context menu extension*. A context menu item can also be added that invokes any file started with the [**ShellExecute**](/windows/win32/api/shellapi/nf-shellapi-shellexecutea) API, such as an application or webpage URL. This is known as a *static context menu item*.

## Developer Audience

This documentation assumes that the reader is familiar with COM operation and component development using C++. It is not currently possible to create an Active Directory Domain Services context menu extension using Microsoft Visual Basic.

## Extending the Context Menu With a Context Menu Extension

A context menu extension is a COM in-proc server that implements certain interfaces and is registered with Active Directory Domain Services.

**To create and install a context menu extension**

1.  Create the context menu extension DLL. A context menu extension is a COM in-proc server that, at a minimum, implements the [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit) and [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) interfaces. For more information, see [Implementing the Context Menu COM Object](implementing-the-context-menu-com-object.md).
2.  Install the context menu sheet extension on computers where the context menu extension is used. This is accomplished by creating a Microsoft Windows Installer package for the context menu extension DLL and deploying the package appropriately using the group policy. For more information, see [Distributing User Interface Components](distributing-user-interface-components.md).
3.  Register the context menu extension in the Windows registry and with Active Directory Domain Services. For more information, see [Registering the Context Menu COM Object in a Display Specifier](registering-the-context-menu-com-object-in-a-display-specifier.md).

## Extending the Context Menu With a Static Context Menu Item

A static context menu item can be used to invoke any file started with the [**ShellExecute**](/windows/win32/api/shellapi/nf-shellapi-shellexecutea) API, such as an application or webpage URL. To accomplished this, the static context menu item for a particular object class must be registered so that the static context menu item is added to the context menu of objects of that class. For more information, see [Registering a Static Context Menu Item](registering-a-static-context-menu-item.md).

 

 