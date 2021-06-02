---
description: This documentation is the primary source of reference material for Windows Installer.
ms.assetid: dfbcc4b6-08bd-4b8a-b658-7010bd0b099c
title: Roadmap to Windows Installer Documentation
ms.topic: article
ms.date: 05/31/2018
---

# Roadmap to Windows Installer Documentation

This documentation is the primary source of reference material for Windows Installer. It provides information about installation packages and the installer service. It also provides complete descriptions of the application programming interface (API) and the elements of the installer database. This documentation also contains a discussion of basic examples of installation and update packages in [Windows Installer Examples](windows-installer-examples.md).

The [Role-based Guide to Windows Installer Documentation](role-based-guide-to-windows-installer-documentation.md) is an alternative provided as a guide to readers that prefer to see links to topics organized by professional role and common task scenarios.

For information about Windows Installer newsgroups see also the topic: [Other Sources of Windows Installer Information](other-sources-of-windows-installer-information.md).

For a list of tips on using the Windows Installer, see [Windows Installer Best Practices](windows-installer-best-practices.md).

The following list describes each section of the installer documentation.

-   [About Windows Installer](about-windows-installer.md) provides an overview of installer capabilities and benefits, such as advertisement, installation-on-demand, resiliency, customization, and component management. This section introduces the concepts of installer components and features, which are essential to understanding how the installer organizes an installation. It also discusses several high-level subjects about installation, such as System Policy, File Versioning Rules, and Rollback Installation.
-   [Using Windows Installer](using-windows-installer.md) discusses a variety of topics, such as a standard method for organizing an application into components that the installer can install or remove from a user's computer; how to download an installation package from the World Wide Web; and using compressed source images.
-   The information in the [What's New in Windows Installer](what-s-new-in-windows-installer.md) sections can be used to identify new features that are not supported by earlier Windows Installer versions.
-   [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md) describes how digital signatures can be used with packages, transforms, patches, merge modules, and external cabinet files.
-   [Assemblies](assemblies.md) explains how to use Windows Installer to install and manage common language run time and Win32 assemblies.
-   [User Interface](user-interface.md) gives information about the installer's user interface capabilities. Although the installer does not provide a user interface, a package author can keep all the data and logic required to run a fully interactive internal or external user interface in the installation database. The Reference section describes elements of the user interface that are specifiable in the database tables, including dialog boxes, controls, and control events.
-   [Standard Actions](standard-actions.md) discusses the standard actions used by the installer in the sequence tables to perform an installation. This information is intended primarily for package developers.
-   [Custom Actions](custom-actions.md) describes how to create additional functionality in the installer. Custom actions enable an author of an installation package to extend the capabilities of standard actions by including executables, dynamic-link libraries, and script. This information is intended for package developers who need to perform installation functions not found elsewhere in the installer.
-   [Properties](properties.md) gives information about the properties the installer uses during an installation. The About and Using sections gives an overview of these global variables and each property is described in the Reference section.
-   [Summary Information Stream](summary-information-stream.md) documents the summary information properties used by the installer. This information is of interest to all developers.
-   [Patching and Upgrades](patching-and-upgrades.md) discusses using the installer to perform file updates, QFEs, minor updates, product upgrades, and patching.
-   [Transforms](transforms.md) explains how to alter or customize an installation database using a database transform and how to generate, secure, and apply transforms.
-   [Package Validation](package-validation.md) discusses using Internal Consistency Evaluators (ICEs) to test the internal consistency of installation packages that are under development.
-   [Merge Modules](merge-modules.md) presents a standard for the design of merge modules. This standard should be followed by developers who are creating their own merge modules as well as by developers who plan to use the installer to deliver shared code to their applications.
-   [Windows Installer on 64-bit Operating Systems](windows-installer-on-64-bit-operating-systems.md) discusses how to use Windows Installer to install and manage installer components designed to run on 64-bit operating systems.
-   [Windows Installer Examples](windows-installer-examples.md) includes a step-by-step example of creating an installation package with an internal user interface in [An Installation Example](an-installation-example.md). For an example of authoring a major upgrade for an existing package, see [An Upgrade Example](an-upgrade-example.md). To learn how a customization transform disables features and adds new resources, see [A Customization Transform Example](a-customization-transform-example.md). For an example of creating a patch package that applies a small update to an existing installation package, see [A Small Update Patching Example](a-small-update-patching-example.md). To learn how to localize an existing installer package, see [A Localization Example](a-localization-example.md).
-   [Automation Interface](automation-interface.md) provides information to developers who want to use the automation interface of Windows Installer.
-   [Installer Functions](installer-functions.md) describes function calls to the installer API. These are the functions that other applications call to access the installer services to install, maintain, or remove applications. The Using sections include discussions about how to request features, initiate installations, and reinstall missing components programmatically. The Reference section is the primary reference material for the installer service functions.
-   [Installer Database](installer-database.md) discusses the installation database. The installer keeps all of the logic and data necessary for an installation in a relational database located in an .msi file. The About section provides an overview with schema diagrams for the major functional groups of tables of the database. The Using section discusses working with the most important of these tables. These sections contain information that is essential to developers who are authoring installation packages or writing package creation tools. The Reference section contains complete reference material for each database table. This section also contains the primary reference for each of the database functions. The database functions are used internally by the installer to access the database and are primarily of interest to developers of installer package creation tools.

 

 



