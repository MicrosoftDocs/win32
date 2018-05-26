---
title: Incorrect Placement of Allocations on a Call Stack
description: Incorrect Placement of Allocations on a Call Stack
ms.assetid: 3097520b-8291-499e-8a1f-9bcba1096ff0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Incorrect Placement of Allocations on a Call Stack

Another allocation issue is the incorrect placement of allocations within the call stack. Routines that perform a large number of repetitive transient allocations with a short lifetime can be indicators of an allocation point that is too deep in the call hierarchy.

Moving the allocation point closer to the root of the call stack can sometimes decrease the number of allocations at the expense of increasing their lifetime. This adjustment can result in CPU savings but should be balanced with its impact on outstanding and peak allocation sizes.

For example, function func01, calls into func02, which then calls func03 frequently. If funct03 allocates and frees a data structure it may be appropriate to move the allocation and free instructions to function func01 or func02, thus avoiding a potentially large number of short lived allocations.

 

 




