---
Description: The FriendlyName property is a null-terminated string that contains the user-friendly name for a fax routing method.
ms.assetid: 9fdcc223-f919-4e55-af89-4734888fdbf7
title: FaxRoutingMethod.FriendlyName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxRoutingMethod.FriendlyName property

The **FriendlyName** property is a null-terminated string that contains the user-friendly name for a fax routing method.

This property is read-only.

## Syntax


```VB
Property FriendlyName As String
```



## Property value

A **String** that receives the user-friendly name to display for the fax routing method.

## Remarks

A fax client application can use the [**Guid**](-mfax-ifaxroutingmethod-get-guid-vb.md) property to uniquely identify a fax routing method. Note that it is possible for multiple routing methods to have the same user-friendly name, and even the same function name. For more information, see [Fax Routing Methods](-mfax-fax-routing-methods.md).

**FriendlyName** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**Guid**](-mfax-ifaxroutingmethod-get-guid-vb.md)
</dt> <dt>

[**FunctionName**](-mfax-ifaxroutingmethod-get-functionname-vb.md)
</dt> <dt>

[**FaxRouteMethod**](/previous-versions/windows/desktop/api/FaxRoute/)
</dt> </dl>

 

 




