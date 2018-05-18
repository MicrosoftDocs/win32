---
title: Win32\_ProductCheck class
description: The Win32\_ProductCheck association WMI class relates instances of CIM\_Check and Win32\_Product.
ms.assetid: 'b75a03c3-1b48-4cee-9fff-1cf92ba39abf'
keywords: ["Win32_ProductCheck class", "Win32_ProductCheck class, described"]
topic_type:
- apiref
api_name:
- Win32_ProductCheck
- Win32_ProductCheck.Check
- Win32_ProductCheck.Product
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_ProductCheck class

The **Win32\_ProductCheck** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates instances of [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206) and [**Win32\_Product**](win32-product.md).

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ProductCheck
{
  CIM_Check     Check;
  Win32_Product Product;
};
```

## Members

The **Win32\_ProductCheck** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ProductCheck** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Check**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the properties of a check available to the product.

</dd> <dt>

**Product**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Product**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the properties of a product being installed.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





