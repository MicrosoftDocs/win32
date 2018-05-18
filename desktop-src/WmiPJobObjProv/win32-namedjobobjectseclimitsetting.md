---
Description: 'The Win32\_NamedJobObjectSecLimitSetting&\#32;WMI class represents the security limit settings for a job object.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'aa396f0b-45d3-43bf-b5ec-15b9e90700d5'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_NamedJobObjectSecLimitSetting class'
---

# Win32\_NamedJobObjectSecLimitSetting class

The **Win32\_NamedJobObjectSecLimitSetting** [WMI class](https://msdn.microsoft.com/library/aa393244) represents the security limit settings for a job object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("NamedJobObjectSecLimitSettingProv"), UUID("{F2D96E32-2A34-475b-878D-B0AE7657519F}"), AMENDMENT]
class Win32_NamedJobObjectSecLimitSetting : CIM_Setting
{
  string                Caption;
  string                Description;
  Win32_TokenPrivileges PrivilegesToDelete;
  Win32_TokenGroups     RestrictedSIDs;
  uint32                SecurityLimitFlags;
  string                SettingID;
  Win32_TokenGroups     SIDsToDisable;
};
```

## Members

The **Win32\_NamedJobObjectSecLimitSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NamedJobObjectSecLimitSetting** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**PrivilegesToDelete**
</dt> <dd> <dl> <dt>

Data type: **Win32\_TokenPrivileges**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the **SecurityLimitFlags** value is set to Filter Tokens you can delete privileges from a token. This property can be **NULL** if you do not want to delete privileges.

</dd> <dt>

**RestrictedSIDs**
</dt> <dd> <dl> <dt>

Data type: **Win32\_TokenGroups**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Deny-only security identifiers (SID) that are added to an access token, if the **SecurityLimitFlags** value is set to Filter Tokens. This property can be **NULL** if you do not want to specify deny-only SIDs.

</dd> <dt>

**SecurityLimitFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security limitations for a job. This property requires at least one of the following properties to be set: **SIDsToDisable**, **PrivilegesToDelete**, or **RestrictedSIDs**.

<dt>

<span id="No_Administrator"></span><span id="no_administrator"></span><span id="NO_ADMINISTRATOR"></span>

<span id="No_Administrator"></span><span id="no_administrator"></span><span id="NO_ADMINISTRATOR"></span>**No Administrator** (0)


</dt> <dd>

Prevents a process in a job from using a token that specifies the local administrators group.

</dd> <dt>

<span id="Restricted_Token"></span><span id="restricted_token"></span><span id="RESTRICTED_TOKEN"></span>

<span id="Restricted_Token"></span><span id="restricted_token"></span><span id="RESTRICTED_TOKEN"></span>**Restricted Token** (1)


</dt> <dd>

Prevents a process in a job from using a token that is not created with the [**CreateRestrictedToken**](https://msdn.microsoft.com/library/windows/desktop/aa446583) function.

</dd> <dt>

<span id="Specific_Token"></span><span id="specific_token"></span><span id="SPECIFIC_TOKEN"></span>

<span id="Specific_Token"></span><span id="specific_token"></span><span id="SPECIFIC_TOKEN"></span>**Specific Token** (2)


</dt> <dd>

Forces processes in a job to run under the specific user security token that owns the process.

</dd> <dt>

<span id="Filter_Tokens"></span><span id="filter_tokens"></span><span id="FILTER_TOKENS"></span>

<span id="Filter_Tokens"></span><span id="filter_tokens"></span><span id="FILTER_TOKENS"></span>**Filter Tokens** (3)


</dt> <dd>

Applies a filter to a token when a process impersonates a client.

</dd> </dl>

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (SettingID), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Instance of a job object security limit setting. Because they are kernel objects, job object names are case sensitive. However, Windows Management Instrumentation (WMI) keys are case insensitive and must specified to distinguish case. To indicate a capital letter, precede the letter by a backslash. For example, "A" and "a" are lowercase and "\\A" and "\\a" are uppercase.

</dd> <dt>

**SIDsToDisable**
</dt> <dd> <dl> <dt>

Data type: **Win32\_TokenGroups**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SIDs to disable for access checking, if the **SecurityLimitFlags** value is set to Filter Tokens. This property can be **NULL** if you do not want to disable SIDs.

</dd> </dl>

## Remarks

The **Win32\_NamedJobObjectSecLimitSetting** class is derived from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipjobj.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipjobj.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 




