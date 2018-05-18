---
title: Context Menu and Property Page Extensions
description: You can add context menu items to the existing context menus for a particular object class within the Active Directory Users and Computers snap-in. You can also add property pages to the property sheet of a particular object class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'adc0225f-5953-4e7f-8c4d-028d9726a3e7'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Context Menu and Property Page Extensions

You can add context menu items to the existing context menus for a particular object class within the Active Directory Users and Computers snap-in. You can also add property pages to the property sheet of a particular object class.

For example, you can create a context menu extension that adds menu items to the context menu of the contact class. When a user views a contact object, your context menu items are displayed with other context menu items in the contact context menu.

This section provides generic instructions for writing context menu and property page extensions to the Active Directory Users and Computers snap-in. For more information about creating a snap-in that is both a context menu and a property sheet extension, see [Extending Active Directory Users and Computers](extending-active-directory-users-and-computers.md).

A snap-in is a COM in-process server DLL that exposes certain interfaces to MMC. A snap-in can hold one or more COM objects required to expose the interfaces of the snap-in to MMC.

**To extend context menus with context menu items from an extension snap-in**

1.  Create a context menu extension snap-in. The snap-in must implement and expose the [**IExtendContextMenu**](iextendcontextmenu.md) interface. For more information about creating a context extension snap-in, see [Extending a Primary Snap-in's Context Menu](extending-a-primary-snap-ins-context-menu.md).
2.  Install the context menu extension snap-in on the computers where you want the extension context menu items to be used. It is recommended that you create a Microsoft Installer package for your snap-in DLL and deploy the package appropriately using the group policy. For more information, see [Microsoft Installer Integration](microsoft-installer-integration.md).
3.  Register the context menu extension snap-in for a particular object class so that its context menu items are added to the context menus of objects of that class. Be aware that you can register the same context menu extension object for more than one class.
4.  When the AddMenuItems method of your snap-in is called, the piDataObject value passed in the call is a pointer to the data object of the currently selected Active Directory object. Your snap-in can call the **GetData** method of the data object using the [**CFSTR\_DSOBJECTNAMES clipboard format**](cfstr-dsobjectnames-clipboard-format.md) to extract context information about the selected Active Directory object.

**To extend property sheets with property pages from an extension snap-in**

1.  Create a property sheet extension snap-in. The COM object must implement and expose the IExtendPropertySheet (or **IExtendPropertySheet2**) interface. For more information about creating a property sheet extension snap-in, see [Extending a Primary Snap-in's Property Sheet](extending-a-primary-snap-ins-property-sheet.md).
2.  Install the property sheet extension snap-in on the computers where you want the extension property pages to be used. It is recommended that you create a Microsoft Installer package for your snap-in DLL and deploy the package appropriately using the group policy. For more information, see [Microsoft Installer Integration](microsoft-installer-integration.md).
3.  Register the property sheet extension snap-in for a particular object class so that its property pages are added to the property sheets of objects of that class. Be aware that you can register the same property sheet extension object for more than one class.
4.  When the CreatePropertyPages method of your snap-in is called, the lpIDataObject value passed in the call is a pointer to the data object of the currently selected Active Directory object. Your snap-in can call the GetData method of the data object using the [**CFSTR\_DSOBJECTNAMES clipboard format**](cfstr-dsobjectnames-clipboard-format.md) to extract context information about the selected Active Directory object.

 

 




