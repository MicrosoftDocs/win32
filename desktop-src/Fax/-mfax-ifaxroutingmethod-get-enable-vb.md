---
Description: The Enable property is a Boolean value that indicates whether a fax routing method is enabled on a particular fax port.
ms.assetid: 750fda76-4c6e-4a8f-8f0f-304ae31f6f0a
title: FaxRoutingMethod.Enable property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxRoutingMethod.Enable property

The **Enable** property is a Boolean value that indicates whether a fax routing method is enabled on a particular fax port.

This property is read/write.

## Syntax


```VB
Property Enable As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the fax routing method is enabled or disabled for the parent fax port. If this parameter is equal to TRUE, the routing method is enabled for the port.

## Remarks

If a fax client application passes a value of TRUE to the **Enable** property, the property enables the routing method for inbound faxes on the parent port.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxRoutingMethod**](-mfax-faxroutingmethod-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxRoutingMethod**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxroutingmethod)
</dt> <dt>

[**IFaxRoutingMethods**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxroutingmethods)
</dt> <dt>

[**CanModify**](-mfax-ifaxport-get-canmodify-vb.md)
</dt> </dl>

 

 




