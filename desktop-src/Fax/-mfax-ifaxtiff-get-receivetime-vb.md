---
Description: Retrieves the ReceiveTime property for a FaxTiff object.
ms.assetid: 149c9bfd-9733-42ec-a583-95f758f5c97e
title: FaxTiff.ReceiveTime property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxTiff.ReceiveTime property

Retrieves the **ReceiveTime** property for a [FaxTiff](-mfax-faxtiff.md) object. The **ReceiveTime** property is a null-terminated string that contains the time at which reception began for an inbound fax file. The string can contain the time at which reception or transmission began for an archived file.

This property is read-only.

## Syntax


```VB
Property ReceiveTime As String
```



## Property value

A **String** that receives the time at which reception or transmission began for the specified fax file.

## Remarks

A fax client application must set the [**Image**](-mfax-ifaxtiff-get-image-vb.md) property before retrieving another property for a [FaxTiff](-mfax-faxtiff.md) object.

The **get\_ReceiveTime** method sets the *pVal* parameter to the time at which reception began for an inbound fax file, if it is available. If the information is not available, the method returns an empty string.

The **ReceiveTime** property is a string that represents the time at which reception began for an inbound fax file, if it is available. If the information is not available, **RecipientName** is "Unavailable".

The **get\_ReceiveTime** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

The fax service formats the string according to the user's locale. It is a concatenation of the date and time the service transmitted the fax. The date is separated from the time by an "@" character. For example, in the English locale, a string would be formatted as follows:

10/02/98@10:15AM

The [**RawReceiveTime**](-mfax-ifaxtiff-get-rawreceivetime-vb.md) property contains the time expressed in Coordinated Universal Time (UTC).

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

[**RawReceiveTime**](-mfax-ifaxtiff-get-rawreceivetime-vb.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




