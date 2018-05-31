---
Description: The Recipients property retrieves a collection of one or more recipients for the fax document.
ms.assetid: 9c1d12a0-f740-4bf0-a448-767e34afa124
title: FaxDocument.Recipients property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.Recipients property

The **Recipients** property retrieves a collection of one or more recipients for the fax document.

This property is read-only.

## Syntax


```VB
Property Recipients As IFaxRecipients
```



## Property value

A variable of type [**IFaxRecipients**](-mfax-faxrecipients-cpp.md) that receives a [**FaxRecipients**](-mfax-faxrecipients.md) object.

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

[**IFaxDocument**](-mfax-faxdocument-cpp.md)
</dt> </dl>

 

 




