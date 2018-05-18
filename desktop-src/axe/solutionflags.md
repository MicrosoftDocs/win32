---
title: SolutionFlags enumeration
description: Determines if the Solution interface will be initialized to run assessments or workloads.
ms.assetid: 'F6DAE7B1-0251-4E1E-ADCE-00524939C52B'
keywords: ["SolutionFlags enumeration Access Execution Engine"]
topic_type:
- apiref
api_name:
- SolutionFlags
api_location:
- AxeHosting.h
api_type:
- HeaderDef
---

# SolutionFlags enumeration

Determines if the Solution interface will be initialized to run assessments or workloads.

## Syntax


```C++
enum SolutionFlags {
  SolutionFlagNone       = 0, 
  SolutionFlagWorkloads  = 0x80000000 

};
```



## Constants

<dl> <dt>

<span id="SolutionFlagNone"></span><span id="solutionflagnone"></span><span id="SOLUTIONFLAGNONE"></span>**SolutionFlagNone**
</dt> <dd>

The Solution interface will be configured to run assessments.

</dd> <dt>

<span id="SolutionFlagWorkloads"></span><span id="solutionflagworkloads"></span><span id="SOLUTIONFLAGWORKLOADS"></span>**SolutionFlagWorkloads**
</dt> <dd>

The Solution interface will be configured to run workloads.

</dd> </dl>

## Remarks

Applications using the Solution interface can run assessments or workloads. Both assessments and workloads are applications that have access to the Support interface in the AXE Execution Assessment API, but workloads do not produce any results.

Workloads only exist to exercise the system under test while an assessment is measuring the system. The **SolutionFlags** are specified in the [**SolutionParameters**](solutionparameters.md).Flags field.

Managed code uses the [**SolutionFlags**](axe-solutionflags_om) enum.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



## See also

<dl> <dt>

[**SolutionParameters**](solutionparameters.md)
</dt> </dl>

 

 





