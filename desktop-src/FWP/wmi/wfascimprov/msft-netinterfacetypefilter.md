---
description: Filters traffic based on the type of interface it is sent or received on.
ms.assetid: 1dc0efd4-43d2-41a9-b98a-aaa2d0eb1dda
title: MSFT\_NetInterfaceTypeFilter class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetInterfaceTypeFilter
- MSFT_NetInterfaceTypeFilter.InterfaceType
- MSFT_NetInterfaceTypeFilter.Name
- MSFT_NetInterfaceTypeFilter.SystemCreationClassName
- MSFT_NetInterfaceTypeFilter.SystemName
- MSFT_NetInterfaceTypeFilter.CreationClassName
- MSFT_NetInterfaceTypeFilter.IsNegated
- MSFT_NetInterfaceTypeFilter.InstallDate
- MSFT_NetInterfaceTypeFilter.OperationalStatus
- MSFT_NetInterfaceTypeFilter.StatusDescriptions
- MSFT_NetInterfaceTypeFilter.Status
- MSFT_NetInterfaceTypeFilter.HealthState
- MSFT_NetInterfaceTypeFilter.CommunicationStatus
- MSFT_NetInterfaceTypeFilter.DetailedStatus
- MSFT_NetInterfaceTypeFilter.OperatingStatus
- MSFT_NetInterfaceTypeFilter.PrimaryStatus
- MSFT_NetInterfaceTypeFilter.InstanceID
- MSFT_NetInterfaceTypeFilter.Caption
- MSFT_NetInterfaceTypeFilter.Description
- MSFT_NetInterfaceTypeFilter.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetInterfaceTypeFilter class

Filters traffic based on the type of interface it is sent or received on.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetInterfaceTypeFilter : CIM_FilterEntryBase
{
  uint32   InterfaceType;
  string   Name;
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName;
  boolean  IsNegated;
  datetime InstallDate;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus;
  uint16   PrimaryStatus;
  string   InstanceID;
  string   Caption;
  string   Description;
  string   ElementName;
};
```

## Members

The **MSFT\_NetInterfaceTypeFilter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetInterfaceTypeFilter** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Used in CimInstance.ToString(). A short string for describing this instance when debugging.

</dd> <dt>

**CommunicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**DetailedStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that uniquely identifies this instance within the PolicyStore.

</dd> <dt>

**InterfaceType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies what types of interface to filter on.

<dl> <dt>

<span id="Local_area_network"></span><span id="local_area_network"></span><span id="LOCAL_AREA_NETWORK"></span>**Local area network** (1)
</dt> <dt>

<span id="Remote_access"></span><span id="remote_access"></span><span id="REMOTE_ACCESS"></span>**Remote access** (4)
</dt> <dt>

<span id="Wireless_"></span><span id="wireless_"></span><span id="WIRELESS_"></span>**Wireless** (2 )
</dt> </dl>

</dd> <dt>

**IsNegated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




