---
description: Learn about Windows Installer concepts that begin with the letter A, such as accessibility and acquisition phase.
ms.assetid: 541fd08c-c21a-4a51-aa1c-d65cc0f5da75
title: A (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# A (Windows Installer)

A [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) H [I](i-gly.md) J K L [M](m-gly.md) N [O](o-gly.md) [P](p-gly.md) [Q](q-gly.md) [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) W X Y Z

<dl> <dt>

<span id="_msi_accessibility_using_windows_installer_gly"></span><span id="_MSI_ACCESSIBILITY_USING_WINDOWS_INSTALLER_GLY"></span>**accessibility**
</dt> <dd>

Design implementation for making the installer's user interface accessible to all users. For more information about accessibility, see the overview topic: [Accessibility](accessibility.md).

</dd> <dt>

<span id="_msi_acquisition_phase_gly"></span><span id="_MSI_ACQUISITION_PHASE_GLY"></span>**acquisition phase**
</dt> <dd>

Phase of installation during which the installer determines procedure. Acquisition phase begins when an application or user instructs [*Windows Installer*](m-gly.md) to install an application or feature. The installer then queries the [*database*](i-gly.md) for information as it generates the [*execution script*](e-gly.md) for the installation. For more information about the phases of an installation, see [Installation Mechanism](installation-mechanism.md).

</dd> <dt>

<span id="_msi_action_gly"></span><span id="_MSI_ACTION_GLY"></span>**action**
</dt> <dd>

Many of the functions performed by Windows Installer are encapsulated into actions. Each action specifies the execution of a particular function and the total procedural flow of the installation is prescribed by the sequence of actions in the [*Sequence tables*](s-gly.md). [*Standard actions*](s-gly.md) are built into Windows Installer. [*Custom actions*](c-gly.md) are written by the author of the installation [*package*](p-gly.md).

</dd> <dt>

<span id="_msi_admin_approval_mode_gly"></span><span id="_MSI_ADMIN_APPROVAL_MODE_GLY"></span>**Admin Approval Mode**
</dt> <dd>

The approval state enabled by User Account Protection (UAC) that runs all users with least privilege, including administrators. Users are required to provide consent to elevate installations that require administrator privileges.

</dd> <dt>

<span id="_msi_advertising_gly"></span><span id="_MSI_ADVERTISING_GLY"></span>**advertising**
</dt> <dd>

Capability to make the interfaces required for loading and to make an application available without installing the application. When a user or application activates an advertised interface, the installer then proceeds to install the necessary components. The two types of advertising are [*assigning*](/windows) and [*publishing*](p-gly.md). For more information, see also [*install-on-demand*](i-gly.md). For more information about how the installer advertises applications, see [Advertisement](advertisement.md).

</dd> <dt>

<span id="_msi_application_information_service_gly"></span><span id="_MSI_APPLICATION_INFORMATION_SERVICE_GLY"></span>**Application Information Service (AIS)**
</dt> <dd>

A system service of Windows Vista that facilitates starting installations that require elevated privileges to run. Provides the Consent UI used by User Account Control to prompt a user for administrator authorization.

</dd> <dt>

<span id="_msi_assigning_gly"></span><span id="_MSI_ASSIGNING_GLY"></span>**assigning**
</dt> <dd>

Makes an application available, and makes it appear as if it has been installed to a user, without actually installing it. Assigning adds shortcuts and icons to the **Start** menu, associates appropriate files, and writes registry entries for the application. When a user tries to open an assigned application, then the installer installs the application. Assigning and [*publishing*](p-gly.md) are two methods of [*advertising*](/windows). For more information, see [Advertisement](advertisement.md).

</dd> <dt>

<span id="_msi_asynchronous_execution_using_windows_installer_gly"></span><span id="_MSI_ASYNCHRONOUS_EXECUTION_USING_WINDOWS_INSTALLER_GLY"></span>**asynchronous execution**
</dt> <dd>

[*Custom action*](c-gly.md) during which the installer runs separate threads of the custom action and the current installation simultaneously. For more information, see [Synchronous and Asynchronous Custom Actions](synchronous-and-asynchronous-custom-actions.md).

</dd> </dl>

 

 
