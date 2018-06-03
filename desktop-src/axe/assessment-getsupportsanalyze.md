---
title: Assessment GetSupportsAnalyze method
description: Returns an indicator of whether the assessment supports re-analysis (analysis separate from execution).
ms.assetid: 2DE64361-5C79-40C3-88B8-D9E2E3379E20
keywords:
- GetSupportsAnalyze method Access Execution Engine
- GetSupportsAnalyze method Access Execution Engine , Assessment interface
- Assessment interface Access Execution Engine , GetSupportsAnalyze method
topic_type:
- apiref
api_name:
- Assessment.GetSupportsAnalyze
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

# Assessment::GetSupportsAnalyze method

Returns an indicator of whether the assessment supports re-analysis (analysis separate from execution).

## Syntax


```C++
virtual HRESULT GetSupportsAnalyze(
  [out] BOOL *analyze
) const = 0;
```



## Parameters

<dl> <dt>

*analyze* \[out\]
</dt> <dd>

The indicator.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The indicator *analyze* is **TRUE** if the assessment supports analyze, and **FALSE** if it does not.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Assessment**](assessment-inf.md)
</dt> </dl>

 

 





