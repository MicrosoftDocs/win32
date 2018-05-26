---
Description: The Refresh method refreshes FaxIncomingQueue object information from the fax server. When the Refresh method is called, any configuration changes made after the last Save method call are lost.
ms.assetid: 2993ab38-f315-48f1-8ff2-6b1d039092dd
title: FaxIncomingQueue.Refresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingQueue.Refresh method

The **Refresh** method refreshes [**FaxIncomingQueue**](-mfax-faxincomingqueue.md) object information from the fax server. When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxincomingqueue-save-vb.md) method call are lost.

## Syntax


```VB
FaxIncomingQueue.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

To use this method, a user must have the [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

 

 




