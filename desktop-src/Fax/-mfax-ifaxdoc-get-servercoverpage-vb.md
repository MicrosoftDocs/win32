---
Description: Sets or retrieves the ServerCoverpage property for a FaxDoc object. The ServerCoverpage property is a Boolean value that indicates whether the specified cover page file is stored on the fax server.
ms.assetid: 86895798-9451-40a8-95e0-35bab5871ede
title: FaxDoc.ServerCoverpage property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDoc.ServerCoverpage property

Sets or retrieves the **ServerCoverpage** property for a [FaxDoc](-mfax-faxdoc.md) object. The **ServerCoverpage** property is a Boolean value that indicates whether the specified cover page file is stored on the fax server.

This property is read/write.

## Syntax


```VB
Property ServerCoverpage As Boolean
```



## Property value

A **Boolean** that specifies or receives a value that indicates whether the specified cover page template file (.cov) is a common cover page file stored on the fax server.

## Remarks

You can send a common cover page or a personal cover page with a fax document. For more information, see [Cover Pages](-mfax-cover-pages.md) and [Sending a Cover Page](-mfax-sending-a-cover-page.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> </dl>

 

 




