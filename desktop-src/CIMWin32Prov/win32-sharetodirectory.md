---
description: The Win32\_ShareToDirectory association WMI class relates a shared resource on the computer system and the directory to which it is mapped.
ms.assetid: f8562539-2cb4-4661-8ef9-8b665e76a292
ms.tgt_platform: multiple
title: Win32_ShareToDirectory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ShareToDirectory
- Win32_ShareToDirectory.Share
- Win32_ShareToDirectory.SharedElement
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_ShareToDirectory class

The **Win32\_ShareToDirectory** association [WMI class](../wmisdk/retrieving-a-class.md) relates a shared resource on the computer system and the directory to which it is mapped.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Association, Dynamic, Provider("CIMWin32"), UUID("{8502C511-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_ShareToDirectory
{
  Win32_Share   REF Share;
  CIM_Directory REF SharedElement;
};
```

## Members

The **Win32\_ShareToDirectory** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ShareToDirectory** class has these properties.

<dl> <dt>

**Share**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Share**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_Share")
</dt> </dl>

Reference to the instance representing the properties of a shared resource available through the directory.

</dd> <dt>

**SharedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Directory**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("CIM\|CIM\_Directory")
</dt> </dl>

Reference to the instance representing the properties of the directory that has been mapped to a shared resource.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](./operating-system-classes.md)
</dt> </dl>

 

 
