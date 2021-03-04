---
description: The CIM\_FRUIncludesProduct class indicates that a field replaceable unit (FRU) may be composed of other products.
ms.assetid: e57dc7f5-4c5b-4ec4-9300-e080053955cb
ms.tgt_platform: multiple
title: CIM_FRUIncludesProduct class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_FRUIncludesProduct
- CIM_FRUIncludesProduct.Component
- CIM_FRUIncludesProduct.FRU
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_FRUIncludesProduct class

The **CIM\_FRUIncludesProduct** class indicates that a field replaceable unit (FRU) may be composed of other products.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{87FEEDCA-DB2A-11d2-85FC-0000F8102E5F}"), Aggregation, Association, AMENDMENT]
class CIM_FRUIncludesProduct
{
  CIM_Product REF Component;
  CIM_FRU     REF FRU;
};
```

## Members

The **CIM\_FRUIncludesProduct** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_FRUIncludesProduct** class has these properties.

<dl> <dt>

**Component**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Product**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the product that is a part of the FRU.

</dd> <dt>

**FRU**
</dt> <dd> <dl> <dt>

Data type: **CIM\_FRU**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

Reference to the FRU.

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



 

