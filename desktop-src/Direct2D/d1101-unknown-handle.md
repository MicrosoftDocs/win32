---
title: D1101 Unknown Handle
ms.assetid: ae40058a-ea17-4262-87dc-0ce852c16c2a
description: An interface not allocated by this DLL was passed to it.
keywords:
- D1101 Unknown Handle Direct2D
topic_type:
- apiref
api_name:
- D1101 Unknown Handle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
ms.custom: "seodec18"
---

# D1101: Unknown Handle

An interface \[*interface*\] not allocated by this DLL was passed to it.

## Placeholders

<dl> <dt>

<span id="interface"></span><span id="INTERFACE"></span>*interface*
</dt> <dd>

The address of the interface.

</dd> </dl> 




 

## Possible Causes

Invalid resource usage. The resource created outside of Direct2D is used with a Direct2D factory, or the resources created on one factory was used with a resource created by another factory.

 

 




