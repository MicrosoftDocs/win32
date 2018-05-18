---
title: MetricThreshold SetOrdinal method
description: Sets the ordinal of the MetricThreshold.
ms.assetid: '242B9A6D-0541-473E-89E4-9F224C01287D'
keywords: ["SetOrdinal method Access Execution Engine", "SetOrdinal method Access Execution Engine , MetricThreshold interface", "MetricThreshold interface Access Execution Engine , SetOrdinal method"]
topic_type:
- apiref
api_name:
- MetricThreshold.SetOrdinal
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThreshold::SetOrdinal method

Sets the ordinal of the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT SetOrdinal(
  [in] UINT ordinal
) = 0;
```



## Parameters

<dl> <dt>

*ordinal* \[in\]
</dt> <dd>

The ordinal.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

The ordinal is the value of element **MetricThreshold/Ordinal**.

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

 

 





