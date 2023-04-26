---
description: Unlocks the test handle that was locked with TestQueryData.
title: TestUnlockData function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TestUnlockData
api_type: 
- DllExport
api_location: 
- kernelbase.dll
---

# TestUnlockData function

Unlocks the test handle that was locked with [TestQueryData](tip-testquerydata-function.md).

## Syntax


```C++
void TestUnlockData(
    HTIPTEST test,
    TestUnlockOptions options,
    PCSTR data,      
    _Out_ TestInfo* result)
```



## Parameters

### test

The test handle to operate on. 

### options

The unlock data options. This parameter can be set to the following values.

| Value	| Description |
|-------|---------|
| 0 | None. |
| 1 | AmbiguousWrite. This update is coming from a test class that was opened with an ambiguous entity, i.e.multiple tests running may assume contention.|

### data

An arbitrary json string.

### result [out]

A [TestInfo](tip-testinfo-structure.md) structure containing information about the test.

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



 

 




