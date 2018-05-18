---
title: ITransformProperty get\_EvaluationFunction method
description: The get\_EvaluationFunction method retrieves the evaluation function used for a transform.
ms.assetid: '7ef9740c-6822-4acc-b113-98c12d1d4e6f'
keywords: ["get_EvaluationFunction method Windows Movie Maker and DVD Maker", "get_EvaluationFunction method Windows Movie Maker and DVD Maker , ITransformProperty interface", "ITransformProperty interface Windows Movie Maker and DVD Maker , get_EvaluationFunction method"]
topic_type:
- apiref
api_name:
- ITransformProperty.get_EvaluationFunction
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ITransformProperty::get\_EvaluationFunction method

The **get\_EvaluationFunction** method retrieves the evaluation function used for a transform.

## Syntax


```C++
HRESULT get_EvaluationFunction(
  [out] EVALUATION_CURVE_TYPE *peFunction
);
```



## Parameters

<dl> <dt>

*peFunction* \[out\]
</dt> <dd>

A value from the [**EVALUATION\_CURVE\_TYPE**](evaluation-curve-type.md) enumeration describing the evaluation function used to calculate intermediary data between property points.

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

[**ITransformProperty Interface**](itransformproperty.md)
</dt> </dl>

 

 





