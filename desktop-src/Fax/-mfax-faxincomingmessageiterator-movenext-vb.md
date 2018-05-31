---
Description: The MoveNext method moves the archive cursor to the next message in the archive of inbound faxes.
ms.assetid: ab40c195-2c2b-41e7-b7d1-02ee2c7b5015
title: FaxIncomingMessageIterator.MoveNext method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessageIterator.MoveNext method

The **MoveNext** method moves the archive cursor to the next message in the archive of inbound faxes.

## Syntax


```VB
FaxIncomingMessageIterator.MoveNext() As Long
```



## Parameters

This method has no parameters.

## Remarks

You can make the iteration process more efficient by using a prefetch buffer. A prefetch buffer contains messages and allows you to iterate through the buffer rather than through a folder. Set the size of the buffer (the number of messages to be held in the buffer) using the [**PrefetchSize**](-mfax-faxincomingmessageiterator-prefetchsize.md) property.

To use this method, a user must have the [**farQUERY\_IN\_ARCHIVE**](-mfax-fax-access-rights-enum.md) access right.

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

[**IFaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator-cpp.md)
</dt> </dl>

 

 




