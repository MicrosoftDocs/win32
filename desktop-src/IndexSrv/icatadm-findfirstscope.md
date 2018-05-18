---
title: ICatAdm FindFirstScope method
description: Initializes scope enumeration for a catalog and checks to see whether a catalog exists.
ms.assetid: '39ac2ad6-fee7-4ddf-89bc-2c0effbbdf40'
keywords: ["FindFirstScope method Indexing Service", "FindFirstScope method Indexing Service , ICatAdm interface", "ICatAdm interface Indexing Service , FindFirstScope method"]
topic_type:
- apiref
api_name:
- ICatAdm.FindFirstScope
api_location:
- Ciodm.dll
api_type:
- COM
---

# ICatAdm::FindFirstScope method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Initializes scope enumeration for a catalog and checks to see whether a catalog exists.

## Syntax


```C++
HRESULT FindFirstScope(
  [out, retval] VARIANT_BOOL *pfFound
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
' Find the first scope
If (objCatAdm.FindFirstScope( ) ) Then
    Set objScopeAdm = objCatAdm.GetScope()
'  Use it
'  Free when finished
    Set objScopeAdm = Nothing
End If 
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ciodm.dll</dt> </dl> |



## See also

<dl> <dt>

[**ICatAdm**](icatadm.md)
</dt> </dl>

 

 





