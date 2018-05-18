---
title: MetricThreshold SetDescriptionProgrammaticName method
description: Sets the description programmatic name of the MetricThreshold.
ms.assetid: 'A5E0D8C7-FF9E-4604-8574-4C538036A58D'
keywords: ["SetDescriptionProgrammaticName method Access Execution Engine", "SetDescriptionProgrammaticName method Access Execution Engine , MetricThreshold interface", "MetricThreshold interface Access Execution Engine , SetDescriptionProgrammaticName method"]
topic_type:
- apiref
api_name:
- MetricThreshold.SetDescriptionProgrammaticName
api_location:
- AxeCore.dll
api_type:
- COM
---

# MetricThreshold::SetDescriptionProgrammaticName method

Sets the description programmatic name of the **MetricThreshold**.

## Syntax


```C++
virtual HRESULT SetDescriptionProgrammaticName(
  [in] LPCWSTR descriptionProgrammaticName
) = 0;
```



## Parameters

<dl> <dt>

*descriptionProgrammaticName* \[in\]
</dt> <dd>

The description programmatic name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

The description programmatic name is the value of element **MetricThreshold/Description/ProgrammaticName**.

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

 

 





