---
title: '_aulldiv Routine'
description: Divides two ULONGLONG integers.
ms.assetid: na
ms.topic: reference
ms.date: 04/29/2019
ms.keywords: _aulldiv, ntoskrnl.exe!_aulldiv 
topic_type: 
- APIRef
api_type: 
- DllExport
api_location: 
- ntoskrnl.exe
api_name: 
- _aulldiv
targetos: Windows
---

# \_aulldiv Routine

Divides two **ULONGLONG** integers.
For example, to divide two uint64 values the compiler might generate a call to the **\_aulldiv** routine.

## Remarks

The **\_aulldiv** routine is a helper routine for the C compiler.
Whether the compiler uses **\_aulldiv** is completely dependent on the optimization set.

This function is used only on x86 platforms.
