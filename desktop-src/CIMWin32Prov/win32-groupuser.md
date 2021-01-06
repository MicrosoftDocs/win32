---
description: The Win32\_GroupUser association WMI class relates a group and an account that is a member of that group.
ms.assetid: 46dd65f0-b729-4b23-8a00-bc33d1a4868b
ms.tgt_platform: multiple
title: Win32_GroupUser class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_GroupUser
- Win32_GroupUser.GroupComponent
- Win32_GroupUser.PartComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_GroupUser class

The **Win32\_GroupUser** association [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) relates a group and an account that is a member of that group.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C508-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_GroupUser : CIM_Component
{
  Win32_Group   REF GroupComponent;
  Win32_Account REF PartComponent;
};
```

## Members

The **Win32\_GroupUser** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_GroupUser** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Group**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("GroupComponent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_Group")
</dt> </dl>

Reference to the instance representing the group of which the account is a member.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Account**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PartComponent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI\|Win32\_Account")
</dt> </dl>

Reference to the instance representing the user or system account that is a part of a group of accounts.

</dd> </dl>

## Remarks

The **Win32\_GroupUser** class is derived from [**CIM\_Component**](cim-component.md).

## Examples

For a PowerShell example of using Win32\_GroupUser to retrieve a list of local group members, see the [List local group members on a remote computer using WMI and PowerShell sample](https://Gallery.TechNet.Microsoft.Com/List-local-group-members-762b48c5) on TechNet Gallery.

The [WMI Information Retriever](https://Gallery.TechNet.Microsoft.Com/e493376c-1286-456b-bd4b-4ac3b0e9bb45) VBScript code example on the TechNet Gallery uses the **Win32\_GroupUser** class to retrieve user information from a number of remote computers.

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

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> </dl>

 

