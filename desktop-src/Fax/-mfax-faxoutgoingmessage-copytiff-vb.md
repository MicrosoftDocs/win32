---
Description: The CopyTiff method copies the Tagged Image File Format Class F (TIFF Class F) file associated with the outbound fax message, to a file on the local computer.
ms.assetid: 96be8d5f-0254-49fd-b0aa-f042ae9ff1ba
title: FaxOutgoingMessage.CopyTiff method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingMessage.CopyTiff method

The **CopyTiff** method copies the Tagged Image File Format Class F (TIFF Class F) file associated with the outbound fax message, to a file on the local computer.

## Syntax


```VB
FaxOutgoingMessage.CopyTiff( _
  ByVal bstrTiffPath As String _
) As Long
```



## Parameters

<dl> <dt>

*bstrTiffPath* \[in\]
</dt> <dd>

Type: **String**

Null-terminated string that contains a fully qualified path and file name on the local computer. This is the file on the local computer to which the fax service will copy the TIFF Class F file associated with the outbound fax message.

</dd> </dl>

## Remarks

To use this method, a user must have the [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) or **farMANAGE\_OUT\_ARCHIVE** access right.

With the [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right, users will be able to use this method only for their own faxes. With the **farMANAGE\_OUT\_ARCHIVE** access right, users will be able to use this method for all faxes on the server.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-outgoing-archive.md)
</dt> <dt>

[**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md)
</dt> <dt>

[**IFaxOutgoingMessage**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingmessage?branch=master)
</dt> </dl>

 

 




