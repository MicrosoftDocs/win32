---
title: WT\_General class
description: Contains general information about the Microsoft iSCSI Target Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d52cdb11-12ad-49e7-956a-d76068067a2e
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_General class iSCSI Software Target API
- WT_General class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_General
- WT_General.Version
- WT_General.IsClustered
- WT_General.Guid
- WT_General.Name
- WT_General.MinVersionSupported
- WT_General.MaxVersionSupported
- WT_General.AuthenticationMethodsSupported
- WT_General.IsRemoteManageable
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WT\_General class

Contains general information about the Microsoft iSCSI Target Server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_General
{
  string  Version;
  boolean IsClustered;
  string  Guid;
  string  Name;
  uint8   MinVersionSupported;
  uint8   MaxVersionSupported;
  uint16  AuthenticationMethodsSupported[];
  boolean IsRemoteManageable;
};
```

## Members

The **WT\_General** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_General** class has these properties.

<dl> <dt>

**AuthenticationMethodsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (None, SRP, CHAP, Kerberos), **ValueMap** (2, 3, 4, 5)
</dt> </dl>

Authentication methods supported by the Microsoft iSCSI Target Server.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (2)


</dt> <dd></dd> <dt>

<span id="SRP"></span><span id="srp"></span>

**SRP** (3)


</dt> <dd></dd> <dt>

<span id="CHAP"></span><span id="chap"></span>

**CHAP** (4)


</dt> <dd></dd> <dt>

<span id="Kerberos"></span><span id="kerberos"></span><span id="KERBEROS"></span>

**Kerberos** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**Guid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique identifier of this installation of the Microsoft iSCSI Target Server.

</dd> <dt>

**IsClustered**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the Microsoft iSCSI Target Server is in a clustered configuration. If **false**, it is in a stand-alone configuration.

</dd> <dt>

**IsRemoteManageable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether the Microsoft iSCSI Target can be managed remotely.

**Windows Server 2012:** This property is not supported until Windows Server 2012 R2.

</dd> <dt>

**MaxVersionSupported**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum version number of the iSCSI protocol specification that is supported by the Microsoft iSCSI Target Server.

</dd> <dt>

**MinVersionSupported**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Minimum version number of the iSCSI protocol specification that is supported by the Microsoft iSCSI Target Server.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Friendly name for this installation of the Microsoft iSCSI Target Server.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Microsoft iSCSI Target Server version information.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





