---
description: File Library Replaces Document Folder
ms.assetid: 80b97bfc-4212-4401-a4a9-d96e2f39be60
title: File Library Replaces Document Folder
ms.topic: article
ms.date: 05/31/2018
---

# File Library Replaces Document Folder

## Affected Platforms

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

**Severity** - Medium  
**Frequency** - High  











## Description

Libraries provide a centralized folder-like experience for file storage, search, and access across multiple locations, both local and remote.

The default locations used by common file dialogs (for example, Open, and Save) have been changed from the Document Folder to the Documents Library. The User Interface is unchanged, but the user will now be able to view, browse, and search the Library using various arrangement views. Files will be saved into the Library default save location unless the user changes the default save location or chooses a different folder.

Developers could create their own libraries or add locations to existing libraries using the IShellLibrary interface. Users can find libraries by using the Known Folder system (for example, FOLDERID\_DocumentsLibrary).

## Manifestation of Impact

The Library is itself a file, and not a folder. Therefore, path manipulations could result errors due to the attempt by the application to concatenate files to files.

## Solution

When using IFileDialog, you must use GetResult method instead of combination of GetFolder and GetFilename as you would in the previous operating system versions. Use the Shell APIs where possible to interact with and manipulate items in the Shell Namespace (for example, IShellItem).

## Leveraging Feature Capabilities

If you want to create your own libraries or add locations to existing libraries, you must use IShellLibrary API. Libraries are themselves Shell Folders so you can enumerate them just like any other Shell Folder.

## Compatibility, Performance, Reliability, and Usability Testing

Using the common file dialog will ensure that users can save directly to their libraries.

## Links to Other Resources

-   **Windows Libraries:** https://msdn.microsoft.com/library/dd758096(VS.85).aspx
-   **Keeping in sync with a library:** https://msdn.microsoft.com/library/dd758094(VS.85).aspx\#library\_keeping\_in\_sync

 

 



