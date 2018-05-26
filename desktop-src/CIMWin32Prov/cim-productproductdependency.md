---
Description: The CIM\_ProductProductDependency class represents an association between two products, which indicates that one must be installed or absent for the other to function. This is conceptually equivalent to the CIM\_ServiceServiceDependency association.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 898b9993-3bdc-4a7c-98c1-ed960014ace8
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_ProductProductDependency class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ProductProductDependency class

The **CIM\_ProductProductDependency** class represents an association between two products, which indicates that one must be installed or absent for the other to function. This is conceptually equivalent to the [**CIM\_ServiceServiceDependency**](cim-serviceservicedependency.md) association.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{65878E68-DB2B-11d2-85FC-0000F8102E5F}"), Association, AMENDMENT]
class CIM_ProductProductDependency
{
  CIM_Product REF DependentProduct;
  CIM_Product REF RequiredProduct;
  uint16          TypeOfDependency;
};
```

## Members

The **CIM\_ProductProductDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ProductProductDependency** class has these properties.

<dl> <dt>

**DependentProduct**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Product**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the product that is dependent on another product.

</dd> <dt>

**RequiredProduct**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Product**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the required product.

</dd> <dt>

**TypeOfDependency**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Nature of the product dependency.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

Unknown.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

Other.

</dd> <dt>

<span id="Product_Must_Be_Installed"></span><span id="product_must_be_installed"></span><span id="PRODUCT_MUST_BE_INSTALLED"></span>

<span id="Product_Must_Be_Installed"></span><span id="product_must_be_installed"></span><span id="PRODUCT_MUST_BE_INSTALLED"></span>**Product Must Be Installed** (2)


</dt> <dd>

Product must be installed.

</dd> <dt>

<span id="Product_Must_Not_Be_Installed"></span><span id="product_must_not_be_installed"></span><span id="PRODUCT_MUST_NOT_BE_INSTALLED"></span>

<span id="Product_Must_Not_Be_Installed"></span><span id="product_must_not_be_installed"></span><span id="PRODUCT_MUST_NOT_BE_INSTALLED"></span>**Product Must Not Be Installed** (3)


</dt> <dd>

Product must not be installed.

</dd> </dl>

</dd> </dl>

## Remarks

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



 

 




