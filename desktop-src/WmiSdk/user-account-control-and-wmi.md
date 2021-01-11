---
description: User Account Control (UAC) affects the WMI data that is returned from a command-line tool, remote access, and how scripts must run. For more information about UAC, see Getting Started with User Account Control.
ms.assetid: f6840aaa-834b-42c8-b641-01c570078fcb
ms.tgt_platform: multiple
title: User Account Control and WMI
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# User Account Control and WMI

User Account Control (UAC) affects the WMI data that is returned from a command-line tool, remote access, and how scripts must run. For more information about UAC, see [Getting Started with User Account Control](https://support.microsoft.com/help/922708/how-to-use-user-account-control-uac-in-windows-vista).

The following sections describe UAC functionality:

-   [User Account Control](#user-account-control-and-wmi)
-   [Account Needed to Run WMI Command-Line Tools](#account-needed-to-run-wmi-command-line-tools)
-   [Handling Remote Connections Under UAC](#handling-remote-connections-under-uac)
-   [UAC Effect on WMI Data Returned to Scripts or Applications](#uac-effect-on-wmi-data-returned-to-scripts-or-applications)
-   [Related topics](#related-topics)

## User Account Control

Under UAC, accounts in the local Administrators group have two [*access tokens*](/windows/desktop/SecGloss/a-gly), one with standard user privileges and one with administrator privileges. Because of UAC access token filtering, a script is normally run under the standard user token, unless it is run "as an Administrator" in elevated privilege mode. Not all scripts required administrative privileges.

Scripts cannot determine programmatically whether they are running under a standard user security token or an Administrator token. The script may fail with an access denied error. If the script requires administrator privileges, then it must be run in the elevated mode. Access to WMI namespaces differs depending on whether the script is run in elevated mode. Some WMI operations, such as getting data or executing most methods, do not require that the account run as an administrator. For more information about default access permissions, see [Access to WMI Namespaces](access-to-wmi-namespaces.md) and [Executing Privileged Operations](executing-privileged-operations.md).

Because of User Account Control, the account running the script must be in the Administrators group on the local computer to have the ability to run with elevated rights.

You can run a script or an application with elevated rights by performing one of the following methods:

**To Run a Script In Elevated Mode**

1.  Open a Command Prompt window by right-clicking Command Prompt in the Start menu and then clicking **Run as administrator**.
2.  Schedule the script to run elevated using Task Scheduler. For more information, see [Security Contexts for Running Tasks](/windows/desktop/TaskSchd/security-contexts-for-running-tasks).
3.  Run the script using the built-in Administrator account.

## Account Needed to Run WMI Command-Line Tools

To run the following [WMI Command-Line Tools](wmi-command-line-tools.md), your account must be in the Administrators group and the tool must be run from an elevated command prompt. The built-in administrator account can also run these tools.

-   [**mofcomp**](mofcomp.md)

-   [**wmic**](wmic.md)

    The first time you run Wmic after system installation, it must be run from an elevated command prompt. The elevated mode may not be required for subsequent executions of Wmic unless the WMI operations require administrator privilege.

-   [**winmgmt**](winmgmt.md)

-   [**wmiadap**](wmiadap.md)

To run the [*WMI Control*](gloss-w.md) (Wmimgmt.msc) and make changes to WMI namespace security or auditing settings, your account must have the Edit Security right explicitly granted or be in the local Administrators group. The built-in Administrator account can also change the security or auditing for a namespace.

Wbemtest.exe, a command-line tool that is not supported by Microsoft Customer Support services, can be run by accounts that are not in the local Administrators group, unless a specific operation requires privileges that are normally granted to Administrator accounts.

## Handling Remote Connections Under UAC

Whether you are connecting to a remote computer in a domain or in a workgroup determines whether UAC filtering occurs.

If your computer is part of a domain, connect to the target computer using a domain account that is in the local Administrators group of the remote computer. Then UAC access token filtering will not affect the domain accounts in the local Administrators group. Do not use a local, nondomain account on the remote computer, even if the account is in the Administrators group.

In a workgroup, the account connecting to the remote computer is a local user on that computer. Even if the account is in the Administrators group, UAC filtering means that a script runs as a standard user. A best practice is to create a dedicated local user group or user account on the target computer specifically for remote connections.

The security must be adjusted to be able to use this account because the account never has had administrative privileges. Give the local user:

-   Remote launch and activate rights to access DCOM. For more information, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).
-   Rights to access the WMI namespace remotely (Remote Enable). For more information, see [Access to WMI Namespaces](access-to-wmi-namespaces.md).
-   Right to access the specific securable object, depending on the security required by the object.

If you use a local account, either because you are in a workgroup or it is a local computer account, you may be forced to give specific tasks to a local user. For example, you can grant the user the right to stop or start a specific service through the SC.exe command, the [**GetSecurityDescriptor**](/windows/desktop/CIMWin32Prov/getsecuritydescriptor-method-in-class-win32-service) and [**SetSecurityDescriptor**](/windows/desktop/CIMWin32Prov/setsecuritydescriptor-method-in-class-win32-service) methods of [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service), or through Group Policy using Gpedit.msc. Some securable objects may not allow a standard user to perform tasks and offer no means to alter the default security. In this case, you may need to disable UAC so that the local user account is not filtered and instead becomes a full administrator. Be aware that for security reasons, disabling UAC should be a last resort.

Disabling Remote UAC by changing the registry entry that controls Remote UAC is not recommended, but may be necessary in a workgroup. The registry entry is **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Policies**\\**system**\\**LocalAccountTokenFilterPolicy**. When the value of this entry is zero (0), Remote UAC access token filtering is enabled. When the value is 1, remote UAC is disabled.

## UAC Effect on WMI Data Returned to Scripts or Applications

If a script or application is running under an account in the Administrators group, but not running with an elevated privilege, then you may not get all the data returned because this account is running as a standard user. The WMI [*providers*](gloss-p.md) for some classes do not return all instances to a standard user account or an Administrator account that is not running as a full administrator because of UAC filtering.

The following classes do not return some instances when the account is filtered by UAC:

-   [**Win32\_Bus**](/windows/desktop/CIMWin32Prov/win32-bus)
-   [**Win32\_Printer**](/windows/desktop/CIMWin32Prov/win32-printer)
-   [**Win32\_ComponentCategory**](/windows/desktop/CIMWin32Prov/win32-componentcategory)
-   [**Win32\_LogicalProgramGroupItem**](/windows/desktop/CIMWin32Prov/win32-logicalprogramgroupitem)
-   [**Win32\_LogicalProgramGroup**](/windows/desktop/CIMWin32Prov/win32-logicalprogramgroup)
-   [**Win32\_NetworkConnection**](/windows/desktop/CIMWin32Prov/win32-networkconnection)
-   [**Win32\_UserAccount**](/windows/desktop/CIMWin32Prov/win32-useraccount)
-   [**Win32\_PrinterDriver**](/windows/desktop/CIMWin32Prov/win32-printerdriver)
-   [**Win32\_PortResource**](/windows/desktop/CIMWin32Prov/win32-portresource)
-   [**Win32\_DeviceMemoryAddress**](/windows/desktop/CIMWin32Prov/win32-devicememoryaddress)

The following classes do not return some properties when the account is filtered by UAC:

-   [**Win32\_NetworkAdapterConfiguration**](/windows/desktop/CIMWin32Prov/win32-networkadapterconfiguration)
-   [**Win32\_DCOMApplicationSetting**](/windows/desktop/CIMWin32Prov/win32-dcomapplicationsetting)
-   [**Win32\_DCOMApplication**](/windows/desktop/CIMWin32Prov/win32-dcomapplication)
-   [**Win32\_Baseboard**](/windows/desktop/CIMWin32Prov/win32-baseboard)
-   [**Win32\_ComputerSystem**](/windows/desktop/CIMWin32Prov/win32-computersystem)
-   [**Win32\_NetworkAdapter**](/windows/desktop/CIMWin32Prov/win32-networkadapter)
-   [**Win32\_MotherboardDevice**](/windows/desktop/CIMWin32Prov/win32-motherboarddevice)
-   [**Win32\_DiskDrive**](/windows/desktop/CIMWin32Prov/win32-diskdrive)
-   [**Win32\_PnPEntity**](/windows/desktop/CIMWin32Prov/win32-pnpentity)
-   [**Win32\_VideoController**](/windows/desktop/CIMWin32Prov/win32-videocontroller)
-   [**Win32\_ParallelPort**](/windows/desktop/CIMWin32Prov/win32-parallelport)
-   [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk)
-   [**Win32\_SystemDriver**](/windows/desktop/CIMWin32Prov/win32-systemdriver)
-   [**Win32\_IRQResource**](/windows/desktop/CIMWin32Prov/win32-irqresource)
-   [**Win32\_NetworkProtocol**](/windows/desktop/CIMWin32Prov/win32-networkprotocol)

## Related topics

<dl> <dt>

[About WMI](about-wmi.md)
</dt> <dt>

[Access to WMI Securable Objects](access-to-wmi-securable-objects.md)
</dt> <dt>

[Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md)
</dt> </dl>

 

 
