---
title: D1102 Too Many Opened Handles
ms.assetid: a7e52926-a4e6-4030-9e90-9df2b3e3edde
description: A large number of unreleased interfaces were found. Currently there are unreleased interfaces allocated by this DLL.
keywords:
- D1102 Too Many Opened Handles Direct2D
topic_type:
- apiref
api_name:
- D1102 Too Many Opened Handles
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
ms.custom: "seodec18"
---

# D1102: Too Many Opened Handles

A large number of unreleased interfaces were found. Currently there are \[*number*\] unreleased interfaces allocated by this DLL.

## Placeholders

<dl> <dt>

<span id="number"></span><span id="NUMBER"></span>*number*
</dt> <dd>

The number of unreleased interfaces allocated by this DLL.

</dd> </dl> 

| &nbsp;      |  &nbsp; |
|-------------|---------|
| Error Level | Warning |



 

## Possible Causes

A large number of resources were created. Although Direct2D has no upper bound on the number of available resources (except memory), the debug layer issues this informational message when it encounters 1001 live objects, 2001 live objects, or 3001 live objects etc, because this might indicate a leak in the application.

 

 




