---
title: ResultSnippet GetErrorsAndWarnings method
description: Returns an ErrorWarningsCollection object that contains the errors and warnings for this ResultsSnippet.
ms.assetid: 951B729D-0AB8-42DE-AD25-BEA2798724EA
keywords:
- GetErrorsAndWarnings method Access Execution Engine
- GetErrorsAndWarnings method Access Execution Engine , ResultSnippet interface
- ResultSnippet interface Access Execution Engine , GetErrorsAndWarnings method
topic_type:
- apiref
api_name:
- ResultSnippet.GetErrorsAndWarnings
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

# ResultSnippet::GetErrorsAndWarnings method

Returns an [**ErrorWarningsCollection**](errorwarningcollection.md) object that contains the errors and warnings for this ResultsSnippet.

## Syntax


```C++
virtual HRESULT GetErrorsAndWarnings(
  [out] ErrorWarningCollection **errorsAndWarnings
) = 0;
```



## Parameters

<dl> <dt>

*errorsAndWarnings* \[out\]
</dt> <dd>

The [**ErrorWarningsCollection**](errorwarningcollection.md) object that this method returns.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ResultSnippet**](resultsnippet.md)
</dt> </dl>

 

 





