---
Description: 'The QueuedMessages property is a number that represents the total number of fax jobs in the fax job queue that are pending processing. This does not include jobs for which the number of retries has been exceeded.'
ms.assetid: '4b03c956-99d6-4d55-8be0-3baa8b9653c2'
title: 'FaxActivity.QueuedMessages property'
---

# FaxActivity.QueuedMessages property

The **QueuedMessages** property is a number that represents the total number of fax jobs in the fax job queue that are pending processing. This does not include jobs for which the number of retries has been exceeded.

This property is read-only.

## Syntax


```VB
Property QueuedMessages As Long
```



## Property value

A **Long** that receives the total number of pending jobs in the fax queue.

## Remarks

To read this property, a user must have the [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-monitoring-fax-activity.md)
</dt> <dt>

[**FaxActivity**](-mfax-faxactivity.md)
</dt> <dt>

[**IFaxActivity**](-mfax-faxactivity-cpp.md)
</dt> </dl>

 

 




