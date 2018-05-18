---
title: Display Specifiers
description: In Active Directory Domain Services, an object class, or class, defines a type of object that can be created in Active Directory Domain Services.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '0c31b02b-9fd3-4547-9ebc-d511a10d7106'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# Display Specifiers

In Active Directory Domain Services, an object class, or class, defines a type of object that can be created in Active Directory Domain Services. The definition of each object class is stored as a [**classSchema**](https://msdn.microsoft.com/library/ms680982) object in the [Active Directory Schema](active-directory-schema.md). In addition to the **classSchema** definition, each object class can have one or more display specifiers that specify the user interface data for objects of that class.

A display specifier is an object of the [**displaySpecifier**](https://msdn.microsoft.com/library/ms682163) class. The attributes of a **displaySpecifier** object specify localized user interface data that describes the various UI elements for a particular object class. Display specifiers store data for property sheets, context menus, icons, creation wizards, and localized class and attribute names. For property pages and context menus, the Windows shell and Active Directory administrative snap-ins use this data to form different user interfaces for administrators and end users—one set of property pages and/or context menus can be associated with administrative applications while a different set of elements can be associated with end user applications.

The [**displaySpecifier**](https://msdn.microsoft.com/library/ms682163) objects are stored in locale-specific containers in the DisplaySpecifiers container in the Configuration container, which is replicated to every domain controller in the enterprise forest. The DisplaySpecifiers container has subcontainers that correspond to the various locales supported by the enterprise installation. These subcontainers are named using language identifiers. For example, the name of the locale container for US-English is 409, which corresponds to the hexadecimal language identifier, 0x0409. Thus, an object class can have multiple display specifiers: one in each locale subcontainer. For more information, and a list of possible language identifiers, see [Language Identifier Constants and Strings](https://msdn.microsoft.com/library/windows/desktop/dd318693). For more information about locales, see [Locales and Languages](https://msdn.microsoft.com/library/windows/desktop/dd318716).

The name of a [**displaySpecifier**](https://msdn.microsoft.com/library/ms682163) object is formed by appending the string "-Display" to the [**lDAPDisplayName**](https://msdn.microsoft.com/library/ms676828) of the object class. For example, the name of a **displaySpecifier** object for the [**user**](https://msdn.microsoft.com/library/ms683980) class is "user-Display".

You can add, delete, or modify properties of a class's [**displaySpecifier**](https://msdn.microsoft.com/library/ms682163) objects to specify the UI elements (class name, attribute names, property sheets, context menus, icon, and so on) that appear for each instance of an object of that class.

For more information about display specifiers, see [DisplaySpecifiers Container](displayspecifiers-container.md).

 

 




