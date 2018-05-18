---
Description: 'The Blocked property is a Boolean value that indicates whether the job queue for incoming faxes is blocked.'
ms.assetid: 'cffd029f-8278-453f-97a2-c000189268ec'
title: 'FaxIncomingQueue.Blocked property'
---

# FaxIncomingQueue.Blocked property

The **Blocked** property is a Boolean value that indicates whether the job queue for incoming faxes is blocked.

This property is read/write.

## Syntax


```VB
Property Blocked As Boolean
```



## Property value

a value that indicates whether the job queue for incoming faxes is blocked.

## Remarks

If this property is equal to **True**, the inbound job queue is blocked and the fax service is not answering incoming fax calls. If this property is equal to **False**, the queue is not blocked.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxIncomingQueue**](-mfax-faxincomingqueue.md)
</dt> <dt>

[**IFaxIncomingQueue**](-mfax-faxincomingqueue-cpp.md)
</dt> </dl>

 

 




