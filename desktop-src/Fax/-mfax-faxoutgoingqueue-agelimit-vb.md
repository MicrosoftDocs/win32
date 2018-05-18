---
Description: 'The AgeLimit property is a value that indicates the number of days that the fax service retains an unsent job in the fax job queue.'
ms.assetid: 'eea0fd7f-c1db-4b63-8f63-143080aed7dc'
title: 'FaxOutgoingQueue.AgeLimit property'
---

# FaxOutgoingQueue.AgeLimit property

The **AgeLimit** property is a value that indicates the number of days that the fax service retains an unsent job in the fax job queue.

This property is read/write.

## Syntax


```VB
Property AgeLimit As Long
```



## Property value

A **Long** that specifies or receives the number of days that the fax service retains an unsent job in the fax job queue.

## Remarks

If the fax job remains in the outbound job queue longer than the value specified, the fax service deletes the job. If the value of this property is zero, the fax service does not enforce an age limit.

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

 

 




