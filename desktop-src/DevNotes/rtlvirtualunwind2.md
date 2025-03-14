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

# RtlVirtualUnwind2 function

Given a representation of the CPU context within a function, it calculates CPU context representing the parent (caller) stack frame.

## Syntax


```C++
NTSYSAPI NTSTATUS RtlVirtualUnwind2(
  [in]                DWORD                          HandlerType,
  [in]                DWORD64                        ImageBase,
  [in]                DWORD64                        ControlPc,
  [in, optional]      PRUNTIME_FUNCTION              FunctionEntry,
  [in, out]           PCONTEXT                       ContextRecord,
  [in, out, optional] PBOOLEAN                       MachineFrameUnwound
  [out]               PVOID                          *HandlerData,
  [out]               PDWORD64                       EstablisherFrame,
  [in, out, optional] PKNONVOLATILE_CONTEXT_POINTERS ContextPointers,
  [in, optional]      PDWORD64                       LowLimit,
  [in, optional]      PDWORD64                       HighLimit,
  [out, optional]     PEXCEPTION_ROUTINE             *HandlerRoutine
  [in]                DWORD                          UnwindFlags
);
```



## Parameters

### HandlerType \[in\]

The handler type. This parameter can be one of the following values.

|Value |Meaning|
|------|-------|
|UNW_FLAG_NHANDLER|The function has no handler.|
|UNW_FLAG_EHANDLER|The function has an exception handler that should be called.|
|UNW_FLAG_UHANDLER|The function has a termination handler that should be called when unwinding an exception.|
|UNW_FLAG_CHAININFO|The FunctionEntry member is the contents of a previous function table entry.|

### ImageBase \[in\]

The base address of the module that includes the function represented by the execution context in the ContextRecord at the time the call is made (input).

### ControlPc \[in\]

The address within the function represented by the ContextRecord state which should be regarded as the Instruction Pointer for the unwind operation. This takes precedence over the Instruction Pointer field in the ContextRecord itself.

### FunctionEntry \[in\]

The address of the function table entry for the function represented by the execution context in the ContextRecord. To obtain the function table entry, call the [RtlLookupFunctionEntry](nf-winnt-rtllookupfunctionentry.md) function. If NULL, the function will be assumed to be a leaf function with no stack frame of its own and a trivial unwind will be performed (e.g. emulate a solitary RET).

### ContextRecord \[in, out\]

A pointer to a [CONTEXT](ns-winnt-arm64_nt_context.md) structure. On entry, this should represent the state of the CPU withing a given function. On succesful return, the context will represent the CPU context at the parent (caller) frame.

### HandlerData \[out\]

TBD

### EstablisherFrame* \[out\]

TBD

### ContextPointers* \[in, out, optional\]

When performing the virtual unwind operation, the unwinder will recover the values for the (callee-saved) registers which were spilled in the stack as part of the transition between the two frames. The stack addresses which each register was restored from will be stored in this structure. This parameter is optional.

### LowLimit [in, optional]

TBD

### HighLimit [in, optional]

TBD

### HandlerRoutine [out, optional]

TBD

### UnwindFlags [in]

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



 

 
