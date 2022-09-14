---
description: The CIM\_RelatedStatistics association represents hierarchies and dependencies of related CIM\_StatisticalInformation classes.
ms.assetid: f5cea01d-7854-4ad4-a89e-db0ce9f4a83f
ms.tgt_platform: multiple
title: CIM_RelatedStatistics class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_RelatedStatistics
- CIM_RelatedStatistics.RelatedStats
- CIM_RelatedStatistics.Stats
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_RelatedStatistics class

The **CIM\_RelatedStatistics** association represents hierarchies and dependencies of related [**CIM\_StatisticalInformation**](cim-statisticalinformation.md) classes.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Association, UUID("{956597A4-7D80-11D2-AAD3-006008C78BC7}"), AMENDMENT]
class CIM_RelatedStatistics
{
  CIM_StatisticalInformation REF RelatedStats;
  CIM_StatisticalInformation REF Stats;
};
```

## Members

The **CIM\_RelatedStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_RelatedStatistics** class has these properties.

<dl> <dt>

**RelatedStats**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StatisticalInformation**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the related statistics or metrics.

</dd> <dt>

**Stats**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StatisticalInformation**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the statistic information or object.

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



 

 




