---
Description: Represents the queue of incoming faxes for a particular fax account. These are the incoming faxes that have not yet been fully processed.
ms.assetid: 7b8fac52-d7c0-4ff4-bc13-e11494d1d6c5
title: FaxAccountFolders.IncomingQueue property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxAccountFolders.IncomingQueue property

Represents the queue of incoming faxes for a particular fax account. These are the incoming faxes that have not yet been fully processed.

This property is read-only.

## Syntax


```VB
Property IncomingQueue As IFaxAccountIncomingQueue
```



## Property value

A variable of type [**IFaxAccountIncomingQueue**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountincomingqueue) that receives a [**FaxIncomingQueue**](-mfax-faxincomingqueue.md) object.

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

[**IFaxAccountFolders**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountfolders)
</dt> </dl>

 

 




