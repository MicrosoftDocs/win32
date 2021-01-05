---
description: The CIM\_SettingContext class associates configuration objects with setting objects.
ms.assetid: 8ed7e150-b4e6-4fd4-809b-32e870b559c4
ms.tgt_platform: multiple
title: CIM_SettingContext class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SettingContext
- CIM_SettingContext.Context
- CIM_SettingContext.Setting
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_SettingContext class

The **CIM\_SettingContext** class associates configuration objects with setting objects. For example, a network adapter's settings could change based on the site or network to which its hosting computer system is attached. In which case, the computer system would have two different configuration objects, corresponding to the differences in network configuration for the two network segments. One configuration would aggregate a setting object for the network adapter when operating on one segment; whereas, the other configuration would aggregate a different network adapter setting object, specific to another segment. Note that many computer settings are independent of the network configuration. For example, both configurations would aggregate the same setting object for the computer system's monitor resolution.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{F0B752E8-DB30-11d2-85FC-0000F8102E5F}"), Aggregation, Association, AMENDMENT]
class CIM_SettingContext
{
  CIM_Configuration REF Context;
  CIM_Setting       REF Setting;
};
```

## Members

The **CIM\_SettingContext** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SettingContext** class has these properties.

<dl> <dt>

**Context**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Configuration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Reference to the configuration object that aggregates the setting.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Setting**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an aggregated setting.

</dd> </dl>

## Remarks

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



 

