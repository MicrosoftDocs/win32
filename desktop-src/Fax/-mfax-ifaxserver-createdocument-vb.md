---
Description: The CreateDocument method creates a FaxDoc object for a specified FaxServer object. The FaxDoc object allows a user to create and transmit a document to one or more fax recipients.
ms.assetid: d0aee512-5bf3-4446-ae5a-529c30a4ef33
title: FaxServer.CreateDocument method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.CreateDocument method

The **CreateDocument** method creates a [FaxDoc](-mfax-faxdoc.md) object for a specified [FaxServer](-mfax-faxserver-client.md) object. The FaxDoc object allows a user to create and transmit a document to one or more fax recipients.

## Syntax


```VB
FaxServer.CreateDocument( _
  ByVal FileName As String, _
  ByRef retVal As Variant _
) As Long
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

Type: **String**

Specifies a null-terminated string that contains the fully qualified path and name of the file that contains the fax document to transmit. The path can be a UNC path or a path beginning with a drive letter.

This parameter can contain any valid local or remote file name. The file must be a properly registered file type, and the fax server must be able to access the file.

</dd> <dt>

*retVal* \[out\]
</dt> <dd>

Type: **Variant\***

Pointer to a [VARIANT](e305240e-9e11-4006-98cc-26f4932d2118) structure that receives an [IDispatch](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface pointer to a [FaxDoc](-mfax-faxdoc.md) object. The method returns a pdispVal member with a VT\_DISPATCH data type.

</dd> </dl>

## Remarks

The **CreateDocument** method retrieves an [IDispatch](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface pointer to a [FaxDoc](-mfax-faxdoc.md) object. A fax client application can also access the [**IFaxDoc**](-mfax-ifaxdoc.md) interface directly by calling the [IUnknown::QueryInterface](http://msdn.microsoft.com/en-us/library/ms682521.aspx) method to retrieve an interface pointer. The **IFaxDoc** interface allows a user to set the properties for a fax document, and then transmit the document.

A fax client application should not call the [CoCreateInstance](http://msdn.microsoft.com/en-us/library/ms686615.aspx) function to retrieve an [**IFaxDoc**](-mfax-ifaxdoc.md) interface pointer because it will not be instantiated correctly.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxServer**](-mfax-faxserver-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[FaxServer](-mfax-faxserver-client.md)
</dt> <dt>

[FaxDoc](-mfax-faxdoc.md)
</dt> <dt>

[IUnknown::QueryInterface](http://msdn.microsoft.com/en-us/library/ms682521.aspx)
</dt> </dl>

 

 




