---
Description: The Message property retrieves the inbound fax message under the archive cursor.
ms.assetid: 145bd690-af6a-45b3-a44b-c692a6a6d363
title: FaxIncomingMessageIterator.Message property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingMessageIterator.Message property

The **Message** property retrieves the inbound fax message under the archive cursor.

This property is read-only.

## Syntax


```VB
Property Message As IFaxIncomingMessage
```



## Property value

A variable of type [**IFaxIncomingMessage**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingmessage?branch=master) that receives a [**FaxIncomingMessage**](-mfax-faxincomingmessage.md) object.

## Remarks

To use this method, a user must have the [**farQUERY\_IN\_ARCHIVE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-incoming-archive.md)
</dt> <dt>

[**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md)
</dt> <dt>

[**IFaxIncomingMessageIterator**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingmessageiterator?branch=master)
</dt> </dl>

 

 




