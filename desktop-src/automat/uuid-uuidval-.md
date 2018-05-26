---
title: uuid(uuidval)
description: Specifies the universally unique ID (UUID) of the item.
ms.assetid: fdeeb0e0-f2ea-4270-8e4e-b3bad7813508
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# uuid(uuidval)

Specifies the universally unique ID (UUID) of the item.

## Parameters

<dl> <dt>

<span id="uuidval"></span><span id="UUIDVAL"></span>*uuidval*
</dt> <dd>

A 16-byte value using hexadecimal digits in the following format: 12345678-1234-1234-1234-123456789ABC.

</dd> </dl>

## Allowed on

Required for library, dispinterface, interface, and coclass. Optional but encouraged for struct, enum, union, module, and typedef.

## Remarks

The uuidval value is returned in the [**TYPEATTR**](/windows/previous-versions/OaIdl/ns-oaidl-tagtypeattr?branch=master) structure retrieved by [**ITypeInfo::GetTypeAttr**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo-gettypeattr?branch=master).

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




