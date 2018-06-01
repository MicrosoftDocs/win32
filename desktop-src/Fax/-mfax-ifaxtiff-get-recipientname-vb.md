---
Description: Retrieves the RecipientName property for a FaxTiff object. The RecipientName property is a null-terminated string that contains the name of the recipient for the specified fax file.
ms.assetid: 778f41ff-f958-45a1-b657-bbb0d49a2789
title: FaxTiff.RecipientName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxTiff.RecipientName property

Retrieves the **RecipientName** property for a [FaxTiff](-mfax-faxtiff.md) object. The **RecipientName** property is a null-terminated string that contains the name of the recipient for the specified fax file.

This property is read-only.

## Syntax


```VB
Property RecipientName As String
```



## Property value

A **String** that receives the name of the recipient of the specified fax file.

## Remarks

A fax client application must set the [**Image**](-mfax-ifaxtiff-get-image-vb.md) property before retrieving another property for a [FaxTiff](-mfax-faxtiff.md) object.

The **get\_RecipientName** method sets the *pVal* parameter to the name of the fax recipient, if it is available. If the information is not available, the method returns "Unavailable".

The **RecipientName** property is a string that represents the name of the fax recipient, if it is available. If the information is not available, **RecipientName** is an empty string.

The **get\_RecipientName** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[SysFreeString](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




