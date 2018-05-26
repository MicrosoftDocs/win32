---
Description: The GetMessages method gets a new iterator (archive cursor) for the archive of inbound fax messages.
ms.assetid: 84d5aeb3-7ba2-4978-be08-82140ba75e97
title: FaxIncomingArchive.GetMessages method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingArchive.GetMessages method

The **GetMessages** method gets a new iterator (archive cursor) for the archive of inbound fax messages.

## Syntax


```VB
FaxIncomingArchive.GetMessages( _
  ByVal lPrefetchSize As Long _
) As IFaxIncomingMessageIterator
```



## Parameters

<dl> <dt>

*lPrefetchSize* \[in\]
</dt> <dd>

Type: **Long**

**Long** value that indicates the size of the prefetch buffer. This value determines how many fax messages the iterator object retrieves from the fax server when the object needs to refresh its contents. The default value is [lDEFAULT\_PREFETCH\_SIZE](-mfax-ldefault-prefetch-size.md).

</dd> </dl>

## Return value

Type: **[**IFaxIncomingMessageIterator**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingmessageiterator?branch=master)\*\***

A [**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md) object.

## Remarks

To use this method, a user must have the [****farQUERY\_IN\_ARCHIVE****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md)
</dt> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-incoming-archive.md)
</dt> <dt>

[**FaxIncomingArchive**](-mfax-faxincomingarchive.md)
</dt> <dt>

[**IFaxIncomingArchive**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingarchive?branch=master)
</dt> </dl>

 

 




