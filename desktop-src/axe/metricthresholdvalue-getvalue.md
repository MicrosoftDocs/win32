---
title: MetricThresholdValue GetValue method
description: Returns the value of the MetricThresholdValue.
ms.assetid: EB673F63-90D5-4553-937C-E4428E4D683D
keywords:
- GetValue method Access Execution Engine
- GetValue method Access Execution Engine , MetricThresholdValue interface
- MetricThresholdValue interface Access Execution Engine , GetValue method
topic_type:
- apiref
api_name:
- MetricThresholdValue.GetValue
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

# MetricThresholdValue::GetValue method

Returns the value of the **MetricThresholdValue**.

## Syntax


```C++
virtual HRESULT GetValue(
  [out] LPCWSTR *value
) const = 0;
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

The value.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **MetricThresholdValue** objects hold data from the **MetricThreshold/MetricThresholdValues/MetricThresholdValue** elements.

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

[**MetricThresholdValue**](metricthresholdvalue-struct.md)
</dt> </dl>

 

 





