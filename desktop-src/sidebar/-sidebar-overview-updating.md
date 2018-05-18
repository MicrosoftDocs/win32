---
title: Gadgets for Windows Sidebar Packaging, Updating, and Refreshing
description: This overview describes how to install or refresh a gadget when updates are made to gadget files during development, debugging, and distribution.
ms.assetid: 'b3441515-744d-4b71-b25b-19d66c13864d'
keywords: ["Windows Sidebar,updates", "Sidebar,updates", "gadgets,updates", "Windows Sidebar,refreshing", "Sidebar,refreshing", "gadgets,refreshing", "Windows Sidebar,packaging", "Sidebar,packaging", "gadgets,packaging", "Windows Sidebar,ZIP files", "Sidebar,ZIP files", "gadgets,ZIP files", "Windows Sidebar,CAB files", "Sidebar,CAB files", "gadgets,CAB files", "Windows Sidebar,manifest", "Sidebar,manifest", "gadgets,manifest", "Windows Sidebar,Web services", "Sidebar,Web services", "gadgets,Web services"]
---

# Gadgets for Windows Sidebar Packaging, Updating, and Refreshing

\[ The Windows Gadget Platform/Sidebar is available for use in the following versions of Windows: Windows 7, Windows Vista, and Windows Server 2008. It may be altered or unavailable in subsequent versions. \]

This overview describes how to install or refresh a gadget when updates are made to gadget files during development, debugging, and distribution.

-   [Packaging a Sidebar Gadget](#packaging-a-sidebar-gadget)
-   [Development and Debugging](#development-and-debugging)
    -   [The Manifest](#the-manifest)
    -   [The Primary HTML, Script, or CSS Files](#the-primary-html-script-or-css-files)
    -   [The Settings and Flyout HTML, Script, or CSS Files](#the-settings-and-flyout-html-script-or-css-files)
-   [Distributing or Installing An Updated Gadget Package](#distributing-or-installing-an-updated-gadget-package)
-   [Gadgets and Web Services](#gadgets-and-web-services)

## Packaging a Sidebar Gadget

Gadgets can be deployed using one of the following methods:

-   A ZIP file. In this package type, the gadget files are collected and compressed into a single file. Many tools, including Windows itself, can create, extract, and edit ZIP files.

    A simple way to create a ZIP file is to deselect the **Hide extensions for known file types** option in the **Folder Options** dialog of Windows Explorer. Create a compressed folder. Copy all of your gadget files into the compressed folder. Change the extension from ".zip" to ".gadget".

-   A Windows cabinet (CAB) file. The CAB file can be code-signed to provide additional information to users.
-   A Windows Installer .msi file.

Both Gadget CAB files and ZIP files must have the .gadget extension. This enables Windows Sidebar to open the package when the user downloads or double-clicks the file.

> [!Note]  
> Some email servers are configured to detect and remove DHTML code when found inside attached files. CAB, ZIP, and gadget files are no exception. For this reason, you may want your gadget to be downloaded from a website.

 

## Development and Debugging

In most cases, it is not necessary to shut down and restart the Sidebar to see updates.

When revising gadget files directly in one of the gadget system folders (`%USER_DATA%\Local\Microsoft\Windows Sidebar\Gadgets` or `%SYSTEM_ROOT%\Program Files\Windows Sidebar\Gadgets`) or in a separate development environment, follow these steps:

### The Manifest

1.  Close the Gadget Picker, if open.
2.  Copy the updated manifest to the gadget folder, if necessary.
3.  Reopen the Gadget Picker.

### The Primary HTML, Script, or CSS Files

1.  Copy the updated files to the gadget folder, if necessary.
2.  Open the Gadget Picker, if necessary. The Gadget Picker does not need to be closed.
3.  Install the updated gadget.

> [!Note]  
> Any versions of the gadget added to the Sidebar prior to the update remain visible and continue to function as before.

 

### The Settings and Flyout HTML, Script, or CSS Files

1.  Close the gadget Settings, if open.
2.  Copy the updated files to the gadget folder, if necessary.

> [!Note]  
> The gadget does not need to be re-added to the Sidebar, the updated functionality will be available when the gadget settings, or the flyout, are re-displayed.

 

## Distributing or Installing An Updated Gadget Package

When installing an updated gadget package, it's advisable to uninstall any previous versions by right-clicking the gadget in the Gadget Picker and selecting "Uninstall" from the context menu. This deletes all pre-existing gadget files. Otherwise, installing an updated gadget by either a self-installing gadget package or copying selected files results in the same behavior described above.

## Gadgets and Web Services

Web services provide an alternative method for gadget developers to update their gadgets. Hosting business logic on a server and the presentation logic on the client (the gadget) allows for discrete updates with little to no intervention by end users.

 

 




