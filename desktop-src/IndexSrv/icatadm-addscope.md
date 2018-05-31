---
title: ICatAdm AddScope method
description: Creates a new scope.
ms.assetid: aa4ad351-7138-429d-b912-9b600da4b292
keywords:
- AddScope method Indexing Service
- AddScope method Indexing Service , ICatAdm interface
- ICatAdm interface Indexing Service , AddScope method
topic_type:
- apiref
api_name:
- ICatAdm.AddScope
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location:
- Ciodm.dll
api_type:
- COM
---

# ICatAdm::AddScope method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Creates a new scope.

## Syntax


```C++
HRESULT AddScope(
  [in]           BSTR         bstrScopeName,
  [in]           VARIANT_BOOL fExclude,
  [in, optional] VARIANT      vtLogon,
  [in, optional] VARIANT      vtPassword,
  [out, retval]  IDispatch    **pIDisp
);
```



## Parameters

<dl> <dt>

*bstrScopeName* \[in\]
</dt> <dd>

The case-insensitive scope path to be created. This path must be unique for a given catalog and must represent a valid local path or a universal naming convention (UNC) path.

</dd> <dt>

*fExclude* \[in\]
</dt> <dd>

If **VARIANT\_TRUE**, excludes this scope from indexing. If **VARIANT\_FALSE**, enables indexing for this scope.

</dd> <dt>

*vtLogon* \[in, optional\]
</dt> <dd>

A string that represents the logon name.

</dd> <dt>

*vtPassword* \[in, optional\]
</dt> <dd>

A string that represents the logon password.

</dd> <dt>

*pIDisp* \[out, retval\]
</dt> <dd>

The new ScopeAdm object. See [**IScopeAdm**](iscopeadm.md).

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                           | Description                                                                                                                       |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_ALREADY\_EXISTS**</dt> </dl> | The path in *bstrScopePath* already is in use.<br/>                                                                         |
| <dl> <dt>**E\_INVALIDARG** </dt> </dl>         | The logon and password values are included for local paths or the logon and password values are missing for UNC paths.<br/> |



 

## Remarks

The *vtLogon* and *vtPassword* parameters are optional. However, they are both required if the scope path is a UNC path. Neither parameter should be specified when the scope path is local.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ciodm.dll</dt> </dl> |



## See also

<dl> <dt>

[**ICatAdm**](icatadm.md)
</dt> </dl>

 

 





