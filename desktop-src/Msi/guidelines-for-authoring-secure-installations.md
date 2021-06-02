---
description: To help maintain a secure environment during software installation, adhere to these guidelines when authoring the Windows Installer package.
ms.assetid: 04d91a9b-0528-4acb-8e11-fc817009db1f
title: Guidelines for Authoring Secure Installations
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Authoring Secure Installations

Adherence to the following guidelines when authoring a Windows Installer package helps maintain a secure environment during installation:

-   Administrators should install managed applications into a target installation folder for which non-admin users do not have change or modify privileges.
-   Make any property set by the user a public property. Private properties cannot be changed by the user interacting with the user interface. For information, see [About Properties](about-properties.md).
-   Do not use properties for passwords or other information that must remain secure. The installer may write the value of a property authored into the [Property table](property-table.md), or created at run time, into a log or the system registry. For additional information, see [Preventing Confidential Information from Being Written into the Log File](preventing-confidential-information-from-being-written-into-the-log-file.md).
-   When the installation requires the installer to use [*elevated*](e-gly.md) privileges, use [Restricted Public Properties](restricted-public-properties.md) to restrict the public properties a user can change. Some restrictions are commonly necessary to maintain a secure environment when the installation requires the installer to use *elevated* privileges.
-   Avoid installing services that impersonate the privileges of a particular user because this may write security data into a log or the system registry. This creates potential for a security problem, password conflict, or the loss of configuration data when the system is restarted. For details, see [ServiceInstall table](serviceinstall-table.md).
-   Use the [LockPermissions table](lockpermissions-table.md) and [MsiLockPermissionsEx table](msilockpermissionsex-table.md) to secure services, files, registry keys, and created folders in a locked-down environment.
-   Add a digital signatures to the installation to ensure the integrity of the files. For details, see [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md) and [Authoring a Fully Verified Signed Installation](authoring-a-fully-verified-signed-installation.md).
-   Author your Windows Installer package such that if the user is denied access to resources, the setup fails in a manner that maintains a secure environment. Check the user's access privileges and determine whether there is sufficient disk space before installation begins. Commonly, the installer should only display a browse dialog box if the current user is an administrator or if the installation does not require [*elevated*](e-gly.md) privileges. For details, see [Source Resiliency](source-resiliency.md).
-   Use [Secured Transforms](secured-transforms.md) to store transforms in a secure file system locally on the user's computer. This prevents the user from having write access to the transform.
-   For information on how to secure media sources of managed applications, see [Source Resiliency](source-resiliency.md).
-   Use the [**Security Summary**](security-summary.md) Property to indicate whether the package should be opened as read-only. This property should be set to read-only recommended for an installation database and to read-only enforced for a transform or patch.
-   The installer runs custom actions with user privileges by default in order to limit the access of custom actions to the system. The installer may run custom actions with [*elevated*](e-gly.md) privileges if a managed application is being installed or if the system policy has been specified for elevated privileges. For details, see [Custom Action Security](custom-action-security.md).
-   Use the [DisablePatch](disablepatch.md) policy to provide security in environments where patching must be restricted.
-   Use the [AppId table](appid-table.md) to register common security and configuration settings for DCOM objects.
-   For related information, see [Guidelines for Securing Custom Actions](guidelines-for-securing-custom-actions.md).
-   For related information, see [Guidelines for Securing Packages on Locked-Down Computers](guidelines-for-securing-packages-on-locked-down-computers.md).
-   Starting with Windows Installer 3.0, [User Account Control (UAC) Patching](user-account-control--uac--patching.md) enables non-administrator users to patch applications installed in the per-machine context. UAC patching is enabled by providing a signer certificate in the [MsiPatchCertificate](msipatchcertificate-table.md) table and signing patches with the same certificate.
-   The capability of the Windows Installer 5.0 to set access permissions on services, files, created folders, and registry entries can help make installation applications more secure. For information, see [Securing Resources](securing-resources-.md).

 

 



