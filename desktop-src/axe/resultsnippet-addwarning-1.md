---
title: ResultSnippet AddWarning method
description: Creates an ErrorWarning object for use by the ResultSnippet object.
ms.assetid: 4B1BEC5C-3F15-4466-8613-A11BB1D014B5
keywords:
- AddWarning method Access Execution Engine
- AddWarning method Access Execution Engine , ResultSnippet interface
- ResultSnippet interface Access Execution Engine , AddWarning method
topic_type:
- apiref
api_name:
- ResultSnippet.AddWarning
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

# ResultSnippet::AddWarning method

Creates an [**ErrorWarning**](errorwarning.md) object for use by the [**ResultSnippet**](resultsnippet.md) object.

## Syntax


```C++
virtual HRESULT AddWarning(
  [in] LPCWSTR message
) = 0;
```



## Parameters

<dl> <dt>

*message* \[in\]
</dt> <dd>

The message text.

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

 

 





