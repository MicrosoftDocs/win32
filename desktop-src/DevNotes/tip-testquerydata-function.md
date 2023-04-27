---
description: Allows modification of the test handle with locking.
title: TestQueryData function
ms.topic: reference
ms.date: 04/27/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TestQueryData
api_type: 
- DllExport
api_location: 
- kernelbase.dll
---

# TestQueryData function

Allows modification of the test handle with locking.

## Syntax


```C++
BOOL TestQueryData(
    HANDLE test,
    unsigned int options,
    unsigned int knownDataSequenceId,
    _Out_ TestInfo* result)
```



## Parameters

### test

The test handle returned from [TestCreate](tip-testcreate-function.md) or [TestOpen](tip-testopen-function.md).

### options

The test query options. This parameter can be set to the following values.

| Value	| Description |
|-------|---------|
| 0 | Default option. |
| 1 | Acquires lock to protect modifications until unlock. |
| 2 | Close handle and mark as complete. |
| 3 | Close handle and mark complete if this is the final handle. |
| 4 | Set when the caller already owns the lock. |


### knownDataSequenceId

The last known *dataSequenceId* of the result. Allows optimization from caller by doing less work when this is the same on subsequent calls.

### result [out]

A [TestInfo](tip-testinfo-structure.md) structure containing information about the test. 

## Return value

True if the operation was successful.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | kernelbase.dll |



 

 




