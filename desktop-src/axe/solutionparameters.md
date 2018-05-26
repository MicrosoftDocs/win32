---
title: SolutionParameters structure
description: This structure defines configuration information for the Solution interface.
ms.assetid: 7A8B1286-0FB9-41B2-8EBB-F55BAA9BE698
keywords:
- SolutionParameters structure Access Execution Engine
topic_type:
- apiref
api_name:
- SolutionParameters
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SolutionParameters structure

This structure defines configuration information for the Solution interface.

## Syntax


```C++
struct SolutionParameters {
  DWORD Size;
  DWORD Flags;
};
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The number of bytes in the structure. Used to detect different versions of structure. This must be set to sizeof( SolutionParameters ) before initializing the Solution interface with this structure.

</dd> <dt>

**Flags**
</dt> <dd>

Specifies flags that control how the Solution interface is initialized. This value can be a combination of the flags defined in the SolutionFlags enumeration.

</dd> </dl>

## Remarks

The Solution interface can be configured to execute assessments or workloads in different ways. Each type of application has state limitations on how it runs and how the Solution interface can interact with it. A solution application is an application that runs assessments. A solution assessment is an assessment that acts as a solution as well except that it can only run workloads, which are essentially sub-assessments. It must initialize the Support interface before it can initialize the Solution interface, and it can only initialize the Solution interface to run workloads.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



## See also

<dl> <dt>

[**SolutionFlags**](solutionflags.md)
</dt> <dt>

[**SolutionError**](solutionerror.md)
</dt> <dt>

[**Support**](support.md)
</dt> </dl>

 

 





