---
Description: The PrefetchSize property indicates the size of the prefetch (read-ahead) buffer.
ms.assetid: 0dc10f14-1ae3-47e5-aab2-53ddaa45b8a0
title: FaxIncomingMessageIterator.PrefetchSize property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingMessageIterator.PrefetchSize property

The **PrefetchSize** property indicates the size of the prefetch (read-ahead) buffer.

This property is read/write.

## Syntax


```VB
Property PrefetchSize As Long
```



## Property value

A **Long** that specifies or receives the size of the prefetch buffer. The value of this property determines how many fax messages the iterator object retrieves from the archive each time the object refreshes its contents. The default value is [lDEFAULT\_PREFETCH\_SIZE](-mfax-ldefault-prefetch-size.md).

## Remarks

The prefetch buffer contains messages and makes the iteration process more efficient because you iterate through the buffer rather than through a folder.

Changes you make to the size of the prefetch buffer take place immediately because [**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md) is a local object.

To use this method, a user must have the [**farQUERY\_IN\_ARCHIVE**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

[**PrefetchSize**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxincomingmessageiterator-get_prefetchsize)
</dt> </dl>

 

 




