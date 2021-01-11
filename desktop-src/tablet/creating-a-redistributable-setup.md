---
description: To distribute an ink-enabled application to computers that are not running either Windows Vista or Windows XP Tablet PC Edition 2005 (that is, computers running Windows XP, Windows Server 2003, or Windows 2000), you must include the necessary merge modules in your setup.
ms.assetid: 97515703-0bf4-4230-ae35-181b48b70c40
title: Creating a Redistributable Setup
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Redistributable Setup

To distribute an ink-enabled application to computers that are not running either Windows Vista or Windows XP Tablet PC Edition 2005 (that is, computers running Windows XP, Windows Server 2003, or Windows 2000), you must include the necessary merge modules in your setup.

The Mstpcrt.msm merge module includes all of the files, resources, registry entries, and setup logic necessary for Windows Installer to install the shared files that other platforms require to run unmanaged applications developed for the Tablet PC. Mstpcrt.msm is consumed by Windows Installer (.msi) files. For applications that use the [**InkDivider**](inkdivider-class.md) object, you must also redistribute InkDiv.msm. For applications that use managed components, you must also include the merge module files for those managed components.

The following table describes the merge module files that ship with the Windows XP Tablet PC Edition Software Development Kit (SDK).



| Redistributable Merge Module | Description                                                                                                                    | Files                                                       |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| InkDiv.msm<br/>        | Installs the unmanaged version of the [**InkDivider**](inkdivider-class.md) object.<br/>                                | InkDiv.dll<br/>                                       |
| Mstpcrt.msm<br/>       | Installs the unmanaged components of the Tablet PC Platform version 1.0.<br/>                                            | Gdiplus.dll, InkEd.dll, Tpcps.dll, Wisptis.exe<br/>   |
| Msvcp60.msm<br/>       | Installs components of the Microsoft Visual C++ runtime.<br/>                                                            | Msvcp60.dll<br/>                                      |
| Msvcrt.msm<br/>        | Installs components of the Microsoft Visual C runtime.<br/>                                                              | Msvcrt.dll<br/>                                       |
| Tpcman17.msm<br/>      | Installs the managed components of the Tablet PC Platform runtime. Requires that the mstpcrt.msm file is installed.<br/> | Microsoft.Ink.dll, Microsoft.Ink.resources.dll<br/>   |
| iaCOM.msm<br/>         | Installs the Automation components of the InkAnalysis API.<br/>                                                          | IACom.dll<br/>                                        |
| iacore.msm<br/>        | Installs the base class components of the InkAnalysis API.<br/>                                                          | IACore.dll<br/> IALoader.dll<br/>               |
| IAWinFrm.msm<br/>      | Installs the managed library components of the InkAnalysis API.<br/>                                                     | Microsoft.Ink.Analysis.dll<br/>                       |
| IAWinFX.msm<br/>       | Installs the Windows Presentation Foundation components of the InkAnalysis API.<br/>                                     | IAWinFX.dll<br/>                                      |
| journal.msm<br/>       | Installs the Journal Reader components.<br/>                                                                             | Journal.dll<br/> Microsoft.ink.journal.dll<br/> |
| rtscom.msm<br/>        | Installs the Automation components of the StylusInput namespace.<br/>                                                    | Rtscom.dll<br/>                                       |



 

> [!Note]  
> To use the functionality of the Microsoft .NET Framework that is included in merge modules for managed components, you must have installed Service Pack 2 of the Framework on the target computer.

 

## Reduced Feature Set

Ink-enabled applications treat mouse events as pen movements to simulate working with a tablet pen. Users can add ink, erase ink, and save ink documents. However, recognition and gestures are not available for users other than those running Windows XP Tablet PC Edition.

Mstpcrt.msm does not include Windows Journal or Tablet PC Input Panel.

The [**PenInputPanel**](peninputpanel-class.md) object does not function on any operating systems besides Windows XP Tablet PC Edition.

## Deployment

> [!Note]  
> If your application uses managed code, you must also deploy the Framework. The Framework must be installed before your Tablet PC managed assemblies are installed.

 

To include Mstpcrt.msm in a Microsoft Visual Studio .NET Setup project:

1.  In the Solution Explorer, select your Setup project.
2.  On the Project menu, click **Add**, and then click **Merge Module**.
    > [!Note]  
    > You can also reach the **Add Modules** dialog box by right-clicking the installer project name in the Solution Explorer, clicking **Add**, and then selecting **Merge Module**.

     

3.  In the **Add Modules** dialog box, navigate to and select **Mstpcrt.msm**.
4.  Click **Open**.

Mstpcrt.msm is added to your Setup project and appears in the Solution Explorer window.

Windows Installer adds the files contained in the merge module to the Program Files folder. To use these files, end users must be logged on with an account that has access to the Program Files folder.

> [!Note]  
> You must add [SelfRegModules Action](../msi/selfregmodules-action.md) and [SelfUnregModules Action](../msi/selfunregmodules-action.md) actions to the installation sequence. The [MsiPublishAssemblies Action](../msi/msipublishassemblies-action.md) and [MsiUnpublishAssemblies Action](/windows/desktop/Msi/msiunpublishassemblies-action) actions receive their order in the installation sequence from these actions.

 

 

