---
description: Filters traffic based on which local application is sending or receiving the traffic.
ms.assetid: 5505bd0d-16a9-4251-a0aa-a82c8896d8c3
title: MSFT\_NetApplicationFilter class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetApplicationFilter
- MSFT_NetApplicationFilter.AppPath
- MSFT_NetApplicationFilter.Package
- MSFT_NetApplicationFilter.Name
- MSFT_NetApplicationFilter.SystemCreationClassName
- MSFT_NetApplicationFilter.SystemName
- MSFT_NetApplicationFilter.CreationClassName
- MSFT_NetApplicationFilter.IsNegated
- MSFT_NetApplicationFilter.InstallDate
- MSFT_NetApplicationFilter.OperationalStatus
- MSFT_NetApplicationFilter.StatusDescriptions
- MSFT_NetApplicationFilter.Status
- MSFT_NetApplicationFilter.HealthState
- MSFT_NetApplicationFilter.CommunicationStatus
- MSFT_NetApplicationFilter.DetailedStatus
- MSFT_NetApplicationFilter.OperatingStatus
- MSFT_NetApplicationFilter.PrimaryStatus
- MSFT_NetApplicationFilter.InstanceID
- MSFT_NetApplicationFilter.Caption
- MSFT_NetApplicationFilter.Description
- MSFT_NetApplicationFilter.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetApplicationFilter class

Filters traffic based on which local application is sending or receiving the traffic.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetApplicationFilter : CIM_FilterEntryBase
{
  string   AppPath;
  string   Package;
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

The **MSFT\_NetApplicationFilter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetApplicationFilter** class has these properties.

<dl> <dt>

**AppPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Path and filename of the executable whose traffic to filter.

</dd> <dt>

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

**Package**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The application package this rule applies to, given as a SID.

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



 

 




