---
title: ResultSnippet AddWarning method
description: Creates an ErrorWarning object for use by the ResultSnippet object.
ms.assetid: 'E02CED38-9937-4B70-B8F4-00ED08E3CACD'
keywords: ["AddWarning method Access Execution Engine", "AddWarning method Access Execution Engine , ResultSnippet interface", "ResultSnippet interface Access Execution Engine , AddWarning method"]
topic_type:
- apiref
api_name:
- ResultSnippet.AddWarning
api_location:
- AxeCore.dll
api_type:
- COM
---

# ResultSnippet::AddWarning method

Creates an [**ErrorWarning**](errorwarning.md) object for use by the [**ResultSnippet**](resultsnippet.md) object.

## Syntax


```C++
virtual HRESULT AddWarning(
  [in] INT     hresult,
  [in] LPCWSTR message
) = 0;
```



## Parameters

<dl> <dt>

*hresult* \[in\]
</dt> <dd>

The **HRESULT** value associated with the new [**ErrorWarning**](errorwarning.md).

</dd> <dt>

*message* \[in\]
</dt> <dd>

The message text.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ResultSnippet**](resultsnippet.md)
</dt> </dl>

 

 





