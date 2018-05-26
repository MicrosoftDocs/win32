---
title: Win32\_ProductResource class
description: The Win32\_ProductResource association WMI class relates instances of Win32\_Product and Win32\_MSIResource.
ms.assetid: e1d541e7-f00c-415a-b7c4-61c3857979c3
keywords:
- Win32_ProductResource class
- Win32_ProductResource class, described
topic_type:
- apiref
api_name:
- Win32_ProductResource
- Win32_ProductResource.Product
- Win32_ProductResource.Resource
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_ProductResource class

The **Win32\_ProductResource** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates instances of [**Win32\_Product**](win32-product.md) and [**Win32\_MSIResource**](win32-msiresource.md).

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ProductResource
{
  Win32_Product     Product;
  Win32_MSIResource Resource;
};
```

## Members

The **Win32\_ProductResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ProductResource** class has these properties.

<dl> <dt>

**Product**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Product**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the properties of a product to the MSI resource.

</dd> <dt>

**Resource**
</dt> <dd> <dl> <dt>

Data type: **Win32\_MSIResource**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the properties of any resource used in the process of installing, upgrading, or patching the product.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



 

 





