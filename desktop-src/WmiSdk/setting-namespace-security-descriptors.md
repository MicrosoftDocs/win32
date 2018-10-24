---
Description: Both C++ applications and scripts running under a full administrator account can change a namespace security descriptor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d3e56b30-d5a8-446a-89aa-645b44a75af6
ms.tgt_platform: multiple
title: Setting Namespace Security Descriptors
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting Namespace Security Descriptors

Both C++ applications and scripts running under a full administrator account can change a namespace security descriptor.

## Namespace Security Descriptors

Each WMI namespace has a [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly), which allows each namespace to have unique security settings that determine who has access to the namespace data and methods. For more information about WMI access security, see [Access to WMI Securable Objects](access-to-wmi-securable-objects.md). [Access to WMI Namespaces](access-to-wmi-namespaces.md) describes the default security settings for WMI namespaces and security auditing in WMI.

You can set account permissions for each WMI namespace in the WMI (CIM) repository in the following ways:

-   When the namespace is created in the MOF file. For more information, see [Setting Namespace Security When the Namespace is Created](setting-namespace-security-when-the-namespace-is-created.md).
-   Manually, using the WMI Control. For more information, see [Setting Namespace Security with the WMI Control](setting-namespace-security-with-the-wmi-control.md).
-   Programmatically, by calling the methods of the [**\_\_SystemSecurity**](--systemsecurity.md) class.

The following methods of the [**\_\_SystemSecurity**](--systemsecurity.md) object associated with each namespace allow you to read or change security on a namespace.

<dl> <dt>

<span id="GetCallerAccessRights"></span><span id="getcalleraccessrights"></span><span id="GETCALLERACCESSRIGHTS"></span>[**GetCallerAccessRights**](--systemsecurity-getcalleraccessrights.md)
</dt> <dd>

Sets the *rights* parameter as a bitmap with each bit corresponding to an access right.

</dd> <dt>

<span id="GetSD"></span><span id="getsd"></span><span id="GETSD"></span>[**GetSD**](--systemsecurity-getsd.md)
</dt> <dd>

Gets the security descriptor for the namespace to which the user is connected. This method returns a security descriptor in binary byte array format. If you are writing a script, use the [**GetSecurityDescriptor**](getsecuritydescriptor-method-in-class---systemsecurity-.md) method.

</dd> <dt>

<span id="SetSD"></span><span id="setsd"></span><span id="SETSD"></span>[**SetSD**](--systemsecurity-setsd.md)
</dt> <dd>

Sets the security descriptor (SD) for the namespace to which a user is connected. This method requires a security descriptor in binary byte array format. If you are writing a script, use the [**SetSecurityDescriptor**](setsecuritydescriptor-method-in-class---systemsecurity.md) method.

</dd> <dt>

<span id="GetSecurityDescriptor"></span><span id="getsecuritydescriptor"></span><span id="GETSECURITYDESCRIPTOR"></span>[**GetSecurityDescriptor**](getsecuritydescriptor-method-in-class---systemsecurity-.md)
</dt> <dd>

Gets the security descriptor that controls access to the WMI namespace associated with the instance of [**\_\_SystemSecurity**](--systemsecurity.md). The security descriptor is returned as an instance of[**\_\_SecurityDescriptor**](--securitydescriptor.md).

</dd> <dt>

<span id="SetSecurityDescriptor"></span><span id="setsecuritydescriptor"></span><span id="SETSECURITYDESCRIPTOR"></span>[**SetSecurityDescriptor**](setsecuritydescriptor-method-in-class---systemsecurity.md)
</dt> <dd>

Writes an updated version of the security descriptor that controls access to the printer. The security descriptor is represented by an instance of [**\_\_SecurityDescriptor**](--securitydescriptor.md).

</dd> <dt>

<span id="Get9XUserList"></span><span id="get9xuserlist"></span><span id="GET9XUSERLIST"></span>[**Get9XUserList**](--systemsecurity-get9xuserlist.md)
</dt> <dd>

Gets the remote access rights for a list of individual users on computers running obsolete versions of Windows, where access control through Windows security descriptors is not available.

</dd> <dt>

<span id="Set9XUserList"></span><span id="set9xuserlist"></span><span id="SET9XUSERLIST"></span>[**Set9XUserList**](--systemsecurity-set9xuserlist.md)
</dt> <dd>

Sets the remote access rights for a list of individual users on computers running obsolete versions of Windows, where access control through Windows security descriptors is not available.

</dd> </dl>

If you are writing scripts, use the [**GetSecurityDescriptor**](getsecuritydescriptor-method-in-class---systemsecurity-.md) and [**SetSecurityDescriptor**](setsecuritydescriptor-method-in-class---systemsecurity.md). You can use the methods of the [**Win32\_SecurityDescriptorHelper**](https://msdn.microsoft.com/library/aa394403) class to alter the security descriptors.

If you are programming in C++, you can manipulate the binary security descriptor using [Security Descriptor Definition Language (SDDL)](https://msdn.microsoft.com/library/windows/desktop/aa379567), and the conversion methods [**ConvertSecurityDescriptorToStringSecurityDescriptor**](https://msdn.microsoft.com/library/windows/desktop/aa376397) and [**ConvertStringSecurityDescriptorToSecurityDescriptor**](https://msdn.microsoft.com/library/windows/desktop/aa376401).

Be aware that, starting with Windows Vista, [User Account Control](Http://go.microsoft.com/fwlink/p/?linkid=84440) (UAC) affects access to WMI data and what can be configured with the [*WMI Control*](gloss-w.md). For more information, see [User Account Control and WMI](user-account-control-and-wmi.md).

## Related topics

<dl> <dt>

[Securing WMI Namespaces](securing-wmi-namespaces.md)
</dt> <dt>

[WMI Security Constants](wmi-security-constants.md)
</dt> <dt>

[Access to WMI Namespaces](access-to-wmi-namespaces.md)
</dt> <dt>

[WMI Security Descriptor Objects](wmi-security-descriptor-objects.md)
</dt> </dl>

 

 



