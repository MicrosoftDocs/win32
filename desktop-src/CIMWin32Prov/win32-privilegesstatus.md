---
description: The Win32\_PrivilegesStatus&\#8194;WMI class reports information about privileges required to complete an operation. It may be returned when an operation failed or when a partially populated instance has been returned.
ms.assetid: 295ec2bd-7996-4031-8503-d4e869d8368d
ms.tgt_platform: multiple
title: Win32_PrivilegesStatus class (CIMWin32 WMI Providers)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PrivilegesStatus
- Win32_PrivilegesStatus.Description
- Win32_PrivilegesStatus.Operation
- Win32_PrivilegesStatus.ParameterInfo
- Win32_PrivilegesStatus.ProviderName
- Win32_PrivilegesStatus.StatusCode
- Win32_PrivilegesStatus.PrivilegesNotHeld
- Win32_PrivilegesStatus.PrivilegesRequired
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32_PrivilegesStatus class (CIMWin32 WMI Providers)

The **Win32\_PrivilegesStatus** [WMI class](../wmisdk/retrieving-a-class.md) reports information about privileges required to complete an operation. It may be returned when an operation failed or when a partially populated instance has been returned.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{BE46D060-7A7C-11d2-BC85-00104B2CF71C}"), AMENDMENT]
class Win32_PrivilegesStatus : __ExtendedStatus
{
  string Description;
  string Operation;
  string ParameterInfo;
  string ProviderName;
  uint32 StatusCode;
  string PrivilegesNotHeld[];
  string PrivilegesRequired[];
};
```

## Members

The **Win32\_PrivilegesStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PrivilegesStatus** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Any user-defined string that describes an error or operational status.

This property is inherited from [**\_\_ExtendedStatus**](../wmisdk/--extendedstatus.md).

</dd> <dt>

**Operation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Operation that takes place at the time of a failure or anomaly. Typically, Windows Management Instrumentation (WMI) sets this property to the name of a COM API for WMI method such as the following: [**IWbemServices::CreateInstanceEnum**](/windows/win32/api/wbemcli/nf-wbemcli-iwbemservices-createinstanceenum).

This property is inherited from [**\_\_ExtendedStatus**](../wmisdk/--extendedstatus.md).

</dd> <dt>

**ParameterInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Parameters involved in an error or status change. For example, if an application attempts to retrieve a class that does not exist, this property is set to the offending class name.

This property is inherited from [**\_\_ExtendedStatus**](../wmisdk/--extendedstatus.md).

</dd> <dt>

**PrivilegesNotHeld**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|AccessControl\|Windows NT Privileges")
</dt> </dl>

Listing required access privileges missing to complete an operation. The types of access privileges can be found under the Windows Privileges.

Example: "SE\_SHUTDOWN\_NAME"

</dd> <dt>

**PrivilegesRequired**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|AccessControl\|Windows NT Privileges")
</dt> </dl>

Listing of all of the privileges required to perform an operation. This includes values from the **PrivilegesNotHeld** property.

Example: "SE\_SHUTDOWN\_NAME"

</dd> <dt>

**ProviderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the provider that causes or reports an error or status change. If a provider is not involved, this string is set to "Windows Management".

This property is inherited from [**\_\_ExtendedStatus**](../wmisdk/--extendedstatus.md).

</dd> <dt>

**StatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains an error or information code for an operation. This can be any value defined by the provider, but the value 0 (zero) is usually reserved to indicate success.

This property is inherited from [**\_\_NotifyStatus**](../wmisdk/--notifystatus.md).

</dd> </dl>

## Remarks

The **Win32\_PrivilegesStatus** class is derived from [**\_\_ExtendedStatus**](../wmisdk/--extendedstatus.md).

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

[**\_\_ExtendedStatus**](../wmisdk/--extendedstatus.md)
</dt> </dl>

 

 
