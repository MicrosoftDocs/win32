---
title: MetricThreshold GetTarget method
description: Returns the target of the MetricThreshold.
ms.assetid: 'A1A29086-D089-496F-91B8-03C98C71282C'
keywords: ["GetTarget method Access Execution Engine", "GetTarget method Access Execution Engine , MetricThreshold interface", "MetricThreshold interface Access Execution Engine , GetTarget method"]
topic_type:
- apiref
api_name:
- MetricThreshold.GetTarget
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThreshold::GetTarget method

Returns the target of the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT GetTarget(
  [out] LPCWSTR *target
) const = 0;
```



## Parameters

<dl> <dt>

*target* \[out\]
</dt> <dd>

The target.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

The target is the value of element **MetricThreshold/Target**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThreshold**](metricthreshold-struct.md)
</dt> </dl>

 

 





