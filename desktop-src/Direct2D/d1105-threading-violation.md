---
title: D1105 Threading Violation
ms.assetid: 2c6cf90b-ce9e-4ea9-849d-22170f65ffb0
description: A rental threaded interface was simultaneously accessed from multiple threads.
keywords:
- D1105 Threading Violation Direct2D
topic_type:
- apiref
api_name:
- D1105 Threading Violation
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
ms.custom: "seodec18"
---

# D1105: Threading Violation

A rental threaded interface \[*interface*\] was simultaneously accessed from multiple threads.

## Placeholders

<dl> <dt>

<span id="interface"></span><span id="INTERFACE"></span>*interface*
</dt> <dd>

The address of the interface that was accessed by multiple threads.

</dd> </dl> 




 

## Possible Causes

Using an object instance from the same single-threaded factory from two different threads.

 

 




