---
Description: 'The DeviceName property is a null-terminated string that contains the name of the device on which the inbound fax message was received.'
ms.assetid: 'dceea0fc-da1a-45a5-8070-420ec652b4d7'
title: 'FaxIncomingMessage.DeviceName property'
---

# FaxIncomingMessage.DeviceName property

The **DeviceName** property is a null-terminated string that contains the name of the device on which the inbound fax message was received.

This property is read-only.

## Syntax


```VB
Property DeviceName As String
```



## Property value

A **String** that receives the name of the fax device on which the fax message was received.

## Remarks

This method returns the name of the fax device rather than the device ID. This is useful because an administrator may remove the device ID after completion of the fax job and before the client's query of the archive of inbound fax messages.

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

 

 




