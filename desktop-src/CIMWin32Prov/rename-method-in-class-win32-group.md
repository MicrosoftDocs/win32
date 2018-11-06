---
Description: Allows the group name to be changed.
ms.assetid: 7eb1360e-7416-4a90-abc6-c9a85a114316
ms.tgt_platform: multiple
title: Rename method of the Win32_Group class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Group.Rename
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Rename method of the Win32\_Group class

The **Rename** [WMI class](https://msdn.microsoft.com/library/aa393244) method allows the group name to be changed.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Rename(
  [in] string Name
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the Windows user account on the domain specified by the **Domain** property of this class.

</dd> </dl>

## Return value

The **Rename** method can return the error codes listed in the following list. For integer values other than those listed, refer to [WMI\_Return Codes](https://msdn.microsoft.com/library/aa394574).

<dl> <dt>

**Success**
</dt> <dd>

0

Success.

</dd> <dt>

**Instance not found**
</dt> <dd>

1

</dd> <dt>

**Instance required**
</dt> <dd>

2

</dd> <dt>

**Invalid parameter**
</dt> <dd>

3

</dd> <dt>

**Group not found**
</dt> <dd>

4

</dd> <dt>

**Domain not found**
</dt> <dd>

5

</dd> <dt>

**Operation is allowed only on the primary domain controller of the domain**
</dt> <dd>

6

</dd> <dt>

**Operation is not allowed on specified special groups; user, admin, local or guest.**
</dt> <dd>

7

</dd> <dt>

**Other API error**
</dt> <dd>

8

</dd> <dt>

**Internal error**
</dt> <dd>

9

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_Group**](win32-group.md)
</dt> <dt>

[**Win32\_LogicalFileSecuritySetting**](https://msdn.microsoft.com/library/aa394180)
</dt> </dl>

 

 




