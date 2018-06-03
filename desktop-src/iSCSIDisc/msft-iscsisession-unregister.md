---
Description: Unregisters the iSCSI session so that it is no longer persistent.
ms.assetid: 28C57A15-682E-4DC7-8443-AEDDD09D1829
title: Unregister method of the MSFT\_iSCSISession class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Unregister method of the MSFT\_iSCSISession class

Unregisters the iSCSI session so that it is no longer persistent.

After the session is unregistered, it will no longer be automatically connected at every restart.

## Syntax


```mof
uint32 Unregister();
```



## Parameters

This method has no parameters.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_iSCSISession**](msft-iscsisession.md)
</dt> </dl>

 

 




