---
Description: The Blocked property is a Boolean value that indicates whether the job queue for outgoing faxes is blocked.
ms.assetid: eb1789d7-2778-4759-ba69-ba7103e47111
title: FaxOutgoingQueue.Blocked property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingQueue.Blocked property

The **Blocked** property is a Boolean value that indicates whether the job queue for outgoing faxes is blocked.

This property is read/write.

## Syntax


```VB
Property Blocked As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the job queue for outgoing faxes is blocked.

## Remarks

If this property is equal to **True**, the outbound job queue is blocked and the fax service is not accepting outbound fax submissions. If this property is equal to **False**, the queue is not blocked.

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

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

[**IFaxOutgoingQueue**](-mfax-faxoutgoingqueue-cpp.md)
</dt> <dt>

[Setting the Outgoing Queue Properties](-mfax-setting-the-outgoing-queue-properties.md)
</dt> </dl>

 

 




