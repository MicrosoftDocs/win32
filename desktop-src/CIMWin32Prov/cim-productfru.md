---
description: The CIM\_ProductFRU class represents an association between the product and a field replaceable unit (FRU), which provides information about product components that have been, or are being replaced.
ms.assetid: 15d682e5-cd90-4fc4-8fff-e3fe1d2a0ac4
ms.tgt_platform: multiple
title: CIM_ProductFRU class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ProductFRU
- CIM_ProductFRU.FRU
- CIM_ProductFRU.Product
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ProductFRU class

The **CIM\_ProductFRU** class represents an association between the product and a field replaceable unit (FRU), which provides information about product components that have been, or are being replaced.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{EB98A1B2-DB36-11d2-85FC-0000F8102E5F}"), Association, AMENDMENT]
class CIM_ProductFRU
{
  CIM_FRU     REF FRU;
  CIM_Product REF Product;
};
```

## Members

The **CIM\_ProductFRU** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ProductFRU** class has these properties.

<dl> <dt>

**FRU**
</dt> <dd> <dl> <dt>

Data type: **CIM\_FRU**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the FRU.

</dd> <dt>

**Product**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Product**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

Reference to the product to which the FRU is applied.

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



 

