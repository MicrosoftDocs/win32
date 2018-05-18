---
Description: 'Disconnects the specified session between an iSCSI initiator and an iSCSI target.'
ms.assetid: '7EC188BC-5B29-4C06-A4D1-0FF3C22BC297'
title: 'Disconnect method of the MSFT\_iSCSITarget class'
---

# Disconnect method of the MSFT\_iSCSITarget class

Disconnects the specified session between an iSCSI initiator and an iSCSI target.

## Syntax


```mof
uint32 Disconnect(
  [in] string SessionIdentifier
);
```



## Parameters

<dl> <dt>

*SessionIdentifier* \[in\]
</dt> <dd>

The session identifier.

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

[**MSFT\_iSCSITarget**](msft-iscsitarget.md)
</dt> </dl>

 

 




