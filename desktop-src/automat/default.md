---
title: default
description: Indicates that the interface or dispinterface represents the default programmability interface. Intended for use by macro languages.
ms.assetid: 50501057-73e9-40cf-be7c-411f78e3b084
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# default

Indicates that the interface or dispinterface represents the default programmability interface. Intended for use by macro languages.

## Allowed on

Coclass member.

## Flags

<dl> IMPLTYPEFLAG\_FDEFAULT  
</dl>

## Remarks

A coclass can have two default members at most. One represents the source interface or dispinterface, and the other represents the sink interface or dispinterface. If the defaultattribute is not specified for any member of the coclass or cotype, the first source and sink members that do not have the [restricted](restricted.md) attribute will be treated as the defaults.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




