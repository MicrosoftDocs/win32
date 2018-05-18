---
title: MetricThresholdValueCollection AddItem method
description: Creates and adds a MetricThresholdValue to the MetricThresholdValueCollection.
ms.assetid: '7677FC3C-3506-449C-95E7-67C5380E5B5E'
keywords: ["AddItem method Access Execution Engine", "AddItem method Access Execution Engine , MetricThresholdValueCollection interface", "MetricThresholdValueCollection interface Access Execution Engine , AddItem method"]
topic_type:
- apiref
api_name:
- MetricThresholdValueCollection.AddItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThresholdValueCollection::AddItem method

Creates and adds a **MetricThresholdValue** to the **MetricThresholdValueCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [in]            LPCWSTR                       descriptionProgrammaticName,
  [in]            MetricThresholdValueValueType valueType,
  [in]            LPCWSTR                       value,
  [out, optional] MetricThresholdValue          **metricThresholdValue
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

The metric threshold value type.

</dd> <dt>

*value* \[in\]
</dt> <dd>

The metric threshold value.

</dd> <dt>

*metricThresholdValue* \[out, optional\]
</dt> <dd>

The **MetricThresholdValue** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **MetricThresholdValueCollection** holds data from element **MetricThreshold/MetricThresholdValues**.

The **MetricThresholdValue** elements hold data from **MetricThresholdValues/MetricThresholdValue** elements.

The description programmatic name is the value of element **MetricThresholdValue/Description/ProgrammaticName**.

The metric threshold value type is the value of element **MetricThresholdValue/ValueType**. See [**MetricThresholdValueValueType**](metricthresholdvaluevaluetype.md) for the value types.

The metric threshold value is the value of element **MetricThresholdValue/Value**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThresholdValueCollection**](metricthresholdvaluecollection.md)
</dt> </dl>

 

 





