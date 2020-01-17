---
UID: 
title: CaptureStackBackTrace function
description: Captures a stack back trace by walking up the stack.
old-location: 
ms.assetid: na
ms.date: 04/10/2019
ms.keywords: RtlCaptureStackBackTrace
ms.topic: reference
req.header: WinBase.h
req.include-header: Windows.h
req.target-type: Windows
req.target-min-winverclnt: Windows XP [desktop apps | UWP apps]
req.target-min-winversvr: Windows Server 2003 [desktop apps | UWP apps]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Kernel32.lib
req.dll: API-MS-Win-Core-rtlsupport-l1-1-0.dll
req.irql: 
topic_type:
- APIRef
api_type: 
api_location:
- API-MS-Win-Core-rtlsupport-l1-1-0.dll
api_name:
- CaptureStackBackTrace
targetos: Windows
req.typenames: 
req.redist: 
---

# CaptureStackBackTrace function

## Description

Captures a stack back trace by walking up the stack and recording the information for each frame.

```cpp
USHORT WINAPI CaptureStackBackTrace(
  _In_      ULONG  FramesToSkip,
  _In_      ULONG  FramesToCapture,
  _Out_     PVOID  *BackTrace,
  _Out_opt_ PULONG BackTraceHash
);
```

## Parameters

### FramesToSkip [in]

The number of frames to skip from the start of the back trace.

### FramesToCapture [in]

The number of frames to be captured.
You can capture up to **MAXUSHORT** frames.

**Windows Server 2003 and Windows XP:**  The sum of the *FramesToSkip* and *FramesToCapture* parameters must be less than 63.

### BackTrace [out]

An array of pointers captured from the current stack trace.

### BackTraceHash [out, optional]

A value that can be used to organize hash tables.
If this parameter is **NULL**, then no hash value is computed.

This value is calculated based on the values of the pointers returned in the BackTrace array.
Two identical stack traces will generate identical hash values.

## Returns

The number of captured frames.

## Remarks

The **CaptureStackBackTrace** function is defined as the **RtlCaptureStackBackTrace** function (the definition is included in the Windows SDK beginning with Windows Vista).
For more information, see WinBase.h and WinNT.h.

## See also
