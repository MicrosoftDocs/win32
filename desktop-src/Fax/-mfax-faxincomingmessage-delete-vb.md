---
Description: The Delete method deletes the specified fax message from the inbound fax archive.
ms.assetid: 5c4e4b71-2626-430a-bcb9-ac7c3a99562f
title: FaxIncomingMessage.Delete method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingMessage.Delete method

The **Delete** method deletes the specified fax message from the inbound fax archive.

## Syntax


```VB
FaxIncomingMessage.Delete() As Long
```



## Parameters

This method has no parameters.

## Remarks

To use this method, a user must have the [**farMANAGE\_IN\_ARCHIVE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

[**IFaxIncomingMessage**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingmessage?branch=master)
</dt> </dl>

 

 




