---
title: MetricThresholdCollection AddItem method
description: Creates and adds a MetricThreshold to the MetricThresholdCollection.
ms.assetid: 9197B37E-F5A9-413F-96A1-F2BBFD1C3BCC
keywords:
- AddItem method Access Execution Engine
- AddItem method Access Execution Engine , MetricThresholdCollection interface
- MetricThresholdCollection interface Access Execution Engine , AddItem method
topic_type:
- apiref
api_name:
- MetricThresholdCollection.AddItem
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

# MetricThresholdCollection::AddItem method

Creates and adds a [**MetricThreshold**](metricthreshold-struct.md) to the **MetricThresholdCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [in]            LPCWSTR         descriptionProgrammaticName,
  [in]            LPCWSTR         metricDefinitionProgrammaticName,
  [out, optional] MetricThreshold **metricThreshold
) = 0;
```



## Parameters

<dl> <dt>

*descriptionProgrammaticName* \[in\]
</dt> <dd>

The description programmatic name.

</dd> <dt>

*metricDefinitionProgrammaticName* \[in\]
</dt> <dd>

The metric definition programmatic name.

</dd> <dt>

*metricThreshold* \[out, optional\]
</dt> <dd>

The **MetricThreshold** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **MetricThresholdCollection** holds data from a **MetricThresholds** element.

A **MetricThreshold** holds data from a **MetricThresholds/MetricThreshold** element.

The description programmatic name is the value of element **MetricThreshold/Description/ProgrammaticName**.

The metric definition programmatic name is the value of element **MetricThreshold/MetricDefinitionProgrammaticName**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**MetricThresholdCollection**](metricthresholdcollection.md)
</dt> </dl>

 

 





