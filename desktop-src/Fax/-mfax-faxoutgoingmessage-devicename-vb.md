---
Description: The DeviceName property is a null-terminated string that contains the name of the device on which the fax message was transmitted.
ms.assetid: 77e64b22-63e0-4a17-91d7-8285623b9384
title: FaxOutgoingMessage.DeviceName property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingMessage.DeviceName property

The **DeviceName** property is a null-terminated string that contains the name of the device on which the fax message was transmitted.

This property is read-only.

## Syntax


```VB
Property DeviceName As String
```



## Property value

A **String** that receives the name of the fax device on which the fax message was transmitted.

## Remarks

This method returns the name of the fax device rather than the device ID. This is useful because an administrator may remove the device ID after completion of the fax job and before the client's query of the archive of fax messages.

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

 

 




