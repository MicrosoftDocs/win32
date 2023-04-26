---
description: Closes a test handle.
title: TestClose function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TestClose
api_type: 
- DllExport
api_location: 
- kernelbase.dll
---

# TestClose function

Closes a test handle.

## Syntax


```C++
void TestClose(
    HTIPTEST test)
```

## Parameters

### test

The test handle to operate on.

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



 

 




