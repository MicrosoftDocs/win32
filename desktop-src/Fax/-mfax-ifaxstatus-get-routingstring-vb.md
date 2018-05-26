---
Description: Retrieves the RoutingString property for the FaxStatus object of a parent FaxPort object. The RoutingString property is a null-terminated string that contains routing information for inbound fax transmissions that is specific to a fax service provider.
ms.assetid: 186cd255-d475-42dd-96a7-128dc5649781
title: FaxStatus.RoutingString property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxStatus.RoutingString property

Retrieves the **RoutingString** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **RoutingString** property is a null-terminated string that contains routing information for inbound fax transmissions that is specific to a fax service provider.

This property is read-only.

## Syntax


```VB
Property RoutingString As String
```



## Property value

A **String** that receives the routing information for an inbound fax transmission. Note that the **RoutingString** property is valid only if the [**Receive**](-mfax-ifaxstatus-get-receive-vb.md) property is equal to **True**.

## Remarks

The **IFaxStatus::get\_RoutingString** method sets the *pVal* parameter to optional inbound routing information, if it is available. If the information is not available, the method returns an empty string.

The **IFaxStatus::get\_RoutingString** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxStatus**](-mfax-faxstatus-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxStatus**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxstatus?branch=master)
</dt> <dt>

[**Receive**](-mfax-ifaxstatus-get-receive-vb.md)
</dt> <dt>

[**IFaxPorts**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxports?branch=master)
</dt> <dt>

[**IFaxPort**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxport?branch=master)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




