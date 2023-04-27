---
description: Changes the keywords of ETW events.
title: TestControlReporting function
ms.topic: reference
ms.date: 04/27/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TestControlReporting
api_type: 
- DllExport
api_location: 
- kernelbase.dll
---

# TestControlReporting function

Changes the keywords of ETW events.

## Syntax


```C++
void TestControlReporting(
    unsigned int reportingRequest)
```



## Parameters

### reportingRequest

The options for changing emitted ETW event. This parameter can have the following values.

| Value | Description |
|-------|-------------|
| 0 | Save process data into persistent storage. |
| 1 | Add keyword bits 45 and 46 back to ETW event. | 
| 2 | Remove keyword bits 45 and 46 from ETW event. |


## Return value

None

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | kernelbase.dll |



 

 




