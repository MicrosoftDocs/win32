---
description: The Win32\_ImplementedCategory association WMI class relates a component category and the Component Object Model (COM) class using its interfaces.
ms.assetid: 7cf32b50-9ae6-44e5-b364-bc74dea3dc17
ms.tgt_platform: multiple
title: Win32_ImplementedCategory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ImplementedCategory
- Win32_ImplementedCategory.Category
- Win32_ImplementedCategory.Component
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_ImplementedCategory class

The **Win32\_ImplementedCategory** association [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) relates a component category and the Component Object Model (COM) class using its interfaces.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Association, Dynamic, Provider("CIMWin32"), UUID("{0F73ED5B-8ED9-11d2-B340-00105A1F8569}"), AMENDMENT]
class Win32_ImplementedCategory
{
  Win32_ComponentCategory REF Category;
  Win32_ClassicCOMClass   REF Component;
};
```

## Members

The **Win32\_ImplementedCategory** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ImplementedCategory** class has these properties.

<dl> <dt>

**Category**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComponentCategory**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_ComponentCategory")
</dt> </dl>

Reference to the instance representing the component category being used by the COM class.

</dd> <dt>

**Component**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ClassicCOMClass**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_ClassicCOMClass")
</dt> </dl>

Reference to the instance representing the COM class using the associated category.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> </dl>

 

