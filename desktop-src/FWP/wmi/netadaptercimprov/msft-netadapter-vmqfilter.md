---
description: MAC address and VLAN ID filters for VMQ and VPorts.
ms.assetid: 91da5a1c-479c-4b98-9927-b63c87666b0e
title: MSFT\_NetAdapter\_VmqFilter class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter_VmqFilter
- MSFT_NetAdapter_VmqFilter.FilterID
- MSFT_NetAdapter_VmqFilter.MacAddress
- MSFT_NetAdapter_VmqFilter.VlanID
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter\_VmqFilter class

MAC address and VLAN ID filters for VMQ and VPorts

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapter_VmqFilter
{
  uint32 FilterID;
  string MacAddress;
  uint16 VlanID;
};
```

## Members

The **MSFT\_NetAdapter\_VmqFilter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapter\_VmqFilter** class has these properties.

<dl> <dt>

**FilterID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Filter identifier.

</dd> <dt>

**MacAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The MAC address filter.

</dd> <dt>

**VlanID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The VLAN ID filter. This value may be NULL.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




