---
description: The CIM\_ActsAsSpare association indicates which elements can be spares or replace other aggregated elements. A spare can operate in &\#0034;hot-standby&\#0034; mode as specified on an element-by-element basis.
ms.assetid: bed8c552-f782-4af9-9441-ff3268182c3b
ms.tgt_platform: multiple
title: CIM_ActsAsSpare class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ActsAsSpare
- CIM_ActsAsSpare.Group
- CIM_ActsAsSpare.HotStandby
- CIM_ActsAsSpare.Spare
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ActsAsSpare class

The **CIM\_ActsAsSpare** association indicates which elements can be spares or replace other aggregated elements. A spare can operate in "hot-standby" mode as specified on an element-by-element basis.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Association, UUID("{64C1726E-DB21-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_ActsAsSpare
{
  CIM_SpareGroup           REF Group;
  boolean                      HotStandby;
  CIM_ManagedSystemElement REF Spare;
};
```

## Members

The **CIM\_ActsAsSpare** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ActsAsSpare** class has these properties.

<dl> <dt>

**Group**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SpareGroup**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the **Group** property that represents the [**CIM\_SpareGroup**](cim-sparegroup.md) class.

</dd> <dt>

**HotStandby**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the spare is operating as a hot standby.

</dd> <dt>

**Spare**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to a managed system element acting as a spare and participating in the spare group.

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



## See also

<dl> <dt>

[CIM Classes](/windows/desktop/WmiSdk/cimclas)
</dt> </dl>

 

