---
title: Engine AnalyzeResults method
description: Analyzes the assessment results.
ms.assetid: '71282C73-2304-4C26-B7FF-91553809E292'
keywords: ["AnalyzeResults method Access Execution Engine", "AnalyzeResults method Access Execution Engine , Engine interface", "Engine interface Access Execution Engine , AnalyzeResults method"]
topic_type:
- apiref
api_name:
- Engine.AnalyzeResults
api_location:
- AxeCore.dll
api_type:
- COM
---

# Engine::AnalyzeResults method

Analyzes the assessment results.

## Syntax


```C++
virtual HRESULT AnalyzeResults(
  [in] AnalyzeResultsInfo *info
) = 0;
```



## Parameters

<dl> <dt>

*info* \[in\]
</dt> <dd>

Information to supply and direct the results analysis activity.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

Parameter *info* is an [**AnalyzeResultsInfo**](analyzeresultsinfo.md) structure.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Engine**](engine-if.md)
</dt> </dl>

 

 





