---
title: ICatAdm GetScope method
description: Retrieves the current scope object.
ms.assetid: 7e4c26d2-cd6e-4b07-a3e3-5d234c176ae7
keywords:
- GetScope method Indexing Service
- GetScope method Indexing Service , ICatAdm interface
- ICatAdm interface Indexing Service , GetScope method
topic_type:
- apiref
api_name:
- ICatAdm.GetScope
api_location:
- Ciodm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ICatAdm::GetScope method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves the current scope object.

## Syntax


```C++
HRESULT GetScope(
  [out, retval] IDispatch **pIDisp
);
```



## Parameters

<dl> <dt>

*pIDisp* \[out, retval\]
</dt> <dd>

The current scope object. See [**IScopeAdm**](iscopeadm.md).

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method assumes that the scope exists and has been found by enumerating a catalog administration object's collection of scopes using [**FindFirstScope**](icatadm-findfirstscope.md) or [**FindNextScope**](icatadm-findnextscope.md).

## Examples

For an example, see [**FindFirstScope**](icatadm-findfirstscope.md) or [**FindNextScope**](icatadm-findnextscope.md).

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

 

 





