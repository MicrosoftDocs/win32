---
title: AnalyzeResultsInfo structure
description: Information about results analysis.
ms.assetid: 22F5BCFA-A6AE-4722-A14F-90DDCD14F42C
keywords:
- AnalyzeResultsInfo structure Access Execution Engine
topic_type:
- apiref
api_name:
- AnalyzeResultsInfo
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# AnalyzeResultsInfo structure

Information about results analysis.

## Syntax


```C++
struct AnalyzeResultsInfo {
  DWORD             Size;
  const JobResults  *Results;
  DWORD             Flags;
  JobExecutionError Error;
  LPCWSTR           ResultsPublishPath;
};
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The size of the structure.

</dd> <dt>

**Results**
</dt> <dd>

A pointer to a [**JobResults**](jobresults.md) object.

</dd> <dt>

**Flags**
</dt> <dd>

Analysis flags, as defined in [**AnalyzeResultsFlags**](analyzeresultsflags.md).

</dd> <dt>

**Error**
</dt> <dd>

The job execution error value, as defined in [**JobExecutionError**](jobexecutionerror.md).

</dd> <dt>

**ResultsPublishPath**
</dt> <dd>

The path where the results are to be copied when analysis is done. If the **PublishToSource** flag is set in the **AnalyzeResultsFlags**, this directory serves as a backup to the source directory.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





