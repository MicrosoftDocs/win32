---
Description: The GetJob method returns an incoming fax job in the job queue according to its ID.
ms.assetid: dab1c31e-cd46-44e0-ad0a-fcae7aa1e83e
title: FaxIncomingQueue.GetJob method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**IFaxIncomingJob**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingjob?branch=master)\*\***

A [**FaxIncomingJob**](-mfax-faxincomingjob.md) object.

## Remarks

To use this method, a user must have the [**farQUERY\_JOBS**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) and [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access rights.

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

[**IFaxIncomingQueue**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingqueue?branch=master)
</dt> </dl>

 

 




