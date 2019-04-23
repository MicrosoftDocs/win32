---
title: '_aulldiv Routine'
author: TimShererWithAquent
description: Divides two ULONGLONG integers.
ms.assetid: na
ms.author: windowssdkdev
ms.topic: article
ms.date: 04/29/2019
ms.keywords: _aulldiv, ntoskrnl.exe!_aulldiv 
api_name: 
- _aulldiv
- ntoskrnl.exe!_aulldiv 
---

# \_aulldiv Routine

Divides two **ULONGLONG** integers.
For example, to divide two uint64 values the compiler might generate a call to the **\_aulldiv** routine.

## Remarks

The **\_aulldiv** routine is a helper routine for the C compiler.
Whether the compiler uses **\_aulldiv** is completely dependent on the optimization set.

This function is used only on x86 platforms.
