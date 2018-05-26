---
Description: Creates and configures a new iSCSI target portal.
ms.assetid: 5816800F-258D-4C22-B86B-F5D51272B75B
title: New method of the MSFT\_iSCSITargetPortal class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# New method of the MSFT\_iSCSITargetPortal class

Creates and configures a new iSCSI target portal.

## Syntax


```mof
uint32 New(
  [in]  string  TargetPortalAddress,
  [in]  uint16  TargetPortalPortNumber,
  [in]  string  InitiatorInstanceName,
  [in]  string  InitiatorPortalAddress,
  [in]  boolean IsHeaderDigest,
  [in]  boolean IsDataDigest,
  [out] String  CreatedTargetPortal
);
```



## Parameters

<dl> <dt>

*TargetPortalAddress* \[in\]
</dt> <dd>

The IP or DNS address associated with the target portal.

</dd> <dt>

*TargetPortalPortNumber* \[in\]
</dt> <dd>

The TCP port number for the target portal. The default value is 3260.

</dd> <dt>

*InitiatorInstanceName* \[in\]
</dt> <dd>

The name of the initiator instance that the iSCSI initiator service uses to send [SendTargets](storage.sendtargets) requests to the target portal. If no instance name is specified, the iSCSI initiator service chooses the initiator instance.

</dd> <dt>

*InitiatorPortalAddress* \[in\]
</dt> <dd>

The IP address or DNS name associated with the initiator portal.

</dd> <dt>

*IsHeaderDigest* \[in\]
</dt> <dd>

If **true**, the initiator should enable the session to use a header digest scheme when logging into the target portal. Otherwise, the header digest setting is determined by the initiator kernel mode driver.

</dd> <dt>

*IsDataDigest* \[in\]
</dt> <dd>

If **true**, the initiator should enable the session to use an iSCSI data digest scheme when logging into the target portal. Otherwise, the data digest setting is determined by the initiator kernel mode driver.

</dd> <dt>

*CreatedTargetPortal* \[out\]
</dt> <dd>

A reference to the newly created [**MSFT\_iSCSITargetPortal**](msft-iscsitargetportal.md) object.

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

 

 




