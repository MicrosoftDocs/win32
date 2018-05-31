---
Description: Represents the queue of outgoing faxes for a particular fax account. These are the faxes that have not yet been sent.
ms.assetid: ffda6bad-4723-40c7-ae25-4f5f9f72f3fb
title: FaxAccountFolders.OutgoingQueue property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxAccountFolders.OutgoingQueue property

Represents the queue of outgoing faxes for a particular fax account. These are the faxes that have not yet been sent.

This property is read-only.

## Syntax


```VB
Property OutgoingQueue As IFaxAccountOutgoingQueue
```



## Property value

A variable of type [**IFaxAccountOutgoingQueue**](-mfax-faxaccountoutgoingqueue-cpp.md) that receives a [**FaxAccountOutgoingQueue**](-mfax-faxaccountoutgoingqueue.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxAccountFolders**](-mfax-faxaccountfolders.md)
</dt> <dt>

[**IFaxAccountFolders**](-mfax-faxaccountfolders-cpp.md)
</dt> </dl>

 

 




