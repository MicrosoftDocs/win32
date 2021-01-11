---
description: Sets the rights parameter as a bitmap with each bit corresponding to an access right.
ms.assetid: f28391a8-2b34-4234-bf1a-4688726b0b4b
ms.tgt_platform: multiple
title: GetCallerAccessRights method of the __SystemSecurity class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __SystemSecurity.GetCallerAccessRights
api_type: 
- COM
api_location: 
- All
---

# GetCallerAccessRights method of the \_\_SystemSecurity class

The **\_\_SystemSecurity::GetCallerAccessRights** method sets the *rights* parameter as a bitmap with each bit corresponding to an access right. Any client can call this to determine which rights the client has. This method is useful for clients that enable or disable features. For example, a GUI application might disable a button if the currently logged-on user does not have method execution rights.

Any enabled client has the right to call **GetCallerAccessRights**, even if that client does not have general method execution rights.

## Syntax


```mof
HRESULT GetCallerAccessRights(
  [out] sint32 rights
);
```



## Parameters

<dl> <dt>

*rights* \[out\]
</dt> <dd>

Access rights of the client. For more information, see [**\_\_SystemSecurity**](--systemsecurity.md) and [WMI Security Constants](wmi-security-constants.md).

<dt>

<span id="WBEM_ENABLE"></span><span id="wbem_enable"></span>

<span id="WBEM_ENABLE"></span><span id="wbem_enable"></span>**WBEM\_ENABLE** (1 (0x1))


</dt> <dd>

Enables the account and grants the user read permissions. This is the default access right for all users.

</dd> <dt>

<span id="WBEM_METHOD_EXECUTE"></span><span id="wbem_method_execute"></span>

<span id="WBEM_METHOD_EXECUTE"></span><span id="wbem_method_execute"></span>**WBEM\_METHOD\_EXECUTE** (2 (0x2))


</dt> <dd>

Allows the execution of methods.

> [!Note]  
> Providers may perform additional access checks.

 

</dd> <dt>

<span id="WBEM_FULL_WRITE_REP"></span><span id="wbem_full_write_rep"></span>

<span id="WBEM_FULL_WRITE_REP"></span><span id="wbem_full_write_rep"></span>**WBEM\_FULL\_WRITE\_REP** (4 (0x4))


</dt> <dd>

Allows the caller, security context, or user to write to classes and instances except for system classes.

</dd> <dt>

<span id="WBEM_PARTIAL_WRITE_REP"></span><span id="wbem_partial_write_rep"></span>

<span id="WBEM_PARTIAL_WRITE_REP"></span><span id="wbem_partial_write_rep"></span>**WBEM\_PARTIAL\_WRITE\_REP** (8 (0x8))


</dt> <dd>

Allows the caller, security context, or user to write provider instances but not static classes or static instances to the repository.

</dd> <dt>

<span id="WBEM_WRITE_PROVIDER"></span><span id="wbem_write_provider"></span>

<span id="WBEM_WRITE_PROVIDER"></span><span id="wbem_write_provider"></span>**WBEM\_WRITE\_PROVIDER** (16 (0x10))


</dt> <dd>

Allows the caller, security context, or user to write classes and instances to providers.

> [!Note]  
> Impersonating providers may do additional access checks.

 

</dd> <dt>

<span id="WBEM_REMOTE_ACCESS"></span><span id="wbem_remote_access"></span>

<span id="WBEM_REMOTE_ACCESS"></span><span id="wbem_remote_access"></span>**WBEM\_REMOTE\_ACCESS** (32 (0x20))


</dt> <dd>

Allows a user account to remotely perform any operations allowed by the permissions set by other bits.

</dd> <dt>

<span id="READ_CONTROL"></span><span id="read_control"></span>

<span id="READ_CONTROL"></span><span id="read_control"></span>**READ\_CONTROL** (131072 (0x20000))


</dt> <dd>

Allows read access to the security descriptors.

</dd> <dt>

<span id="WRITE_DAC"></span><span id="write_dac"></span>

<span id="WRITE_DAC"></span><span id="write_dac"></span>**WRITE\_DAC** (262144 (0x40000))


</dt> <dd>

Allows write access to discretionary access control lists (DACL).

</dd> </dl> </dd> </dl>

## Return value

This method returns an **HRESULT** that indicates the status of the method call. The following list lists the return values that are of significance to [**Set9XUserList**](--systemsecurity-set9xuserlist.md). For scripting and Visual Basic applications, the result can be obtained from [OutParameters.ReturnValue](parsing-outparameters-objects.md). For more information, see [Constructing InParameters Objects and Parsing OutParameters Objects](constructing-inparameters-objects-and-parsing-outparameters-objects.md).

<dl> <dt>

**WBEM\_E\_METHOD\_DISABLED**
</dt> <dd>

This method is not supported on supported versions of Windows.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[**\_\_SystemSecurity**](--systemsecurity.md)
</dt> <dt>

[**\_\_SystemSecurity::GetSD**](--systemsecurity-getsd.md)
</dt> <dt>

[**\_\_SystemSecurity::SetSD**](--systemsecurity-setsd.md)
</dt> <dt>

[WMI Security Constants](wmi-security-constants.md)
</dt> <dt>

[**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace)
</dt> <dt>

[**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor)
</dt> <dt>

[Securing WMI Namespaces](securing-wmi-namespaces.md)
</dt> <dt>

WMI Security Constants
</dt> </dl>

 

