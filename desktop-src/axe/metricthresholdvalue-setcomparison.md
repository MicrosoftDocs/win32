---
title: MetricThresholdValue SetComparison method
description: Sets the comparison setting of the MetricThresholdValue.
ms.assetid: CAA80788-F1E6-4D2E-986D-CA2E058A568E
keywords:
- SetComparison method Access Execution Engine
- SetComparison method Access Execution Engine , MetricThresholdValue interface
- MetricThresholdValue interface Access Execution Engine , SetComparison method
topic_type:
- apiref
api_name:
- MetricThresholdValue.SetComparison
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MetricThresholdValue::SetComparison method

Sets the comparison setting of the **MetricThresholdValue**.

## Syntax


```C++
virtual HRESULT SetComparison(
  [in] MetricThresholdValueComparison comparison
) = 0;
```



## Parameters

<dl> <dt>

*comparison* \[in\]
</dt> <dd>

The comparison setting.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **MetricThresholdValue** objects hold data from the **MetricThreshold/MetricThresholdValues/MetricThresholdValue** elements.

The comparison setting is the value of element **MetricThresholdValue/Comparison**. See [**MetricThresholdValueComparison**](metricthresholdvaluecomparison.md) for the comparison settings.

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

 

 





