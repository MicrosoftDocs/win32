---
Description: 'Registers the iSCSI session to be persistent.'
ms.assetid: '9D313B5F-07F7-4C52-9C49-27687CE1FA92'
title: 'Register method of the MSFT\_iSCSISession class'
---

# Register method of the MSFT\_iSCSISession class

Registers the iSCSI session to be persistent.

After the session is marked as persistent, it will be automatically connected at every restart.

## Syntax


```mof
uint32 Register(
   boolean IsMultipathEnabled
);
```



## Parameters

<dl> <dt>

*IsMultipathEnabled* 
</dt> <dd>

If **true**, the ISCSI initiator service allows multiple sessions to the same target portal.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_iSCSISession**](msft-iscsisession.md)
</dt> </dl>

 

 




