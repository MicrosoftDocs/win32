---
Description: Returns an incoming fax job in the job queue of the current fax account according to the job's ID.
ms.assetid: 42d4e337-7036-4c12-9ec8-bffe8de37c41
title: FaxAccountIncomingQueue.GetJob method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**IFaxIncomingJob**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingjob)\*\***

A [**FaxIncomingJob**](-mfax-faxincomingjob.md) object.

## Remarks

To use this method, a user must have the [**far2SUBMIT\_LOW**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum_2) access rights.

If the setting "All incoming faxes are viewable by everyone" is true (see [**IncomingFaxesArePublic**](/previous-versions/windows/desktop/api/Faxcomex/nf-faxcomex-ifaxconfiguration-get_incomingfaxesarepublic)) or if the current user has [****far2MANAGE\_RECEIVE\_FOLDER****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum_2) access rights, then the set returned includes all the messages present in the fax server incoming queue.

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

[**IFaxAccountIncomingQueue**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountincomingqueue)
</dt> </dl>

 

 




