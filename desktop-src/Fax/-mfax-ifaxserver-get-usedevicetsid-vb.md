---
Description: Sets or retrieves the UseDeviceTsid property for a FaxServer object. The UseDeviceTsid property is a Boolean value that indicates whether the fax server uses the device's transmitting station identifier (TSID) instead of a user-specified TSID.
ms.assetid: c0ab5267-7867-4587-b5ac-f8500bcfb64a
title: FaxServer.UseDeviceTsid property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.UseDeviceTsid property

Sets or retrieves the **UseDeviceTsid** property for a [FaxServer](-mfax-faxserver-client.md) object. The **UseDeviceTsid** property is a Boolean value that indicates whether the fax server uses the device's transmitting station identifier (TSID) instead of a user-specified TSID.

This property is read/write.

## Syntax


```VB
Property UseDeviceTsid As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the fax server uses the device's TSID or a user-specified TSID for outgoing fax transmissions. If this parameter is equal to **True**, the fax server uses the device's TSID.

## Remarks

To ensure that the TSID for a port is associated with outbound faxes, set the **UseDeviceTsid** property equal to **True**. This overrides the TSID a user can optionally specify for an outbound fax by setting the [**Tsid**](-mfax-ifaxdoc-get-tsid-vb.md) property.

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

[**Tsid**](-mfax-ifaxdoc-get-tsid-vb.md)
</dt> </dl>

 

 




