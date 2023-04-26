---
description: Contains metadata for a test handle.
title: TestInfo structure
ms.topic: reference
ms.date: 01/22/2023
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

# EDP_CONTEXT structure

Contains metadata for a test handle.

## Syntax


```C++
struct TestInfo
{
    GUID testId;
    unsigned int dataSequenceId;
    TestFlags flags;
    PSTR data;
    LONGLONG startPerformanceCounter;
    unsigned int observedSleepTimeInMs;
    TestProperties properties;
};
```

## Members

### testId

The test instance identifier.

### dataSequenceId

The version of the test data.

### flags

The flags of the test data.

### data

An arbitrary json string.

### startPerformanceCounter

The counter of the start of the test.

### observedSleepTimeInMs

The amount of time spent in sleep or suspended state.

### properties

The test properties.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |




 

 




