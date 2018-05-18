---
Description: 'The GetJob method returns an outbound fax job in the job queue according to its ID.'
ms.assetid: '688fb115-df7b-40f1-a3aa-25ad6333afd4'
title: 'FaxOutgoingQueue.GetJob method'
---

# FaxOutgoingQueue.GetJob method

The **GetJob** method returns an outbound fax job in the job queue according to its ID.

## Syntax


```VB
FaxOutgoingQueue.GetJob( _
  ByVal bstrJobId As String _
) As FaxOutgoingJob
```



## Parameters

<dl> <dt>

*bstrJobId* \[in\]
</dt> <dd>

Type: **String**

Specifies the job ID.

</dd> </dl>

## Return value

Type: **[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)\*\***

A [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md) object.

## Remarks

To use this method, a user must have the [****farSUBMIT\_LOW****](-mfax-fax-access-rights-enum.md) or [****farQUERY\_JOBS****](-mfax-fax-access-rights-enum.md) access right.

With the [****farSUBMIT\_LOW****](-mfax-fax-access-rights-enum.md) access right, users can use this method only for their own faxes. With the [****farQUERY\_JOBS****](-mfax-fax-access-rights-enum.md) access right, users can use this method for all faxes on the server.

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

[Managing Outgoing Jobs](-mfax-managing-outgoing-jobs.md)
</dt> </dl>

 

 




