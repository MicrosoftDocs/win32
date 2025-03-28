---
description: Given a representation of the CPU context within a function, calculates CPU context representing the parent (caller) stack frame.
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

Given a representation of the CPU context within a function, calculates CPU context representing the parent (caller) stack frame.

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

The address of the function table entry for the function represented by the execution context in the ContextRecord. To obtain the function table entry, call the [RtlLookupFunctionEntry](/windows/win32/api/winnt/nf-winnt-rtllookupfunctionentry) function. If NULL, the function will be assumed to be a leaf function with no stack frame of its own and a trivial unwind will be performed (e.g. emulate a solitary RET).

### ContextRecord \[in, out\]

A pointer to a [CONTEXT](/windows/win32/api/winnt/ns-winnt-context) structure. On entry, this should represent the state of the CPU within a given function. On successful return, the context will represent the CPU context at the parent (caller) frame.

### HandlerData \[out\]

This parameter provides a pointer that, on return, receives the Exception Handler Data associated with function that was running in the stack frame the unwinder unwound from (input). The format of the data is opaque to the unwinder and is expected to be processed and understood by the `HandlerRoutine`.

### EstablisherFrame* \[out\]

This parameter provides a pointer that, on return, receives the `Establisher Frame` associated with function that was running in the stack frame the unwinder unwound from (input).
Windows uses the `Establisher Frame` to uniquely identify a specific stack frame in a given stack. For example, this value can be then provided to [**RtlUnwindEx**](/windows/win32/api/winnt/nf-winnt-rtlunwindex) to identify the frame at which the stack unwind operation should stop at. This value is also provided to the Exception Handlers when unwinding the stack so they can locate particular data in the stack. An example of this is the /GS cookie validation handler using the `Establisher Frame` to locate the position of the cookie in the stack.

The actual definition of the `Establisher Frame` is platform-specific:

|Platform|Definition|
|--------|----------|
|Arm64|It always represents the value of the `Stack Pointer` when the function was entered. This value does not change regardless of where in the function `ControlPc` points at, including within the Prolog and Epilog of the function|
|x86-64|This value depends on where `ControlPc` points at in the function. When the `ControlPc` points to the Body of a function, the value is well defined as the value of the stack pointer within the Body, when the function doesn't have a `Frame Pointer`, or the value of the `Frame Pointer` when it has one. In the Prolog of a function `Establisher Frame` is the same as the `Stack Pointer` up to the point where a `Frame Pointer` is defined after which is remains constant - if one is never defined, `Establisher Frame` continues to *shadow* the `Stack Pointer` all the way to the body of the function, after which it must remain constant until it reaches the Epilog. `Establisher Frame` is not well defined in the Epilog of a function.|

### ContextPointers* \[in, out, optional\]

When performing the virtual unwind operation, the unwinder will recover the values for the (callee-saved) registers which were spilled in the stack as part of the transition between the two frames. The stack addresses which each register was restored from will be stored in this structure. This parameter is optional.

### LowLimit [in, optional]

This optional parameter provides a value to test for stack **overflow**. If, during unwinding, the Stack Pointer moves beyond (lower numeric value, in architectures where the stack grows towards lower values) the value of `LowLimit`, the unwind will fail with `STATUS_BAD_STACK`.

### HighLimit [in, optional]

This optional parameter provides a value to test for stack **underflow**. If, during unwinding, the Stack Pointer moves prior (higher numeric value, in architectures where the stack grows towards lower values) the value of `HighLimit`, the unwind will fail with `STATUS_BAD_STACK`.

### HandlerRoutine [out, optional]

This optional parameter provides a function pointer that, on return, receives the Exception Handler routine associated with function that was running in the stack frame the unwinder unwound from (input).

### UnwindFlags [in]

A bitmask of option flags with the following values and meanings:

|Name|Value|Meaning|Notes|
|----|-----|-------|-----|
|RTL_VIRTUAL_UNWIND2_VALIDATE_PAC|0x00000001UL|During stack unwinding, verify the PAC signature of return address values. Without this flag, the PAC signature is removed from the return address values without verification.|Arm64 only|


## Return value

This function returns zero on success. (More detail).

See [NTSTATUS Values](/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55) for a list of NTSTATUS values.


## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.


## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11 \[desktop apps only\]<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2022 \[desktop apps only\]<br/>                                                                                    |
| Target platform<br/>          | <dl> <dt>[Universal](https://msdn.microsoft.com/Library/Windows/Hardware/EB2264A4-BAE8-446B-B9A5-19893936DDCA)</dt> </dl> |
| Header<br/>                   | <dl> <dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl>                                                    |



## See also



 

 
