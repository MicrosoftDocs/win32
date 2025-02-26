---
description: TBD.
title: RtlVirtualUnwind2 function (Wdm.h)
ms.topic: reference
ms.date: 02/20/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlVirtualUnwind2
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# RtlCompareUnicodeString function

Compares two Unicode strings.

## Syntax


```C++
NTSYSAPI PEXCEPTION_ROUTINE RtlVirtualUnwind2(
  [in]                DWORD                          HandlerType,
  [in]                DWORD64                        ImageBase,
  [in]                DWORD64                        ControlPc,
  [in]                PRUNTIME_FUNCTION              FunctionEntry,
  [in, out]           PCONTEXT                       ContextRecord,
  [out]               PVOID                          *HandlerData,
  [out]               PDWORD64                       EstablisherFrame,
  [in, out, optional] PKNONVOLATILE_CONTEXT_POINTERS ContextPointers
);
```



## Parameters

### HandlerType \[in\]

TBD

### ImageBase \[in\]

TBD

### ControlPc \[in\]

TBD

### FunctionEntry \[in\]

TBD

### ContextRecord \[in, out\]

TBD

### HandlerData \[out\]

TBD

### EstablisherFrame* \[out\]

TBD

### ContextPointers* \[in, out, optional\]

TBD


## Return value

TBD



| Return code                                                                               | Description                                     |
|-------------------------------------------------------------------------------------------|-------------------------------------------------|
| TBD       | TBD          |



## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.


## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                    |
| Target platform<br/>          | <dl> <dt>[Universal](https://msdn.microsoft.com/Library/Windows/Hardware/EB2264A4-BAE8-446B-B9A5-19893936DDCA)</dt> </dl> |
| Header<br/>                   | <dl> <dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl>                                                    |



## See also



 

 
