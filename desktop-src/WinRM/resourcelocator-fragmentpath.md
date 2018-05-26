---
title: ResourceLocator.FragmentPath property
description: Gets or sets the path for a resource fragment or property when ResourceLocator is used in Session object operations such as Session.Get, Session.Put, or Session.Enumerate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4d059b57-fca5-4a75-9396-6505920498c3
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
keywords:
- FragmentPath property Windows Remote Management
- FragmentPath property Windows Remote Management , ResourceLocator object
- ResourceLocator object Windows Remote Management , FragmentPath property
topic_type:
- apiref
api_name:
- ResourceLocator.FragmentPath
api_location:
- WSMAuto.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ResourceLocator.FragmentPath property

Gets or sets the path for a [*resource*](windows-remote-management-glossary.md#winrm-gloss-resource) [*fragment*](windows-remote-management-glossary.md#winrm-gloss-fragment) or property when [**ResourceLocator**](resourcelocator.md) is used in [**Session**](session.md) object operations such as [**Session.Get**](session-get.md), [**Session.Put**](session-put.md), or [**Session.Enumerate**](session-enumerate.md).

This property is read/write.

## Syntax


```VB
ResourceLocator.FragmentPath
```



## Property value

String that identifies the fragment or property of the resource. For example, if the resource is a disk drive and the requested property is Manufacturer, the string may contain `Diskdrive/Manufacturer`. The fragment text is case-sensitive. In this case, you cannot use `diskdrive/manufacturer`.

## Remarks

**IWSManResourceLocator::FragmentPath** is the corresponding C++ property.

You can specify one element of an array property by supplying the array index as shown in the following example. Be aware that array indexing starts with 1 rather than 0.


```VB
Const Uri = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_NetworkAdapterConfiguration"
Const FragmentPath = "DNSServerSearchOrder[1]"
```



To get the whole array, specify the array property name as shown in the following example.


```VB
Const Uri = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_NetworkAdapterConfiguration"
Const FragmentPath = "DNSServerSearchOrder"
```



## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**ResourceLocator**](resourcelocator.md)
</dt> </dl>

 

 





