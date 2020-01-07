---
title: '_allmul Routine'
description: Multiplies two LONGLONG or ULONGLONG integers.
ms.assetid: na
ms.topic: reference
ms.date: 04/29/2019
ms.keywords: _allmul, ntoskrnl.exe!_allmul
topic_type: 
- APIRef
api_type: 
- DllExport
api_location: 
- ntoskrnl.exe
api_name: 
- _allmul
targetos: Windows
---

# \_allmul Routine

Multiplies two **LONGLONG** or **ULONGLONG** integers.
For example, to multiply two int64 values the compiler might generate a call to the **\_allmul** routine.

## Remarks

The **\_allmul** routine is a helper routine for the C compiler.
Whether the compiler uses **\_allmul** is completely dependent on the optimization set.

This routine is used only on x86 platforms.
