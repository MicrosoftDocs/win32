---
Description: 'Removes an iSCSI target portal.'
ms.assetid: '88E00681-6621-4411-BC43-080646DAAB01'
title: 'Remove method of the MSFT\_iSCSITargetPortal class'
---

# Remove method of the MSFT\_iSCSITargetPortal class

Removes an iSCSI target portal.

## Syntax


```mof
uint32 Remove(
  [in] string InitiatorInstanceName,
  [in] string InitiatorPortalAddress,
  [in] uint16 TargetPortalPortNumber,
  [in] string TargetPortalAddress
);
```



## Parameters

<dl> <dt>

*InitiatorInstanceName* \[in\]
</dt> <dd>

The name of the initiator instance.

</dd> <dt>

*InitiatorPortalAddress* \[in\]
</dt> <dd>

The IP address or DNS name associated with the initiator portal.

</dd> <dt>

*TargetPortalPortNumber* \[in\]
</dt> <dd>

The TCP port number for the target portal.

</dd> <dt>

*TargetPortalAddress* \[in\]
</dt> <dd>

The string representing the IP or DNS address of the target portal.

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

[**MSFT\_iSCSITargetPortal**](msft-iscsitargetportal.md)
</dt> </dl>

 

 




