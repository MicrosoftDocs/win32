---
description: Emits event to an ETW provider with the properties in the input struct.
title: TestReport function
ms.topic: reference
ms.date: 04/27/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TestReport
api_type: 
- DllExport
api_location: 
- kernelbase.dll
---

# TestReport function

Emits event to an ETW provider with the properties in the input struct.

## Syntax


```C++
void TestReport(
    TipReportingInfo* reportingInfo)
```

## Parameters

### reportingInfo

A [TipReportingInfo](tip-tipreportinginfo-structure.md) containing the properties that will be included in the ETW event as fields.

## Return value

None.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | kernelbase.dll |



 

 




