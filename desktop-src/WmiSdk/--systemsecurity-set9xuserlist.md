---
description: Sets the remote access rights for a list of individual users on computers running obsolete versions of Windows, where access control through Windows security descriptors is not available.
ms.assetid: f6da65d3-86dd-4fc8-b4c0-f7ddc8536d4e
ms.tgt_platform: multiple
title: '__SystemSecurity::Set9XUserList method'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __SystemSecurity.Set9XUserList
api_type: 
- COM
api_location: 
- all
---

# \_\_SystemSecurity::Set9XUserList method

The **\_\_SystemSecurity::Set9XUserList** method sets the remote access rights for a list of individual users on computers running obsolete versions of Windows, where access control through Windows security descriptors is not available.

The list is specified as an array of embedded objects where each object is an instance of the [**\_\_NTLMUser9X**](--ntlmuser9x.md) class. This functions similar to the security descriptor, but it is more limited. Groups are not supported and there is no control over local access, because the local user always has full access. Both deny and allow access control entries (ACE) are permitted, and because of this, the ACE order is important in the discretionary access control list (DACL). For more information, see [Order of ACEs in a DACL](/windows/desktop/SecAuthZ/order-of-aces-in-a-dacl).

## Syntax


```C++
HRESULT Set9XUserList(
  [in] __NTLMUser9X ul[]
);
```



## Parameters

<dl> <dt>

*ul* \[in\]
</dt> <dd>

Array of users.

</dd> </dl>

## Return value

This method returns an **HRESULT** that indicates the status of the method call. The following list lists the return values that are of significance to **Set9XUserList**. For scripting and Visual Basic applications, the result can be obtained from [OutParameters.ReturnValue](parsing-outparameters-objects.md). For more information, see [Constructing InParameters Objects and Parsing OutParameters Objects](constructing-inparameters-objects-and-parsing-outparameters-objects.md).

<dl> <dt>

**WBEM\_E\_METHOD\_DISABLED**
</dt> <dd>

This method is not supported.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
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

[**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace)
</dt> <dt>

[**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor)
</dt> <dt>

[Securing WMI Namespaces](securing-wmi-namespaces.md)
</dt> <dt>

[WMI Security Constants](wmi-security-constants.md)
</dt> </dl>

 

