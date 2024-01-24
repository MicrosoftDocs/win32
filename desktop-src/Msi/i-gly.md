---
description: Learn about Windows Installer concepts that begin with the letter I, such as Import Address table and install level.
ms.assetid: b8e0a14f-ebdc-4b8f-a884-f6276dccda49
title: I (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# I (Windows Installer)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) H I J K L [M](m-gly.md) N [O](o-gly.md) [P](p-gly.md) [Q](q-gly.md) [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) W X Y Z

<dl> <dt>

<span id="_msi_.idt_file_gly"></span><span id="_MSI_.IDT_FILE_GLY"></span>**.idt file**
</dt> <dd>

Exported installer database table. For more information, see [Importing and Exporting](importing-and-exporting.md) and [Windows Installer File Extensions](windows-installer-file-extensions.md).

</dd> <dt>

<span id="_msi_import_address_table_gly"></span><span id="_MSI_IMPORT_ADDRESS_TABLE_GLY"></span>**Import Address table (IAT)**
</dt> <dd>

Where the computed virtual address is saved from each function imported from all DLLs.

</dd> <dt>

<span id="_msi_internal_user_interface_gly"></span><span id="_MSI_INTERNAL_USER_INTERFACE_GLY"></span>**internal user interface**
</dt> <dd>

Built-in capabilities of the installer that can be used to author a graphical UI for installation. An author may choose an [*external user interface*](e-gly.md). For more information, see [About the User Interface](about-the-user-interface.md).

</dd> <dt>

<span id="_msi_install_level_gly"></span><span id="_MSI_INSTALL_LEVEL_GLY"></span>**install level**
</dt> <dd>

Specified installation value. An application is installed only if its own level is less than or equal to the install level. The set of applications chosen for installation can therefore be changed by altering the install level. For more information, see [Feature Table](feature-table.md).

</dd> <dt>

<span id="_msi_install_on_demand_gly"></span><span id="_MSI_INSTALL_ON_DEMAND_GLY"></span>**installation-on-demand**
</dt> <dd>

Service that installs applications or features as requested by the user or another application. [*Advertising*](a-gly.md) makes a feature or application available for install-on-demand installation. For more information, see: [Installation-on-Demand](installation-on-demand.md).

</dd> <dt>

<span id="_msi_installation_context_gly"></span><span id="_MSI_INSTALLATION_CONTEXT_GLY"></span>**installation context**
</dt> <dd>

The combination of installation rights and installation types produces three different installation contexts: per-user non-managed, per-user managed, and per-machine managed. There is no such thing as per-machine non-managed.

</dd> <dt>

<span id="_msi_installer_gly"></span><span id="_MSI_INSTALLER_GLY"></span>**installer**
</dt> <dd>

The [*Windows Installer*](m-gly.md).

</dd> <dt>

<span id="_msi_installer_database_gly"></span><span id="_MSI_INSTALLER_DATABASE_GLY"></span>**installer database**
</dt> <dd>

Relational database containing setup instructions for an installation. The installer database is stored in the [*.msi file*](m-gly.md). For more information, see [Installer Database](installer-database.md).

</dd> <dt>

<span id="_msi_installer_function_gly"></span><span id="_MSI_INSTALLER_FUNCTION_GLY"></span>**installer function**
</dt> <dd>

Called by a user or application to obtain installer services and functionality. This is the application programming interface of the installer. For information, see [Installer Function Reference](installer-function-reference.md).

</dd> <dt>

<span id="_msi_installer_package_authoring_tool_gly"></span><span id="_MSI_INSTALLER_PACKAGE_AUTHORING_TOOL_GLY"></span>**installer package authoring tool**
</dt> <dd>

Software that enables a developer to create and edit an [*.msi file*](m-gly.md). This together with any [*external source files*](e-gly.md) comprise a [*package*](p-gly.md) containing all the information required for an installation.

</dd> <dt>

<span id="_msi_internal_source_files_gly"></span><span id="_MSI_INTERNAL_SOURCE_FILES_GLY"></span>**internal source files**
</dt> <dd>

Stored in the [*.msi file*](m-gly.md). Multiple internal source files can be compressed and stored together in a [*cabinet file*](c-gly.md) that is stored within an .msi file.

</dd> </dl>

 

 



