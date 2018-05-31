---
Description: Sets or retrieves the ArchiveOutboundFaxes property for a FaxServer object. The ArchiveOutboundFaxes property is a Boolean value that indicates whether the fax server archives outgoing fax transmissions.
ms.assetid: af23fb55-68e0-42bb-bdcb-1cddcf4328b8
title: FaxServer.ArchiveOutboundFaxes property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.ArchiveOutboundFaxes property

Sets or retrieves the **ArchiveOutboundFaxes** property for a [FaxServer](-mfax-faxserver-client.md) object. The **ArchiveOutboundFaxes** property is a Boolean value that indicates whether the fax server archives outgoing fax transmissions.

This property is read/write.

## Syntax


```VB
Property ArchiveOutboundFaxes As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the fax server archives outgoing fax transmissions. If this parameter is equal to **True**, the server archives outgoing transmissions in the directory specified by the [**ArchiveDirectory**](-mfax-ifaxserver-get-archivedirectory-vb.md) property.

## Remarks

The fax server ignores this property unless the [**ArchiveDirectory**](-mfax-ifaxserver-get-archivedirectory-vb.md) property is specified.

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

[**ArchiveDirectory**](-mfax-ifaxserver-get-archivedirectory-vb.md)
</dt> </dl>

 

 




