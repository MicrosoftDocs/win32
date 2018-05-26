---
Description: The GetMessages method returns a new iterator (archive cursor) for the archive of outbound fax messages. For more information, see FaxOutgoingMessageIterator.
ms.assetid: 8daf6fba-dd69-479c-b17d-ba2729fe6773
title: FaxOutgoingArchive.GetMessages method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingArchive.GetMessages method

The **GetMessages** method returns a new iterator (archive cursor) for the archive of outbound fax messages. For more information, see [**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md).

## Syntax


```VB
FaxOutgoingArchive.GetMessages( _
  ByVal lPrefetchSize As Long, _
  ByVal FaxOutgoingMessageIterator As IFaxOutgoingMessageIterator _
) As Long
```



## Parameters

<dl> <dt>

*lPrefetchSize* 
</dt> <dd>

Type: **Long**

A **Long** value that specifies the size of the prefetch buffer. This value determines how many fax messages the iterator object retrieves from the fax server when the object needs to refresh its contents. The default value is [lDEFAULT\_PREFETCH\_SIZE](-mfax-ldefault-prefetch-size.md).

</dd> <dt>

*FaxOutgoingMessageIterator* 
</dt> <dd>

Type: **[**IFaxOutgoingMessageIterator**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingmessageiterator?branch=master)\*\***

A [**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md) object.

</dd> </dl>

## Remarks

To use this method, a user must have the [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) or **farQUERY\_OUT\_ARCHIVE** access right. With the **farSUBMIT\_LOW** access right, the user will be able to use this method only for his own faxes. With the **farQUERY\_OUT\_ARCHIVE** access right, he will be able to use this method for all of the faxes on the server.

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

[**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md)
</dt> </dl>

 

 




