---
Description: Enables Indexing Service to start automatically.
ms.assetid: c2fdbaa4-216f-4c5c-8e4c-27b46e8ea7e0
title: IAdminIndexServer::EnableCI method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAdminIndexServer::EnableCI method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Enables Indexing Service to start automatically.

## Syntax


```C++
HRESULT EnableCI(
  [in] VARIANT_BOOL fAutoStart
);
```



## Parameters

<dl> <dt>

*fAutoStart* \[in\]
</dt> <dd>

**VARIANT\_TRUE** if the Indexing Service should start automically. **VARIANT\_FALSE** if it should be started manually.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The default setting for the Indexing Service for it to be started manually. When *fAutoStart* is set to **VARIANT\_TRUE**, this method configures the Indexing Service to start automatically when the system reboots. After the service is started, it proceeds to process content on the system and place it into the index.

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

[**IAdminIndexServer**](iadminindexserver.md)
</dt> </dl>

 

 




