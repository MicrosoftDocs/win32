---
title: EVALUATION\_CURVE\_TYPE enumeration
description: The EVALUATION\_CURVE\_TYPE enumeration describes how a property should change over time. This value is entered in the XML initialization file and is used only as a tool to help the transform calculate a numeric value for a specific time.
ms.assetid: eeb3dc9c-2aff-4786-9fb3-a862e160fb59
keywords:
- EVALUATION_CURVE_TYPE enumeration Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- EVALUATION_CURVE_TYPE
api_location:
- GPUPipelineTime.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EVALUATION\_CURVE\_TYPE enumeration

The **EVALUATION\_CURVE\_TYPE** enumeration describes how a property should change over time. This value is entered in the XML initialization file and is used only as a tool to help the transform calculate a numeric value for a specific time.

## Syntax


```C++
typedef enum eEVALUATION_CURVE_TYPE { 
  StepEvaluation           = 0,
  LinearEvaluation         = 1,
  SquareEvaluation         = 2,
  InverseSquareEvaluation  = 3,
  SineEvaluation           = 4
} EVALUATION_CURVE_TYPE;
```



## Constants

<dl> <dt>

<span id="StepEvaluation"></span><span id="stepevaluation"></span><span id="STEPEVALUATION"></span>**StepEvaluation**
</dt> <dd>

Specifies that the value remains unchanged between time points and the value changes instantaneously from one value to the next at a time point.

</dd> <dt>

<span id="LinearEvaluation"></span><span id="linearevaluation"></span><span id="LINEAREVALUATION"></span>**LinearEvaluation**
</dt> <dd>

A straight line between time points.

</dd> <dt>

<span id="SquareEvaluation"></span><span id="squareevaluation"></span><span id="SQUAREEVALUATION"></span>**SquareEvaluation**
</dt> <dd>

A curve where the value between time points increases with the square of the time.

</dd> <dt>

<span id="InverseSquareEvaluation"></span><span id="inversesquareevaluation"></span><span id="INVERSESQUAREEVALUATION"></span>**InverseSquareEvaluation**
</dt> <dd>

A curve where the value between time points is the inverse of the square of the time.

</dd> <dt>

<span id="SineEvaluation"></span><span id="sineevaluation"></span><span id="SINEEVALUATION"></span>**SineEvaluation**
</dt> <dd>

A sinusoidal curve between time points.

</dd> </dl>

## Remarks

A transition or effect can have only a single curve associated with it.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 





