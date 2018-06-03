---
title: MetricThresholdValue GetValueType method
description: Returns the value type of the MetricThresholdValue.
ms.assetid: 77D14675-8441-4906-B440-4D6C77E6D51B
keywords:
- GetValueType method Access Execution Engine
- GetValueType method Access Execution Engine , MetricThresholdValue interface
- MetricThresholdValue interface Access Execution Engine , GetValueType method
topic_type:
- apiref
api_name:
- MetricThresholdValue.GetValueType
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MetricThresholdValue::GetValueType method

Returns the value type of the **MetricThresholdValue**.

## Syntax


```C++
virtual HRESULT GetValueType(
  [out] MetricThresholdValueValueType *valueType
) const = 0;
```



## Parameters

<dl> <dt>

*valueType* \[out\]
</dt> <dd>

The value type.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **MetricThresholdValue** objects hold data from the **MetricThreshold/MetricThresholdValues/MetricThresholdValue** elements.

The value type is the value of element **MetricThresholdValue/ValueType**. See [**MetricThresholdValueValueType**](metricthresholdvaluevaluetype.md) for the value types.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThresholdValue**](metricthresholdvalue-struct.md)
</dt> </dl>

 

 





