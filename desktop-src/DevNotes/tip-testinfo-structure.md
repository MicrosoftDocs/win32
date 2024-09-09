---
description: Contains metadata for a test handle.
title: TestInfo structure
ms.topic: reference
ms.date: 04/27/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TestInfo
api_type: 
- HeaderDef
api_location: 
- None
---

# TestInfo structure

Contains metadata for a test handle.

## Syntax


```C++
struct TestInfo
{
    GUID testId;
    unsigned int dataSequenceId;
    unsigned int flags;
    PSTR data;
    LONGLONG startPerformanceCounter;
    unsigned int observedSleepTimeInMs;
    unsigned int properties;
};
```

## Members

### testId

The test instance identifier.

### dataSequenceId

The version of the test data.

### flags

The flags of the test data. This can be set to a combination of the following values.

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

### data

An arbitrary JSON string.

### startPerformanceCounter

The counter of the start of the test.

### observedSleepTimeInMs

The amount of time spent in sleep or suspended state.

### properties

The test properties. This value is only present when the *option* value of 131072 is specified in the call to [TestCreate](tip-testcreate-function.md) or [TestOpen](tip-testopen-function.md). This field can be set to a combination of the following values.

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

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows Build 22000                         |
| Minimum supported server | Windows Server 2022                         |
| Header                   | None  |




 

 




