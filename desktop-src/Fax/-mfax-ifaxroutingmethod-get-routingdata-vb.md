---
Description: The RoutingData property is a null-terminated string that contains the routing string for an incoming fax transmission.
ms.assetid: aff86dda-f252-4ba1-80f6-1cf09732ddf6
title: FaxRoutingMethod.RoutingData property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxRoutingMethod.RoutingData property

The **RoutingData** property is a null-terminated string that contains the routing string for an incoming fax transmission.

This property is read-only.

## Syntax


```VB
Property RoutingData As String
```



## Property value

A **String** that receives the routing string for an incoming fax transmission. The string must be of the form: `Canonical-Phone-Number[|Additional-Routing-Info]` where `Canonical-Phone-Number` is defined in the [Address](http://msdn.microsoft.com/library/en-us/tapi/tapi3/address_ovr.asp) topic of the TAPI documentation (see the Canonical Address subheading); and `Additional-Routing-Info` is the *subaddress* of a Canonical Address, and uses the subaddress format.

## Remarks

**RoutingData** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxRoutingMethod**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxroutingmethod?branch=master)
</dt> <dt>

[**IFaxRoutingMethods**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxroutingmethods?branch=master)
</dt> </dl>

 

 




