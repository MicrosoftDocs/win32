---
Description: The AtEOF property is the end of file marker for the archive of inbound fax messages.
ms.assetid: 40abe45a-895a-47a7-bb9f-f743b56da8c6
title: FaxIncomingMessageIterator.AtEOF property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingMessageIterator.AtEOF property

The **AtEOF** property is the end of file marker for the archive of inbound fax messages. If this property is equal to **True**, the archive cursor has moved beyond the last fax message in the inbound fax archive. If this property is equal to **False**, the archive cursor has not yet reached the end of the archive.

This property is read-only.

## Syntax


```VB
Property AtEOF As Boolean
```



## Property value

A **Boolean** that receives a value that indicates whether the archive cursor has moved beyond the last message in the inbound fax archive.

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

 

 




