---
Description: The Subject property is a null-terminated string that contains the contents of the subject field on the cover page of the fax.
ms.assetid: c20fca81-6961-49bf-9d23-1a415e3a6515
title: FaxOutgoingMessage.Subject property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingMessage.Subject property

The **Subject** property is a null-terminated string that contains the contents of the subject field on the cover page of the fax.

This property is read-only.

## Syntax


```VB
Property Subject As String
```



## Property value

A **String** that receives text that describes the subject of the fax message. The text appears on the cover page.

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

[**IFaxOutgoingMessage**](-mfax-faxoutgoingmessage-cpp.md)
</dt> </dl>

 

 




