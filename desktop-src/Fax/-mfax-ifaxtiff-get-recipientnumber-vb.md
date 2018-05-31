---
Description: Retrieves the RecipientNumber property for a FaxTiff object. The RecipientNumber property is a null-terminated string that contains the fax number to which a fax was transmitted.
ms.assetid: 5180cb6e-5489-4aeb-99fe-b5648fcabecb
title: FaxTiff.RecipientNumber property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxTiff.RecipientNumber property

Retrieves the **RecipientNumber** property for a [FaxTiff](-mfax-faxtiff.md) object. The **RecipientNumber** property is a null-terminated string that contains the fax number to which a fax was transmitted.

This property is read-only.

## Syntax


```VB
Property RecipientNumber As String
```



## Property value

A **String** that receives the fax number for the recipient of the fax document.

## Remarks

A fax client application must set the [**Image**](-mfax-ifaxtiff-get-image-vb.md) property before retrieving another property for a [FaxTiff](-mfax-faxtiff.md) object.

The **RecipientNumber** property has meaning only for outbound fax transmissions. This is because the [**Csid**](-mfax-ifaxtiff-get-csid-vb.md) property and the **RecipientNumber** property are identical for inbound faxes.

The **get\_RecipientNumber** method sets the *pVal* parameter to the fax number of the fax recipient, if it is available. If the information is not available, the method returns "Unavailable".

The **RecipientNumber** property is a string that represents the fax number of the fax recipient, if it is available. If the information is not available, **RecipientNumber** is an empty string.

The **get\_RecipientNumber** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxTiff**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxtiff)
</dt> <dt>

[**Image**](-mfax-ifaxtiff-get-image-vb.md)
</dt> <dt>

[**Csid**](-mfax-ifaxtiff-get-csid-vb.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




