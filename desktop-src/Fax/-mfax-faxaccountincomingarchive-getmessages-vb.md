---
Description: Returns a new iterator (archive cursor) for the archive of inbound fax messages for a particular fax account.
ms.assetid: 1f3fbd1a-d3fe-421f-920e-efa99d8ff638
title: FaxAccountIncomingArchive.GetMessages method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxAccountIncomingArchive.GetMessages method

Returns a new iterator (archive cursor) for the archive of inbound fax messages for a particular fax account.

## Syntax


```VB
FaxAccountIncomingArchive.GetMessages( _
  ByVal lPrefetchSize As Long _
) As IFaxIncomingMessageIterator2
```



## Parameters

<dl> <dt>

*lPrefetchSize* \[in\]
</dt> <dd>

Type: **Long**

**Long** value that indicates the size of the prefetch buffer. This value determines how many fax messages the iterator object retrieves from the fax server when the object needs to refresh its contents. The default value is [lDEFAULT\_PREFETCH\_SIZE](-mfax-ldefault-prefetch-size.md).

</dd> </dl>

## Return value

Type: **IFaxIncomingMessageIterator2\*\***

A [**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md) object.

## Remarks

If the setting 'All incoming faxes are viewable by everyone' is true (see [**IncomingFaxesArePublic**](/windows/previous-versions/Faxcomex/nf-faxcomex-ifaxconfiguration-get_incomingfaxesarepublic?branch=master)) or if [****far2MANAGE\_RECEIVE\_FOLDER****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum_2?branch=master) access rights, then the fax service enumerates all faxes in the Incoming archive of the Fax Server Receive Folder.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxIncomingMessageIterator**](-mfax-faxincomingmessageiterator.md)
</dt> <dt>

[**FaxAccountIncomingArchive**](-mfax-faxaccountincomingarchive.md)
</dt> <dt>

[**IFaxAccountIncomingArchive**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccountincomingarchive?branch=master)
</dt> </dl>

 

 




