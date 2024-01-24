---
description: Contains methods that let you access and modify the security settings for a namespace.
ms.assetid: a54fdd85-feb8-4727-9f26-fe4f213cab6b
ms.tgt_platform: multiple
title: __SystemSecurity class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- __SystemSecurity
api_type:
- Schema
api_location:
- All
---

# \_\_SystemSecurity class

The **\_\_SystemSecurity** system class contains methods that let you access and modify the security settings for a namespace. The **\_\_SystemSecurity** class is a singleton class in each namespace.

> [!Note]  
> For more information, see [Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __SystemSecurity
{
};
```

## Members

The **\_\_SystemSecurity** class has these types of members:

-   [Methods](#methods)

### Methods

The **\_\_SystemSecurity** class has these methods.




| Method | Description | 
|--------|-------------|
| [**Get9XUserList**](--systemsecurity-get9xuserlist.md) | Gets a list of users who are allowed remote access.<br> **Note:** This method does not work on supported versions of Windows. Use [**GetSD**](--systemsecurity-getsd.md) instead.<br> | 
| <a href="--systemsecurity-getcalleraccessrights.md"><strong>GetCallerAccessRights</strong></a> | Returns a mask with each bit that corresponds to an access right.<br /> | 
| <a href="--systemsecurity-getsd.md"><strong>GetSD</strong></a> | Gets the <a href="/windows/desktop/api/winnt/ns-winnt-security_descriptor"><strong>SECURITY_DESCRIPTOR</strong></a> for the namespace to which the user is connected.<br /> | 
| <a href="getsecuritydescriptor-method-in-class---systemsecurity-.md"><strong>GetSecurityDescriptor</strong></a> | Gets the security descriptor that controls access to the WMI namespace associated with the instance of <strong>__SystemSecurity</strong>. The security descriptor is returned as an instance of<a href="--securitydescriptor.md"><strong>__SecurityDescriptor</strong></a>.<br /> | 
| [**Set9XUserList**](--systemsecurity-set9xuserlist.md) | Sets a list of users who are allowed remote access.<br> **Note:** This method does not work on supported versions of Windows. Use [**SetSD**](--systemsecurity-setsd.md) instead.<br> | 
| <a href="--systemsecurity-setsd.md"><strong>SetSD</strong></a> | Sets the security descriptor for the namespace to which the user is connected.<br /> | 
| <a href="setsecuritydescriptor-method-in-class---systemsecurity.md"><strong>SetSecurityDescriptor</strong></a> | Writes an updated version of the security descriptor that controls access to the printer. The security descriptor is represented by an instance of <a href="--securitydescriptor.md"><strong>__SecurityDescriptor</strong></a>.<br /> | 




 

## Remarks

You can require that client scripts and applications use an encrypted connection for authentication by adding the **RequiresEncryption** qualifier to the .mof file that creates the namespace. You can also modify an existing namespace by adding this attribute and compile the .mof file again. For more information about how to use **RequiresEncryption**, see [Requiring an Encrypted Connection to a Namespace](requiring-an-encrypted-connection-to-a-namespace.md).

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

[WMI Security Constants](wmi-security-constants.md)
</dt> <dt>

[WMI Security Descriptor Objects](wmi-security-descriptor-objects.md)
</dt> <dt>

[Securing WMI Namespaces](securing-wmi-namespaces.md)
</dt> <dt>

[Establishing Inheritance of Namespace Security](establishing-inheritance-of-namespace-security.md)
</dt> <dt>

[Access Control Lists (ACLs)](/windows/desktop/SecAuthZ/access-control-lists)
</dt> <dt>

[**Security\_Descriptor**](/windows/desktop/api/winnt/ns-winnt-security_descriptor)
</dt> </dl>

