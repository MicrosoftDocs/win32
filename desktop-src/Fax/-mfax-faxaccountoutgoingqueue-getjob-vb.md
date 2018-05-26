---
Description: Returns an outgoing fax job in the job queue of the current fax account according to the jobs ID.
ms.assetid: 1aa1f0a4-5444-4734-b17c-0b3609e33a1b
title: FaxAccountOutgoingQueue.GetJob method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxAccountOutgoingQueue.GetJob method

Returns an outgoing fax job in the job queue of the current fax account according to the job's ID.

## Syntax


```VB
FaxAccountOutgoingQueue.GetJob( _
  ByVal bstrJobId As String _
) As IFaxOutgoingJob2
```



## Parameters

<dl> <dt>

*bstrJobId* \[in\]
</dt> <dd>

Type: **String**

Specifies the job ID.

</dd> </dl>

## Return value

Type: **[**IFaxOutgoingJob2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingjob2?branch=master)\*\***

A [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxAccountOutgoingQueue**](-mfax-faxaccountoutgoingqueue.md)
</dt> <dt>

[**IFaxAccountOutgoingQueue**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccountoutgoingqueue?branch=master)
</dt> </dl>

 

 




