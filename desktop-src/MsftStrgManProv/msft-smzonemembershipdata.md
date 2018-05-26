---
title: MSFT\_SMZoneMembershipData class
description: Represents membership data for a zone.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3b3d7c3f-0ac6-4882-a65c-4192c53929f1
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMZoneMembershipData class
- MSFT_SMZoneMembershipData class, described
topic_type:
- apiref
api_name:
- MSFT_SMZoneMembershipData
- MSFT_SMZoneMembershipData.ObjectId
- MSFT_SMZoneMembershipData.Caption
- MSFT_SMZoneMembershipData.Description
- MSFT_SMZoneMembershipData.ElementName
- MSFT_SMZoneMembershipData.ConnectivityMemberType
- MSFT_SMZoneMembershipData.OtherConnectivityMemberType
- MSFT_SMZoneMembershipData.ConnectivityMemberID
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMZoneMembershipData class

Represents membership data for a zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMZoneMembershipData
{
  String ObjectId;
  string Caption;
  string Description;
  string ElementName;
  uint16 ConnectivityMemberType;
  string OtherConnectivityMemberType;
  string ConnectivityMemberID;
};
```

## Members

The **MSFT\_SMZoneMembershipData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMZoneMembershipData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short textual description of the object.

</dd> <dt>

**ConnectivityMemberID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identification of the member in the format of the type specified by the **ConnectivityMemberType** property.

</dd> <dt>

**ConnectivityMemberType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of identification used in the **ConnectivityMemberID** property.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Permanent_Address"></span><span id="permanent_address"></span><span id="PERMANENT_ADDRESS"></span>

**Permanent Address** (2)


</dt> <dd></dd> <dt>

<span id="Network_Address"></span><span id="network_address"></span><span id="NETWORK_ADDRESS"></span>

**Network Address** (3)


</dt> <dd></dd> <dt>

<span id="Switch_Port_ID"></span><span id="switch_port_id"></span><span id="SWITCH_PORT_ID"></span>

**Switch Port ID** (4)


</dt> <dd></dd> <dt>

<span id="Logical_Port_Group"></span><span id="logical_port_group"></span><span id="LOGICAL_PORT_GROUP"></span>

**Logical Port Group** (5)


</dt> <dd></dd> <dt>

<span id="Connectivity_Collection"></span><span id="connectivity_collection"></span><span id="CONNECTIVITY_COLLECTION"></span>

**Connectivity Collection** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>7 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object.

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

</dd> <dt>

**OtherConnectivityMemberType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the connectivity member type when the **ConnectivityMemberType** value is **Other**.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





