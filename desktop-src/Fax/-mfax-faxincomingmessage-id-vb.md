---
Description: The Id property is a null-terminated string that contains a unique ID for the inbound fax message.
ms.assetid: 42003b93-f9ed-4337-9c5b-daf22320fb41
title: FaxIncomingMessage.Id property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessage.Id property

The **Id** property is a null-terminated string that contains a unique ID for the inbound fax message.

This property is read-only.

## Syntax


```VB
Property Id As String
```



## Property value

A **String** that receives a unique ID for the inbound fax message.

## Remarks

Note that this is the same value that identified the associated fax job when the job was in the job queue.

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

[**IFaxIncomingMessage**](-mfax-faxincomingmessage-cpp.md)
</dt> </dl>

 

 




