---
description: Contains metadata to be sent in ETW event.
title: TipReportingInfo structure
ms.topic: reference
ms.date: 01/22/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TipReportingInfo
api_type: 
- HeaderDef
api_location: 
- None
---

# TipReportingInfo structure

Contains metadata to be sent in ETW event.

## Syntax


```C++
struct TipReportingInfo
{
    unsigned int testCaseId;           
    PCSTR testCaseName;                
    unsigned int properties;         
    GUID testId;                       
    unsigned int flags;                   
    unsigned char completionKind; 
    unsigned short reason;             
    PCSTR reasonName;                  
    LONGLONG startPerformanceCounter;  
    unsigned int observedSleepTimeInMs;
    PCSTR data;                        
    HRESULT lastResult;                
    PCSTR lastFile;                    
    unsigned short lastLine;           
    unsigned int durationMs;           
    unsigned int hash;                 
    unsigned int metricsBucket;        
    unsigned int testCaseIdStart;      
}

```

## Members

### testCaseId

The *testCaseId* field of emitted ETW event.

### testCaseName

The *testCaseName* field of emitted ETW event.

### properties

The *properties* field of emitted ETW event. This field can be set to a combination of the following values.

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

### testId

The *testId* field of emitted ETW event.

### flags

The *flags* field of emitted ETW event. This can be set to a combination of the following values.

| Value | Description |
|-------|-------------|
| 0 | Default flags. |
| 256 | Test has been marked complete. |
| 512 | Test has been explicitly completed. |
| 1024 | Test has contention with multiple callers are calling [TestUnlockData](tip-testunlockdata-function.md) with options value of 1. |
| 65536 | Failed to acquire the cross-process lock. |
| 131072 | Failed to wait on the cross-process lock. |
| 262144 | Failed to read or write to persistent storage. |
| 524288 | Failed to parse persisted data. |
| 1048576 | Failed allocate memory. |
| 2097152 | Signals that *metricsBucket* and *testCaseIdStart* will be included in [TipReportingInfo](tip-tipreportinginfo-structure.md). |
| 4194304 | Signals that [TestControlReporting](tip-testcontrolreporting-function.md) a has been called with value 2. |

### completionKind

The *completionKind* field of emitted ETW event. This field can be set to the following values:

| Value | Description |
|---------|-----------|
| 0 | No completion kind. |
| 1 | Success completion kind. |
| 2 | Warning completion kind. |
| 3 | Failure completion kind. |
| 4 | Ignored completion kind. |

### reason

The *reason* field of emitted ETW event.

### reasonName

The *reasonName* field of emitted ETW event.

### startPerformanceCounter

The *startPerformanceCounter* field of emitted ETW event.

### observedSleepTimeInMs

The *observedSleepTimeInMs* field of emitted ETW event.

### data

The *data* field of emitted ETW event.

### lastResult

The *lastResult* field of emitted ETW event.

### lastFile

The *lastFile* field of emitted ETW event.

### lastLine

The *lastLine* field of emitted ETW event.

### durationMs

The *durationMs* field of emitted ETW event.

### hash

The *hash* field of emitted ETW event.

### metricsBucket

The *metricsBucket* field of emitted ETW event.

### testCaseIdStart

The *testCaseIdStart* field of emitted ETW event.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |




 

 




