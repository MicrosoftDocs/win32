---
description: The CIM\_CompatibleProduct class represents an association between products that indicates whether two referenced products are interoperable, such as whether they can be installed together, or whether one can be the physical container for the other, and so on.
ms.assetid: d822b052-981a-4a66-8404-b4f5f4681502
ms.tgt_platform: multiple
title: CIM_CompatibleProduct class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_CompatibleProduct
- CIM_CompatibleProduct.CompatibilityDescription
- CIM_CompatibleProduct.CompatibleProduct
- CIM_CompatibleProduct.Product
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_CompatibleProduct class

The **CIM\_CompatibleProduct** class represents an association between products that indicates whether two referenced products are interoperable, such as whether they can be installed together, or whether one can be the physical container for the other, and so on.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{2F648FBA-DB22-11d2-85FC-0000F8102E5F}"), Association, AMENDMENT]
class CIM_CompatibleProduct
{
  string          CompatibilityDescription;
  CIM_Product REF CompatibleProduct;
  CIM_Product REF Product;
};
```

## Members

The **CIM\_CompatibleProduct** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CompatibleProduct** class has these properties.

<dl> <dt>

**CompatibilityDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string that defines how the two referenced products are interoperable, compatible, and whether there are compatibility limitations.

</dd> <dt>

**CompatibleProduct**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Product**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the compatible product.

</dd> <dt>

**Product**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Product**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the product for which compatible offerings are defined.

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



 

 




