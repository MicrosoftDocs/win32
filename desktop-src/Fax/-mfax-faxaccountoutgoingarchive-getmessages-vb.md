---
Description: Returns a new iterator (archive cursor) for the archive of outbound fax messages for a particular fax account.
ms.assetid: f8bfd7a9-def7-4c2a-91ba-bf523a7c6de4
title: FaxAccountOutgoingArchive.GetMessages method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxAccountOutgoingArchive.GetMessages method

Returns a new iterator (archive cursor) for the archive of outbound fax messages for a particular fax account.

## Syntax


```VB
FaxAccountOutgoingArchive.GetMessages( _
  ByVal lPrefetchSize As Long _
) As IFaxOutgoingMessageIterator2
```



## Parameters

<dl> <dt>

*lPrefetchSize* \[in\]
</dt> <dd>

Type: **Long**

**Long** value that indicates the size of the prefetch buffer. This value determines how many fax messages the iterator object retrieves from the fax server when the object needs to refresh its contents. The default value is [lDEFAULT\_PREFETCH\_SIZE](-mfax-ldefault-prefetch-size.md).

</dd> </dl>

## Return value

Type: **IFaxOutgoingMessageIterator2\*\***

A [**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingMessageIterator**](-mfax-faxoutgoingmessageiterator.md)
</dt> <dt>

[**FaxAccountOutgoingArchive**](-mfax-faxaccountoutgoingarchive.md)
</dt> <dt>

[**IFaxAccountOutgoingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountoutgoingarchive)
</dt> </dl>

 

 




