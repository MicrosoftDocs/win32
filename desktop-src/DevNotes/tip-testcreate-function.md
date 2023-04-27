---
description: Returns a new test handle.
title: TestCreate function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TestCreate
api_type: 
- DllExport
api_location: 
- kernelbase.dll
---

# TestCreate function

Returns a new test handle.

## Syntax


```C++
HANDLE TestCreate(
    unsigned int testCaseId,
    unsigned int options,
    unsigned char storage,          
    unsigned int  properties,  
    PCSTR data,                      
    _Out_ GUID* testId)
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
| 131072 | Indicates that additional “properties” field will be included in the [TestInfo](tip-testinfo-structure.md) structure returned from [TestOpen](tip-testopen-function.md). |


### storage

The test storage options. This parameter can be set to the following values.

| Value	| Description |
|-------|---------|
| 1 | Data will be stored in process. |
| 2 | Data will be stored out of process. |


### properties

The test properties. This parameter can be set to a combination of the following values.

| Value	| Description |
|-------|---------|
| 0 | Default properties. |
| 1 | The test data will not be removed from storage when no test handles exist. |
| 2 | Adds keyword bit 45 to failure ETW event once per process. |
| 4 | Adds keyword bit 46 to each failure ETW event. |
| 8 | Adds keyword bit 45 to success ETW event. |
| 16 | Adds keyword bit 46 to each success ETW event. |
| 32 | Sets test expiration to 24 hours. |
| 64 | Sets test expiration to 7 days. |
| 128 | Adds keyword bit 45 to failure ETW event. |
| 256 | Adds keyword bit 45 to success ETW event once per process. |
| 512 | Restricts ETW event property metricsBucket to 8 bits. |
| 2048 | Includes keyword bit 3 in ETW event. |
| 4096 | Includes keyword bit 2 in ETW event. |
| 8192 | Includes keyword bit 4 in ETW event. |


### data

An arbitrary json string.

### testId [out]

The identifier of the test instance.

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



 

 




