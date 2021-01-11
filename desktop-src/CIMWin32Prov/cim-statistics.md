---
description: The CIM\_Statistics class represents an association that relates managed system elements to the statistical groups that apply to them.
ms.assetid: fc75991b-adcd-4e47-b610-7503f6bb7c03
ms.tgt_platform: multiple
title: CIM_Statistics class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Statistics
- CIM_Statistics.Element
- CIM_Statistics.Stats
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_Statistics class

The **CIM\_Statistics** class represents an association that relates managed system elements to the statistical groups that apply to them.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Association, UUID("{956597A3-7D80-11D2-AAD3-006008C78BC7}"), AMENDMENT]
class CIM_Statistics
{
  CIM_ManagedSystemElement   REF Element;
  CIM_StatisticalInformation REF Stats;
};
```

## Members

The **CIM\_Statistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Statistics** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) class for which statistical or metric data is defined.

</dd> <dt>

**Stats**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StatisticalInformation**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the statistical information or object.

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



 

 




