---
Description: Sets or retrieves the ServerCoverpage property for a FaxServer object. The ServerCoverpage property is a Boolean value that indicates whether the fax server permits the use of common cover pages only.
ms.assetid: b8e22223-eada-44b6-9a84-45b5a29f6eb2
title: FaxServer.ServerCoverpage property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.ServerCoverpage property

Sets or retrieves the **ServerCoverpage** property for a [FaxServer](-mfax-faxserver-client.md) object. The **ServerCoverpage** property is a Boolean value that indicates whether the fax server permits the use of common cover pages only.

This property is read/write.

## Syntax


```VB
Property ServerCoverpage As Boolean
```



## Property value

A **Boolean** that specifies or receives whether fax client applications can include a user-designed cover page with a fax transmission, or whether the fax server permits the use of common cover pages only.

If this value is **True**, the client must use the common cover page located on the fax server. If this value is **False**, the client can use any cover page file.

## Remarks

If you set the **ServerCoverpage** property equal to **True**, users will be able to transmit only approved cover pages that are located on the fax server. For more information, see [Cover Pages](-mfax-cover-pages.md) and [Sending a Cover Page](-mfax-sending-a-cover-page.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxServer**](-mfax-faxserver-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[FaxServer](-mfax-faxserver-client.md)
</dt> <dt>

[Cover Pages](-mfax-cover-pages.md)
</dt> <dt>

[Sending a Cover Page](-mfax-sending-a-cover-page.md)
</dt> </dl>

 

 




