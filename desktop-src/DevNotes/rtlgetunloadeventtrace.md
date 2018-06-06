---
Description: Enables the dump code to get the unloaded module information from Ntdll.dll for storage in the minidump.
ms.assetid: 017398da-e13e-4261-bda5-6f400a91dbe3
title: RtlGetUnloadEventTrace function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RtlGetUnloadEventTrace function

\[This function may be changed or removed from Windows without further notice.\]

Enables the dump code to get the unloaded module information from Ntdll.dll for storage in the minidump.

## Syntax


```C++
 PRTL_UNLOAD_EVENT_TRACE RtlGetUnloadEventTrace(void);
```



## Parameters

This function has no parameters.

## Return value

This function returns a pointer to an array. For more information, see Remarks.

## Remarks

The RtlpUnloadEventTrace array is defined as follows:

``` syntax
#define RTL_UNLOAD_EVENT_TRACE_NUMBER 64

typedef struct _RTL_UNLOAD_EVENT_TRACE {
    PVOID BaseAddress;   // Base address of dll
    SIZE_T SizeOfImage;  // Size of image
    ULONG Sequence;      // Sequence number for this event
    ULONG TimeDateStamp; // Time and date of image
    ULONG CheckSum;      // Image checksum
    WCHAR ImageName[32]; // Image name
} RTL_UNLOAD_EVENT_TRACE, *PRTL_UNLOAD_EVENT_TRACE;

RTL_UNLOAD_EVENT_TRACE RtlpUnloadEventTrace[RTL_UNLOAD_EVENT_TRACE_NUMBER];
```

This function has no associated header file. The associated import library, Ntdll.lib, is available in the Windows Driver Kit (WDK). You can also call this function using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 




