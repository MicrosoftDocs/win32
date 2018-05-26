---
Description: The GetJob method returns an outbound fax job in the job queue according to its ID.
ms.assetid: 688fb115-df7b-40f1-a3aa-25ad6333afd4
title: FaxOutgoingQueue.GetJob method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

To use this method, a user must have the [****farSUBMIT\_LOW****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) or [****farQUERY\_JOBS****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

With the [****farSUBMIT\_LOW****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right, users can use this method only for their own faxes. With the [****farQUERY\_JOBS****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right, users can use this method for all faxes on the server.

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

[**IFaxOutgoingQueue**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingqueue?branch=master)
</dt> <dt>

[Managing Outgoing Jobs](-mfax-managing-outgoing-jobs.md)
</dt> </dl>

 

 




