---
description: Contains the properties that will be included in the ETW event as fields.
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

Under WIP policy, represents the enterprise context (such as enterprise IDs) of a process.

## Syntax


```C++
struct TipReportingInfo
{
    unsigned int testCaseId;           
    PCSTR testCaseName;                
    TestProperties properties;         
    GUID testId;                       
    TestFlags flags;                   
    TestCompletionKind completionKind; 
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

The *properties* field of emitted ETW event.

### testId

The *testId* field of emitted ETW event.

### flags

The *flags* field of emitted ETW event.

### completionKind

The *completionKind* field of emitted ETW event.

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




 

 




