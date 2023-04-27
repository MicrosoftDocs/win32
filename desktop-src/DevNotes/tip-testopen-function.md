---
description: Returns an existing test handle that was created with TestCreate.
title: TestOpen function
ms.topic: reference
ms.date: 04/27/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TestOpen
api_type: 
- DllExport
api_location: 
- kernelbase.dll
---

# TestOpen function

Returns an existing test handle that was created with [TestCreate](tip-testcreate-function.md).

## Syntax


```C++
HANDLE TestOpen(
    unsigned int testCaseId,               
    unsigned int options,   
    unsigned char storage,
    GUID* testId,            
    _Out_ TestInfo* result)
```



## Parameters

### testCaseId

The test identifier.

### options

The test retrieval options. This parameter can be set to the following values.

| Value	| Description |
|-------|---------|
| 0	| Default option. |
| 1	| Optimize retrieval with locking, like subsequently calling [TestQueryData](tip-testquerydata-function.md). |
| 2 | Deprecated, this is the same as default option. |
| 131072 | Indicates that additional “properties” field will be included in the returned  [TestInfo](tip-testinfo-structure.md) structure. |

### storage

The test storage options. This parameter can be set to the following values.

| Value	| Description |
|-------|---------|
| 1 | Data will be stored in process. |
| 2 | Data will be stored out of process. |

### testId

The identifier of the test instance.

### result [out]

A [TestInfo](tip-testinfo-structure.md) structure containing information about the test. 

## Return value

The test handle.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | kernelbase.dll |



 

 




