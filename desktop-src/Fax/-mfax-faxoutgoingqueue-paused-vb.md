---
Description: The Paused property is a Boolean value that indicates whether the job queue for outgoing faxes is paused.
ms.assetid: 59ba15d3-487b-4d38-8a63-6c0028f226b3
title: FaxOutgoingQueue.Paused property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingQueue.Paused property

The **Paused** property is a Boolean value that indicates whether the job queue for outgoing faxes is paused.

This property is read/write.

## Syntax


```VB
Property Paused As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the job queue for outgoing faxes is paused.

## Remarks

If this property is equal to **True**, the job queue is paused and the fax service is not processing jobs in the queue. If this property is equal to **False**, the outgoing queue is not paused.

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

 

 




