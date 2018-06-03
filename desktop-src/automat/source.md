---
title: source
description: Indicates that a member is a source of events.
ms.assetid: 7f0e6349-9d31-4ab6-9a91-3822e81188e5
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# source

Indicates that a member is a source of events.

## Allowed on

Member of a coclass, property, or method.

## Flags

<dl> IMPLTYPEFLAG\_FSOURCE  
VARFLAG\_SOURCE  
FUNCFLAG\_SOURCE  
</dl>

## Remarks

For a member of a coclass, this attribute indicates that the member is called rather than implemented.

On a property or method, this attribute indicates that the member returns an object or VARIANT that is a source of events. The object implements the interface [**IConnectionPointContainer**](https://msdn.microsoft.com/library/windows/desktop/ms683857).

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




