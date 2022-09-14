---
description: The CIM\_ProductSoftwareFeatures association identifies the software features for a particular product.
ms.assetid: cd6190f8-d86e-44c8-b506-48016a7c22e1
ms.tgt_platform: multiple
title: CIM_ProductSoftwareFeatures class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ProductSoftwareFeatures
- CIM_ProductSoftwareFeatures.Component
- CIM_ProductSoftwareFeatures.Product
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ProductSoftwareFeatures class

The **CIM\_ProductSoftwareFeatures** association identifies the software features for a particular product.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{7C39D12A-DB2B-11d2-85FC-0000F8102E5F}"), Association, Aggregation, Abstract, AMENDMENT]
class CIM_ProductSoftwareFeatures
{
  CIM_SoftwareFeature REF Component;
  CIM_Product         REF Product;
};
```

## Members

The **CIM\_ProductSoftwareFeatures** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ProductSoftwareFeatures** class has these properties.

<dl> <dt>

**Component**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SoftwareFeature**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (FALSE), [**Weak**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Reference to the component.

</dd> <dt>

**Product**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Product**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (0), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (FALSE), [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Reference to the product.

</dd> </dl>

## Remarks

WMI does not implement this class. For WMI classes derived from **CIM\_ProductSoftwareFeatures**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



 

