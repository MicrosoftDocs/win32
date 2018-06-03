---
title: Win32\_ProductSoftwareFeatures class
description: The Win32\_ProductSoftwareFeatures association WMI class identifies the software features for a particular product.
ms.assetid: 42a0e9c8-0659-44a1-8f1a-53ab95fb0320
keywords:
- Win32_ProductSoftwareFeatures class
- Win32_ProductSoftwareFeatures class, described
topic_type:
- apiref
api_name:
- Win32_ProductSoftwareFeatures
- Win32_ProductSoftwareFeatures.Component
- Win32_ProductSoftwareFeatures.Product
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ProductSoftwareFeatures class

The **Win32\_ProductSoftwareFeatures** association [WMI class](https://msdn.microsoft.com/library/aa393244) identifies the software features for a particular product.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ProductSoftwareFeatures : CIM_ProductSoftwareFeatures
{
  Win32_SoftwareFeature Component;
  Win32_Product         Product;
};
```

## Members

The **Win32\_ProductSoftwareFeatures** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ProductSoftwareFeatures** class has these properties.

<dl> <dt>

**Component**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SoftwareFeature**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the properties of a software feature that is related to the product.

</dd> <dt>

**Product**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Product**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the properties of a product.

</dd> </dl>

## Remarks

The **Win32\_ProductSoftwareFeatures** class is derived from [**CIM\_ProductSoftwareFeatures**](https://msdn.microsoft.com/library/aa387985).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





