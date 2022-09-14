---
description: Defines the settings for virtual system migration that is managed by an instance of the CIM\_VirtualSystemMigrationService class.
ms.assetid: c28ed48b-bacc-49c8-9131-2543c0edb3fd
title: CIM_VirtualSystemMigrationSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_VirtualSystemMigrationSettingData
- CIM_VirtualSystemMigrationSettingData.MigrationType
- CIM_VirtualSystemMigrationSettingData.Priority
- CIM_VirtualSystemMigrationSettingData.Bandwidth
- CIM_VirtualSystemMigrationSettingData.BandwidthUnit
- CIM_VirtualSystemMigrationSettingData.OtherTransportType
- CIM_VirtualSystemMigrationSettingData.TransportType
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_VirtualSystemMigrationSettingData class

Defines the settings for virtual system migration that is managed by an instance of the [**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md) class.

## Syntax

``` syntax
[Experimental, Abstract, Version("2.20.0"), UMLPackagePath("CIM::System::Virtualization"), AMENDMENT]
class CIM_VirtualSystemMigrationSettingData : CIM_SettingData
{
  uint16 MigrationType;
  uint16 Priority;
  uint16 Bandwidth;
  string BandwidthUnit;
  string OtherTransportType;
  uint16 TransportType;
};
```

## Members

The **CIM\_VirtualSystemMigrationSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_VirtualSystemMigrationSettingData** class has these properties.

<dl> <dt>

**Bandwidth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Gauge**](/windows/desktop/WmiSdk/standard-qualifiers), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VirtualSystemMigrationSettingData**.**BandwidthUnit**")
</dt> </dl>

The bandwidth assigned to or requested for a virtual system migration operation. "0" is default bandwidth for migration requests.

The **Bandwidth** and **Priority** properties may be used in conjunction. Migration processes that have the highest equal **Priority** values share the available bandwidth based on their requested bandwidth. If not all bandwidth is consumed by this set of processes, migration processes with the next lower equal **Priority** values share the remaining bandwidth. If more bandwidth remains, migration processes with the next lower equal **Priority** values are considered.

The unit used in **Bandwidth** property is specified by the value of the **BandwidthUnit** property.

If the value of the **BandwidthUnit** property is "percent", the following rules apply:

-   The value of the **Bandwidth** property must be between "0" and "100", with higher values indicating a higher bandwidth.
-   A value of "100" indicates all available bandwidth for performing virtual system migration operations.
-   Values between "1" and "100" linearly correlate with the available bandwidth range. For example, a value of 50 requests half of the available bandwidth.

</dd> <dt>

**BandwidthUnit**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VirtualSystemMigrationSettingData**.**Bandwidth**"), **IsPUnit**
</dt> </dl>

The unit used by the **Bandwidth** property. The value of this property should be a legal value of the Programmatic Units qualifier defined in Appendix C.1 of DSP0004 V2.4 or later.

> [!Note]  
> Profiles such as DMTF DSP1081 define how clients can discover the set of units supported by an implementation, and ranges and increments for values of the **Bandwidth** property.

 

</dd> <dt>

**MigrationType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of migration operation to perform.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Live"></span><span id="live"></span><span id="LIVE"></span>

**Live** (2)


</dt> <dd></dd> <dt>

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>

**Resume** (3)


</dt> <dd></dd> <dt>

<span id="Restart"></span><span id="restart"></span><span id="RESTART"></span>

**Restart** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**OtherTransportType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VirtualSystemMigrationSettingData**.**TransportType**")
</dt> </dl>

The type of transport to apply if the value of **TransportType** is "1" (other).

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative migration importance that the virtual system migration implementation may use to order or assign preference among multiple pending migration requests. The lower the value, the higher the priority. "0" is default bandwidth for migration requests.

</dd> <dt>

**TransportType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VirtualSystemMigrationSettingData**.**OtherTransportType**")
</dt> </dl>

The type of transport to apply to a virtual system migration operation.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="SSH"></span><span id="ssh"></span>

**SSH** (2)


</dt> <dd></dd> <dt>

<span id="TLS"></span><span id="tls"></span>

**TLS** (3)


</dt> <dd></dd> <dt>

<span id="TLS_Strict"></span><span id="tls_strict"></span><span id="TLS_STRICT"></span>

**TLS Strict** (4)


</dt> <dd></dd> <dt>

<span id="TCP"></span><span id="tcp"></span>

**TCP** (5)


</dt> <dd></dd> <dt>

<span id="IPC"></span><span id="ipc"></span>

**IPC** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_SettingData**](cim-settingdata.md)
</dt> </dl>

 

