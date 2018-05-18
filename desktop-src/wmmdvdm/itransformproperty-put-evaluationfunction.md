---
title: ITransformProperty put\_EvaluationFunction method
description: The put\_EvaluationFunction method specifies the evaluation function that is used to calculate intermediary data between property points.
ms.assetid: 'cb927e22-fe36-4b21-9926-f3e27a96f910'
keywords: ["put_EvaluationFunction method Windows Movie Maker and DVD Maker", "put_EvaluationFunction method Windows Movie Maker and DVD Maker , ITransformProperty interface", "ITransformProperty interface Windows Movie Maker and DVD Maker , put_EvaluationFunction method"]
topic_type:
- apiref
api_name:
- ITransformProperty.put_EvaluationFunction
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ITransformProperty::put\_EvaluationFunction method

The **put\_EvaluationFunction** method specifies the evaluation function that is used to calculate intermediary data between property points.

## Syntax


```C++
HRESULT put_EvaluationFunction(
  [in] EVALUATION_CURVE_TYPE eFunction
);
```



## Parameters

<dl> <dt>

*eFunction* \[in\]
</dt> <dd>

A value from the [**EVALUATION\_CURVE\_TYPE**](evaluation-curve-type.md) enumeration describing the type of evaluation function used to calculate intermediary data between property points.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

The default curve value, if not specified, is StepEvaluation.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**EVALUATION\_CURVE\_TYPE**](evaluation-curve-type.md)
</dt> <dt>

[**ITransformProperty Interface**](itransformproperty.md)
</dt> </dl>

 

 





