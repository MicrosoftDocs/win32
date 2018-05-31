---
Description: The GetJob method returns an incoming fax job in the job queue according to its ID.
ms.assetid: dab1c31e-cd46-44e0-ad0a-fcae7aa1e83e
title: FaxIncomingQueue.GetJob method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**IFaxIncomingJob**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingjob)\*\***

A [**FaxIncomingJob**](-mfax-faxincomingjob.md) object.

## Remarks

To use this method, a user must have the [**farQUERY\_JOBS**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) and [**farSUBMIT\_LOW**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access rights.

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

[**IFaxIncomingQueue**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingqueue)
</dt> </dl>

 

 




