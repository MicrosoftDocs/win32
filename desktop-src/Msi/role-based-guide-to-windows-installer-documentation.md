---
description: Windows Installer is the recommended solution for the installation and setup of applications on Windows.
ms.assetid: 13f41020-5275-44cd-b26b-f45483700d8a
title: Role-based Guide to Windows Installer Documentation
ms.topic: article
ms.date: 05/31/2018
---

# Role-based Guide to Windows Installer Documentation

Windows Installer is the recommended solution for the installation and setup of applications on Windows. Therefore, some of the information contained in this SDK will be of interest to a wide range of software development and IT professionals. This section is provided as a guide to readers who prefer to see links to topics organized by professional role and common task scenarios. Because roles can differ greatly between organizations, the following grouping should only be considered as a guide to a location to start searching for the information you need.

-   [Application Developers](#application-developers)
-   [Setup Authors](#setup-authors)
-   [IT Professionals](#it-professionals)
-   [Infrastructure Developers](#infrastructure-developers)

This documentation is intended for software developers who want to make applications that use Windows Installer. As the primary source of reference material for the installer, the SDK provides information about installation packages and the installer service. It contains complete descriptions of the application programming interface (API) and the elements of the installer database.

For more information, see [Other Sources of Windows Installer Information](other-sources-of-windows-installer-information.md).

## Application Developers

Application developers create applications that call the Windows Installer application programming interface and install Windows installer packages at run time. The Windows Installer can do work in an application such as self-repair and installation-on-demand. Typically, application Developers do the following:

-   Enable installation-on-demand of applications at run time from within another application.

    For more information, see the following:

    -   [Using Installer Functions](using-installer-functions.md)
    -   [Installer Function Reference](installer-function-reference.md)
    -   [Installation-On-Demand](installation-on-demand.md)
    -   [Component Management](component-management.md)
    -   [Editing Installer Shortcuts](editing-installer-shortcuts.md)
    -   [**OLEAdvtSupport Property**](oleadvtsupport.md)
    -   [Platform Support of Advertisement](platform-support-of-advertisement.md)

-   Enable self-repair of applications by reinstalling components as needed at run time.

    For more information, see the following:

    -   [Using Installer Functions](using-installer-functions.md)
    -   [Installer Function Reference](installer-function-reference.md)
    -   [Resiliency](resiliency.md)
    -   [Source Resiliency](source-resiliency.md)
    -   [Searching for a Broken Feature or Component](searching-for-a-broken-feature-or-component.md)
    -   [Replacing Existing Files](replacing-existing-files.md)

-   Display a user interface to collect user information and configuration preferences the first time an application is installed or run. The user interface must be added by the Setup Author of the Windows Installer package.

    For more information, see the following:

    -   [Using Installer Functions](using-installer-functions.md)
    -   [Initializing an Application](initializing-an-application.md)
    -   [FirstRun Dialog](firstrun-dialog.md)
    -   [About the User Interface](about-the-user-interface.md)

-   Create applications that use an indirection model to refer to components with parallel functionality. The qualified component categories must be added by the Setup Author of the Windows Installer package.

    For more information, see the following:

    -   [Qualified Components](qualified-components.md)
    -   [Using Qualified Components](using-qualified-components.md)

-   Use private and side-by-side assemblies to isolate applications and reduce DLL conflicts.

    For more information, see the following:

    -   [Assemblies](assemblies.md)
    -   [Assembly Registry Keys Written by Windows Installer](assembly-registry-keys-written-by-windows-installer-.md)
    -   [Installing Win32 Assemblies for Side-by-Side Sharing on Windows XP](installing-win32-assemblies-for-side-by-side-sharing-on-windows-xp.md)
    -   [Installing Win32 Assemblies for the Private Use of an Application on Windows XP](installing-win32-assemblies-for-the-private-use-of-an-application-on-windows-xp.md)
    -   [MsiAssembly Table](msiassembly-table.md)
    -   [MsiAssemblyName Table](msiassemblyname-table.md)
    -   [**MsiProvideAssembly**](/windows/desktop/api/Msi/nf-msi-msiprovideassemblya)
    -   [**MsiWin32AssemblySupport Property**](msiwin32assemblysupport.md)
    -   [**MsiNetAssemblySupport Property**](msinetassemblysupport.md)
    -   [**Isolated Components**](isolated-components.md)

-   Prepare the application to install its own comprehensive major upgrades.

    For more information, see the following:

    -   [Patching and Upgrades](patching-and-upgrades.md)
    -   [Major Upgrades](major-upgrades.md)
    -   [**UpgradeCode Property**](upgradecode.md)
    -   [**Using an UpgradeCode**](using-an-upgradecode.md)
    -   [Preventing an Old Package from Installing Over a Newer Version](preventing-an-old-package-from-installing-over-a-newer-version.md)

-   Prepare the application to install its own minor upgrades, small updates, or fixes.

    For more information, see the following:

    -   [Patching and Upgrades](patching-and-upgrades.md)
    -   [Small Updates](small-updates.md)
    -   [Minor Upgrades](minor-upgrades.md)

-   Organize application resources into components that can work with the Windows Installer.

    For more information, see the following:

    -   [Windows Installer Components](windows-installer-components.md)
    -   [Working with Features and Components](working-with-features-and-components.md)
    -   [Using Transitive Components](using-transitive-components.md)
    -   [What happens if the component rules are broken?](what-happens-if-the-component-rules-are-broken.md)
    -   [Organizing Applications into Components](organizing-applications-into-components.md)
    -   [Isolated Components](isolated-components.md)
    -   [Qualified Components](qualified-components.md)

## Setup Authors

Setup Authors create Windows Installer packages (.msi files) that contain the setup logic and information needed to install an application. They typically use authoring tools such as [Orca.exe](orca-exe.md) to populate the Windows Installer database with the setup logic and information. Typically, Setup Authors do the following:

-   Determine the functionality available with different Windows Installer versions.

    For more information, see the following:

    -   [Determining the Windows Installer Version](determining-the-windows-installer-version.md)
    -   [Released Versions of Windows Installer](released-versions-of-windows-installer.md)
    -   [What's New in Windows Installer](what-s-new-in-windows-installer.md)

-   Organize application resources into Windows Installer components.

    For more information, see the following:

    -   [Windows Installer Components](windows-installer-components.md)
    -   [Organizing Applications into Components](organizing-applications-into-components.md)
    -   [Changing the Component Code](changing-the-component-code.md)
    -   [What happens if the component rules are broken?](what-happens-if-the-component-rules-are-broken.md)
    -   [Windows Installer Examples](windows-installer-examples.md)

-   Use third-party Windows Installer package authoring tools or SDK tools such as [Orca.exe](orca-exe.md) to populate an installation database and create a Windows Installer package.

    For more information, see the following:

    -   [Windows Installer Development Tools](windows-installer-development-tools.md)
    -   [Installation Package, About the Installer Database](installation-package.md)
    -   [Windows Installer File Extensions](windows-installer-file-extensions.md)
    -   [Database Tables](database-tables.md)
    -   [Package Codes](package-codes.md)
    -   [Authoring a Large Package](authoring-a-large-package.md)
    -   [Windows Installer on 64-bit Operating Systems](windows-installer-on-64-bit-operating-systems.md)
    -   [Naming Custom Tables, Properties, and Actions](naming-custom-tables-properties-and-actions.md)
    -   [OLE Limitations on Streams](ole-limitations-on-streams.md)
    -   [Column Definition Format](column-definition-format.md)
    -   [Reducing the Size of an .msi File](reducing-the-size-of-an--msi-file.md)

-   Author the Windows Installer database to install files.

    For more information, see the following:

    -   [Core Tables Group](core-tables-group.md)
    -   [File Tables Group](file-tables-group.md)
    -   [File Table](file-table.md)
    -   [File Searching](file-searching.md)
    -   [File Costing](file-costing.md)
    -   [File Installation](file-installation.md)
    -   [Companion Files](companion-files.md)
    -   [File Versioning Rules](file-versioning-rules.md)
    -   [Default File Versioning](default-file-versioning.md)
    -   [Replacing Existing Files](replacing-existing-files.md)
    -   [Using Cabinets and Compressed Sources](using-cabinets-and-compressed-sources.md)
    -   [Removing Stranded Files](removing-stranded-files.md)
    -   [Installing Permanent Components, Files, Fonts, Registry Keys](installing-permanent-components-files-fonts-registry-keys.md)
    -   [FileSFPCatalog Table](filesfpcatalog-table.md)
    -   [Searching for a File and Creating a Property Holding the File's Path](searching-for-a-file-and-creating-a-property-holding-the-file-s-path.md)
    -   [Searching for a Directory and a File in the Directory](searching-for-a-directory-and-a-file-in-the-directory.md)
    -   [Windows Installer Examples](windows-installer-examples.md)

-   Author a Windows Installer database that installs a directory structure and folders.

    For more information, see the following:

    -   [Core Tables Group](core-tables-group.md)
    -   [File Tables Group](file-tables-group.md)
    -   [Component Table](component-table.md)
    -   [Directory Table](directory-table.md)
    -   [Using the Directory Table](using-the-directory-table.md)
    -   [Using a Directory Property in a Path](using-a-directory-property-in-a-path.md)
    -   [System Folder Properties](property-reference.md)
    -   [CreateFolder Table](createfolder-table.md)
    -   [LockPermissions Table](lockpermissions-table.md)
    -   [MsiLockPermissionsEx Table](msilockpermissionsex-table.md)
    -   [Changing the Target Location for a Directory](changing-the-target-location-for-a-directory.md)
    -   [Windows Installer Examples](windows-installer-examples.md)

-   Author a Windows Installer database that installs registry keys.

    For more information, see the following:

    -   [Core Tables Group](core-tables-group.md)
    -   [Registry Tables Group](registry-tables-group.md)
    -   [Registry Table](registry-table.md)
    -   [Modifying the Registry](modifying-the-registry.md)
    -   [Adding or Removing Registry Keys on the Installation or Removal of Components](adding-or-removing-registry-keys-on-the-installation-or-removal-of-components.md)
    -   [Adding and Removing an Application and Leaving No Trace in the Registry](adding-and-removing-an-application-and-leaving-no-trace-in-the-registry.md)
    -   [Installing Permanent Components, Files, Fonts, Registry Keys](installing-permanent-components-files-fonts-registry-keys.md)
    -   [Searching for Existing Applications, Files, Registry Entries or .ini File Entries](searching-for-existing-applications-files-registry-entries-or--ini-file-entries.md)
    -   [Searching for a Registry Entry and Creating a Property Holding the Value of the Registry](searching-for-a-registry-entry-and-creating-a-property-holding-the-value-of-the-registry.md)
    -   [Assembly Registry Keys Written by the Windows Installer](assembly-registry-keys-written-by-windows-installer-.md)
    -   [Uninstall Registry Key](uninstall-registry-key.md)
    -   [SelfReg Table](selfreg-table.md)
    -   [Specifying the Order of Self Registration](specifying-the-order-of-self-registration.md)
    -   [Windows Installer Examples](windows-installer-examples.md)

-   Author a Windows Installer database that installs services.

    For more information, see the following:

    -   [ServiceInstall Table](serviceinstall-table.md)
    -   [ServiceControl Table](servicecontrol-table.md)
    -   [Component Table](component-table.md)

-   Author a Windows Installer database that installs isolated components or COM components.

    For more information, see the following:

    -   [Registry Tables Group](registry-tables-group.md)
    -   [Class Table](class-table.md)
    -   [Complus Table](complus-table.md)
    -   [Isolated Components](isolated-components.md)
    -   [Using Isolated Components](using-isolated-components.md)
    -   [Installation of Isolated Components](installation-of-isolated-components.md)
    -   [Reinstallation of Isolated Components](reinstallation-of-isolated-components.md)
    -   [Removal of Isolated Components](removal-of-isolated-components.md)
    -   [Installing a COM Component to a Private Location](installing-a-com-component-to-a-private-location.md)
    -   [Make a COM Component in an Existing Package Private](make-a-com-component-in-an-existing-package-private.md)
    -   [Installing a COM+ Application with the Windows Installer](installing-a-com--application-with-the-windows-installer.md)
    -   [Installing a non-COM Component to a Private Location](installing-a-non-com-component-to-a-private-location.md)
    -   [Make a non-COM Component in an Existing Package Private](make-a-non-com-component-in-an-existing-package-private.md)

-   Author a Windows Installer database that installs assemblies.

    For more information, see the following:

    -   [MsiAssembly Table](msiassembly-table.md)
    -   [MsiAssemblyName Table](msiassemblyname-table.md)
    -   [Assemblies](assemblies.md)
    -   [Assembly Registry Keys Written by the Windows Installer](assembly-registry-keys-written-by-windows-installer-.md)
    -   [Installation of Win32 Assemblies](installation-of-win32-assemblies.md)

-   Author a Windows Installer database that installs ODBC drivers and translators.

    For more information, see the following:

    -   [ODBCAttribute Table](odbcattribute-table.md)
    -   [ODBCDriver Table](odbcdriver-table.md)
    -   [ODBCTranslator Table](odbctranslator-table.md)
    -   [ODBCDataSource Table](odbcdatasource-table.md)
    -   [ODBCSourceAttribute Table](odbcsourceattribute-table.md)

-   Author a Windows Installer database that installs MIME.

    For more information, see the following:

    -   [MIME Table](mime-table.md)
    -   [Extension Table](extension-table.md)
    -   [Modifying the Registry](modifying-the-registry.md)

-   Author a Windows Installer database that installs environment variables.

    For more information, see the following:

    -   [Environment Table](environment-table.md)

-   Author a Windows Installer database that installs shortcuts.

    For more information, see the following:

    -   [Shortcut Table](shortcut-table.md)
    -   [MsiShortcutProperty Table](msishortcutproperty-table.md)
    -   [Editing Installer Shortcuts](editing-installer-shortcuts.md)
    -   [Windows Installer Examples](windows-installer-examples.md)

-   Author a Windows Installer database that installs multiple instances of applications.

    For more information, see the following:

    -   [Installing Multiple Instances of Products and Patches](installing-multiple-instances-of-products-and-patches.md)
    -   [Authoring Multiple Instances with Instance Transforms](authoring-multiple-instances-with-instance-transforms.md)
    -   [Installing Multiple Instances with Instance Transforms](installing-multiple-instances-with-instance-transforms.md)

-   Specify default feature selection states and options.

    For more information, see the following:

    -   [Core Tables Group](core-tables-group.md)
    -   [Component Table](component-table.md)
    -   [Feature Table](feature-table.md)
    -   [FeatureComponents Table](featurecomponents-table.md)
    -   [Controlling Feature Selection States](controlling-feature-selection-states.md)
    -   [Feature Installation Options Properties](property-reference.md)

-   Specify conditions that must be met to install an application or selected components.

    For more information, see the following:

    -   [Condition Table](condition-table.md)
    -   [LaunchCondition Table](launchcondition-table.md)
    -   [Component Table](component-table.md)
    -   [Using Properties in Conditional Statements](using-properties-in-conditional-statements.md)
    -   [Conditional Statement Syntax](conditional-statement-syntax.md)
    -   [Conditioning Actions to Run During Removal](conditioning-actions-to-run-during-removal.md)
    -   [Examples of Conditional Statement Syntax](examples-of-conditional-statement-syntax.md)

-   Author the sequence of actions used to install the application.

    For more information, see the following:

    -   [Using a Sequence Table](using-a-sequence-table.md)
    -   [Installation Procedure Tables Group](installation-procedure-tables-group.md)
    -   [Sequence Table Detailed Example](sequence-table-detailed-example.md)
    -   [Actions with Sequencing Restrictions](actions-with-sequencing-restrictions.md)
    -   [Actions without Sequencing Restrictions](actions-without-sequencing-restrictions.md)
    -   [Using Properties in Conditional Statements](using-properties-in-conditional-statements.md)
    -   [Conditional Statement Syntax](conditional-statement-syntax.md)
    -   [Examples of Conditional Statement Syntax](examples-of-conditional-statement-syntax.md)
    -   [Conditioning Actions to Run During Removal](conditioning-actions-to-run-during-removal.md)
    -   [Standard Actions](standard-actions.md)
    -   [Windows Installer Examples](windows-installer-examples.md)

-   Prepare the installation package of the application for future upgrades of the application by the Windows Installer service.

    For more information, see the following:

    -   [Patching and Upgrades](patching-and-upgrades.md)
    -   [Preparing an Application for Future Major Upgrades](preparing-an-application-for-future-major-upgrades.md)
    -   [Using an UpgradeCode](using-an-upgradecode.md)
    -   [Upgrade Table](upgrade-table.md)
    -   [**UpgradeCode Property**](upgradecode.md)
    -   [Preventing an Old Package from Installing Over a Newer Version](preventing-an-old-package-from-installing-over-a-newer-version.md)
    -   [Changing the Product Code](changing-the-product-code.md)
    -   [Updating Assemblies](updating-assemblies.md)
    -   [Windows Installer Examples](windows-installer-examples.md)

-   Troubleshoot Windows Installer packages under development.

    For more information, see the following:

    -   [Package Validation](package-validation.md)
    -   [Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md)
    -   [Windows Installer Logging](windows-installer-logging.md)
    -   [Checking the Installation of Features, Components, Files](checking-the-installation-of-features-components-files.md)
    -   [Authoring a Large Package](authoring-a-large-package.md)
    -   [Wilogutl.exe](wilogutl-exe.md)
    -   [Windows Installer Development Tools](windows-installer-development-tools.md)
    -   [Validating Merge Modules](validating-merge-modules.md)
    -   [Validating an Installation Database](validating-an-installation-database.md)
    -   [Validating an Installation Upgrade](validating-an-installation-upgrade.md)
    -   [Searching for a Broken Feature or Component](searching-for-a-broken-feature-or-component.md)
    -   [Windows Installer Error Messages](windows-installer-error-messages.md)
    -   [Logging of Reboot Requests](logging-of-reboot-requests.md)

-   Ensure a secure setup and installation of the application.

    For more information, see the following:

    -   [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md)
    -   [Guidelines for Securing Custom Actions](guidelines-for-securing-custom-actions.md)
    -   [Custom Action Security](custom-action-security.md)
    -   [Guidelines for Securing Packages on Locked-Down Computers](guidelines-for-securing-packages-on-locked-down-computers.md)
    -   [Authoring a Fully Verified Signed Installation Using Automation](authoring-a-fully-verified-signed-installation-using-automation.md)
    -   [A URL-Based Windows Installer Installation Example](a-url-based-windows-installer-installation-example.md)
    -   [Authoring the User Interface for Password Input](authoring-the-user-interface-for-password-input.md)
    -   [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md)
    -   [Using Windows Installer with UAC](using-windows-installer-with-uac.md)
    -   [User Account Control (UAC) Patching](user-account-control--uac--patching.md)
    -   [Msicert.exe](msicert-exe.md)
    -   [**AdminUser property**](adminuser.md)
    -   [**Privileged property**](privileged.md)
    -   [**SecureCustomProperties property**](securecustomproperties.md)

-   Create a user interface to present options to configure the installation and obtain information from the user about the pending installation process.

    For more information, see the following:

    -   [About the User Interface](about-the-user-interface.md)
    -   [Adding Controls and Text](adding-controls-and-text.md)
    -   [Authoring a ProgressBar Control](authoring-a-progressbar-control.md)
    -   [Authoring Disk Prompt Messages](authoring-disk-prompt-messages.md)
    -   [Authoring a Conditional "Please Wait . . ." Message Box](authoring-a-conditional-please-wait-------message-box.md)
    -   [Previewing the User Interface](previewing-the-user-interface.md)
    -   [Adding Text Stored in a Property](adding-text-stored-in-a-property.md)
    -   [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui)

-   Create an external user interface to present a custom user interface to configure the installation and obtain information from the user about the pending installation process.

    For more information, see the following:

    -   [**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia)
    -   [Monitoring an Installation Using MsiSetExternalUIRecord](monitoring-an-installation-using-msisetexternaluirecord.md)
    -   [Parsing Windows Installer Messages](parsing-windows-installer-messages.md)
    -   [Returning Values from an External User Interface Handler](returning-values-from-an-external-user-interface-handler.md)
    -   [INSTALLUI\_HANDLER](/windows/desktop/api/Msi/nc-msi-installui_handlera)
    -   [Handling Progress Messages Using MsiSetExternalUI](handling-progress-messages-using-msisetexternalui.md)
    -   [Monitoring an Installation Using MsiSetExternalUI](monitoring-an-installation-using-msisetexternalui.md)

-   Set information for the application in **Add/Remove Programs** (ARP.)

    For more information, see the following:

    -   [Configuring Add/Remove Programs with Windows Installer](configuring-add-remove-programs-with-windows-installer.md)
    -   [Adding and Removing an Application and Leaving No Trace in the Registry](adding-and-removing-an-application-and-leaving-no-trace-in-the-registry.md)
    -   [Uninstall Registry Key](uninstall-registry-key.md)

-   Write custom actions to handle setup logic that is not natively supported by Windows Installer.

    For more information, see the following:

    -   [Custom Actions](custom-actions.md)
    -   [Summary List of All Custom Action Types](summary-list-of-all-custom-action-types.md)
    -   [Guidelines for Securing Custom Actions](guidelines-for-securing-custom-actions.md)
    -   [Custom Action Reference](custom-action-reference.md)
    -   [Using a Custom Action to Create User Accounts on a Local Computer](using-a-custom-action-to-create-user-accounts-on-a-local-computer.md)
    -   [Using a Custom Action to Launch an Installed File at the End of the Installation](using-a-custom-action-to-launch-an-installed-file-at-the-end-of-the-installation.md)
    -   [Accessing a Database or Session from Inside a Custom Action](accessing-a-database-or-session-from-inside-a-custom-action.md)
    -   [Accessing the Current Installer Session from Inside a Custom Action](accessing-the-current-installer-session-from-inside-a-custom-action.md)
    -   [Changing the System State Using a Custom Action](changing-the-system-state-using-a-custom-action.md)

-   Bootstrap the Windows Installer onto a user's computer.

    For more information, see the following:

    -   [Bootstrapping](bootstrapping.md)
    -   [Instmsi.exe](instmsi-exe.md)
    -   [Internet Download Bootstrapping](internet-download-bootstrapping.md)
    -   [Msistuff.exe](msistuff-exe.md)
    -   [A URL-Based Windows Installer Installation Example](a-url-based-windows-installer-installation-example.md)
    -   [Configuring the Setup.exe Resources](configuring-the-setup-exe-resources.md)
    -   [Downloading an Installation from the Internet](downloading-an-installation-from-the-internet.md)

-   Adhere to Active Accessibility guidelines when writing Windows Installer packages.

    For more information, see the following:

    -   [Accessibility](accessibility.md)

-   Prepare for the internationalization of an application setup.

    For more information, see the following:

    -   [Preparing a Windows Installer Package for Localization](preparing-a-windows-installer-package-for-localization.md),
    -   [Localizing a Windows Installer Package](localizing-a-windows-installer-package.md)
    -   [Code Page Handling (Windows Installer)](code-page-handling-windows-installer-.md)
    -   [Adding Localized Resources](adding-localized-resources.md)
    -   [A Localization Example](a-localization-example.md)
    -   [Localizing the Error and ActionText Tables](localizing-the-error-and-actiontext-tables.md)
    -   [Localizing Database Columns](localizing-database-columns.md)
    -   [Creating a Database with a Neutral Code Page](creating-a-database-with-a-neutral-code-page.md)
    -   [Code Page Handling of Imported and Exported Tables](code-page-handling-of-imported-and-exported-tables.md)
    -   [Localizing the Language Displayed by Dialogs](localizing-the-language-displayed-by-dialogs.md)
    -   [Importing Localized Error and ActionText Tables](importing-localized-error-and-actiontext-tables.md)
    -   [Updating ProductLanguage and ProductCode Properties](updating-productlanguage-and-productcode-properties.md)
    -   [Updating a Summary Information Stream](updating-a-summary-information-stream.md)
    -   [Qualified Components](qualified-components.md)
    -   [UIText Table](uitext-table.md)
    -   [Manage Language and Codepage](manage-language-and-codepage.md)
    -   [Checking the Installation Database Code Page](checking-the-installation-database-code-page.md)

-   Create Windows Installer packages for 32-bit and 64-bit platforms.

    For more information, see the following:

    -   [Windows Installer on 64-bit Operating Systems](windows-installer-on-64-bit-operating-systems.md)
    -   [64-Bit Custom Actions](64-bit-custom-actions.md)
    -   [Using 64-bit Custom Actions](using-64-bit-custom-actions.md)
    -   [Using 64-bit Merge Modules](using-64-bit-merge-modules.md)

-   Redistribute shared Windows Installer components and setup logic as merge modules.

    For more information, see the following:

    -   [Merge Modules](merge-modules.md)
    -   [Authoring a Language Transform for a Multiple Language Merge Module](authoring-a-language-transform-for-a-multiple-language-merge-module.md)
    -   [Applying a Configurable Merge Module with Customizations](applying-a-configurable-merge-module-with-customizations.md)

-   Schedule or suppress reboots during a Windows Installer installation.

    For more information, see the following:

    -   [System Reboots](system-reboots.md)
    -   [Logging of Reboot Requests](logging-of-reboot-requests.md)

-   Create updates or fixes for an existing application by creating a patch.

    For more information, see the following:

    -   [Creating a Small Update Patch](creating-a-small-update-patch.md)
    -   [A Small Update Patching Example](a-small-update-patching-example.md)

-   Author a dual-purpose package capable of installing an application either for only the current user or for all users of the computer.

    For more information, see the following:

    -   [Installation Context](installation-context.md)
    -   [Single Package Authoring](single-package-authoring.md)
    -   [Single Package Authoring Example](single-package-authoring-example.md)

-   Customize services on the computer using the Windows Installer.

    For more information, see the following:

    -   [Using Services Configuration](using-services-configuration.md)

-   Secure resources on the computer using the Windows Installer.

    For more information, see the following:

    -   [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md)
    -   [Securing Resources](securing-resources-.md)

-   Enumerate all components installed on the computer and obtain the key path for the component.

    For more information, see the following:

    -   [Enumerating Components](enumerating-components-.md)

-   Install multiple packages using [*transaction processing*](t-gly.md).

    For more information, see the following:

    -   [Multiple-Package Installations](multiple-package-installations.md)

-   Embed a custom user interface in the Windows Installer package.

    For more information, see the following:

    -   [Using the User Interface](using-the-user-interface.md)
    -   [Using an Embedded UI](using-an-embedded-ui.md)

## IT Professionals

IT Professionals and Administrators customize and deploy existing Windows Installer packages. These users repackage setups for existing applications into Windows Installer installation packages, and install and maintain administrative images of Windows Installer installations on networks.

-   Customize applications and setup by generating and applying Windows Installer transforms

    For more information, see the following:

    -   [Customization](customization.md)
    -   [Database Transforms](database-transforms.md)
    -   [A Customization Transform Example](a-customization-transform-example.md)
    -   [Merges and Transforms](merges-and-transforms.md)
    -   [Using Transforms to Add Resources](using-transforms-to-add-resources.md)
    -   [Generate a Transform](generate-a-transform.md)
    -   [Command Line Options](command-line-options.md)
    -   [Msitran.exe](msitran-exe.md)
    -   [Apply a Transform](apply-a-transform.md)
    -   [View a Transform](view-a-transform.md)
    -   [View Differences Between Two Databases](view-differences-between-two-databases.md)
    -   [Patching Customized Applications](patching-customized-applications.md)

-   Deploy a Windows Installer installation package, update, or patch.

    For more information, see the following:

    -   [Installing an Application](installing-an-application.md)
    -   [Patching and Upgrades](patching-and-upgrades.md)
    -   [Transforms](transforms.md)
    -   [Installing a Package with Elevated Privileges for a Non-Admin](installing-a-package-with-elevated-privileges-for-a-non-admin.md)
    -   [Applying Major Upgrades by Patching the Local Installation of the Product](applying-major-upgrades-by-patching-the-local-installation-of-the-product.md)
    -   [Applying Major Upgrades by Installing the Product](applying-major-upgrades-by-installing-the-product.md)
    -   [Applying Small Updates by Patching the Local Installation of the Product](applying-small-updates-by-patching-the-local-installation-of-the-product.md)
    -   [Applying Small Updates by Reinstalling the Product](applying-small-updates-by-reinstalling-the-product.md)
    -   [Applying Small Updates by Patching an Administrative Image](applying-small-updates-by-patching-an-administrative-image.md)
    -   [Patching Initial Installations](patching-initial-installations.md)
    -   [Command Line Options](command-line-options.md)

-   Troubleshoot Windows Installer packages.

    For more information, see the following:

    -   [Windows Installer Logging](windows-installer-logging.md)
    -   [Checking the Installation of Features, Components, Files](checking-the-installation-of-features-components-files.md)
    -   [Wilogutl.exe](wilogutl-exe.md)
    -   [Searching for a Broken Feature or Component](searching-for-a-broken-feature-or-component.md)
    -   [Windows Installer Error Messages](windows-installer-error-messages.md)
    -   [Msicert.exe](msicert-exe.md)

-   Use scripting to query Windows Installer packages for information about a product and modify the installation.

    For more information, see the following:

    -   [Automation Interface](automation-interface.md)
    -   [Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
    -   [Using Windows Installer with WMI](using-windows-installer-with-wmi.md)

-   Create and maintain administrative installations.

    For more information, see the following:

    -   [Administrative Installation](administrative-installation.md)
    -   [Command Line Options](command-line-options.md)
    -   [**AdminProperties Property**](adminproperties.md)
    -   [Applying Small Updates by Patching an Administrative Image](applying-small-updates-by-patching-an-administrative-image.md)
    -   [Applying a Patch Package to an Administrative Installation](applying-a-patch-package-to-an-administrative-installation.md)
    -   [Action Execution Order](action-execution-order.md)
    -   [**IsAdminPackage Property**](isadminpackage.md)
    -   [Order of Property Precedence](order-of-property-precedence.md)
    -   [**AdminProperties Property**](adminproperties.md)

-   Make an application available to all users of a computer or to a specified user only.

    For more information, see the following:

    -   [Installation Context](installation-context.md)
    -   [**ALLUSERS Property**](allusers.md)

-   Interpret packages, install products, and configure feature options using a command line.

    For more information, see the following:

    -   [Command Line Options](command-line-options.md)
    -   [Setting Public Property Values on the Command Line](setting-public-property-values-on-the-command-line.md)
    -   [Getting and Setting Properties](getting-and-setting-properties.md)
    -   [Reinstalling a Feature or Application](reinstalling-a-feature-or-application.md)
    -   [Applying Small Updates by Patching the Local Installation of the Product](applying-small-updates-by-patching-the-local-installation-of-the-product.md)
    -   [Applying Small Updates by Reinstalling the Product](applying-small-updates-by-reinstalling-the-product.md)
    -   [Changing the Target Location for a Directory](changing-the-target-location-for-a-directory.md)
    -   [Applying Small Updates by Patching an Administrative Image](applying-small-updates-by-patching-an-administrative-image.md)
    -   [Applying Major Upgrades by Installing the Product](applying-major-upgrades-by-installing-the-product.md)
    -   [Configuration Properties](property-reference.md)
    -   [Feature Installation Options Properties](property-reference.md)

-   Work with policy to manage access rights and permissions.

    For more information, see the following:

    -   [Machine Policies](machine-policies.md),
    -   [User Policies](user-policies.md),
    -   [Installing a Package with Elevated Privileges for a Non-Admin](installing-a-package-with-elevated-privileges-for-a-non-admin.md)
    -   [Advertising a Per-User Application To Be Installed with Elevated Privileges](advertising-a-per-user-application-to-be-installed-with-elevated-privileges.md)
    -   [Using a Custom Action to Create User Accounts on a Local Computer](using-a-custom-action-to-create-user-accounts-on-a-local-computer.md)
    -   [**AdminUser Property**](adminuser.md)
    -   [**Privileged Property**](privileged.md)
    -   [**EnableUserControl Property**](enableusercontrol.md)
    -   [**UserSID Property**](usersid.md)
    -   [**SecureCustomProperties Property**](securecustomproperties.md)

-   Install multiple packages using [*transaction processing*](t-gly.md).

    For more information, see the following:

    -   [Multiple-Package Installations](multiple-package-installations.md)

-   Embed a custom user interface within a Windows Installer package..

    For more information, see the following:

    -   [Using the User Interface](using-the-user-interface.md)
    -   [Using an Embedded UI](using-an-embedded-ui.md)

## Infrastructure Developers

Infrastructure Developers can create unified platforms for the deployment and management of software that uses the Windows Installer service. They can use the Windows Installer programming interface to query, manage, and distribute applications, patches, and sources on a system.

-   Locate, inventory and query for the state, information, and clients of components.

    For more information, see the following:

    -   [Component-Specific Functions](installer-function-reference.md)
    -   [System Status Functions](installer-function-reference.md)
    -   [Installer Object](installer-object.md)
    -   [Product Object](product-object.md)
    -   [Patch Object](patch-object.md)

-   Inventory and query for information and the state of products and features.

    For more information, see the following:

    -   [Inventory products and patches](inventory-products-and-patches-.md)
    -   [System Status Functions](installer-function-reference.md)
    -   [Product Query Functions](installer-function-reference.md)
    -   [Installer Object](installer-object.md)
    -   [Product Object](product-object.md)
    -   [Patch Object](patch-object.md)

-   Improve source resiliency by using the Windows Installer to inventory, query, and modify the source list of applications, upgrades, and patches.

    For more information, see the following:

    -   [**SOURCELIST Property**](sourcelist.md)
    -   [**Source Resiliency**](source-resiliency.md)
    -   [Installation and Configuration Functions](installer-function-reference.md)
    -   [Installer Object](installer-object.md)
    -   [Product Object](product-object.md)
    -   [Patch Object](patch-object.md)

-   Improve source resiliency by using the Windows Installer to inventory, query, and modify media sources.

    For more information, see the following:

    -   [**SOURCELIST Property**](sourcelist.md)
    -   [Source Resiliency](source-resiliency.md)
    -   [Installation and Configuration Functions](installer-function-reference.md)
    -   [Product Object](product-object.md)
    -   [Patch Object](patch-object.md)

-   Inventory and query for information and the state of patches.

    For more information, see the following:

    -   [Inventory products and patches](inventory-products-and-patches-.md)
    -   [Installer Function Reference](installer-function-reference.md)
    -   [Patch Object](patch-object.md)

-   Work with policy to manage access rights and permissions.

    For more information, see the following:

    -   [Machine Policies](machine-policies.md)
    -   [User Policies](user-policies.md)
    -   [Installing a Package with Elevated Privileges for a Non-Admin](installing-a-package-with-elevated-privileges-for-a-non-admin.md)
    -   [Advertising a Per-User Application To Be Installed with Elevated Privileges](advertising-a-per-user-application-to-be-installed-with-elevated-privileges.md)
    -   [Using a Custom Action to Create User Accounts on a Local Computer](using-a-custom-action-to-create-user-accounts-on-a-local-computer.md)
    -   [**AdminUser Property**](adminuser.md)
    -   [**Privileged Property**](privileged.md)
    -   [**EnableUserControl Property**](enableusercontrol.md)
    -   [**UserSID Property**](usersid.md)
    -   [**SecureCustomProperties Property**](securecustomproperties.md)

 

 



