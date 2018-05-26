---
title: MetricThresholdValue GetInclusion method
description: Returns the inclusion setting of the MetricThresholdValue.
ms.assetid: 2C865E9D-466D-4740-B966-0B5F2D6D2DB2
keywords:
- GetInclusion method Access Execution Engine
- GetInclusion method Access Execution Engine , MetricThresholdValue interface
- MetricThresholdValue interface Access Execution Engine , GetInclusion method
topic_type:
- apiref
api_name:
- MetricThresholdValue.GetInclusion
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

# MetricThresholdValue::GetInclusion method

Returns the inclusion setting of the **MetricThresholdValue**.

## Syntax


```C++
virtual HRESULT GetInclusion(
  [out] MetricThresholdValueInclusion *inclusion
) const = 0;
```



## Parameters

<dl> <dt>

*inclusion* \[out\]
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

 

 





