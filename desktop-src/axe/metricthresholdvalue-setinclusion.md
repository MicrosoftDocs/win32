---
title: MetricThresholdValue SetInclusion method
description: Sets the inclusion setting of the MetricThresholdValue.
ms.assetid: D634F394-C805-4A7E-A04F-26A686A5A624
keywords:
- SetInclusion method Access Execution Engine
- SetInclusion method Access Execution Engine , MetricThresholdValue interface
- MetricThresholdValue interface Access Execution Engine , SetInclusion method
topic_type:
- apiref
api_name:
- MetricThresholdValue.SetInclusion
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

# MetricThresholdValue::SetInclusion method

Sets the inclusion setting of the **MetricThresholdValue**.

## Syntax


```C++
virtual HRESULT SetInclusion(
  [in] MetricThresholdValueInclusion inclusion
) = 0;
```



## Parameters

<dl> <dt>

*inclusion* \[in\]
</dt> <dd>

The inclusion setting.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **MetricThresholdValue** objects hold data from the **MetricThreshold/MetricThresholdValues/MetricThresholdValue** elements.

The inclusion setting is the value of element **MetricThresholdValue/Inclusion**. See [**MetricThresholdValueInclusion**](metricthresholdvalueinclusion.md) for the inclusion settings.

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

 

 





