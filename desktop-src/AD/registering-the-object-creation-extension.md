---
title: Registering the Object Creation Extension
description: When an object creation extension DLL in Active Directory Domain Services is created, it must be registered with the Windows registry and Active Directory Domain Services to make COM and the Active Directory administrative MMC snap-ins aware of the extension.
ms.assetid: 6e950c6c-1a4f-4de0-9be1-004c31d4734c
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Registering the Object Creation Extension

When an object creation extension DLL in Active Directory Domain Services is created, it must be registered with the Windows registry and Active Directory Domain Services to make COM and the Active Directory administrative MMC snap-ins aware of the extension.

## Registering in the Windows Registry

Like all COM servers, an object creation extension must be registered in the Windows registry. The extension is registered under the following key:

```
HKEY_CLASSES_ROOT
   CLSID
      <extension CLSID>
         InProcServer32
            (Default) = <extension path>
            ThreadingModel = Apartment
```

"&lt;extension CLSID&gt;" is the string representation of the CLSID as produced by the [**StringFromCLSID**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) function. "&lt;extension path&gt;" contains the path and file name of the extension DLL. The **ThreadingModel** value for all object creation extensions must be "Apartment".

## Registering with Active Directory Domain Services

Object creation extension registration is specific to one locale. If the object creation extension applies to all locales, it must be registered in the object class's **displaySpecifier** object in all of the locale subcontainers in the DisplaySpecifiers container. If the object creation extension is localized for a certain locale, register it in the **displaySpecifier** object in that locale's subcontainer. For more information about the DisplaySpecifiers container and locales, see [Display Specifiers](display-specifiers.md) and [DisplaySpecifiers Container](displayspecifiers-container.md).

There are two DisplaySpecifier attributes that an object creation extension can be registered under. These are **creationWizard** and **createWizardExt**.

The **creationWizard** attribute identifies primary object creation extensions to replace the existing or native object creation wizard in Active Directory administrative snap-ins. A primary creation extension provides the first set of pages and is hosted in the same way as native pages. This attribute is single-valued and requires the following format:


```C++
<CLSID>
```



The "&lt;CLSID&gt;" is the string representation of the COM object's CLSID as produced by the [**StringFromCLSID**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) function.

The **createWizardExt** attribute identifies secondary object creation extensions. A secondary creation extension adds wizard pages to the native pages or primary extension. This attribute is multi-valued and requires the following format:


```C++
<order number>,<CLSID>
```



The "&lt;order number&gt;" is an unsigned number that represents the page's position in the wizard. When a creation wizard is displayed, the values are sorted using a comparison of each value's "&lt;order number&gt;". If more than one value has the same "&lt;order number&gt;", those pages are loaded in the order they are read from the Active Directory server. If possible, you should use a non-existing "&lt;order number&gt;" (that is, one that has not been used by other values in the property). There is no prescribed starting position, and gaps are allowed in the "&lt;order number&gt;" sequence.

The "&lt;CLSID&gt;" is the string representation of the COM object's CLSID as produced by the [**StringFromCLSID**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) function.

 

 