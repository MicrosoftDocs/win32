---
title: ResultSnippet AddWarning method
description: Creates an ErrorWarning object for use by the ResultSnippet object.
ms.assetid: A4155994-4208-49BD-BEC5-B0D4EA08D650
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
  [in]            INT          hresult,
  [in]            LPCWSTR      message,
  [out, optional] ErrorWarning **warning
) = 0;
```



## Parameters

<dl> <dt>

*hresult* \[in\]
</dt> <dd>

The **HRESULT** value associated with the new warning.

</dd> <dt>

*message* \[in\]
</dt> <dd>

The message text.

</dd> <dt>

*warning* \[out, optional\]
</dt> <dd>

The [**ErrorWarning**](errorwarning.md) object that this method generates for the new warning.

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

 

 





