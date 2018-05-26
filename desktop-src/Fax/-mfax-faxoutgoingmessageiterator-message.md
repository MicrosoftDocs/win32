---
Description: The Message property retrieves the outbound fax message under the archive cursor.
ms.assetid: fe8aac1e-1438-4984-9802-97f0a44b2893
title: FaxOutgoingMessageIterator.Message property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingMessageIterator.Message property

The **Message** property retrieves the outbound fax message under the archive cursor.

This property is read-only.

## Syntax


```VB
Property Message As FaxOutgoingMessage
```



## Property value

A [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md) object.

## Remarks

To use this method, a user must have the [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) and **farQUERY\_OUT\_ARCHIVE** access rights.

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

[**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md)
</dt> <dt>

[**IFaxOutgoingMessageIterator**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingmessageiterator?branch=master)
</dt> </dl>

 

 




