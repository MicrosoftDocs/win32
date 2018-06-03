---
title: MetricThresholdValue SetDescriptionProgrammaticName method
description: Sets the description programmatic name of the MetricThresholdValue.
ms.assetid: B3256515-8E75-4314-9B7C-75FDADED33BB
keywords:
- SetDescriptionProgrammaticName method Access Execution Engine
- SetDescriptionProgrammaticName method Access Execution Engine , MetricThresholdValue interface
- MetricThresholdValue interface Access Execution Engine , SetDescriptionProgrammaticName method
topic_type:
- apiref
api_name:
- MetricThresholdValue.SetDescriptionProgrammaticName
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

# MetricThresholdValue::SetDescriptionProgrammaticName method

Sets the description programmatic name of the **MetricThresholdValue**.

## Syntax


```C++
virtual HRESULT SetDescriptionProgrammaticName(
  [in] LPCWSTR descriptionProgrammaticName
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

 

 





