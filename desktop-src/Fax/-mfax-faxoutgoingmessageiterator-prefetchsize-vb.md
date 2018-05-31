---
Description: The PrefetchSize property indicates the size of the prefetch (read-ahead) buffer. This determines how many fax messages the iterator object retrieves from the fax server when the object needs to refresh its contents.
ms.assetid: 8c634532-4bc9-4395-84aa-76bb38a81f3d
title: FaxOutgoingMessageIterator.PrefetchSize property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingMessageIterator.PrefetchSize property

The **PrefetchSize** property indicates the size of the prefetch (read-ahead) buffer. This determines how many fax messages the iterator object retrieves from the fax server when the object needs to refresh its contents.

This property is read/write.

## Syntax


```VB
Property PrefetchSize As Long
```



## Property value

A **Long** value that receives the size of the prefetch buffer.

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

[lDEFAULT\_PREFETCH\_SIZE](-mfax-ldefault-prefetch-size.md)
</dt> <dt>

[**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md)
</dt> <dt>

[**IFaxOutgoingMessageIterator**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingmessageiterator)
</dt> </dl>

 

 




