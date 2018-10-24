---
Description: Starting with Windows Vista, many securable objects have methods for getting or setting the security descriptor. With appropriate permissions, you can read or change security descriptors on securable objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: da660e7e-f32d-4b7d-b979-f7b482a73fa2
ms.tgt_platform: multiple
title: Changing Access Security on Securable Objects
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Changing Access Security on Securable Objects

Printers, services, registry keys, DCOM applications, and WMI namespaces are securable objects. The access to securable objects is protected by [*security descriptors*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly), which specify the users who have access. Starting with Windows Vista, many securable objects have methods for getting or setting the security descriptor. With appropriate permissions, you can read or change security descriptors on securable objects. Using these methods, you can control which user accounts or groups have access to a printer, service, WMI namespace, or other object. For more information about security descriptors and their use in WMI, see [Access to WMI Securable Objects](access-to-wmi-securable-objects.md).

The following sections are discussed in this topic:

-   [Objects and Security Descriptor Methods](#objects-and-security-descriptor-methods)
-   [Converting Between Security Descriptor Formats](#converting-between-security-descriptor-formats)
-   [Security Issues](#security-issues)
-   [Related topics](#related-topics)

## Objects and Security Descriptor Methods

The following list contains the methods that securable objects have to enable you to read or change the security descriptor:

-   WMI Namespaces

    A provider can establish security that only allows certain groups to have access to the data in a WMI namespace. Namespace security is controlled by methods on the [**\_\_SystemSecurity**](--systemsecurity.md) class. Starting with Windows Vista, the [**GetSecurityDescriptor**](getsecuritydescriptor-method-in-class---systemsecurity-.md) and [**SetSecurityDescriptor**](setsecuritydescriptor-method-in-class---systemsecurity.md) methods return and write [**\_\_SecurityDescriptor**](--securitydescriptor.md) objects. For more information, see [Setting Namespace Security Descriptors](setting-namespace-security-descriptors.md).

-   Registry keys

    Starting with Windows Vista, you can secure registry keys so that they cannot be changed by unauthorized users. The [**StdRegProv**](https://msdn.microsoft.com/library/aa393664) class has the [**GetSecurityDescriptor**](https://msdn.microsoft.com/library/aa390771) and [**SetSecurityDescriptor**](https://msdn.microsoft.com/library/aa393591) methods. These methods return and write [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) objects.

-   Printers

    Starting with Windows Vista, you can secure access to instances of the [**Win32\_Printer**](https://msdn.microsoft.com/library/aa394363) class using the [**GetSecurityDescriptor**](https://msdn.microsoft.com/library/aa390778) and [**SetSecurityDescriptor**](https://msdn.microsoft.com/library/aa393594) methods. These methods return and write [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) objects.

-   Services

    Starting with Windows Vista, you can secure access to instances of the [**Win32\_Service**](https://msdn.microsoft.com/library/aa394418) class using the [**GetSecurityDescriptor**](https://msdn.microsoft.com/library/aa390785) and [**SetSecurityDescriptor**](https://msdn.microsoft.com/library/aa393596) methods. These methods return and write [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) objects.

-   DCOM applications

    DCOM application instances have several security descriptors. Starting with Windows Vista, use methods of the [**Win32\_DCOMApplicationSetting**](https://msdn.microsoft.com/library/aa394118) class to get or change the various security descriptors. Security descriptors are returned as instances of the [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) class.

    To get or change the configuration permissions, call the [**GetConfigurationSecurityDescriptor**](https://msdn.microsoft.com/library/aa390441) or [**SetConfigurationSecurityDescriptor**](https://msdn.microsoft.com/library/aa393287) methods.

    To get or change the access permissions, call the [**GetAccessSecurityDescriptor**](https://msdn.microsoft.com/library/aa390439) or [**SetAccessSecurityDescriptor**](https://msdn.microsoft.com/library/aa393283) methods.

    To get or change the startup and activation permissions, call the [**GetLaunchSecurityDescriptor**](https://msdn.microsoft.com/library/aa390457) or [**SetLaunchSecurityDescriptor**](https://msdn.microsoft.com/library/aa393309) methods,

-   Files

    The [**GetSecurityDescriptor**](https://msdn.microsoft.com/library/aa390773) and [**SetSecurityDescriptor**](https://msdn.microsoft.com/library/aa393592) methods are in the [**Win32\_LogicalFileSecuritySetting**](https://msdn.microsoft.com/library/aa394180) class, rather than in the [**CIM\_DataFile**](https://msdn.microsoft.com/library/aa387236) class.

-   Shares

    The [**GetSecurityDescriptor**](https://msdn.microsoft.com/library/aa390774) and [**SetSecurityDescriptor**](https://msdn.microsoft.com/library/aa393593) methods are in the [**Win32\_LogicalShareSecuritySetting**](https://msdn.microsoft.com/library/aa394188) class, rather than in the [**Win32\_Share**](https://msdn.microsoft.com/library/aa394435) class.

> [!Note]  
> When a new [*Security Access Control List (SACL)*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) is not specified in a call to a **SetSecurityDescriptor** method, then the security descriptor SACL on the target securable object is set to **NULL** so that the previous SACL setting does not persist.

 

## Converting Between Security Descriptor Formats

Security descriptors are complex binary byte arrays that must normally be created and changed in C++. After you have used one of the Get methods to obtain the security descriptor, the [**Win32\_SecurityDescriptorHelper**](https://msdn.microsoft.com/library/aa394403) class supplies methods that convert security descriptors into either [Security Descriptor Definition Language (SDDL)](https://msdn.microsoft.com/library/windows/desktop/aa379567) or to [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) instances.

You can manipulate the Access Control Lists (ACL) more easily in [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) instances or in SDDL. For more information about the structure and use of security descriptors in WMI, see [WMI Security Descriptor Objects](wmi-security-descriptor-objects.md).

In C++ or C# use conversion functions to convert binary security descriptors to [Security Descriptor Definition Language (SDDL)](https://msdn.microsoft.com/library/windows/desktop/aa379567). To modify security descriptor values in C++ applications, use [**ConvertSecurityDescriptorToStringSecurityDescriptor**](https://msdn.microsoft.com/library/windows/desktop/aa376397) and [**ConvertStringSecurityDescriptorToSecurityDescriptor**](https://msdn.microsoft.com/library/windows/desktop/aa376401).

## Security Issues

It is recommended that changes to security descriptors be done with great caution so that the security of the object is not compromised. Be aware that the order of access control entries (ACEs) in a discretionary access control list (DACL) can affect access security. For more information, see [Order of ACEs in a DACL](https://msdn.microsoft.com/library/windows/desktop/aa379298).

## Related topics

<dl> <dt>

[WMI Security Descriptor Objects](wmi-security-descriptor-objects.md)
</dt> <dt>

[Security Descriptor Helper Class](https://msdn.microsoft.com/library/aa394403)
</dt> <dt>

[Security Best Practices](https://msdn.microsoft.com/library/windows/desktop/ms717796)
</dt> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> <dt>

[Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860)
</dt> <dt>

[Access to WMI Namespaces](access-to-wmi-namespaces.md)
</dt> </dl>

 

 



