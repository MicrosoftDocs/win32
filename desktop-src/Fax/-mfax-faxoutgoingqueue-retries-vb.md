---
Description: The Retries property is a value that indicates the number of times that the fax service attempts to retransmit an outgoing fax when the initial transmission fails.
ms.assetid: 7821a52b-006b-4f03-97f5-f51587584feb
title: FaxOutgoingQueue.Retries property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingQueue.Retries property

The **Retries** property is a value that indicates the number of times that the fax service attempts to retransmit an outgoing fax when the initial transmission fails.

This property is read/write.

## Syntax


```VB
Property Retries As Long
```



## Property value

A **Long** that specifies or receives the number of times that the fax service attempts to retransmit an outgoing fax when the initial transmission fails. Can have a value of 0 to 99.

## Remarks

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md)
</dt> <dt>

[**IFaxOutgoingQueue**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingqueue)
</dt> <dt>

[Setting the Outgoing Queue Properties](-mfax-setting-the-outgoing-queue-properties.md)
</dt> </dl>

 

 




