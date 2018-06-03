---
title: MetricThresholdValue GetDescriptionProgrammaticName method
description: Returns the description programmatic name of the MetricThresholdValue.
ms.assetid: 583DA8F0-98F2-4812-AC6B-4AD09958DA0E
keywords:
- GetDescriptionProgrammaticName method Access Execution Engine
- GetDescriptionProgrammaticName method Access Execution Engine , MetricThresholdValue interface
- MetricThresholdValue interface Access Execution Engine , GetDescriptionProgrammaticName method
topic_type:
- apiref
api_name:
- MetricThresholdValue.GetDescriptionProgrammaticName
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

# MetricThresholdValue::GetDescriptionProgrammaticName method

Returns the description programmatic name of the **MetricThresholdValue**.

## Syntax


```C++
virtual HRESULT GetDescriptionProgrammaticName(
  [out] LPCWSTR *descriptionProgrammaticName
) const = 0;
```



## Parameters

<dl> <dt>

*descriptionProgrammaticName* \[out\]
</dt> <dd>

The description programmatic name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **MetricThresholdValue** objects hold data from the **MetricThreshold/MetricThresholdValues/MetricThresholdValue** elements.

The description programmatic name is the value of element **MetricThresholdValue/Description/ProgrammaticName**.

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

 

 





