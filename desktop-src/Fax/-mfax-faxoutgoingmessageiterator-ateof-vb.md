---
Description: The AtEOF property is the end-of-file marker for the archive of outbound fax messages.
ms.assetid: 161ad22b-b175-4c97-91eb-012eb36e7e10
title: FaxOutgoingMessageIterator.AtEOF property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingMessageIterator.AtEOF property

The AtEOF property is the end-of-file marker for the archive of outbound fax messages.

This property is read-only.

## Syntax


```VB
Property AtEOF As Boolean
```



## Property value

A **Boolean** that receives the position of the archive cursor.

## Remarks

If this property is equal to **True**, the archive cursor has moved beyond the last fax message in the archive. If this property is equal to **False**, the archive cursor has not reached the end of the archive.

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

 

 




