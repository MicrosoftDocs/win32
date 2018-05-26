---
Description: Represents an iSCSI target portal.
ms.assetid: 13125658-2FA4-4A3D-93BC-CBB804F4F0A6
title: MSFT\_iSCSITargetPortal class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_iSCSITargetPortal class

Represents an iSCSI target portal.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSITargetPortal
{
  string  TargetPortalAddress;
  uint16  TargetPortalPortNumber;
  string  InitiatorInstanceName;
  string  InitiatorPortalAddress;
  boolean IsHeaderDigest;
  boolean IsDataDigest;
};
```

## Members

The **MSFT\_iSCSITargetPortal** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_iSCSITargetPortal** class has these methods.



| Method                                          | Description                                                  |
|:------------------------------------------------|:-------------------------------------------------------------|
| [**New**](msft-iscsitargetportal-new.md)       | Creates and configures a new iSCSI target portal.<br/> |
| [**Remove**](msft-iscsitargetportal-remove.md) | Removes an iSCSI target portal.<br/>                   |
| [**Update**](msft-iscsitargetportal-update.md) | Updates information about an iSCSI target portal.<br/> |



 

### Properties

The **MSFT\_iSCSITargetPortal** class has these properties.

<dl> <dt>

**InitiatorInstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the initiator instance that the iSCSI initiator service uses to send [SendTargets](storage.sendtargets) requests to the target portal. If no instance name is specified, the iSCSI initiator service chooses the initiator instance.

</dd> <dt>

**InitiatorPortalAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address or DNS name associated with the initiator portal.

</dd> <dt>

**IsDataDigest**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the initiator should enable the session to use an iSCSI data digest scheme when logging into the target portal. Otherwise, the data digest setting is determined by the initiator kernel mode driver.

</dd> <dt>

**IsHeaderDigest**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, the initiator should enable the session to use a header digest scheme when logging into the target portal. Otherwise, the header digest setting is determined by the initiator kernel mode driver.

</dd> <dt>

**TargetPortalAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The IP or DNS address associated with the target portal.

</dd> <dt>

**TargetPortalPortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The TCP port number for the target portal. The default value is 3260.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



 

 




