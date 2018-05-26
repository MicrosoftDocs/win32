---
title: CreateMergedTraceFile function
description: The CreateMergedTraceFile function merges multiple WPT/ETW trace files into a single output file.
ms.assetid: 0fa4a8ae-29a7-4f02-9a44-3facbb63fc44
keywords:
- CreateMergedTraceFile function Windows Performance Analyzer
topic_type:
- apiref
api_name:
- CreateMergedTraceFile
api_location:
- KernelTraceControl.dll
- KernelTraceControl.dll.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CreateMergedTraceFile function

The **CreateMergedTraceFile** function merges multiple WPT/ETW trace files into a single output file.

## Syntax


```C++
ULONG
WINAPI CreateMergedTraceFile(
  _In_ LPCWSTR wszMergedFileName,
  _In_ LPCWSTR wszTraceFileNames[],
  _In_ ULONG   cTraceFileNames,
  _In_ DWORD   dwExtendedDataFlags
);
```



## Parameters

<dl> <dt>

*wszMergedFileName* \[in\]
</dt> <dd>

Specifies the name of the output trace file.

</dd> <dt>

*wszTraceFileNames* \[in\]
</dt> <dd>

Pointer to an array of WPT/ETW trace files to be merged.

</dd> <dt>

*cTraceFileNames* \[in\]
</dt> <dd>

Count of the elements in the *wszTraceFileNames* array.

</dd> <dt>

*dwExtendedDataFlags* \[in\]
</dt> <dd>

Flags specify the System Information to be injected in the merged trace file. For more information concerning valid flags, see [**Custom Injection of System Information**](custom-injection-of-system-information.md).

</dd> </dl>

## Return value

**CreateMergedTraceFile** returns **ERROR\_SUCCESS** if the call was successful.

Possible error return values include:



| Return code                                                                                                  | Description                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **ERROR\_REVISION\_MISMATCH** </dt> </dl>   | Possibly indicates the trace files being merged contain events with different versions that could not be merged.<br/> |
| <dl> <dt> **ERROR\_INSUFFICIENT\_BUFFER** </dt> </dl> | Possibly indicates the merged trace does not contain a complete set of events from each file.<br/>                    |



 

In the case where neither of these error return codes is appropriate, a [System Error Code](http://go.microsoft.com/fwlink/p/?linkid=141506) is returned.

## Remarks

Two or more trace files from simultaneous sessions that were captured on the same machine can be merged into a single trace file. Trace files from other tracing sessions may also be merged if those files have the same boot times. Optionally, the merge operation adds meta-information concerning the merged traces.

> [!Note]  
> An unmerged kernel trace cannot decode symbols correctly. For more information on symbol decoding, see [MSDN](http://go.microsoft.com/fwlink/p/?linkid=141514).

 

**Unicode/ANSI:** The API is implemented in Unicode only.

> [!Note]  
> This API could be used to inject extended data into a single trace file. In this case the array *wszMergedFileName* contains only a single element, which is the name of the trace file.

 

## Requirements



|                    |                                                                                                                                                               |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows Vista and later versions of the Windows operating system. This function is distributed with the Windows Performance Analyzer.<br/> |
| Header<br/>  | <dl> <dt>KernelTraceControl.h (include KernelTraceControl.h)</dt> </dl>                                |
| Library<br/> | <dl> <dt>KernelTraceControl.dll</dt> </dl>                                                             |



## See also

<dl> <dt>

[**Custom Injection of System Information**](custom-injection-of-system-information.md)
</dt> </dl>

 

 





