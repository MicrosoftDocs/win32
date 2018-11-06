---
Description: Indicates that a search has finished.
title: IShellFolderSearchableCallback::RunEnd method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellFolderSearchableCallback.RunEnd
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellFolderSearchableCallback::RunEnd method

Indicates that a search has finished.

## Syntax


```C++
HRESULT RunEnd(
  [in] DWORD dwReserved
);
```



## Parameters

<dl> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved. Must be set to 0.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 




