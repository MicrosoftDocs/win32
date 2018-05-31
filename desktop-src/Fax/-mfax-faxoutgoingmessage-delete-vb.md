---
Description: The Delete method deletes the fax message from the outbound archive.
ms.assetid: 62f56c02-caab-48bd-8057-961c16b941a1
title: FaxOutgoingMessage.Delete method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingMessage.Delete method

The **Delete** method deletes the fax message from the outbound archive.

## Syntax


```VB
FaxOutgoingMessage.Delete() As Long
```



## Parameters

This method has no parameters.

## Remarks

To use this method, a user must have the [**farSUBMIT\_LOW**](-mfax-fax-access-rights-enum.md) or **farMANAGE\_OUT\_ARCHIVE** access right.

With the [**farSUBMIT\_LOW**](-mfax-fax-access-rights-enum.md) access right, users will be able to use this method only for their own faxes. With the **farMANAGE\_OUT\_ARCHIVE** access right, users will be able to use this method for all faxes on the server.

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

 

 




