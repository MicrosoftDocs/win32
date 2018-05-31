---
Description: The Guid property is a null-terminated string that contains the GUID that uniquely identifies the fax routing method.
ms.assetid: 3108d8db-cdcf-4d5a-8e1e-caf93be6ed94
title: FaxRoutingMethod.Guid property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxRoutingMethod.Guid property

The **Guid** property is a null-terminated string that contains the GUID that uniquely identifies the fax routing method.

This property is read-only.

## Syntax


```VB
Property Guid As String
```



## Property value

A **String** that receives the GUID that uniquely identifies an extension-defined fax routing method. The fax routing extension DLL identified by the [**ImageName**](-mfax-ifaxroutingmethod-get-imagename-vb.md) property exports the function.

## Remarks

A fax client application can use the **Guid** property to uniquely identify a fax routing method. It is possible for multiple routing methods to have the same user-friendly name, and even the same function name. For more information, see [Fax Routing Methods](-mfax-fax-routing-methods.md).

**Guid** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxRoutingMethod**](-mfax-ifaxroutingmethod.md)
</dt> <dt>

[**IFaxRoutingMethods**](-mfax-ifaxroutingmethods.md)
</dt> <dt>

[**FriendlyName**](-mfax-ifaxroutingmethod-get-friendlyname-vb.md)
</dt> <dt>

[**FunctionName**](-mfax-ifaxroutingmethod-get-functionname-vb.md)
</dt> </dl>

 

 




