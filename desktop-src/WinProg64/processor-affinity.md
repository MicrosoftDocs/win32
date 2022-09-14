---
title: Processor Affinity Under WOW64
description: 32-bit Windows supports a maximum of 32 processors. Therefore, functions such as GetProcessAffinityMask simulate a computer with 32 processors when called under WOW64.
ms.assetid: f50a03e8-1c23-4eb0-a1ff-471c28d6b611
keywords:
- processor affinity 64-bit Windows Programming
- WOW64 64-bit Windows Programming , processor affinity
ms.topic: article
ms.date: 05/31/2018
---

# Processor Affinity Under WOW64

32-bit Windows supports a maximum of 32 processors. Therefore, functions such as [**GetProcessAffinityMask**](/windows/desktop/api/winbase/nf-winbase-getprocessaffinitymask) simulate a computer with 32 processors when called under WOW64.

The affinity mask is obtained by performing a bitwise OR operation of the top 32 bits of the mask with the low 32 bits. Therefore, if a thread has affinity for processors 0, 1, and 32, WOW64 reports the affinity as 0 and 1, because processor 32 maps to processor 0. Functions that set processor affinity, such as [**SetThreadAffinityMask**](/windows/desktop/api/winbase/nf-winbase-setthreadaffinitymask), restrict processors to the first 32 processors under WOW64.

For more information about processor affinity, see [Multiple Processors](/windows/desktop/ProcThread/multiple-processors).

 

 