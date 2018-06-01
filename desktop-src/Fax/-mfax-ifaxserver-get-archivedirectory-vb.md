---
Description: The ArchiveDirectory method retrieves the ArchiveDirectory property for a FaxServer object. The ArchiveDirectory property is a null-terminated string that contains the location in which the fax server stores archived outbound faxes.
ms.assetid: 4d4505a0-9ced-4c8c-b75e-0080ff2e3742
title: FaxServer.ArchiveDirectory property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.ArchiveDirectory property

The **ArchiveDirectory** method retrieves the **ArchiveDirectory** property for a [FaxServer](-mfax-faxserver-client.md) object. The **ArchiveDirectory** property is a null-terminated string that contains the location in which the fax server stores archived outbound faxes.

This property is read/write.

## Syntax


```VB
Property ArchiveDirectory As String
```



## Property value

A **String** that specifies or receives the fully qualified path of the directory in which the fax server should archive outgoing fax transmissions. The path can be a UNC path or a path beginning with a drive letter. The fax server ignores this value if the [**ArchiveOutboundFaxes**](-mfax-ifaxserver-get-archiveoutboundfaxes-vb.md) property is **False**.

## Remarks

Set the [**ArchiveOutboundFaxes**](-mfax-ifaxserver-get-archiveoutboundfaxes-vb.md) property to **True** to archive faxes in the directory specified by the **ArchiveDirectory** property. The fax server must have access to the directory to successfully store outbound fax transmissions.

The **get\_ArchiveDirectory** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**ArchiveOutboundFaxes**](-mfax-ifaxserver-get-archiveoutboundfaxes-vb.md)
</dt> <dt>

[Freeing Fax Resources](-mfax-freeing-fax-resources.md)
</dt> </dl>

 

 




