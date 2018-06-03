---
title: AnalyzeResultsFlags enumeration
description: Flags that affect the execution of Engine AnalyzeResults.
ms.assetid: 86A12457-4093-40CC-8351-BDCBFF5898A2
keywords:
- AnalyzeResultsFlags enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- AnalyzeResultsFlags
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# AnalyzeResultsFlags enumeration

Flags that affect the execution of [**Engine::AnalyzeResults**](engine-analyzeresults.md).

## Syntax


```C++
enum AnalyzeResultsFlags {
  None             = 0, 
  ExecuteAsync     = 0x1 << 0 , 
  PublishToSource  = 0x1 << 1  

};
```



## Constants

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None**
</dt> <dd>

No flag set.

</dd> <dt>

<span id="ExecuteAsync"></span><span id="executeasync"></span><span id="EXECUTEASYNC"></span>**ExecuteAsync**
</dt> <dd>

**Engine::AnalyzeResults** returns immediately, before it completes its analysis.

</dd> <dt>

<span id="PublishToSource"></span><span id="publishtosource"></span><span id="PUBLISHTOSOURCE"></span>**PublishToSource**
</dt> <dd>

**Engine::AnalyzeResults** publishes its results to the location that was the source of results used for the results analysis.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





