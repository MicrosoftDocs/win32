---
title: retval
description: Designates the parameter that receives the return value of the member.
ms.assetid: 171d8eb3-ab20-4cb9-a17a-903ebc81c48d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# retval

Designates the parameter that receives the return value of the member.

## Allowed on

Parameters of interface members that describe methods or get properties.

## Flags

<dl> IDLFLAG\_FRETVAL  
</dl>

## Remarks

This attribute can be used only on the last parameter of the member. The parameter must have the [out](out.md) attribute and must be a pointer type.

Parameters with this attribute are not displayed in user-oriented browsers.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




