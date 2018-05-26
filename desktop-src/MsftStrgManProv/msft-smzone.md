---
title: MSFT\_SMZone class
description: Represents a zone.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d662126b-b090-42f0-9a1f-5a9e0c1ef406
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMZone class
- MSFT_SMZone class, described
topic_type:
- apiref
api_name:
- MSFT_SMZone
- MSFT_SMZone.ObjectId
- MSFT_SMZone.Active
- MSFT_SMZone.ConnectivityStatus
- MSFT_SMZone.Caption
- MSFT_SMZone.Description
- MSFT_SMZone.ElementName
- MSFT_SMZone.ZoneType
- MSFT_SMZone.OtherZoneTypeDescription
- MSFT_SMZone.ZoneSubType
- MSFT_SMZone.OtherZoneSubTypeDescription
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMZone class

Represents a zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMZone
{
  String  ObjectId;
  boolean Active;
  uint16  ConnectivityStatus;
  string  Caption;
  string  Description;
  string  ElementName;
  uint16  ZoneType;
  string  OtherZoneTypeDescription;
  uint16  ZoneSubType;
  string  OtherZoneSubTypeDescription;
};
```

## Members

The **MSFT\_SMZone** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMZone** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this zone is currently active, that is, under enforcement of a Windows Fabric service.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short textual description of the object.

</dd> <dt>

**ConnectivityStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current or potential connectivity between endpoints in this collection.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Connectivity_Up"></span><span id="connectivity_up"></span><span id="CONNECTIVITY_UP"></span>

**Connectivity/Up** (2)


</dt> <dd></dd> <dt>

<span id="No_Connectivity_Down"></span><span id="no_connectivity_down"></span><span id="NO_CONNECTIVITY_DOWN"></span>

**No Connectivity/Down** (3)


</dt> <dd></dd> <dt>

<span id="Partitioned"></span><span id="partitioned"></span><span id="PARTITIONED"></span>

**Partitioned** (4)


</dt> <dd></dd> </dl>

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

**OtherZoneSubTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Zone.ZoneSubType")
</dt> </dl>

Describes the Zone subtype when the **ZoneSubType** value is **Other**.

</dd> <dt>

**OtherZoneTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Zone.ZoneType")
</dt> </dl>

Describes the Zone type when the **ZoneType** value is **Other**.

</dd> <dt>

**ZoneSubType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Zone.OtherZoneSubTypeDescription")
</dt> </dl>

Modifies the value of the **ZoneType** property.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="SCSI"></span><span id="scsi"></span>

**SCSI** (2)


</dt> <dd></dd> <dt>

<span id="VI"></span><span id="vi"></span>

**VI** (3)


</dt> <dd></dd> <dt>

<span id="IP"></span><span id="ip"></span>

**IP** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**ZoneType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Zone.OtherZoneTypeDescription")
</dt> </dl>

The type of zoning to be enforced.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

**Default** (2)


</dt> <dd></dd> <dt>

<span id="Protocol"></span><span id="protocol"></span><span id="PROTOCOL"></span>

**Protocol** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

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

 

 





