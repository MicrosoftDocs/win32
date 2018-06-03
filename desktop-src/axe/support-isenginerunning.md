---
title: Support IsEngineRunning method
description: Determines if the Axe engine is running, which tells an assessment if it is running under Axe.
ms.assetid: 488925DC-BAD4-4741-A1AE-B12F64CCA338
keywords:
- IsEngineRunning method Access Execution Engine
- IsEngineRunning method Access Execution Engine , Support interface
- Support interface Access Execution Engine , IsEngineRunning method
topic_type:
- apiref
api_name:
- Support.IsEngineRunning
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

# Support::IsEngineRunning method

Determines if the Axe engine is running, which tells an assessment if it is running under Axe.

## Syntax


```C++
virtual HRESULT IsEngineRunning(
  [out] BOOL *engineRunning
) const = 0;
```



## Parameters

<dl> <dt>

*engineRunning* \[out\]
</dt> <dd>

A Boolean value that indicates whether the Axe engine is running.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

This method enables an assessment to determine if Axe is running.

Managed code uses the [**Support.EngineRunning**](https://www.bing.com/search?q=**Support.EngineRunning**) property.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> </dl>

 

 





