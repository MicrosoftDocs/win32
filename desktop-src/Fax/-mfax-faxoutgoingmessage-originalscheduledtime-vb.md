---
Description: The OriginalScheduledTime property specifies the time that the fax message was originally scheduled for transmission.
ms.assetid: 75a732d9-3b69-461e-a510-c93605569043
title: FaxOutgoingMessage.OriginalScheduledTime property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingMessage.OriginalScheduledTime property

The **OriginalScheduledTime** property specifies the time that the fax message was originally scheduled for transmission.

This property is read-only.

## Syntax


```VB
Property OriginalScheduledTime As Date
```



## Property value

A **Date** value that represents the date and time that the fax was originally scheduled for processing. **OriginalScheduledTime** is expressed in local system time.

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

 

 




