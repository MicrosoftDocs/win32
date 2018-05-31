---
Description: Sets or retrieves the Branding property for a FaxServer object. The Branding property is a Boolean value that indicates whether the fax server generates branding information at the top of fax transmissions.
ms.assetid: 79552927-191f-48c8-a456-44f669ce418b
title: FaxServer.Branding property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.Branding property

Sets or retrieves the **Branding** property for a [FaxServer](-mfax-faxserver-client.md) object. The **Branding** property is a Boolean value that indicates whether the fax server generates branding information at the top of fax transmissions.

This property is read/write.

## Syntax


```VB
Property Branding As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the fax server generates a brand (banner) at the top of fax transmissions. If this parameter is equal to **True**, the fax server generates branding information.

## Remarks

A brand is an informational header at the top of most fax pages that typically contains the transmission time, the page count, and the transmitting station identifier. Branding may be required by law in some locales.

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
</dt> </dl>

 

 




