---
description: Retrieves the size and location of the dynamically unloaded module list for the current process.
ms.assetid: 53ac9a7f-aa4a-412d-a6f7-a3a73bede5c2
title: RtlGetUnloadEventTraceEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlGetUnloadEventTraceEx
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# RtlGetUnloadEventTraceEx function

\[This function may be changed or removed from Windows without further notice.\]

Retrieves the size and location of the dynamically unloaded module list for the current process.

## Syntax


```C++
VOID WINAPI RtlGetUnloadEventTraceEx(
  _Out_ PULONG *ElementSize,
  _Out_ PULONG *ElementCount,
  _Out_ PVOID  *EventTrace
);
```



## Parameters

<dl> <dt>

*ElementSize* \[out\]
</dt> <dd>

A pointer to a variable that contains the size of an element in the list.

</dd> <dt>

*ElementCount* \[out\]
</dt> <dd>

A pointer to a variable that contains the number of elements in the list.

</dd> <dt>

*EventTrace* \[out\]
</dt> <dd>

A pointer to an array of **RTL\_UNLOAD\_EVENT\_TRACE** structures. For more information, see Remarks.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The loader stores unloaded event information in locations that can be read across processes by taking advantage of the fact that Ntdll.dll is loaded at the same base address in all processes. When a debugger needs to query unloaded module information, it calls this function to determine the address at which the variables reside, then queries the virtual memory in the target process at those addresses to read the actual values.

Each element in the list is defined as follows.

``` syntax
typedef struct _RTL_UNLOAD_EVENT_TRACE {
    PVOID BaseAddress;   // Base address of dll
    SIZE_T SizeOfImage;  // Size of image
    ULONG Sequence;      // Sequence number for this event
    ULONG TimeDateStamp; // Time and date of image
    ULONG CheckSum;      // Image checksum
    WCHAR ImageName[32]; // Image name
} RTL_UNLOAD_EVENT_TRACE, *PRTL_UNLOAD_EVENT_TRACE;
```

This function has no associated header file. The associated import library, Ntdll.lib, is available in the Windows Driver Kit (WDK). You can also call this function using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 
