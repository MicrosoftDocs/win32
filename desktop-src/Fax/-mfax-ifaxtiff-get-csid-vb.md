---
Description: Retrieves the Csid property for a FaxTiff object. The Csid property is a string that contains called station identifier (CSID) information, which is typically the fax number of the device that received the specified fax file.
ms.assetid: 2e08d581-cb6d-43fa-b84f-413406ad0faf
title: FaxTiff.Csid property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxTiff.Csid property

Retrieves the **Csid** property for a [FaxTiff](-mfax-faxtiff.md) object. The **Csid** property is a string that contains called station identifier (CSID) information, which is typically the fax number of the device that received the specified fax file.

This property is read-only.

## Syntax


```VB
Property Csid As String
```



## Property value

A **String** that receives the CSID.

## Remarks

A fax client application must set the [**Image**](-mfax-ifaxtiff-get-image-vb.md) property before retrieving another property for a [FaxTiff](-mfax-faxtiff.md) object.

The **get\_Csid** method sets the *pVal* parameter to the string that identifies the called device, if that information is available. If the information is not available, the method returns "Unavailable".

The **Csid** property is a string that identifies the called device, if that information is available. If the information is not available, **Csid** is an empty string.

The **get\_Csid** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxTiff**](-mfax-ifaxtiff.md)
</dt> <dt>

[**Image**](-mfax-ifaxtiff-get-image-vb.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




