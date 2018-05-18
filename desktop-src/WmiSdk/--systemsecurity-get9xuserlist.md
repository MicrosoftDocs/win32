---
Description: 'Gets the remote access rights for a list of individual users on computers running obsolete versions of Windows , where access control through Windows security descriptors is not available.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '79a596db-5f85-4664-8989-f309286eca0d'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: '\_\_SystemSecurity::Get9XUserList method'
---

# \_\_SystemSecurity::Get9XUserList method

The [**\_\_SystemSecurity::Set9XUserList**](--systemsecurity-set9xuserlist.md) method gets the remote access rights for a list of individual users on computers running obsolete versions of Windows , where access control through Windows security descriptors is not available.

This functions similar to the security descriptor, but it is more limited. Groups are not supported and there is no control over local access, because the local user always has full access. Both deny and allow access control entries (ACE) are permitted, and because of this, the ACE order is important in the discretionary access control list (DACL). For more information, see [Order of ACEs in a DACL](https://msdn.microsoft.com/library/windows/desktop/aa379298).

## Syntax


```C++
HRESULT Get9XUserList(
  [out] __NTLMUser9X ul[]
);
```



## Parameters

<dl> <dt>

*ul* \[out\]
</dt> <dd>

Array of users.

</dd> </dl>

## Return value

This method returns an **HRESULT** that indicates the status of the method call. The following list lists the return values that are of significance to **Get9XUserList**. For scripting and Visual Basic applications, the result can be [OutParameters.ReturnValue](parsing-outparameters-objects.md). For more information, see [Constructing InParameters Objects and Parsing OutParameters Objects](constructing-inparameters-objects-and-parsing-outparameters-objects.md).

<dl> <dt>

**WBEM\_E\_METHOD\_DISABLED**
</dt> <dd>

This method is not supported on supported versions of Windows.

</dd> </dl>

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | all WMI namespaces<br/>  |



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

[**Win32\_ACE**](https://msdn.microsoft.com/library/aa394063)
</dt> <dt>

[**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402)
</dt> <dt>

[Securing WMI Namespaces](securing-wmi-namespaces.md)
</dt> <dt>

[WMI Security Constants](wmi-security-constants.md)
</dt> </dl>

 

 




