---
Description: Returns an incoming fax job in the job queue of the current fax account according to the jobs ID.
ms.assetid: 42d4e337-7036-4c12-9ec8-bffe8de37c41
title: FaxAccountIncomingQueue.GetJob method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxAccountIncomingQueue.GetJob method

Returns an incoming fax job in the job queue of the current fax account according to the job's ID.

## Syntax


```VB
FaxAccountIncomingQueue.GetJob( _
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

To use this method, a user must have the [**far2SUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum_2?branch=master) access rights.

If the setting "All incoming faxes are viewable by everyone" is true (see [**IncomingFaxesArePublic**](/windows/previous-versions/Faxcomex/nf-faxcomex-ifaxconfiguration-get_incomingfaxesarepublic?branch=master)) or if the current user has [****far2MANAGE\_RECEIVE\_FOLDER****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum_2?branch=master) access rights, then the set returned includes all the messages present in the fax server incoming queue.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxAccountIncomingQueue**](-mfax-faxaccountincomingqueue.md)
</dt> <dt>

[**IFaxAccountIncomingQueue**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccountincomingqueue?branch=master)
</dt> </dl>

 

 




