---
description: Starting with Windows Vista, many securable objects have methods for getting or setting the security descriptor. With appropriate permissions, you can read or change security descriptors on securable objects.
ms.assetid: da660e7e-f32d-4b7d-b979-f7b482a73fa2
ms.tgt_platform: multiple
title: Changing Access Security on Securable Objects
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Changing Access Security on Securable Objects

Printers, services, registry keys, DCOM applications, and WMI namespaces are securable objects. The access to securable objects is protected by [*security descriptors*](/windows/desktop/SecGloss/s-gly), which specify the users who have access. Starting with Windows Vista, many securable objects have methods for getting or setting the security descriptor. With appropriate permissions, you can read or change security descriptors on securable objects. Using these methods, you can control which user accounts or groups have access to a printer, service, WMI namespace, or other object. For more information about security descriptors and their use in WMI, see [Access to WMI Securable Objects](access-to-wmi-securable-objects.md).

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

    Starting with Windows Vista, you can secure registry keys so that they cannot be changed by unauthorized users. The [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class has the [**GetSecurityDescriptor**](/previous-versions/windows/desktop/regprov/getsecuritydescriptor-method-in-class-stdregprov) and [**SetSecurityDescriptor**](/previous-versions/windows/desktop/regprov/setsecuritydescriptor-method-in-class-stdregprov) methods. These methods return and write [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) objects.

-   Printers

    Starting with Windows Vista, you can secure access to instances of the [**Win32\_Printer**](/windows/desktop/CIMWin32Prov/win32-printer) class using the [**GetSecurityDescriptor**](/windows/desktop/CIMWin32Prov/getsecuritydescriptor-method-in-class-win32-printer) and [**SetSecurityDescriptor**](/windows/desktop/CIMWin32Prov/setsecuritydescriptor-method-in-class-win32-printer) methods. These methods return and write [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) objects.

-   Services

    Starting with Windows Vista, you can secure access to instances of the [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) class using the [**GetSecurityDescriptor**](/windows/desktop/CIMWin32Prov/getsecuritydescriptor-method-in-class-win32-service) and [**SetSecurityDescriptor**](/windows/desktop/CIMWin32Prov/setsecuritydescriptor-method-in-class-win32-service) methods. These methods return and write [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) objects.

-   DCOM applications

    DCOM application instances have several security descriptors. Starting with Windows Vista, use methods of the [**Win32\_DCOMApplicationSetting**](/windows/desktop/CIMWin32Prov/win32-dcomapplicationsetting) class to get or change the various security descriptors. Security descriptors are returned as instances of the [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) class.

    To get or change the configuration permissions, call the [**GetConfigurationSecurityDescriptor**](/windows/desktop/CIMWin32Prov/getconfigurationsecuritydescriptor-method-in-class-win32-dcomapplicationsetting) or [**SetConfigurationSecurityDescriptor**](/windows/desktop/CIMWin32Prov/setconfigurationsecuritydescriptor-method-in-class-win32-dcomapplicationsetting) methods.

    To get or change the access permissions, call the [**GetAccessSecurityDescriptor**](/windows/desktop/CIMWin32Prov/getaccesssecuritydescriptor-method-in-class-win32-dcomapplicationsetting) or [**SetAccessSecurityDescriptor**](/windows/desktop/CIMWin32Prov/setaccesssecuritydescriptor-method-in-class-win32-dcomapplicationsetting) methods.

    To get or change the startup and activation permissions, call the [**GetLaunchSecurityDescriptor**](/windows/desktop/CIMWin32Prov/getlaunchsecuritydescriptor-in-class-win32-dcomapplicationsetting) or [**SetLaunchSecurityDescriptor**](/windows/desktop/CIMWin32Prov/setlaunchsecuritydescriptor-method-in-class-win32-dcomapplicationsetting) methods,

-   Files

    The [**GetSecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/getsecuritydescriptor-method-in-class-win32-logicalfilesecuritysetting) and [**SetSecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/setsecuritydescriptor-method-in-class-win32-logicalfilesecuritysetting) methods are in the [**Win32\_LogicalFileSecuritySetting**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalfilesecuritysetting) class, rather than in the [**CIM\_DataFile**](/windows/desktop/CIMWin32Prov/cim-datafile) class.

-   Shares

    The [**GetSecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/getsecuritydescriptor-method-in-class-win32-logicalsharesecuritysetting) and [**SetSecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/setsecuritydescriptor-method-in-class-win32-logicalsharesecuritysetting) methods are in the [**Win32\_LogicalShareSecuritySetting**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalsharesecuritysetting) class, rather than in the [**Win32\_Share**](/windows/desktop/CIMWin32Prov/win32-share) class.

> [!Note]  
> When a new [*Security Access Control List (SACL)*](/windows/desktop/SecGloss/s-gly) is not specified in a call to a **SetSecurityDescriptor** method, then the security descriptor SACL on the target securable object is set to **NULL** so that the previous SACL setting does not persist.

 

## Converting Between Security Descriptor Formats

Security descriptors are complex binary byte arrays that must normally be created and changed in C++. After you have used one of the Get methods to obtain the security descriptor, the [**Win32\_SecurityDescriptorHelper**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptorhelper) class supplies methods that convert security descriptors into either [Security Descriptor Definition Language (SDDL)](/windows/desktop/SecAuthZ/security-descriptor-definition-language) or to [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) instances.

You can manipulate the Access Control Lists (ACL) more easily in [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) instances or in SDDL. For more information about the structure and use of security descriptors in WMI, see [WMI Security Descriptor Objects](wmi-security-descriptor-objects.md).

In C++ or C# use conversion functions to convert binary security descriptors to [Security Descriptor Definition Language (SDDL)](/windows/desktop/SecAuthZ/security-descriptor-definition-language). To modify security descriptor values in C++ applications, use [**ConvertSecurityDescriptorToStringSecurityDescriptor**](/windows/desktop/api/sddl/nf-sddl-convertsecuritydescriptortostringsecuritydescriptora) and [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora).

## Security Issues

It is recommended that changes to security descriptors be done with great caution so that the security of the object is not compromised. Be aware that the order of access control entries (ACEs) in a discretionary access control list (DACL) can affect access security. For more information, see [Order of ACEs in a DACL](/windows/desktop/SecAuthZ/order-of-aces-in-a-dacl).

## Related topics

<dl> <dt>

[WMI Security Descriptor Objects](wmi-security-descriptor-objects.md)
</dt> <dt>

[Security Descriptor Helper Class](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptorhelper)
</dt> <dt>

[Security Best Practices](/windows/desktop/SecBP/best-practices-for-the-security-apis)
</dt> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> <dt>

[Access Control](/windows/desktop/SecAuthZ/access-control)
</dt> <dt>

[Access to WMI Namespaces](access-to-wmi-namespaces.md)
</dt> </dl>

 

 
