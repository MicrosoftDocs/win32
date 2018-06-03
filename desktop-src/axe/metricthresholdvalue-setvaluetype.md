---
title: MetricThresholdValue SetValueType method
description: Sets the value type of the MetricThresholdValue.
ms.assetid: 68AA8319-2EAC-4186-A195-1C2B77383D88
keywords:
- SetValueType method Access Execution Engine
- SetValueType method Access Execution Engine , MetricThresholdValue interface
- MetricThresholdValue interface Access Execution Engine , SetValueType method
topic_type:
- apiref
api_name:
- MetricThresholdValue.SetValueType
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

# MetricThresholdValue::SetValueType method

Sets the value type of the **MetricThresholdValue**.

## Syntax


```C++
virtual HRESULT SetValueType(
  [in] MetricThresholdValueValueType valueType
) = 0;
```



## Parameters

<dl> <dt>

*valueType* \[in\]
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

 

 





