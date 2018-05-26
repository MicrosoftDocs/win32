---
Description: The MoveFirst method moves the archive cursor to the first fax message in the archive of inbound faxes.
ms.assetid: 6b3aaf7a-5435-4fe1-a942-d80a0dbe2dea
title: FaxIncomingMessageIterator.MoveFirst method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingMessageIterator.MoveFirst method

The **MoveFirst** method moves the archive cursor to the first fax message in the archive of inbound faxes.

## Syntax


```VB
FaxIncomingMessageIterator.MoveFirst() As Long
```



## Parameters

This method has no parameters.

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

 

 




