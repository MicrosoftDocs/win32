---
title: Object Creation Wizards
description: In the administrative MMC snap-ins of Active Directory Domain Services, the user can create new objects in a directory by opening the context menu for the container where the new object will be created, choosing New, and choosing the class of object to create. Creating new instances of an object starts the object creation wizard. Each object class may specify the use of a specific creation wizard, or it may use a generic creation wizard. For common classes, such as user and organizationalUnit, the Active Directory Users and Computers snap-in provides a standard set of creation wizards.There are two ways to extend a creation wizard Replace an existing wizard, or provide one if one does not exist for the class The existing wizard is replaced by creating a primary object creation extension. A primary creation extension provides the first set of pages and is hosted in the same way as native pages. A primary creation extension also supports the extensibility mechanism so that other creation wizard extensions can be invoked. For an example of a primary extension, see the scpwizard sample in the Platform Software Development Kit (SDK).Extend an existing wizard An existing wizard can be extended with an secondary object creation extension. A secondary creation extension adds wizard pages to the native pages or primary extension. For more information and an example of a secondary creation extension, see the userwizard sample in the Platform SDK.
ms.assetid: 7ac7ec21-72a9-4d1f-80f1-1eb5bfa2b296
ms.tgt_platform: multiple
keywords:
- objects AD ,creation wizards
ms.topic: article
ms.date: 05/31/2018
---

# Object Creation Wizards

In the administrative MMC snap-ins of Active Directory Domain Services, the user can create new objects in a directory by opening the context menu for the container where the new object will be created, choosing **New**, and choosing the class of object to create. Creating new instances of an object starts the object creation wizard. Each object class may specify the use of a specific creation wizard, or it may use a generic creation wizard. For common classes, such as [**user**](/windows/desktop/ADSchema/c-user) and [**organizationalUnit**](/windows/desktop/ADSchema/c-organizationalunit), the Active Directory Users and Computers snap-in provides a standard set of creation wizards.

There are two ways to extend a creation wizard:

-   Replace an existing wizard, or provide one if one does not exist for the class: The existing wizard is replaced by creating a *primary object creation extension*. A primary creation extension provides the first set of pages and is hosted in the same way as native pages. A primary creation extension also supports the extensibility mechanism so that other creation wizard extensions can be invoked. For an example of a primary extension, see the scpwizard sample in the Platform Software Development Kit (SDK).
-   Extend an existing wizard: An existing wizard can be extended with an *secondary object creation extension*. A secondary creation extension adds wizard pages to the native pages or primary extension. For more information and an example of a secondary creation extension, see the userwizard sample in the Platform SDK.

## Developer Audience

This documentation assumes that the reader is familiar with COM operation and component development using C++. It is not currently possible to create an extension to the Active Directory object creation wizard using Visual Basic.

## Creating an Active Directory Object Creation Extension

Both primary and secondary object creation extensions are COM in-proc servers that implement certain interfaces and are registered with Active Directory Domain Services.

**To create and install an object creation extension**

1.  Create the object creation extension DLL. An object creation extension is a COM in-proc server that, at a minimum, implements the [**IDsAdminNewObjExt**](/windows/desktop/api/DSAdmin/nn-dsadmin-idsadminnewobjext) interface. For more information, see [Implementing the Object Creation Extension COM Object](implementing-the-object-creation-extension-com-object.md).
2.  Install the creation extension on computers where the creation extension is to be used. To do this, create a Microsoft Windows Installer package for the creation extension DLL and deploy the package appropriately using the group policy. For more information, see [Distributing User Interface Components](distributing-user-interface-components.md).
3.  Register the creation extension in the Windows registry and with Active Directory Domain Services. For more information, see [Registering the Object Creation Extension](registering-the-object-creation-extension.md).

## Using an Object Creation Wizard

An object creation wizard can also be invoked from an application other than the administrative MMC snap-ins of Active Directory Domain Services. For more information, see [Invoking Creation Wizards from Your Application](invoking-creation-wizards-from-your-application.md).

If a creation wizard is not registered for an object class, the administrative snap-ins provide a generic creation wizard. The generic creation wizard is built at run time from the list of mandatory properties for the class of object created. For each mandatory property, a page is added to the UI. The generic creation wizard is not extensible. If extensibility is required, it must be replaced with a primary object creation extension.

 

 