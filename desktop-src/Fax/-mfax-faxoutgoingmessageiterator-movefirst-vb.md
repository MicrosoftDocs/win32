---
Description: The MoveFirst method moves the archive cursor to the first fax message in the outbound archive.
ms.assetid: 3e9fb244-4e40-4fff-8960-d9760f0b2445
title: FaxOutgoingMessageIterator.MoveFirst method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingMessageIterator.MoveFirst method

The **MoveFirst** method moves the archive cursor to the first fax message in the outbound archive.

## Syntax


```VB
FaxOutgoingMessageIterator.MoveFirst() As Long
```



## Parameters

This method has no parameters.

## Remarks

To use this method, a user must have the [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) and **farQUERY\_OUT\_ARCHIVE** access rights.

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

 

 




