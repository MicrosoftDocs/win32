---
description: "Learn more about: __CxxFrameHandler3"
title: "__CxxFrameHandler3"
ms.date: "11/20/2023"
ms.topic: reference
api_name: ["__CxxFrameHandler3"]
api_location: ["msvcr110.dll", "msvcrt.dll", "msvcr80.dll", "msvcr100.dll", "msvcr110_clr0400.dll", "msvcr90.dll", "msvcr120.dll", "ucrtbase_enclave.dll"]
api_type: ["DLLExport"]
topic_type: ["apiref"]
f1_keywords: ["__CxxFrameHandler3"]
helpviewer_keywords: ["__CxxFrameHandler3"]
ms.assetid: e9ee9043-6f08-4d79-88ae-1a52a93ae9ed
---
# `__CxxFrameHandler3`

Internal CRT function. Used by the CRT to handle structured exception frames.

## Syntax

```cpp
void* __CxxFrameHandler3(
      EHExceptionRecord  *pExcept,
      EHRegistrationNode *pRN,
      void               *pContext,
      DispatcherContext  *pDC
   );
```

## Parameters

*`pExcept`*\
Exception record that is passed to the possible **`catch`** statements.

*`pRN`*\
Dynamic information about the stack frame that is used to handle the exception.

*`pContext`*\
Context info. (Not used on Intel processors.)

*`pDC`*\
Additional information about the function entry and stack frame. (Not used on Intel processors.)

## Remarks

## Requirements

| Routine | Exported by |
|---|---|
| **`__CxxFrameHandler3`** | `<ucrtbase_enclave.dll>` |
