---
description: WMI uses a standard Windows security descriptor to control access to WMI namespaces.
ms.assetid: 5cf9886c-04fa-480e-889f-b64a6a70d053
ms.tgt_platform: multiple
title: Access to WMI Namespaces
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Access to WMI Namespaces

WMI uses a standard Windows *security descriptor* to control access to WMI namespaces. When you connect to WMI, either through the WMI "winmgmts" moniker or a call to [**IWbemLocator::ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver) or [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md), you connect to a specific namespace.

The following information is discussed in this topic:

-   [WMI Namespace Security](#wmi-namespace-security)
-   [WMI Namespace Auditing](#wmi-namespace-auditing)
-   [Types of Namespace Events](#types-of-namespace-events)
-   [Namespace Access Settings](#namespace-access-settings)
-   [Default Permissions on WMI Namespaces](#default-permissions-on-wmi-namespaces)
-   [Related topics](#related-topics)

## WMI Namespace Security

WMI maintains namespace security by comparing the [*access token*](/windows/desktop/SecGloss/a-gly) of the user connecting to the namespace with the [*security descriptor*](/windows/desktop/SecGloss/s-gly) of the namespace. For more information about Windows security, see [Access to WMI Securable Objects](access-to-wmi-securable-objects.md).

Be aware that, starting with Windows Vista, [User Account Control (UAC)](https://www.microsoft.com/technet/windowsvista/security/uac.mspx) affects access to WMI data and what can be configured with the [*WMI Control*](gloss-w.md). For more information, see [Default Permissions on WMI Namespaces](#default-permissions-on-wmi-namespaces) and [User Account Control and WMI](user-account-control-and-wmi.md).

Access to WMI namespaces is also affected when the connection is from a remote computer. For more information, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md), [Securing a Remote WMI Connection](securing-a-remote-wmi-connection.md), and [Connecting Through Windows Firewall](/windows/desktop/WmiSdk/connecting-to-wmi-remotely-starting-with-vista).

Providers must rely on the impersonation setting for the connection to determine if the client script or application should receive data. For more information about script and client applications, see [Setting Client Application Process Security](setting-client-application-process-security.md). For more information about [*provider*](gloss-p.md) impersonation, see [Developing a WMI Provider](developing-a-wmi-provider.md).

## WMI Namespace Auditing

WMI uses the namespace [*System access control lists (SACL)*](/windows/desktop/SecGloss/s-gly) to audit namespace activity. To enable auditing of WMI namespaces, use the **Security** tab on the [*WMI Control*](gloss-w.md) to change the auditing settings for the namespace.

Auditing is not enabled during the installation of the operating system. To enable auditing, click the **Auditing** tab in the standard **Security** window. Then you can add an auditing entry.

Group Policy for the local computer must be set to allow auditing. You can enable auditing by running the Gpedit.msc MMC snap-in and setting **Audit Object Access** under **Computer Configuration** > **Windows Settings** > **Security Settings** > **Local Policies** > **Audit Policy**.

An auditing entry edits the SACL of the namespace. When you add an auditing entry, it is either a user, group, computer, or built-in security principal. After adding the entry, you can set the access operations that result in Security Log events. For example, for the group Authenticated Users, you can click Execute Methods. This setting results in Security Log events whenever a member of the Authenticated Users group executes a method in that namespace. The Event ID for WMI events is 4662.

Your account must be in the Administrators group and running under elevated privilege to change the auditing settings. The built-in Administrator account can also change the security or auditing for a namespace. For more information about running in elevated mode, see [User Account Control and WMI](user-account-control-and-wmi.md).

WMI auditing generates success or failure events for attempts to access WMI namespaces. The service does not audit the success or failure of provider operations. For example, when a script connects to WMI and a namespace, it may fail because the account under which the script is running does not have access to that the namespace or may attempt an operation, such as editing the DACL, that is not granted.

If you are running under an account in the Administrators group, you can view the namespace auditing events in the **Event Viewer** user interface.

## Types of Namespace Events

WMI traces the following types of events in the Security Event Log:

-   Audit Success

    The operation must successfully complete two steps for an Audit Success. First, WMI grants access to the client application or script based on the client SID and the namespace DACL. Second, the requested operation matches the access rights in the namespace SACL for that user or group.

-   Audit Failure

    WMI denies access to the namespace, but the requested operation matches the access rights in the namespace SACL for that user or group.

## Namespace Access Settings

You can view the namespace access rights for various accounts on the WMI Control. These constants are described in [**Namespace Access Rights Constants**](namespace-access-rights-constants.md). You can change the access to a WMI namespace using the WMI Control or programmatically. For more information, see [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md).

WMI audits changes in all of the access permissions listed in the following list except for the Remote Enable permission. The changes are logged as audit success or failure corresponding to the Edit Security permission.

<dl> <dt>

<span id="Execute_Methods"></span><span id="execute_methods"></span><span id="EXECUTE_METHODS"></span>Execute Methods
</dt> <dd>

Permits the user to execute methods defined on WMI classes. Corresponds to the **WBEM\_METHOD\_EXECUTE** access permission constant.

</dd> <dt>

<span id="Full_Write"></span><span id="full_write"></span><span id="FULL_WRITE"></span>Full Write
</dt> <dd>

Permits full read, write, and delete access to WMI classes and class instances, both static and dynamic. Corresponds to the **WBEM\_FULL\_WRITE\_REP** access permission constant.

</dd> <dt>

<span id="Partial_Write"></span><span id="partial_write"></span><span id="PARTIAL_WRITE"></span>Partial Write
</dt> <dd>

Permits write access to static WMI class instances. Corresponds to the **WBEM\_PARTIAL\_WRITE\_REP** access permission constant.

</dd> <dt>

<span id="Provider_Write"></span><span id="provider_write"></span><span id="PROVIDER_WRITE"></span>Provider Write
</dt> <dd>

Permits write access to dynamic WMI class instances. Corresponds to the **WBEM\_WRITE\_PROVIDER** access permission constant.

</dd> <dt>

<span id="Enable_Account"></span><span id="enable_account"></span><span id="ENABLE_ACCOUNT"></span>Enable Account
</dt> <dd>

Permits read access to WMI class instances. Corresponds to the **WBEM\_ENABLE** access permission constant.

</dd> <dt>

<span id="Remote_Enable"></span><span id="remote_enable"></span><span id="REMOTE_ENABLE"></span>Remote Enable
</dt> <dd>

Permits access to the namespace by remote computers. Corresponds to the **WBEM\_REMOTE\_ACCESS** access permission constant.

</dd> <dt>

<span id="Read_Security"></span><span id="read_security"></span><span id="READ_SECURITY"></span>Read Security
</dt> <dd>

Permits read-only access to DACL settings. Corresponds to the **READ\_CONTROL** access permission constant.

</dd> <dt>

<span id="Edit_Security"></span><span id="edit_security"></span><span id="EDIT_SECURITY"></span>Edit Security
</dt> <dd>

Permits write access to DACL settings. Corresponds to the **WRITE\_DAC** access permission constant.

</dd> </dl>

## Default Permissions on WMI Namespaces

The default security groups are:

-   Authenticated Users
-   LOCAL SERVICE
-   NETWORK SERVICE
-   Administrators (on the local computer)

The default access permissions for the Authenticated Users, LOCAL SERVICE, and NETWORK SERVICE are:

-   Execute Methods
-   Full Write
-   Enable Account

Accounts in the Administrators group have all rights available to them, including editing security descriptors. However, because of User Account Control (UAC), the WMI Control or the script must be running at elevated security. For more information, see [User Account Control and WMI](user-account-control-and-wmi.md).

Sometimes a script or application must enable an administrator privilege, such as **SeSecurityPrivilege**, to carry out an operation. For example, a script can execute the [**GetSecurityDescriptor**](/windows/desktop/CIMWin32Prov/getsecuritydescriptor-method-in-class-win32-printer) method of the [**Win32\_Printer**](/windows/desktop/CIMWin32Prov/win32-printer) class without **SeSecurityPrivilege** and get the security information in the [*discretionary access control list (DACL)*](/windows/desktop/SecGloss/d-gly) of the printer object [*security descriptor*](/windows/desktop/SecGloss/s-gly). However, the SACL information is not returned to the script unless the **SeSecurityPrivilege** privilege is available and enabled for the account. If the account does not have the privilege available, then it cannot be enabled. For more information, see [Executing Privileged Operations](executing-privileged-operations.md).

## Related topics

<dl> <dt>

[About WMI](about-wmi.md)
</dt> </dl>

 

 
