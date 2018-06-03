---
title: nonextensible
description: Indicates that the IDispatch implementation includes only the properties and methods listed in the interface description.
ms.assetid: 62e902bf-142d-4a8c-a5dc-2801a77ddd71
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# nonextensible

Indicates that the [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) implementation includes only the properties and methods listed in the interface description.

## Allowed on

Dispinterface, interface.

## Flags

<dl> TYPEFLAG\_FNONEXTENSIBLE  
</dl>

## Remarks

The interface must have the [dual](dual.md) attribute.

By default, Automation assumes that interfaces can add members at run time, meaning that it assumes the interfaces are extensible.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




