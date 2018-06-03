---
title: MetricThreshold AddMetricThresholdValue method
description: Creates and adds a MetricThresholdValue to the MetricThreshold.
ms.assetid: 683BA9A9-DEC2-4572-A99F-405A624BDDF8
keywords:
- AddMetricThresholdValue method Access Execution Engine
- AddMetricThresholdValue method Access Execution Engine , MetricThreshold interface
- MetricThreshold interface Access Execution Engine , AddMetricThresholdValue method
topic_type:
- apiref
api_name:
- MetricThreshold.AddMetricThresholdValue
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

# MetricThreshold::AddMetricThresholdValue method

Creates and adds a [**MetricThresholdValue**](metricthresholdvalue-struct.md) to the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT AddMetricThresholdValue(
  [in]            LPCWSTR                       descriptionProgrammaticName,
  [in]            MetricThresholdValueValueType valueType,
  [in]            LPCWSTR                       value,
  [out, optional] MetricThresholdValue          **metricThresholdValue
) = 0;
```



## Parameters

<dl> <dt>

*descriptionProgrammaticName* \[in\]
</dt> <dd>

The description programmatic name.

</dd> <dt>

*valueType* \[in\]
</dt> <dd>

The value type.

</dd> <dt>

*value* \[in\]
</dt> <dd>

The value.

</dd> <dt>

*metricThresholdValue* \[out, optional\]
</dt> <dd>

The **MetricThresholdValue** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

A **MetricThresholdValue** holds data from a **MetricThreshold/MetricThresholdValues/MetricThresholdValue** element.

The description programmatic name is the value of element **MetricThresholdValue/Description/ProgrammaticName**.

The value type is the value of element **MetricThresholdValue/ValueType**. See [**MetricThresholdValueValueType**](metricthresholdvaluevaluetype.md) for the value types.

The value is the value of element **MetricThresholdValue/Value**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThreshold**](metricthreshold-struct.md)
</dt> </dl>

 

 





