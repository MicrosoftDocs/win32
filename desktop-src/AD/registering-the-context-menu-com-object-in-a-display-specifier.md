---
title: Registering the Context Menu COM Object in a Display Specifier
description: This topic shows the registry keys that need to be modified to register a context menu COM object.
ms.assetid: 389bc249-4849-4763-9d1b-b35598a51050
ms.tgt_platform: multiple
keywords:
- Registering the Context Menu COM Object in a Display Specifier
- context menu COM object AD , registering
ms.topic: article
ms.date: 05/31/2018
---

# Registering the Context Menu COM Object in a Display Specifier

When you use COM to create a context menu extension DLL for an Active Directory directory service, the extension must be registered with the Windows registry and Active Directory Domain Services to notify the Active Directory administrative MMC snap-ins and the Windows shell of the extension.

## Registering in the Windows Registry

Like all COM servers, a context menu extension must be registered in the registry. The extension is registered under the following key.

```
HKEY_CLASSES_ROOT
   CLSID
      <clsid>
```

*&lt;clsid&gt;* is the string representation of the CLSID as produced by the [**StringFromCLSID**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) function. Under the *&lt;clsid&gt;* key, there is an **InProcServer32** key that identifies the object as a 32-bit in-proc server. Under the **InProcServer32** key, the location of the DLL is specified in the default value and the threading model is specified in the **ThreadingModel** value. All context menu extension must use the "Apartment" threading model.

## Registering with Active Directory Domain Services

Context menu extension registration is specific to one locale. If the context menu extension applies to all locales, it must be registered in the object class [**displaySpecifier**](/windows/desktop/ADSchema/c-displayspecifier) object in all of the locale subcontainers in the Display Specifiers container. If the context menu extension is localized for a certain locale, it must be registered in the **displaySpecifier** object in that locale's subcontainer. For more information about the Display Specifiers container and locales, see [Display Specifiers](display-specifiers.md) and [DisplaySpecifiers Container](displayspecifiers-container.md).

There are two display specifier attributes that a context menu extension item can be registered under. These are [**adminContextMenu**](/windows/desktop/ADSchema/a-admincontextmenu) and [**shellContextMenu**](/windows/desktop/ADSchema/a-shellcontextmenu).

The [**adminContextMenu**](/windows/desktop/ADSchema/a-admincontextmenu) attribute identifies administrative context menus to display in Active Directory administrative snap-ins. The context menu appears when the user displays the context menu for objects of the appropriate class in one of the Active Directory administrative MMC snap-ins.

The [**shellContextMenu**](/windows/desktop/ADSchema/a-shellcontextmenu) attribute identifies end-user context menus to display in the Windows shell. The context menu appears when the user views the context menu for objects of the appropriate class in the Windows Explorer. Beginning with Windows Server 2003, the Windows shell no longer displays objects of Active Directory Domain Services.

All of these attributes are multi-valued.

When registering a context menu extension, the values for the [**adminContextMenu**](/windows/desktop/ADSchema/a-admincontextmenu) and [**shellContextMenu**](/windows/desktop/ADSchema/a-shellcontextmenu) attributes require the following format.


```C++
<order number>,<clsid>
```



The "&lt;order number&gt;" is an unsigned number that represents the item position in the context menu. When a context menu is displayed, the values are sorted using a comparison of each value's "&lt;order number&gt;". If more than one value has the same "&lt;order number&gt;", those context menu extensions are loaded in the order they are read from the Active Directory server. If possible, use a non-existing "&lt;order number&gt;", that is, one that has not been used by other values in the property. There is no prescribed starting position and gaps are allowed in the "&lt;order number&gt;" sequence.

The "&lt;clsid&gt;" is the string representation of the CLSID as produced by the [**StringFromCLSID**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) function.

In the Windows shell, multiple-selection context menu items are supported. In this case, the context menu extension is invoked for each selected object. In Active Directory administrative snap-ins, multiple-selection context menu extension items are also supported. In this case, the [**DSOBJECTNAMES**](/windows/desktop/api/Dsclient/ns-dsclient-dsobjectnames) structure will contain a [**DSOBJECT**](/windows/desktop/api/Dsclient/ns-dsclient-dsobject) structure for each directory object selected.

> [!IMPORTANT]
> For the Windows shell, display specifier information is retrieved at user logon and cached for the user's session. For the administrative snap-ins, the display specifier data is retrieved when the snap-in is loaded and is cached for the duration of the process. For the Windows shell, this means changes to display specifiers take effect after a user logs off and back on again. For the administrative snap-ins, changes take effect when the snap-in or console file is reloaded, that is, if you start a new instance of the console file or new Mmc.exe instance and add the snap-in, the latest display specifier data is retrieved.

 

For more information, and a code example of how to implement a context menu extension, see [Example Code for Implementation of the Context Menu COM Object](example-code-for-implementation-of-the-context-menu-com-object.md).

 

 
