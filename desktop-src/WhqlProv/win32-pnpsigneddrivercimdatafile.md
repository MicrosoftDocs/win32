---
title: Win32\_PnPSignedDriverCIMDataFile class
description: The Win32\_PnPSignedDriverCIMDataFile association WMI class finds all binary files associated with a PnP driver.
ms.assetid: 'd919605f-dd81-405d-9e06-d35fc5389fd4'
keywords: ["Win32_PnPSignedDriverCIMDataFile class", "Win32_PnPSignedDriverCIMDataFile class, described"]
topic_type:
- apiref
api_name:
- Win32_PnPSignedDriverCIMDataFile
- Win32_PnPSignedDriverCIMDataFile.Antecedent
- Win32_PnPSignedDriverCIMDataFile.Dependent
api_location:
- SignDrv.dll
api_type:
- DllExport
---

# Win32\_PnPSignedDriverCIMDataFile class

The **Win32\_PnPSignedDriverCIMDataFile** association [WMI class](https://msdn.microsoft.com/library/aa393244) finds all binary files associated with a PnP driver.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_PnPSignedDriverCIMDataFile : CIM_Dependency
{
  Win32_PnPSignedDriver REF Antecedent;
  CIM_DataFile          REF Dependent;
};
```

## Members

The **Win32\_PnPSignedDriverCIMDataFile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PnPSignedDriverCIMDataFile** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PnPSignedDriver**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to a [**Win32\_PnPSignedDriver**](win32-pnpsigneddriver.md) instance that represents a signed PnP driver.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_DataFile**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to a [**CIM\_DataFile**](https://msdn.microsoft.com/library/aa387236) instance that represents the binary file associated with the PnP driver.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>WhqlProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SignDrv.dll</dt> </dl>  |



## See also

<dl> <dt>

[Computer System Hardware Classes](https://msdn.microsoft.com/library/aa389273)
</dt> </dl>

 

 





