---
title: ICatAdm IsCatalogRunning method
description: Determines whether the catalog is in read/write mode.
ms.assetid: 79ad81d6-820d-4f2d-945e-0ba939eed067
keywords:
- IsCatalogRunning method Indexing Service
- IsCatalogRunning method Indexing Service , ICatAdm interface
- ICatAdm interface Indexing Service , IsCatalogRunning method
topic_type:
- apiref
api_name:
- ICatAdm.IsCatalogRunning
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

# ICatAdm::IsCatalogRunning method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Determines whether the catalog is in read/write mode.

## Syntax


```C++
HRESULT IsCatalogRunning(
  [out, retval] VARIANT_BOOL *pfIsRunning
);
```



## Parameters

<dl> <dt>

*pfIsRunning* \[out, retval\]
</dt> <dd>

**VARIANT\_TRUE** if the catalog is in read/write mode, otherwise **VARIANT\_FALSE**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 





