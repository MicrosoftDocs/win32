---
Description: Retrieves the Routing property for a FaxTiff object. The Routing property is a null-terminated string that contains the inbound routing string for a specified fax file.
ms.assetid: e39e0e99-0812-4226-9118-e0e072bf3084
title: FaxTiff.Routing property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxTiff.Routing property

Retrieves the **Routing** property for a [FaxTiff](-mfax-faxtiff.md) object. The **Routing** property is a null-terminated string that contains the inbound routing string for a specified fax file.

This property is read-only.

## Syntax


```VB
Property Routing As String
```



## Property value

A **String** that receives inbound routing information for the specified fax file.

## Remarks

A fax client application must set the [**Image**](-mfax-ifaxtiff-get-image-vb.md) property before retrieving another property for a [FaxTiff](-mfax-faxtiff.md) object.

The routing information is specific to a fax service provider (FSP); for example, direct inward dialing (DID) routing digits.

The **get\_Routing** method sets the *pVal* parameter to optional inbound routing information specified for the fax file, if it is available. If the information is not available, the method returns "Unavailable".

The **Routing** property is a string that represents optional inbound routing information specified for the fax file, if it is available. If the information is not available, **Routing** is an empty string.

The [**get\_Image**](-mfax-ifaxtiff-get-image-vb.md) method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxTiff**](-mfax-faxtiff-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxTiff**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxtiff?branch=master)
</dt> <dt>

[**Image**](-mfax-ifaxtiff-get-image-vb.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




