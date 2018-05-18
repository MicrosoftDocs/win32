---
Description: 'Sets a CHAP secret key for use with iSCSI initiator connections.'
ms.assetid: '5CC3A50C-32DB-40D9-ACAE-04DA7324C6F9'
title: 'SetCHAPSecret method of the MSFT\_iSCSISession class'
---

# SetCHAPSecret method of the MSFT\_iSCSISession class

Sets a CHAP secret key for use with iSCSI initiator connections.

## Syntax


```mof
uint32 SetCHAPSecret(
  [in] string ChapSecret
);
```



## Parameters

<dl> <dt>

*ChapSecret* \[in\]
</dt> <dd>

The CHAP secret to use for CHAP connections.

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

 

 




