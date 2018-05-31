---
Description: The CopyTiff method copies the Tagged Image File Format Class F (TIFF Class F) file associated with the inbound fax message to a file on the local computer.
ms.assetid: 31329a99-26a3-4b17-9b26-2dea1e9589df
title: FaxIncomingMessage.CopyTiff method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessage.CopyTiff method

The **CopyTiff** method copies the Tagged Image File Format Class F (TIFF Class F) file associated with the inbound fax message to a file on the local computer.

## Syntax


```VB
FaxIncomingMessage.CopyTiff( _
  ByVal bstrTiffPath As String _
) As Long
```



## Parameters

<dl> <dt>

*bstrTiffPath* \[in\]
</dt> <dd>

Type: **String**

Null-terminated **String** that specifies a fully qualified path and file name on the local computer. The fax service will copy the TIFF Class F file associated with the inbound fax message to the specified file.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-incoming-archive.md)
</dt> <dt>

[**FaxIncomingMessage**](-mfax-faxincomingmessage.md)
</dt> <dt>

[**IFaxIncomingMessage**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingmessage)
</dt> </dl>

 

 




