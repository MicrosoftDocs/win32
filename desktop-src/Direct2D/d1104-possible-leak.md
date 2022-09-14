---
title: D1104 Possible Leak
ms.assetid: 564de2e2-5004-43e8-8616-1ab11127738a
description: The factory was released but the interface created from it is still alive. While it is valid to release resources after releasing the factory, this condition could be indicative of a memory leak.
keywords:
- D1104 Possible Leak Direct2D
topic_type:
- apiref
api_name:
- D1104 Possible Leak
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
ms.custom: "seodec18"
---

# D1104: Possible Leak

The factory \[*factory*\] was released but the interface \[*interface*\] created from it is still alive. While it is valid to release resources after releasing the factory, this condition could be indicative of a memory leak.

## Placeholders

<dl> <dt>

<span id="factory"></span><span id="FACTORY"></span>*factory*
</dt> <dd>

The address of the factory that was released.

</dd> <dt>

<span id="interface"></span><span id="INTERFACE"></span>*interface*
</dt> <dd>

The address of the interface that was created on the *factory*.

</dd> </dl> 

| &nbsp;      |    &nbsp;   |
|-------------|-------------|
| Error Level | Information |



 

## Possible Causes

The factory was released but the interface created from it is still alive.

 

 




