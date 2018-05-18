---
title: ResultSnippet AddError method
description: Creates an ErrorWarning error object for use by the ResultSnippet object.
ms.assetid: '998B2419-0684-4BD3-9E08-212A5CDE209A'
keywords: ["AddError method Access Execution Engine", "AddError method Access Execution Engine , ResultSnippet interface", "ResultSnippet interface Access Execution Engine , AddError method"]
topic_type:
- apiref
api_name:
- ResultSnippet.AddError
api_location:
- AxeCore.dll
api_type:
- COM
---

# ResultSnippet::AddError method

Creates an [**ErrorWarning**](errorwarning.md) error object for use by the [**ResultSnippet**](resultsnippet.md) object.

## Syntax


```C++
virtual HRESULT AddError(
  [in]            INT          hresult,
  [in]            LPCWSTR      message,
  [out, optional] ErrorWarning **warning
) = 0;
```



## Parameters

<dl> <dt>

*hresult* \[in\]
</dt> <dd>

The **HRESULT** value associated with the new error.

</dd> <dt>

*message* \[in\]
</dt> <dd>

The message text.

</dd> <dt>

*warning* \[out, optional\]
</dt> <dd>

The [**ErrorWarning**](errorwarning.md) error object that this method generates for the new error.

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

 

 





