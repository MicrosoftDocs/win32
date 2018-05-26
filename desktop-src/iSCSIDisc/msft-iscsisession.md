---
Description: Represents an iSCSI session.
ms.assetid: DF4AC54D-B5C1-4DA3-9890-42AD8BF739E4
title: MSFT\_iSCSISession class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_iSCSISession class

Represents an iSCSI session.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSISession
{
  string  SessionIdentifier;
  string  InitiatorSideIdentifier;
  string  TargetSideIdentifier;
  uint32  NumberOfConnections;
  string  TargetNodeAddress;
  string  InitiatorPortalAddress;
  boolean IsDataDigest;
  boolean IsHeaderDigest;
  string  AuthenticationType;
  string  InitiatorNodeAddress;
  string  InitiatorInstanceName;
  boolean IsConnected;
  boolean IsPersistent;
  boolean IsDiscovered;
};
```

## Members

The **MSFT\_iSCSISession** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_iSCSISession** class has these methods.



| Method                                                   | Description                                                                  |
|:---------------------------------------------------------|:-----------------------------------------------------------------------------|
| [**Register**](msft-iscsisession-register.md)           | Registers the iSCSI session to be persistent.<br/>                     |
| [**SetCHAPSecret**](msft-iscsisession-setchapsecret.md) | Sets a CHAP secret key for use with iSCSI initiator connections.<br/>  |
| [**Unregister**](msft-iscsisession-unregister.md)       | Unregisters the iSCSI session so that it is no longer persistent.<br/> |



 

### Properties

The **MSFT\_iSCSISession** class has these properties.

<dl> <dt>

**AuthenticationType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of authentication to use when logging into the target.

</dd> <dt>

**InitiatorInstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the initiator instance that the iSCSI initiator service uses to send [SendTargets](storage.sendtargets) requests to the target portal. If no instance name is specified, the iSCSI initiator service chooses the initiator instance.

</dd> <dt>

**InitiatorNodeAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IQN of the initiator.

</dd> <dt>

**InitiatorPortalAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address or DNS name associated with the initiator portal.

</dd> <dt>

**InitiatorSideIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The initiatior side identifier.

</dd> <dt>

**IsConnected**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, there is an active connection to the target.

</dd> <dt>

**IsDataDigest**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the initiator should enable the session to use an iSCSI data digest scheme when logging into the target portal. Otherwise, the data digest setting is determined by the initiator kernel mode driver.

</dd> <dt>

**IsDiscovered**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, iSCSI discovery has been performed against the target.

</dd> <dt>

**IsHeaderDigest**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the initiator should enable the session to use a header digest scheme when logging into the target portal. Otherwise, the header digest setting is determined by the initiator kernel mode driver.

</dd> <dt>

**IsPersistent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the session is persistent and will be reestablished when the computer is restarted.

</dd> <dt>

**NumberOfConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of iSCSI connections in this session.

</dd> <dt>

**SessionIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The session identifier.

</dd> <dt>

**TargetNodeAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The iSCSI qualified name (IQN) of the target.

</dd> <dt>

**TargetSideIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The target side identifier.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



 

 




