---
Description: Updates information about an iSCSI target portal.
ms.assetid: FF178A52-4022-4B31-8779-DC119EDA1829
title: Update method of the MSFT\_iSCSITargetPortal class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Update method of the MSFT\_iSCSITargetPortal class

Updates information about an iSCSI target portal.

## Syntax


```mof
uint32 Update(
  [in] string InitiatorInstanceName,
  [in] string InitiatorPortalAddress,
  [in] string TargetPortalAddress,
  [in] uint16 TargetPortalPortNumber
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

*TargetPortalAddress* \[in\]
</dt> <dd>

The IP or DNS address of the target portal to be updated.

</dd> <dt>

*TargetPortalPortNumber* \[in\]
</dt> <dd>

The TCP port number for the target portal to be updated.

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

 

 




