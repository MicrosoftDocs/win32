---
description: The CIM\_ProductSupport class represents an association between product and support access that conveys how support is obtained for the product.
ms.assetid: 61c62556-0cf3-438c-b9c7-152505bf7ed6
ms.tgt_platform: multiple
title: CIM_ProductSupport class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ProductSupport
- CIM_ProductSupport.Product
- CIM_ProductSupport.Support
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ProductSupport class

The **CIM\_ProductSupport** class represents an association between product and support access that conveys how support is obtained for the product. Various types of support are available for a product; the same support object can provide assistance for multiple products.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{8D6D6880-DB2B-11d2-85FC-0000F8102E5F}"), Association, AMENDMENT]
class CIM_ProductSupport
{
  CIM_Product       REF Product;
  CIM_SupportAccess REF Support;
};
```

## Members

The **CIM\_ProductSupport** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ProductSupport** class has these properties.

<dl> <dt>

**Product**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Product**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the product.

</dd> <dt>

**Support**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SupportAccess**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the product support.

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



 

 




