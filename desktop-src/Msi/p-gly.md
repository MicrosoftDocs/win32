---
description: Learn about Windows Installer concepts that begin with the letter P, such as package code and patching.
ms.assetid: 868f5ed3-b179-404b-9462-1d3a179103f8
title: P (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# P (Windows Installer)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) H [I](i-gly.md) J K L [M](m-gly.md) N [O](o-gly.md) P [Q](q-gly.md) [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) W X Y Z

<dl> <dt>

<span id="_msi_package_using_windows_installer_gly"></span><span id="_MSI_PACKAGE_USING_WINDOWS_INSTALLER_GLY"></span>**package**
</dt> <dd>

[*.msi file*](m-gly.md) and any [*external source files*](e-gly.md) that may be pointed to by this file. A package therefore contains all the information the Windows Installer needs to run the UI and to install or uninstall the application. For more information, see also [*installer database*](i-gly.md).

</dd> <dt>

<span id="_msi_package_code_gly"></span><span id="_MSI_PACKAGE_CODE_GLY"></span>**package code**
</dt> <dd>

GUID that identifies a particular package. A unique package code is required because some transforms or patch packages can be applied to more than one application or can upgrade an application into another application or version. For more information, see [Package Codes](package-codes.md).

</dd> <dt>

<span id="_msi_patching_gly"></span><span id="_MSI_PATCHING_GLY"></span>**patching**
</dt> <dd>

Method of updating a file that replaces only the bits being changed, rather than the entire file. This means that users can download an upgrade patch for a product that is much smaller than the entire product. For more information, see [Patch Packages](patch-packages.md).

</dd> <dt>

<span id="_msi_patch_file_gly"></span><span id="_MSI_PATCH_FILE_GLY"></span>**patch file**
</dt> <dd>

P [atch package](patch-packages.md) used for patching. For more information, see [Patching and Upgrades](patching-and-upgrades.md).

</dd> <dt>

<span id="_msi_preview_mode_using_windows_installer_gly"></span><span id="_MSI_PREVIEW_MODE_USING_WINDOWS_INSTALLER_GLY"></span>**preview mode**
</dt> <dd>

Mode for viewing the design of the UI. For more information, see [Previewing the User Interface](previewing-the-user-interface.md).

</dd> <dt>

<span id="_msi_progress_bar_gly"></span><span id="_MSI_PROGRESS_BAR_GLY"></span>**progress bar**
</dt> <dd>

Control the installer can display during script execution time representing the progress of the installation. For more information, see [Authoring a ProgressBar Control](authoring-a-progressbar-control.md).

</dd> <dt>

<span id="_msi_property_gly"></span><span id="_MSI_PROPERTY_GLY"></span>**property**
</dt> <dd>

Global variables used during an installation. (See [About Properties](about-properties.md).)

The term "property" also refers to an attribute of an automation object. (See [Automation Interface](automation-interface.md).)

</dd> <dt>

<span id="_msi_publishing_gly"></span><span id="_MSI_PUBLISHING_GLY"></span>**publishing**
</dt> <dd>

Method of [*advertising*](a-gly.md) a feature or application. Publishing does not populate the UI. However, if another application attempts to open a published application, there is enough information present for the installer to assign the published application. For more information, see [*assigning*](a-gly.md) and [Components and Features](components-and-features.md).

</dd> </dl>

 

 



