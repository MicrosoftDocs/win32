---
title: entry(entryid)
description: Identifies the entry point in the DLL.
ms.assetid: a193252c-b16b-40a4-886e-fecb71d89b3b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# entry(entryid)

Identifies the entry point in the DLL.

## Parameters

<dl> <dt>

<span id="entryid"></span><span id="ENTRYID"></span>*entryid*
</dt> <dd>

If *entryid* is a string, this is a named entry point. If *entryid* is a number, the entry point is defined by an ordinal.

</dd> </dl>

## Allowed on

Functions in a module (required).

## Remarks

This attribute provides a way to obtain the address of a function in a module. This is typically done by calling [**ITypeInfo::AddressOfMember**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo-addressofmember) or by using GetProcAddress from Windows.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




