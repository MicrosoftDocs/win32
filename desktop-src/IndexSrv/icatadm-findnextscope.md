---
title: ICatAdm FindNextScope method
description: Enumerates a collection of scopes for the current catalog and checks whether another catalog exists.
ms.assetid: 10c4db08-a61e-4e54-afb6-10e46abc0420
keywords:
- FindNextScope method Indexing Service
- FindNextScope method Indexing Service , ICatAdm interface
- ICatAdm interface Indexing Service , FindNextScope method
topic_type:
- apiref
api_name:
- ICatAdm.FindNextScope
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

# ICatAdm::FindNextScope method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Enumerates a collection of scopes for the current catalog and checks whether another catalog exists.

## Syntax


```C++
HRESULT FindNextScope(
  [out, retval] VARIANT_BOOL *pfFound
);
```



## Parameters

<dl> <dt>

*pfFound* \[out, retval\]
</dt> <dd>

**VARIANT\_TRUE** if a scope was found, **VARIANT\_FALSE** otherwise.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If a scope exists, use [**GetScope**](icatadm-getscope.md) to retrieve the scope object.

## Examples


```VB
' Enumerate through the scopes
Do While (objCatAdm.FindNextScope() ) 
    Set objScopeAdm = objCatAdm.GetScope() 
'  Use it
'  Free it when done
    Set objScopeAdm = Nothing
Loop
```



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

 

 





