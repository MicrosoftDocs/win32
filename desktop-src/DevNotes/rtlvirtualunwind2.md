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

Given a representation of the CPU context within a function, it calculates CPU context representing the parent stack frame.

## Syntax


```C++
NTSYSAPI NTSTATUS RtlVirtualUnwind2(
  [in]                DWORD                          HandlerType,
  [in]                DWORD64                        ImageBase,
  [in]                DWORD64                        ControlPc,
  [in]                PRUNTIME_FUNCTION              FunctionEntry,
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

This parameter is only present on x64.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="UNW_FLAG_NHANDLER"></a><a id="unw_flag_nhandler"></a><dl>
<dt><b>UNW_FLAG_NHANDLER</b></dt>
<dt>0x0</dt>
</dl>
</td>
<td width="60%">
The function has no handler.

</td>
</tr>
<tr>
<td width="40%"><a id="UNW_FLAG_EHANDLER"></a><a id="unw_flag_ehandler"></a><dl>
<dt><b>UNW_FLAG_EHANDLER</b></dt>
<dt>0x1</dt>
</dl>
</td>
<td width="60%">
The function has an exception handler that should be called.

</td>
</tr>
<tr>
<td width="40%"><a id="UNW_FLAG_UHANDLER"></a><a id="unw_flag_uhandler"></a><dl>
<dt><b>UNW_FLAG_UHANDLER</b></dt>
<dt>0x2</dt>
</dl>
</td>
<td width="60%">
The function has a termination handler that should be called when unwinding an exception.

</td>
</tr>
<tr>
<td width="40%"><a id="UNW_FLAG_CHAININFO"></a><a id="unw_flag_chaininfo"></a><dl>
<dt><b>UNW_FLAG_CHAININFO</b></dt>
<dt>0x4</dt>
</dl>
</td>
<td width="60%">
The <b>FunctionEntry</b> member is the contents of a previous function table entry.

</td>
</tr>
</table>

### ImageBase \[in\]

The base address of the module to which the function belongs.

### ControlPc \[in\]

The virtual address where control left the specified function.

### FunctionEntry \[in\]

The address of the function table entry for the specified function. To obtain the function table entry, call the [RtlLookupFunctionEntry](nf-winnt-rtllookupfunctionentry.md) function.

### ContextRecord \[in, out\]

A pointer to a [CONTEXT](ns-winnt-arm64_nt_context.md) structure that represents the context of the previous frame.

### HandlerData \[out\]

TBD

### EstablisherFrame* \[out\]

TBD

### ContextPointers* \[in, out, optional\]

An optional pointer to a context pointers structure.

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



 

 
