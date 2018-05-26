---
title: Property Pages for Use with Display Specifiers
description: Active Directory Domain Services provide a mechanism for adding pages to the property sheet displayed for a directory object from the Active Directory administrative snap-ins or the Windows shell.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c1dd84e2-50f9-4903-a4b5-4473515e4d0e
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- display specifiers AD ,property pages for use with
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Property Pages for Use with Display Specifiers

Active Directory Domain Services provide a mechanism for adding pages to the property sheet displayed for a directory object from the Active Directory administrative snap-ins or the Windows shell. To add a page to the property sheet, implement a property sheet extension.

## Developer Audience

This documentation assumes that the reader is familiar with COM operation and component development using C++. It is not currently possible to create an Active Directory property sheet extension using Visual Basic.

## Creating an Active Directory Property Sheet Extension

A *property sheet extension* is a COM in-proc server that implements certain interfaces and is registered with Active Directory Domain Services. To create a property sheet extension, perform the following steps.

**To create an Active Directory property sheet extension**

1.  Create the property sheet extension DLL. A property sheet extension is a COM in-proc server that, at a minimum, implements the [**IShellExtInit**](_win32_ishellextinit_cpp) and [**IShellPropSheetExt**](_win32_ishellpropsheetext_cpp) interfaces. For more information, see [Implementing the Property Page COM Object](implementing-the-property-page-com-object.md).
2.  Install the property sheet extension on the computers where the property sheet extension is to be used. To do this, create a Microsoft Windows Installer package for the property sheet extension DLL and deploy the package appropriately using the group policy. For more information, see [Distributing User Interface Components](distributing-user-interface-components.md).
3.  Register the property sheet extension in the Windows registry and with Active Directory Domain Services. For more information, see [Registering the Property Page COM Object in a Display Specifier](registering-the-property-page-com-object-in-a-display-specifier.md).

 

 




