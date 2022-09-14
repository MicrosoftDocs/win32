---
description: The RegOpenUserClassesRoot function provides a merged view for processes, such as services, that are dealing with clients other than the interactive user.
ms.assetid: 3815d487-2d58-4ba8-85d2-cae6a642a791
title: Merged View of HKEY_CLASSES_ROOT
ms.topic: article
ms.date: 05/31/2018
---

# Merged View of HKEY\_CLASSES\_ROOT

The [**RegOpenUserClassesRoot**](/windows/desktop/api/Winreg/nf-winreg-regopenuserclassesroot) function provides a merged view for processes, such as services, that are dealing with clients other than the interactive user. In this case, the **HKEY\_CLASSES\_ROOT** key provides a view of the registry that merges the information from **HKEY\_LOCAL\_MACHINE\\Software\\Classes** with the information from **HKEY\_CURRENT\_USER\\Software\\Classes**.

The system uses the following rules to merge information from the two sources:

-   The merged view includes all subkeys of the **HKEY\_CURRENT\_USER\\Software\\Classes** key.
-   The merged view includes all immediate subkeys of the **HKEY\_LOCAL\_MACHINE\\Software\\Classes** key that do not duplicate the subkeys of **HKEY\_CURRENT\_USER\\Software\\Classes**.
-   At the end of this topic is a list of subkeys that are found in both **HKEY\_LOCAL\_MACHINE\\Software\\Classes** and **HKEY\_CURRENT\_USER\\Software\\Classes**. The immediate subkeys of these keys from the **HKEY\_LOCAL\_MACHINE** tree are included in the merged view only if they are not duplicates of immediate subkeys from the **HKEY\_CURRENT\_USER** tree. The merged view does not include the **HKEY\_LOCAL\_MACHINE** contents of duplicate subkeys.

If an application is run with administrator rights and User Account Control is disabled, the COM runtime ignores per-user COM configuration and accesses only per-machine COM configuration. Applications that require administrator rights should register dependent COM objects during installation to the per-machine COM configuration store (**HKEY\_LOCAL\_MACHINE\\Software\\Classes**). For more information, see [AC: UAC: COM Per-User Configuration](/previous-versions/bb756926(v=msdn.10)).

**Windows Server 2003 and Windows XP/2000:** Applications can register dependent COM objects to either the per-machine or per-user COM configuration store (**HKEY\_LOCAL\_MACHINE\\Software\\Classes** or **HKEY\_CURRENT\_USER\\Software\\Classes**).

The following example shows a set of subkeys under the **HKEY\_LOCAL\_MACHINE** and **HKEY\_CURRENT\_USER** keys and the resulting merged view of **HKEY\_CLASSES\_ROOT**.

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes**    **CLSID**       *2*       *4*          **inprocserver32**          **localserver32**       *7*

**HKEY\_CURRENT\_USER\\Software\\Classes**    **CLSID**       *1*       *4*          **localserver**       *6*       *10*          **localserver**

**HKEY\_CLASSES\_ROOT**    **CLSID**       *1*       *2*       *4*          **inprocserver32**          **localserver**          **localserver32**       *6*       *7*       *10*          **localserver**

The following subkeys are found in both **HKEY\_LOCAL\_MACHINE\\Software\\Classes** and **HKEY\_CURRENT\_USER\\Software\\Classes**. From the **HKEY\_LOCAL\_MACHINE** tree, the immediate subkeys of these keys are included in the merged view only if they are not duplicates of immediate subkeys from the **HKEY\_CURRENT\_USER** tree. The merged view does not include the **HKEY\_LOCAL\_MACHINE** contents of duplicate subkeys.

**\***  
**\*\\shellex**  
**\*\\shellex\\ContextMenuHandlers**  
**\*\\shellex\\PropertySheetHandlers**  
**AppID**  
**ClsID**  
**Component Categories**  
**Drive**  
**Drive\\shellex**  
**Drive\\shellex\\ContextMenuHandlers**  
**Drive\\shellex\\PropertySheetHandlers**  
**FileType**  
**Folder**  
**Folder\\shellex**  
**Folder\\shellex\\ColumnHandler**  
**Folder\\shellex\\ContextMenuHandlers**  
**Folder\\shellex\\ExtShellFolderViews**  
**Folder\\shellex\\PropertySheetHandlers**  
**Installer\\Components**  
**Installer\\Features**  
**Installer\\Products**  
**Interface**  
**Mime**  
**Mime\\Database**  
**Mime\\Database\\Charset**  
**Mime\\Database\\Codepage**  
**Mime\\Database\\Content Type**  
**Typelib**  


 

 
