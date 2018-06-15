---
title: D1109 Draw Failure
ms.assetid: 76154839-719e-4c73-a80e-f9216f3468e3
description: 
keywords:
- D1109 Draw Failure Direct2D
topic_type:
- apiref
api_name:
- D1109 Draw Failure
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D1109: Draw Failure

A Draw call by a render target failed \[*resource*\]. Tags \[*tag1*, *tag2*\].

## Placeholders

<dl> <dt>

<span id="resource"></span><span id="RESOURCE"></span>*resource*
</dt> <dd>

The address of the render target.

</dd> <dt>

<span id="tag1"></span><span id="TAG1"></span>*tag1*
</dt> <dd>

The first tag value (see [**SetTags**](https://msdn.microsoft.com/en-us/library/Dd316892(v=VS.85).aspx) more for information).

</dd> <dt>

<span id="tag2"></span><span id="TAG2"></span>*tag2*
</dt> <dd>

The second tag value (see [**SetTags**](https://msdn.microsoft.com/en-us/library/Dd316892(v=VS.85).aspx) more for information).

</dd> </dl> 

|             |         |
|-------------|---------|
| Error Level | Warning |



 

## Possible Causes

There are many reasons that a Draw call might fail. For more information, see the Direct2D SDK documentation for the method that failed.

 

 




