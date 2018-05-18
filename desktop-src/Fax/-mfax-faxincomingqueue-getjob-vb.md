---
Description: 'The GetJob method returns an incoming fax job in the job queue according to its ID.'
ms.assetid: 'dab1c31e-cd46-44e0-ad0a-fcae7aa1e83e'
title: 'FaxIncomingQueue.GetJob method'
---

# FaxIncomingQueue.GetJob method

The **GetJob** method returns an incoming fax job in the job queue according to its ID.

## Syntax


```VB
FaxIncomingQueue.GetJob( _
  ByVal bstrJobId As String _
) As IFaxIncomingJob
```



## Parameters

<dl> <dt>

*bstrJobId* \[in\]
</dt> <dd>

Type: **String**

Specifies the job ID.

</dd> </dl>

## Return value

Type: **[**IFaxIncomingJob**](-mfax-faxincomingjob-cpp.md)\*\***

A [**FaxIncomingJob**](-mfax-faxincomingjob.md) object.

## Remarks

To use this method, a user must have the [**farQUERY\_JOBS**](-mfax-fax-access-rights-enum.md) and [**farSUBMIT\_LOW**](-mfax-fax-access-rights-enum.md) access rights.

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

 

 




