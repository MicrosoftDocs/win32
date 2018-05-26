---
Description: Creates a session between an iSCSI initiator and an iSCSI target.
ms.assetid: 810027C9-0C63-4FCA-9BFA-B2366A7F2BF7
title: Connect method of the MSFT\_iSCSITarget class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Connect method of the MSFT\_iSCSITarget class

Creates a session between an iSCSI initiator and an iSCSI target.

## Syntax


```mof
uint32 Connect(
  [in]  string  NodeAddress,
  [in]  string  TargetPortalAddress,
  [in]  uint16  TargetPortalPortNumber,
  [in]  string  InitiatorPortalAddress,
  [in]  boolean IsDataDigest,
  [in]  boolean IsHeaderDigest,
  [in]  boolean ReportToPnP,
  [in]  string  AuthenticationType,
  [in]  boolean IsMultipathEnabled,
  [in]  boolean IsPersistent,
  [in]  string  InitiatorInstanceName,
  [out] String  CreatediSCSISession
);
```



## Parameters

<dl> <dt>

*NodeAddress* \[in\]
</dt> <dd>

The iSCSI qualified name (IQN) of the target.

</dd> <dt>

*TargetPortalAddress* \[in\]
</dt> <dd>

The IP address or DNS name associated with the target portal.

</dd> <dt>

*TargetPortalPortNumber* \[in\]
</dt> <dd>

The TCP port number for the target portal.

</dd> <dt>

*InitiatorPortalAddress* \[in\]
</dt> <dd>

The IP address or DNS name associated with the initiator portal.

</dd> <dt>

*IsDataDigest* \[in\]
</dt> <dd>

If **true**, the initiator should enable the session to use an iSCSI data digest scheme when logging into the target portal. Otherwise, the data digest setting is determined by the initiator kernel mode driver.

</dd> <dt>

*IsHeaderDigest* \[in\]
</dt> <dd>

If **true**, the initiator should enable the session to use a header digest scheme when logging into the target portal. Otherwise, the header digest setting is determined by the initiator kernel mode driver.

</dd> <dt>

*ReportToPnP* \[in\]
</dt> <dd>

If **true**, the operation is reported to PnP.

</dd> <dt>

*AuthenticationType* \[in\]
</dt> <dd>

The type of authentication to use when logging into the target.

</dd> <dt>

*IsMultipathEnabled* \[in\]
</dt> <dd>

If **true**, the iSCSI initiator service allows multiple sessions to the same target portal.

</dd> <dt>

*IsPersistent* \[in\]
</dt> <dd>

If **true**, the session is automatically connected at every restart.

</dd> <dt>

*InitiatorInstanceName* \[in\]
</dt> <dd>

The name of the initiator instance that the iSCSI initiator service uses to send [SendTargets](storage.sendtargets) requests to the target portal. If no instance name is specified, the iSCSI initiator service chooses the initiator instance.

</dd> <dt>

*CreatediSCSISession* \[out\]
</dt> <dd>

A reference to the newly created [**MSFT\_iSCSISession**](msft-iscsisession.md) object.

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

 

 




