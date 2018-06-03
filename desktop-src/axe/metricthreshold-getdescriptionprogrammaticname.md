---
title: MetricThreshold GetDescriptionProgrammaticName method
description: Returns the description programmatic name of the MetricThreshold.
ms.assetid: EF033DA6-035C-4F22-B1DB-6FF27C295986
keywords:
- GetDescriptionProgrammaticName method Access Execution Engine
- GetDescriptionProgrammaticName method Access Execution Engine , MetricThreshold interface
- MetricThreshold interface Access Execution Engine , GetDescriptionProgrammaticName method
topic_type:
- apiref
api_name:
- MetricThreshold.GetDescriptionProgrammaticName
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

# MetricThreshold::GetDescriptionProgrammaticName method

Returns the description programmatic name of the **MetricThreshold**.

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

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

The description programmatic name is the value of element **MetricThreshold/Description/ProgrammaticName**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThreshold**](metricthreshold-struct.md)
</dt> </dl>

 

 





