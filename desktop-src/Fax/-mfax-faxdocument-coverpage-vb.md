---
Description: The CoverPage property is a null-terminated string that contains the name of the cover page template file (.cov) to associate with the fax document.
ms.assetid: ae883970-dfd4-4811-b5a6-c666e1289707
title: FaxDocument.CoverPage property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.CoverPage property

The **CoverPage** property is a null-terminated string that contains the name of the cover page template file (.cov) to associate with the fax document.

This property is read/write.

## Syntax


```VB
Property CoverPage As String
```



## Property value

A **String** that specifies or receives the name of the cover page file to associate with the fax document. The string can consist of the file name only for a server-based cover page file, or the UNC path to a personal cover page file.

## Remarks

To specify a server-based cover page file, you must set the [**CoverPageType**](-mfax-faxdocument-coverpagetype-vb.md) property to 2.

To specify a local or personal cover page file, you must set the [**CoverPageType**](-mfax-faxdocument-coverpagetype-vb.md) property to 1.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-sending-a-fax.md)
</dt> <dt>

[**FaxDocument**](-mfax-faxdocument.md)
</dt> <dt>

[**IFaxDocument**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdocument)
</dt> </dl>

 

 




