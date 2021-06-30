---
description: Learn about Windows Installer concepts that begin with the letter C, such as cabinet file and checksum.
ms.assetid: f98d19c5-5187-4718-b241-3ec69454c2d6
title: C (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# C (Windows Installer)

[A](a-gly.md) [B](b-gly.md) C [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) H [I](i-gly.md) J K L [M](m-gly.md) N [O](o-gly.md) [P](p-gly.md) [Q](q-gly.md) [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) W X Y Z

<dl> <dt>

<span id="_msi_cabinet_file_using_windows_installer_gly"></span><span id="_MSI_CABINET_FILE_USING_WINDOWS_INSTALLER_GLY"></span>**cabinet file**
</dt> <dd>

Single file, usually with a .cab extension, that stores compressed files in a file library. The cabinet format is an efficient way to package multiple files because compression is performed across file boundaries, significantly improving compression ratio. For information about creating cabinets, see [Cabinet Files](cabinet-files.md).

</dd> <dt>

<span id="_msi_checksum_gly"></span><span id="_MSI_CHECKSUM_GLY"></span>**checksum**
</dt> <dd>

Computed value that depends on the contents of a file. It is stored with data to detect file corruption. The system checks this value to ensure that the data is uncorrupted.

</dd> <dt>

<span id="_msi_component_using_windows_installer_gly"></span><span id="_MSI_COMPONENT_USING_WINDOWS_INSTALLER_GLY"></span>**component**
</dt> <dd>

Smallest piece of an installation handled by the installer, also a building-block of an application or feature from the programmer's perspective. Examples of components are a group of related files, a COM object, or a library. For more information, see [Components and Features](components-and-features.md).

</dd> <dt>

<span id="_msi_committing_databases_using_windows_installer_gly"></span><span id="_MSI_COMMITTING_DATABASES_USING_WINDOWS_INSTALLER_GLY"></span>**committing databases**
</dt> <dd>

Accumulated changes made in a database. The changes are not reflected in the actual database until the database is committed. For more information, see [Committing Databases](committing-databases.md).

</dd> <dt>

<span id="_msi_controlevent_gly"></span><span id="_MSI_CONTROLEVENT_GLY"></span>**ControlEvent**
</dt> <dd>

Aspect of functionality of the installer's user interface. A typical ControlEvent triggers some action by the installer upon the activation of a dialog box control or other event. For more information, see [ControlEvent Overview](controlevent-overview.md).

</dd> <dt>

<span id="_msi_costing_gly"></span><span id="_MSI_COSTING_GLY"></span>**costing**
</dt> <dd>

Method used by the installer to determine disk space requirements for installation. Costing takes into account factors such as whether existing files need to be overwritten. For more information, see [File Costing](file-costing.md).

</dd> <dt>

<span id="_msi_.cub_file_gly"></span><span id="_MSI_.CUB_FILE_GLY"></span>**.cub file**
</dt> <dd>

Validation module that stores and provides access to ICE custom actions. For more information, see [Sample .cub File](sample--cub-file.md). For more information, see also [Windows Installer File Extensions](windows-installer-file-extensions.md).

</dd> <dt>

<span id="_msi_custom_action_using_windows_installer_gly"></span><span id="_MSI_CUSTOM_ACTION_USING_WINDOWS_INSTALLER_GLY"></span>**custom action**
</dt> <dd>

Written by the author of the [*package*](p-gly.md) but not built into the installer as a standard action. For more information, see [Custom Actions](custom-actions.md).

</dd> </dl>

 

 



