---
description: 'This section enumerates a list of tips, linked to the main Windows Installer SDK documentation, to help Application Developers, Setup Authors, IT Professionals, and Infrastructure Developers discover best practices for using the Windows Installer:'
ms.assetid: ff48d995-fe6f-4d1b-898d-67574ed3c5b7
title: Windows Installer Best Practices
ms.topic: article
ms.date: 05/31/2018
---

# Windows Installer Best Practices

This section enumerates a list of tips, linked to the main Windows Installer SDK documentation, to help Application Developers, Setup Authors, IT Professionals, and Infrastructure Developers discover best practices for using the Windows Installer:

-   [Update the Windows Installer version.](#update-the-windows-installer-version)
-   [Meet the Windows Logo certification requirements.](#meet-the-windows-logo-certification-requirements)
-   [Prepare the package for localization.](#prepare-the-package-for-localization)
-   [Update your Windows Installer development tools and documentation.](#update-your-windows-installer-development-tools-and-documentation)
-   [If you decide to repackage a legacy setup application, follow good repackaging practices.](#if-you-decide-to-repackage-a-legacy-setup-application-follow-good-repackaging-practices)
-   [Do not try to replace protected resources.](#do-not-try-to-replace-protected-resources)
-   [Do not depend upon non-critical resources.](#do-not-depend-upon-non-critical-resources)
-   [Use the API to retrieve Windows Installer configuration information.](#use-the-api-to-retrieve-windows-installer-configuration-information)
-   [Organize the installation of your application around components.](#organize-the-installation-of-your-application-around-components)
-   [Reduce the size of large Windows Installer packages.](#reduce-the-size-of-large-windows-installer-packages)
-   [If you use custom actions, follow good custom action practices.](#if-you-use-custom-actions-follow-good-custom-action-practices)
-   [If you use assemblies, follow good assembly practices](#if-you-use-assemblies-follow-good-assembly-practices)
-   [Do not ship concurrent installations.](#do-not-ship-concurrent-installations)
-   [Keep package names and package codes consistent.](#keep-package-names-and-package-codes-consistent)
-   [Do not use the SelfReg and TypeLib tables.](#do-not-use-the-selfreg-and-typelib-tables)
-   [Provide the option to install without a user interface.](#provide-the-option-to-install-without-a-user-interface)
-   [Avoid using the AlwaysInstallElevated policy.](#avoid-using-the-alwaysinstallelevated-policy)
-   [Enable the DisableMedia policy to limit unauthorized installation.](#enable-the-disablemedia-policy-to-limit-unauthorized-installation)
-   [Keep the original package source files secure and available to users.](#keep-the-original-package-source-files-secure-and-available-to-users)
-   [Enable verbose logging on user's computer when troubleshooting deployment.](#enable-verbose-logging-on-users-computer-when-troubleshooting-deployment)
-   [Uninstallation leaves the user's computer in a clean state.](#uninstallation-leaves-the-users-computer-in-a-clean-state)
-   [Test packages for both per-user and per-machine installation deployment.](#test-packages-for-both-per-user-and-per-machine-installation-deployment)
-   [Plan and test a servicing strategy before shipping the application.](#plan-and-test-a-servicing-strategy-before-shipping-the-application)
-   [Reduce the dependency of updates upon the original sources.](#reduce-the-dependency-of-updates-upon-the-original-sources)
-   [Do not distribute unserviceable merge modules.](#do-not-distribute-unserviceable-merge-modules)
-   [Avoid patching administrative installations.](#avoid-patching-administrative-installations)
-   [Register updates to run with elevated privilege.](#register-updates-to-run-with-elevated-privilege)
-   [Use the MsiPatchSequence Table to sequence patches.](#use-the-msipatchsequence-table-to-sequence-patches)
-   [Test the installation package thoroughly.](#test-the-installation-package-thoroughly)
-   [Fix all validation errors before deploying a new or revised installation package.](#fix-all-validation-errors-before-deploying-a-new-or-revised-installation-package)
-   [Author a secure installation.](#author-a-secure-installation)
-   [Use PMSIHANDLE instead of HANDLE](#use-pmsihandle-instead-of-handle)

## Update the Windows Installer version.

-   Use Windows Installer 5.0 on Windows Server 2008 R2 and Windows 7. This is the Windows Installer version provided with the operating system.
-   Use Windows Installer 4.5 on Windows Server 2008, Windows Server 2003 with Service Pack 1 (SP1), Windows Vista with Service Pack 1 (SP1), or Windows XP with Service Pack 2 (SP2). For information about obtaining the latest Windows Installer version, see [Windows Installer Redistributables](windows-installer-redistributables.md).
-   Use Windows Installer 3.1 on Windows 2000 with Service Pack 3 (SP3). Windows Installer version 3.1 has features that facilitate better application servicing and [patching](patching.md).
-   Many important features were introduced with version 3.0 and are listed in the section [Not Supported in Windows Installer Version 2.0](not-supported-in-windows-installer-version-2-0.md). Installation packages and updates that were created for Windows Installer 2.0 can be installed using Windows Installer 3.0 and later. Patch packages that contain the new tables used by Windows Installer 3.0 can still be applied using earlier versions of Windows Installer but without the Windows Installer 3.0 patching functionality. It is also possible to author patches that explicitly require the Windows Installer 3.0 that cannot be applied by earlier versions of Windows Installer. If a user is unable to update the installer version, ensure that your application or update will be compatible with a future update of the Windows Installer.
-   For a list of the Windows Installer features not supported by earlier versions of the Windows installer see [What's New in Windows Installer](what-s-new-in-windows-installer.md).

## Meet the Windows Logo certification requirements.

-   Even if you do not intend to submit your application to the logo program, following the logo certification guidelines can help make your Windows Installer package better. For an overview of the logo requirements, and links to specific logo certification programs, see [Windows Installer and Logo Requirements](windows-installer-and-logo-requirements.md).

## Prepare the package for localization.

-   It is a good practice to prepare for future localization when authoring the original installation package. You can follow the suggested package localization procedure in [Localizing a Windows Installer Package](localizing-a-windows-installer-package.md).

## Update your Windows Installer development tools and documentation.

-   The [Windows Installer Development Tools](windows-installer-development-tools.md) are not redistributable, and you should only use the versions of these tools available from Microsoft. These are available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md) in the Microsoft Windows Software Development Kit (SDK).
-   Several independent software vendors offer tools to create or modify Windows Installer packages. These tools can provide a package authoring environment that may be easier to use than the tools provided in the Windows Installer SDK. You can learn more about these tools from the information resources discussed in [Other Sources of Windows Installer Information](other-sources-of-windows-installer-information.md).
-   The capability to build a package from text files may be more intuitive for some developers. The Windows Installer XML (WiX) toolset available on [Sourceforge.net](https://sourceforge.net/projects/wix) builds Windows installation packages from XML source code.
-   The documentation in the [Windows Installer SDK](./windows-installer-portal.md) released in the MSDN Online Library is updated the most frequently.
-   Use the recent version of [Msizap.exe](msizap-exe.md) (version 3.1.4000.2726 or greater) that is available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md) for Windows Vista or greater. Lesser versions of Msizap.exe can remove information about all updates that have been applied to other applications on the user's computer. If this information is removed, these other applications may need to be removed and reinstalled to receive additional updates.
-   The database table editor [Orca.exe](orca-exe.md) is a database table editor for creating and editing Windows Installer packages and merge modules. It has a basic GUI interface but supports advanced editing of Windows Installer databases. Even if you use another application as your primary development tool, you may find using Orca.exe is convenient when troubleshooting and testing a package.
-   See [Other Sources of Windows Installer Information](other-sources-of-windows-installer-information.md) for current Windows Installer information available in blogs, technical chats, newsgroups, technical articles, and websites.

## If you decide to repackage a legacy setup application, follow good repackaging practices.

Many application vendors provide native Windows Installer packages for the installation or their products. Software that converts an existing legacy setup application into a Windows Installer package is referred to as a repackaging tool. Repackaging an existing setup application is not the best development practice. Applications that have been designed from the start to take advantage of Windows Installer features can be easier for users to install and service. If you decide to use a repackaging software the following practices can help you produce a better Windows Installer package.

-   Repackaging tools convert legacy installations into a Windows Installer package by taking a picture of a staging system before and after installation. Any registry changes, file changes, or system setting that occurs during the capture process is included in the installation. Configure the hardware and software of the computer used to repackage the installation as close as possible to the intended user's system. Create a separate package for each different hardware configuration. Repackage using a clean staging computer. Remove any unnecessary applications. Stop all unnecessary processes. Close all non-essential system services.
-   Always make a copy of the original installation before starting to work on it. Always work on the copy. Never stop a repackager before it finishes building the package. If the repackager damages the package you will still have the original.
-   Do not repackage Microsoft software updates into a Windows Installer package. Microsoft releases software updates, such as service packs, as self-extracting files that automatically runs installation. These updates use different installers than the Windows Installer to replace protected Windows resources and cannot be converted into a Windows Installer package. For information about how to deploy Windows service packs, see the service pack's deployment guide on [Microsoft TechNet](https://technet.microsoft.com/).
-   Do not use a repackaging tool to convert a Windows Installer package into a new package. The Windows Installer adds configuration information to the system as well as application resources. When a repackaging tool compares the system before and after the installation, the repackager misinterprets the configuration information as part of the application. This usually damages the repackaged application. Instead use [customization transforms](a-customization-transform-example.md) to modify an existing Windows Installer package, or make an new package. You can create customization transforms using the [Msitran.exe](msitran-exe.md) tool.
-   Do not use a repackaging tool to consolidate several Windows Installer packages into a single package. Instead you can use the [Msistuff.exe](msistuff-exe.md) tool to configure the Setup.exe bootstrap executable to install the packages one after another.
-   Make your Windows Installer package so that it can be easily customized by the customer. Global variables used by the Windows Installer during an installation can be set using public [properties](properties.md) or [customization transforms](a-customization-transform-example.md). Provide documentation for the use of those properties and practical default values for all customizable values. For information about getting and setting properties see [Using Properties](using-properties.md). For an example of a customization transform see [A Customization Transform Example](a-customization-transform-example.md).

## Do not try to replace protected resources.

Windows Installer packages should not attempt to replace protected resources during installation or update. The Windows Installer does not remove or replace these resources because Windows prevents the replacement of essential system files, folders, and registry keys. Protecting these resources prevents application and operating system failures.

-   When running on Windows Server 2008 or Windows Vista, the Windows Installer skips the installation of any file or registry key that is protected by [Windows Resource Protection](../wfp/windows-resource-protection-portal.md) (WRP), the installer enters a warning in the log file, and continues with the remainder of the installation without an error. For information, see [Using Windows Installer and Windows Resource Protection](windows-resource-protection-on-windows-vista.md).
-   WRP is the new name for Windows File Protection (WFP). WRP protects registry keys and folders as well as essential system files. In Windows Server 2003, Windows XP, and Windows 2000, when the Windows Installer encountered a WFP-protected file, the installer would request that WFP install the file. For information, see [Using Windows Installer and Windows Resource Protection](windows-resource-protection-on-windows-vista.md).

## Do not depend upon non-critical resources.

Your installation or update should not depend upon the installation of non-critical resources for the following reasons.

-   Custom actions can fail if they depend upon a component belonging to a feature that the user advertises rather than installs.
-   Custom actions sequenced before the [InstallFinalize](installfinalize-action.md) action can fail if they depend on a component containing an assembly that is being installed. The Windows Installer does not commit assemblies to the Global Assembly Cache (GAC) until the InstallFinalize action completes.

## Use the API to retrieve Windows Installer configuration information.

The installation of your application or update should not depend upon direct access to Windows Installer configuration information saved on your computer. Instead use the Windows Installer application programming interface to retrieve configuration information. The location and format of configuration information is managed by the Windows Installer service and can change.

-   The Installation and Configuration Functions of the Windows Installer API are described in the [Installer Function Reference](installer-function-reference.md).
-   The [Configuration Properties](property-reference.md) are described in the Property Reference.
-   The automation methods and properties are described in the [Automation Interface Reference](automation-interface-reference.md). The sample script WiLstPrd.vbs connects to an Installer object and enumerates registered products and product information. For information see [List Products, Properties, Features, and Components](list-products-properties-features-and-components.md).

## Organize the installation of your application around components.

The Windows Installer service installs or removes collections of resources referred to as [components](windows-installer-components.md). Because components are commonly shared, the author of an installation package must follow rules when specifying the components of a feature or application.

-   Adhere to the component rules when [Organizing Applications into Components](organizing-applications-into-components.md) to ensure that new components, or new versions of components, can be installed and removed without damaging other applications. You can follow the procedure described in [Defining Installer Components](defining-installer-components.md).
-   The installer tracks every component by the respective component ID GUID specified in the [Component table](component-table.md). It is essential for the operation of the Windows Installer reference-counting mechanism that the component ID GUID is correct. Follow the guidelines in [Changing the Component Code](changing-the-component-code.md).
-   If your package must break the component rules, be aware of the possible consequences and ensure that your installation never installs these components where they may damage components on the user's system. For information see [What happens if the component rules are broken?](what-happens-if-the-component-rules-are-broken.md).
-   Be aware how the Windows Installer applies the [File Versioning Rules](file-versioning-rules.md) when [Replacing Existing Files](replacing-existing-files.md). The Windows Installer first determines whether the component's key file is already installed before attempting to install any of the files of the component. If the installer finds a file with the same name as the component's key file installed in the target location, it compares the version, date, and language of the two key files and uses file versioning rules to determine whether to install the component provided by the package. If the installer determines it needs to replace the component base upon the key file, then it uses the file versioning rules on each installed file to determine whether to replace the file.

## Reduce the size of large Windows Installer packages.

Very large Windows Packages take system resources and can be difficult for users to install. It is good practice to reduce the size of very large Windows Installer Packages by the following methods.

-   Compress the files in the installation and store them in a cabinet (.cab) file . The Installer allows the .cab file to be stored as a separate external file, or as a data stream in the MSI package itself. For information see [Using Cabinets and Compressed Sources](using-cabinets-and-compressed-sources.md).
-   Remove wasted storage space in the .msi file using one of the options discussed in [Reducing the Size of an .msi File](reducing-the-size-of-an--msi-file.md).
-   If your Windows Installer package contains more than 32767 files, you must change the schema of the database. For information see [Authoring a Large Package](authoring-a-large-package.md).

## If you use custom actions, follow good custom action practices.

The Windows Installer has many built-in [standard actions](standard-actions-reference.md) for the installation and maintenance of applications. Developers should attempt to rely upon the standard actions as much as practical, rather than create their own [custom actions](custom-actions.md). However, there are situations where the developer of an installation package finds it necessary to write a custom action.

-   Follow the guidelines for [Using Custom Actions](using-custom-actions.md).
-   Follow the [Guidelines for Securing Custom Actions](guidelines-for-securing-custom-actions.md). Custom actions that use sensitive information should not write this information into the log. For information see [Custom Action Security](custom-action-security.md).
-   Custom Actions must not attempt to set a System Restore entry point from within a custom action. For information see [Setting a restore point from a Custom Action](setting-a-restore-point-from-a-custom-action.md).
-   Return error messages from custom actions and write them to the log to facilitate troubleshooting custom actions. For information see [Error Message Custom Actions](error-message-custom-actions.md) and [Returning Error Messages from Custom Actions](returning-error-messages-from-custom-actions.md).
-   Do not change the system state from an immediate custom action. Custom actions that change the system directly or call another system service must be deferred to the time when the installation script is executed. Every [deferred execution custom action](deferred-execution-custom-actions.md) that changes the system state must be preceded by a [rollback custom action](rollback-custom-actions.md) to undo the system state change on an installation rollback. For information see [Changing the System State Using a Custom Action](changing-the-system-state-using-a-custom-action.md).
-   Custom actions that perform complex installation operations should be an [executable file](executable-files.md) or [dynamic-link library](dynamic-link-libraries.md). Limit the use of custom actions based on [scripts](scripts.md) to simple installation operations.
-   Make the details of what your custom action does to the system easily discoverable to system administrators. Put the details of registry entries and files used by your custom action into a custom table and have the custom action read from this table. This is demonstrated by the example in [Using a Custom Action to Create User Accounts on a Local Computer](using-a-custom-action-to-create-user-accounts-on-a-local-computer.md). For information on adding custom tables to a database, see [Working with Queries](working-with-queries.md) and [Examples of Database Queries Using SQL and Script](examples-of-database-queries-using-sql-and-script.md).
-   A custom actions should not display a dialog box. Custom actions requiring a user interface can use the [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) function instead. See [Sending Messages to Windows Installer Using MsiProcessMessage](sending-messages-to-windows-installer-using-msiprocessmessage.md).
-   Custom actions must not use any of the functions listed on the page: [Functions Not for Use in Custom Actions](functions-not-for-use-in-custom-actions.md).
-   If the installation is intended to run on a terminal server, test that all your custom actions are capable of running on a terminal server. For more information see [**TerminalServer**](terminalserver.md) property.
-   To have a custom action run when a particular patch is uninstalled the custom action must either be present in the original application or be in a patch for the product that is always applied. For more information see [Patch Uninstall Custom Actions](patch-uninstall-custom-actions.md).
-   Custom actions should not use the UI level as a condition for sending error messages to the installer because this can interfere with logging and external messages. For information see [Determining UI Level from a Custom Action](determining-ui-level-from-a-custom-action.md).
-   Use conditional statements and [Conditional Statement Syntax](conditional-statement-syntax.md) to ensure that your package correctly runs custom actions, does not run a custom actions, or runs alternate custom action when the package is uninstalled. Test that the package works as expected when [uninstalling custom actions](uninstalling-custom-actions.md). For information see [Conditioning Actions to Run During Removal](conditioning-actions-to-run-during-removal.md)
-   If the installation must be capable of being run by users that do not have administrator privileges, test to ensure that all the custom actions can be run with non-administrator privileges. Custom actions require elevated privileges to modify parts of the system that are not user specific. The installer may run custom actions with elevated privileges if a managed application is being installed or if the system policy has been specified for elevated privileges. Any custom actions the require elevated privileges must include the msidbCustomActionTypeInScript and msidbCustomActionTypeNoImpersonate [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md) in the custom action type. This is demonstrated by the example in [Using a Custom Action to Create User Accounts on a Local Computer](using-a-custom-action-to-create-user-accounts-on-a-local-computer.md).

## If you use assemblies, follow good assembly practices

If your package uses software [assemblies](assemblies.md), follow the guidelines for [Adding Assemblies to a Package](adding-assemblies-to-a-package.md), [Updating Assemblies](updating-assemblies.md), and [Installing and Removing Assemblies](installing-and-removing-assemblies.md).

## Do not ship concurrent installations.

[Concurrent Installations](concurrent-installations.md), also called Nested Installations, install another Windows Installer package during a currently running installation. The use of concurrent installations is not a good practice because they are difficult for customers to service. Patching and upgrading may not work with concurrent installations. The recommended alternative to using concurrent installations is to instead use a setup application and external UI handler to install several Windows Installer packages sequentially.

For more information about using an external UI handler see [Monitoring an Installation Using MsiSetExternalUI](monitoring-an-installation-using-msisetexternalui.md). For more information about using a record-based external handler, see [Monitoring an Installation Using MsiSetExternalUIRecord](monitoring-an-installation-using-msisetexternaluirecord.md).

Concurrent installations are sometimes used in controlled corporate environments to install applications that are not intended for the public. Follow these guidelines if you decide to use concurrent installations.

-   Do not use concurrent installations to install or update a shipping product.
-   Concurrent installations should not share components.
-   An administrative installation should not contain a concurrent installation.
-   Integrated ProgressBars should not be used with concurrent installations.
-   Resources that are to be advertised should not be installed by a concurrent installation.
-   A package that performs a concurrent installation of an application should also uninstall the concurrent application when the parent product is uninstalled. A nested installation exists under the context of the parent product in the Add/Remove Programs in Control Panel.

## Keep package names and package codes consistent.

The .msi file can be given any name that helps users identify the package, but the name should not be changed without also changing the product code.

-   Give your .msi file a user-friendly name that enables the user to identify the contents of the Windows Installer package.
-   The [product code](product-codes.md) is the principal identification of an application and must change whenever there is a comprehensive update to the application. For information, see [**ProductCode**](productcode.md) and [Changing the Product Code](changing-the-product-code.md). Changing the name of the application's .msi file is considered a comprehensive change and always requires a corresponding change of the product code to maintain consistency.
-   The [package code](package-codes.md) is the primary identifier used by the installer to search for and validate the correct package for a given installation. No two nonidentical .msi files should ever have the same package code. If a package is changed without changing the package code, the installer may not use the newer package if both are still accessible to the installer. The package code is stored in the [**Revision Number Summary**](revision-number-summary.md) Property of the [Summary Information Stream](summary-information-stream.md).
-   Note that letters in product code and package code [GUIDs](guid.md) must all be uppercase.

## Do not use the SelfReg and TypeLib tables.

-   Installation package authors are strongly advised against using self registration and the [SelfReg](selfreg-table.md) table. Instead they should register modules by authoring one or more of the tables in the [Registry Tables Group](registry-tables-group.md). Many of the benefits of the Windows Installer are lost with self registration because self-registration routines tend to hide critical configuration information. For a list of the reasons for avoiding self registration see [SelfReg table](selfreg-table.md).
-   Installation package authors are strongly advised against using the [TypeLib](typelib-table.md) table. Instead of using the TypeLib table, register type libraries by using [Registry](registry-table.md) table. If an installation using the TypeLib table fails and must be rolled back, the rollback may not restore the computer to the same state that existed prior to the rollback.

## Provide the option to install without a user interface.

Administrators often prefer to deploy applications within a corporation without requiring user interaction. It is good practice to enable your application to provide the option of being installed with the [user interface level](user-interface-levels.md) of None.

-   Use [public properties](public-properties.md) for configuration information. Administrators can provide this information on the command-line.
-   Do not require that the installation depend upon information gathered from user interaction with dialog boxes. This information is not available during a silent installation.
-   Do not automatically restart the user's computer during a silent installation.
-   Administrators can set the [user interface level](user-interface-levels.md) when installing by using the [command line option](command-line-options.md) "/q". The user interface level can also be set programmatically with a call to [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui).

## Avoid using the AlwaysInstallElevated policy.

If the [AlwaysInstallElevated](alwaysinstallelevated.md) policy is not set, applications not distributed by the administrator are installed using the user's privileges and only managed applications get elevated privileges. Setting this policy directs Windows Installer to use system permissions when it installs the application on the system. This method can open a computer to a security risk, because when this policy is set, a non-administrator user can run installations with [*elevated*](e-gly.md) privileges and access secure locations on the computer. It is a good practice to use another method than the AlwaysInstallElevated policy when [Installing a Package with Elevated Privileges for a Non-Admin](installing-a-package-with-elevated-privileges-for-a-non-admin.md) or [Patching Per-User Managed Applications](patching-per-user-managed-applications.md).

## Enable the DisableMedia policy to limit unauthorized installation.

The [DisableMedia](disablemedia.md) policy can prevent unauthorized installation of applications. When this policy is enabled, users and administrators running a maintenance installation of one product are prevented from using the Browse Dialog to browse media sources, such as CD-ROM, for the sources of other installable products. Browsing for other products is prevented regardless of whether the installation is done with elevated privileges. It is still possible for the user to reinstall the product from media if the user has a correctly labeled media source.

## Keep the original package source files secure and available to users.

In some cases the original source of the Windows Installer package may be needed to install-on-demand, repair, or update an application. If the installer is unable to locate an available source, the user is asked to provide media or to go to a network location containing the needed sources. It is a good practice to ensure that the installer has the sources it needs without having to prompt the user.

-   Use [Digital Signatures and External Cabinet Files](digital-signatures-and-external-cabinet-files.md) to ensure that the origial sources being used by the installer are secure. An uncompressed source image stored in an public location is not secure.
-   Include a complete list of network or URL source paths to the application's installation package in the [**SOURCELIST**](sourcelist.md) property.
-   Use a Distributed File System (DFS) share for the source path.
-   Use the Windows Installer API to retrieve and modify source list information for Windows Installer applications and patches. For information see [Managing Installation Sources](managing-installation-sources.md).
-   Use the methods and properties of the [**Installer Object**](installer-object.md), [**Product Object**](product-object.md), and [**Patch Object**](patch-object.md) to retrieve and modify source list information for Windows Installer applications and patches.
-   Adhere to points listed in [Preventing a Patch from Requiring Access to the Original Installation Source](preventing-a-patch-from-requiring-access-to-the-original-installation-source.md) points to minimize the possibility that your patch will require access to the original sources.
-   Store the package source files in a location that is not the system's temporary folder. Windows Installer source files stored in the temporary folder can become unavailable to users.

## Enable verbose logging on user's computer when troubleshooting deployment.

[Windows Installer Logging](windows-installer-logging.md) includes a verbose logging option that can be enabled on a user's computer. The information in a verbose log can helpful when trying to troubleshoot Windows Installer package deployment.

-   You can enable verbose logging on the user's computer by using [Command Line Options](command-line-options.md), the [**MsiLogging**](msilogging.md) property, [Logging policy](logging.md), [**MsiEnableLog**](/windows/desktop/api/Msi/nf-msi-msienableloga), and [**EnableLog**](installer-enablelog.md) method.
-   A very useful resource for interpreting Windows Installer log files is [Wilogutl.exe](wilogutl-exe.md). This tool assists the analysis of log files and displays suggested solutions to errors that are found in a log file.
-   The verbose logging option should be used only for troubleshooting purposes and should not be left on because it can have adverse effects on system performance and disk space. Each time you use the Add/Remove Programs tool in Control Panel, a new file is created.

## Uninstallation leaves the user's computer in a clean state.

Application removal is as important as installation. When a Windows Installer package is uninstalled it should leave no useless parts of itself behind on the user's computer.

-   If a file that should have been removed from the user's computer remains installed after running an uninstall, the installer may not be removing the component containing the file for one or more of the reasons described in [Removing Stranded Files](removing-stranded-files.md).
-   If an application must be registered, author the package to remove registry information when the application is uninstalled. For information see [Adding or Removing Registry Keys on the Installation or Removal of Components](adding-or-removing-registry-keys-on-the-installation-or-removal-of-components.md). If an application is not registered, the application is not listed in the Add or Remove Programs feature in Control Panel and cannot be managed by using the Windows Installer.
-   To hide an application from the Add or Remove Programs feature in Control Panel and still be able to use the Windows Installer to manage the application, follow the guidelines described in [Adding and Removing an Application and Leaving No Trace in the Registry](adding-and-removing-an-application-and-leaving-no-trace-in-the-registry.md).
-   Custom actions should be conditioned to run or not as needed upon uninstallation. Different custom actions may need to run on install and uninstall.
-   User-specific customization information can be stored in a text file on the computer. This has the advantage that the file can be removed when the application is uninstalled, even if the user of this customization is not currently logged on.

## Test packages for both per-user and per-machine installation deployment.

It is good practice to enable customers to decide whether to deploy a package for installation in either the per-machine or per-user [installation context](installation-context.md).

-   Consider whether the application should be available to only particular users or all users of the computer during the development process.
-   Test that the package works correctly for both the per-user installation and per-machine installation contexts.
-   Make the package easily customizable and let customers decide whether to deploy it per-user or per-machine.

## Plan and test a servicing strategy before shipping the application.

You should decide how you intend to service the application before deploying the application for the first time.

-   Consider the types of updates you expect to use to service your application in the future. The Windows Installer provides three types of updates: [Small Update](small-updates.md), [Minor Upgrade](minor-upgrades.md), and [Major Upgrades](major-upgrades.md). The differences between these are described in [Patching and Upgrades](patching-and-upgrades.md) topic.
-   Before shipping your application, test that it works as expected after servicing with each update type.

## Reduce the dependency of updates upon the original sources.

If the original source files are required to update your application, this can make servicing the application more difficult. The following methods can help reduce the dependence of updates upon the original sources.

-   Use a [*delta patch*](d-gly.md) to update the baseline versions of your application, such as the RTM version and the service pack versions. Follow the guidelines for using delta patches described in the topic: [Reducing Patch Size](reducing-patch-size.md).
-   Follow the recommendations listed in the topic: [Preventing a Patch from Requiring Access to the Original Installation Source](preventing-a-patch-from-requiring-access-to-the-original-installation-source.md).

## Do not distribute unserviceable merge modules.

Applications should not depend on [merge modules](merge-modules.md) for the installation of component if the owner of the merge module and the owner of the application are different. This can make it difficult to service the application because both owners need to coordinate to update the application or module. Without knowing all the applications that have used the merge module, the owner of the application is unable update the merge module without risking that the update might be incompatible with another application. The owner of the merge module has no direct method for updating Windows Installer packages that have already installed the merge module.

-   Consider providing the needed components to users as another Windows Installer installation.

## Avoid patching administrative installations.

Provide on a network an [administrative installation](administrative-installation.md) of your application's original Windows Installer package to enable members of a workgroup to install the application. Users of this administrative image should then apply updates to the local instance of the application located on their computer. This keeps users in synchronization with the administrative image. Applying updates to the administrative installation is not recommended for the following reasons.

-   The size and latency of the download required for users to obtain an update is increased compared to downloading a patch. The entire updated Windows Installer package and source files must download, recached, and reinstalled.
-   Users are unable to [installation-on-demand](installation-on-demand.md) and repair applications from an updated administrative installation until they recache and reinstall the application.
-   Applying a patch to an administrative installation removes the digital signature from the package. An administrator must resign the package. For more information about using digital signatures, see [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md).
-   Many binary patches target the RTM image of the application and require a previous file version. The local instance of an application installed from an updated administrative installation may not work with other updates. Many binary patch applications can fail.
-   Applying a patch to an administrative installation updates the source files and the .msi file but does not stamp the network image with information about the update. Users cannot determine which updates they have received from the administrative installation. This makes it impossible to sequence updates applied on the user side with those already applied on the administrative image side.
-   Patches applied to an administrative installation are not [uninstallable patches](uninstallable-patches.md). This can prevent the package code cached on the user's computer from becoming different than the package code on the administrative installation. If the package code cached on the user's computer becomes different from that on the administrative installation, reinstall the application from the administrative installation and then patch the client computer.
-   If you decide to apply small updates by patching an administrative image, follow the guidelines described in the topic: [Applying Small Updates by Patching an Administrative Image](applying-small-updates-by-patching-an-administrative-image.md).

## Register updates to run with elevated privilege.

Beginning with Windows Installer 3.0, it is possible to apply patches to an application that has been installed in a per-user-managed context, after the patch has been registered as having elevated privileges. You cannot apply patches to applications that are installed in a per-user managed context using versions of Windows Installer earlier than version 3.0.

-   Use the [**SourceListAddSource**](patch-sourcelistaddsource.md) method or [**MsiSourceListAddSourceEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourceexa) function to register a patch package as having elevated privileges. Follow the guidelines and examples provided in [Patching Per-User Managed Applications](patching-per-user-managed-applications.md).
-   When running Windows Installer version 4.0 on Windows Vista you can also use [User Account Control (UAC) Patching](user-account-control--uac--patching.md) to enables the authors of Windows Installer installations to identify digitally-signed patches that can be applied in the future by non-administrator users. This is only available with the installation of packages in the per-machine [installation context](installation-context.md) (ALLUSERS=1).
-   Ensure that least-privilege patching has not been disabled by setting the [**MSIDISABLELUAPATCHING**](msidisableluapatching.md) property or the [DisableLUAPatching](disableluapatching.md) policy.

## Use the MsiPatchSequence Table to sequence patches.

Include a [MsiPatchSequence Table](msipatchsequence-table.md) in your package and add patch sequencing information. Beginning with Windows Installer version 3.0, the installer can use the MsiPatchSequence Table when [installing multiple patches](installing-multiple-patches.md) to determine the best patch application sequence. Use the guidelines described in the [Patch Sequencing in Windows Installer version 3.0](https://www.microsoft.com/downloads/details.aspx?FamilyID=ad7ac91e-2493-4549-ae6f-bf5e007c12a3) white paper for defining patch families.

-   If practical, specify all patches as belonging to a single patch family. In many cases a single patch family provides enough flexibility to sequence patches. The complexity of authoring increases when multiple patch families are used. Assign a meaningful name to the patch family and assign sequence values in that patch family that increase over time. Follow the [Multiple Patching Example](multiple-patching-example.md) to apply patches in the order in which they have been issued.
-   Use the [PatchSequence Table](patchsequence-table--patchwiz-dll-.md) in [Patchwiz.dll](patchwiz-dll.md) to generate the information in [MsiPatchSequence Table](msipatchsequence-table.md). The version of PATCHWIZ.DLL that was released with Windows Installer 3.0 can automatically generate patch sequencing information. For more information on how to add a new patch, see [Generating Patch Sequence Information](generating-patch-sequence-information---patchwiz-dll-.md). For more information about patch sequencing scenarios, see the whitepaper: [Patch Sequencing in Windows Installer version 3.0](https://www.microsoft.com/downloads/details.aspx?FamilyID=ad7ac91e-2493-4549-ae6f-bf5e007c12a3).

## Test the installation package thoroughly.

Test for correct installation, repair, and removal of your Windows Installer package. You can divide your testing process into the following parts.

-   Installation Testing - Test the installation with all possible combinations of application features. Test all types of installation, including [Administrative Installation](administrative-installation.md), [Rollback Installation](rollback-installation.md), and [Installation-On-Demand](installation-on-demand.md). Try all possible methods of installation, including clicking on the .msi file, [command line options](command-line-options.md), and installing from the control panel. Test that the package can be installed by users in all possible privilege contexts. Try installing the package after it has been deployed by all possible methods. Enable [Windows Installer Logging](windows-installer-logging.md) for each test and resolve all errors found in the installer log and event log.
-   User Interface Testing - Test the package when installed with all possible [user interface levels](user-interface-levels.md). Test the package installed with no user interface and with all information provided through the user interface. Ensure the [Accessibility](accessibility.md) of the user interface and that the user interface functions as expected for different screen resolutions and font sizes.
-   Servicing and Repair Testing - Test that the package can handle [Patching and Upgrades](patching-and-upgrades.md) delivered by a [Small Update](small-updates.md), [Minor Upgrade](minor-upgrades.md), and [Major Upgrades](major-upgrades.md). Before deploying the package, write a trial update of each type and try applying it to the original package.
-   Uninstall Testing - Verify that when the package is removed it leaves no useless parts of itself behind on the user's computer and that only information belonging to the package has been removed. Reboot the test computer after uninstalling the package and verify the integrity of common system tools and other standard applications. Test that the package can be removed by users in all possible privilege contexts. Test all methods to remove the package, click the .msi file, try the [command line options](command-line-options.md), and try removing the package from the control panel. Enable [Windows Installer Logging](windows-installer-logging.md) for each test and resolve all errors found in the installer log and event log.
-   Product Functionality Testing - Ensure that the application functions as expected after the installation, repair, or removal of the package.

## Fix all validation errors before deploying a new or revised installation package.

Run [package validation](package-validation.md) on a new or revised Windows Installer package before attempting to install it for the first time. Validation checks the Windows Installer database for authoring errors. Attempting to install a package that does not pass validation can damage the user's system.

-   You can validate your package using [Orca.exe](orca-exe.md) or [Msival2.exe](msival2-exe.md). Both tools are provided with the Windows SDK. Third-party vendors may also incorporate the ICE validation system into their authoring environment.
-   You can use the standard set of [Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md) included in the .cub files provided with the SDK, or customize validation by [Building an ICE](building-an-ice.md) and adding it to the .cub file.
-   You can use the Evalcom2.dll to implement [Validation Automation](validation-automation.md) for installation packages and merge modules.

## Author a secure installation.

Following these guidelines when developing your package to help maintain a secure environment during installation.

-   [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md)
-   [Guidelines for Securing Packages on Locked-Down Computers](guidelines-for-securing-packages-on-locked-down-computers.md)
-   [Guidelines for Securing Custom Actions](guidelines-for-securing-custom-actions.md)

## Use PMSIHANDLE instead of HANDLE

The **PMSIHANDLE** type variables is defined in msi.h. It is recommended that your application use the **PMSIHANDLE** type because the installer closes **PMSIHANDLE** objects as they go out of scope, whereas your application must close **MSIHANDLE** objects by calling [**MsiCloseHandle**](/windows/desktop/api/Msi/nf-msi-msiclosehandle). **PMSIHandle** provides a casting operator to **MSIHANDLE** for API signature compatibility.

For example, if you use code like this:

``` syntax
MSIHANDLE hRec = MsiCreateRecord(3);
```

Change it to:

``` syntax
PMSIHANDLE hRec = MsiCreateRecord(3);
```

 

 
