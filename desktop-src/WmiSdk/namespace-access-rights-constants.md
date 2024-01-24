---
description: WMI has security constants used for namespace access checking by \_\_SystemSecurity::GetCallerAccessRights.
ms.assetid: 2e905078-d510-4417-8acb-a6ff535d9d0b
ms.tgt_platform: multiple
title: Namespace Access Rights Constants (Wbemcli.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WBEM_ENABLE
- WBEM_METHOD_EXECUTE
- WBEM_FULL_WRITE_REP
- WBEM_PARTIAL_WRITE_REP
- WBEM_WRITE_PROVIDER
- WBEM_REMOTE_ACCESS
api_type: 
- HeaderDef
api_location: 
- Wbemcli.h
---

# Namespace Access Rights Constants

WMI has security constants used for namespace access checking by [**\_\_SystemSecurity::GetCallerAccessRights**](--systemsecurity-getcalleraccessrights.md). For security information about access control lists (ACLs, DACLs, or SACLs), see [Access Control Lists (ACLs)](/windows/desktop/SecAuthZ/access-control-lists) and [**Standard Access Rights**](/windows/desktop/SecAuthZ/standard-access-rights). These constants are defined in the **WBEM\_SECURITY\_FLAGS** enumeration.

<dl> <dt>

<span id="WBEM_ENABLE"></span><span id="wbem_enable"></span>**WBEM\_ENABLE**
</dt> <dd> <dl> <dt>

1 (0x1)
</dt> <dt>



Enables the account and grants the user read permissions. This is a default access right for all users and corresponds to the Enable Account permission on the Security tab of the [*WMI Control*](gloss-w.md). For more information, see [Setting Namespace Security with the WMI Control](setting-namespace-security-with-the-wmi-control.md).


</dt> </dl> </dd> <dt>

<span id="WBEM_METHOD_EXECUTE"></span><span id="wbem_method_execute"></span>**WBEM\_METHOD\_EXECUTE**
</dt> <dd> <dl> <dt>

2 (0x2)
</dt> <dt>



Allows the execution of methods. Providers can perform additional access checks. This is a default access right for all users and corresponds to the Execute Methods permission on the Security tab of the WMI Control.


</dt> </dl> </dd> <dt>

<span id="WBEM_FULL_WRITE_REP"></span><span id="wbem_full_write_rep"></span>**WBEM\_FULL\_WRITE\_REP**
</dt> <dd> <dl> <dt>

4 (0x4)
</dt> <dt>



Allows a user account to write to classes in the WMI repository as well as instances. A user cannot write to system classes. Only members of the Administrators group have this permission. **WBEM\_FULL\_WRITE\_REP** corresponds to the Full Write permission on the Security tab of the WMI Control.


</dt> </dl> </dd> <dt>

<span id="WBEM_PARTIAL_WRITE_REP"></span><span id="wbem_partial_write_rep"></span>**WBEM\_PARTIAL\_WRITE\_REP**
</dt> <dd> <dl> <dt>

8 (0x8)
</dt> <dt>



Allows you to write data to instances only, not classes. A user cannot write classes to the [*WMI repository*](gloss-w.md). Only members of the Administrators group have this right. **WBEM\_PARTIAL\_WRITE\_REP** corresponds to the Partial Write permission on the Security tab of the WMI Control.


</dt> </dl> </dd> <dt>

<span id="WBEM_WRITE_PROVIDER"></span><span id="wbem_write_provider"></span>**WBEM\_WRITE\_PROVIDER**
</dt> <dd> <dl> <dt>

16 (0x10)
</dt> <dt>



Allows writing classes and instances to providers. Note that providers can do additional access checks when impersonating a user. This is a default access right for all users and corresponds to the Provider Write permission on the Security tab of the WMI Control.


</dt> </dl> </dd> <dt>

<span id="WBEM_REMOTE_ACCESS"></span><span id="wbem_remote_access"></span>**WBEM\_REMOTE\_ACCESS**
</dt> <dd> <dl> <dt>

32 (0x20)
</dt> <dt>



Allows a user account to remotely perform any operations allowed by the permissions described above. Only members of the Administrators group have this right. **WBEM\_REMOTE\_ACCESS** corresponds to the Remote Enable permission on the Security tab of the WMI Control.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl> |



## See also

<dl> <dt>

[WMI Security Constants](wmi-security-constants.md)
</dt> <dt>

[Securing WMI Namespaces](securing-wmi-namespaces.md)
</dt> <dt>

[Access to WMI Namespaces](access-to-wmi-namespaces.md)
</dt> <dt>

[WMI Security Descriptor Objects](wmi-security-descriptor-objects.md)
</dt> <dt>

[Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md)
</dt> </dl>

 

