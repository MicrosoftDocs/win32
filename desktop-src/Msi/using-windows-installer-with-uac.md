---
description: Windows Installer complies with User Account Control (UAC) in Windows Vista.
ms.assetid: 13955ded-6b7f-475f-bb0f-6530a0b4963f
title: Using Windows Installer with UAC
ms.topic: article
ms.date: 05/31/2018
---

# Using Windows Installer with UAC

Windows Installer complies with [*User Account Control*](u-gly.md) (UAC) in Windows Vista. With authorization from an administrator, the Windows Installer can install applications or patches on behalf of a user that may not be a member of the Administrators group. This is referred to as an [*elevated*](e-gly.md) installation because the Windows Installer makes changes to the system on behalf of the user that would not normally be allowed if the user were making the changes directly.

-   When using Windows Vista in a corporate environment, applications can be designated as managed applications. Using application deployment and [Group Policy](/previous-versions/windows/desktop/Policy/group-policy-start-page), administrators can lockdown directories and then assign or publish the managed applications in those directories to [*standard users*](s-gly.md) for install, repair, or removal. Managed applications are registered in the **HKEY\_LOCAL\_MACHINE** registry hive. Once an application has been registered as a managed application, subsequent installation operations always run with elevated privileges. If the user is running as an administrator, no prompting is required to continue the installation. If the user is running as a standard user, and the application has already been assigned or published, the installation of the managed application can continue without prompting.
-   When using Windows Vista in a non-corporate environment, UAC handles the elevation of application installation. Windows Installer 4.0 can call to the [*Application Information Service*](a-gly.md) (AIS) to request administrator authorization to elevate an installation. Before an installation identified as requiring administrator privileges can be run, UAC prompts the user for consent to elevate the installation. The consent prompt is displayed by default, even if the user is a member of the local Administrators group, because administrators run as standard users until an application or system component that requires administrative credential requests permission to run. This user experience is called [*Admin Approval Mode*](a-gly.md) (AAM). If a standard user attempts to install the application, the user has to get a person with administrator privilege to provide them their administrator credentials to continue the installation. This user experience is called an [*Over the Shoulder*](o-gly.md) (OTS) credential prompt.
-   Because UAC restricts privileges during the stages of an installation, developers of Windows Installer packages should not assume that their installation will always have access to all parts of the system. Windows Installer package developers should therefore adhere to the package guidelines described in [Guidelines for Packages](guidelines-for-packages.md) to ensure their package works with UAC and Windows Vista. A package that has been authored and tested to comply with UAC should contain the [**MSIDEPLOYMENTCOMPLIANT**](msideploymentcompliant.md) property set to 1.
-   An administrator can also use the methods described in the section: [Installing a Package with Elevated Privileges for a Non-Admin](installing-a-package-with-elevated-privileges-for-a-non-admin.md) to enable a non-administrator user to install an application with elevated system privileges.
-   Privileges are required to install an application in the per-user-managed context, and therefore subsequent Windows Installer reinstallations or repairs of the application are also performed by the installer using elevated privileges. This means that only patches from trusted sources can be applied to an application in the per-user-managed state. Beginning with Windows Installer 3.0, you can apply a patch to a per-user managed application after the patch has been registered as having elevated privileges. For information see [Patching Per-User Managed Applications](patching-per-user-managed-applications.md).

> [!Note]  
> When elevated privileges are not required to install a Windows Installer package, the author of the package can suppress the dialog box that UAC displays to prompt users for administrator authorization. For more information, see [Authoring Packages without the UAC Dialog Box](authoring-packages-without-the-uac-dialog-box.md).

 

 

 
