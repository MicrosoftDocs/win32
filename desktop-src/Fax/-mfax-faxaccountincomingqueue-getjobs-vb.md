---
Description: Returns the collection of inbound fax jobs in the queue for the current fax account.
ms.assetid: 2fd8a18c-391e-464d-886d-63cc3b0740dd
title: FaxAccountIncomingQueue.GetJobs method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxAccountIncomingQueue.GetJobs method

Returns the collection of inbound fax jobs in the queue for the current fax account.

## Syntax


```VB
FaxAccountIncomingQueue.GetJobs() As IFaxIncomingJobs
```



## Parameters

This method has no parameters.

## Return value

Type: **[**IFaxIncomingJobs**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingjobs)\*\***

A [**FaxIncomingJobs**](-mfax-faxincomingjobs.md) object.

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

 

 




