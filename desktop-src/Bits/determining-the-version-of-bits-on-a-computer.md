---
title: Determining the Version of BITS on a Computer
description: To determine the version of BITS on the client computer, check the version of QMgr.dll.
ms.assetid: b6057ae4-3bf0-4304-ae50-5da5e82a0bed
ms.topic: article
ms.date: 05/31/2018
---

# Determining the Version of BITS on a Computer

To determine the version of BITS on the client computer, check the version of QMgr.dll. To find the version number of the DLL:

-   Locate QMgr.dll in %windir%\\System32.
-   Right-click QMgr.dll and click **Properties**.
-   Click the **Version** tab.
-   Note the version number.

You can also use the following PowerShell code to determine the version of the .dll on your system:

`get-item "C:\Windows\System32\qmgr.dll" | Select-Object -ExpandProperty VersionInfo`

If the DLL also exists in %windir%\\System32\\Bits, repeat the previous steps. BITS uses the DLL with the higher version number.

The following table lists the versions of BITS and their corresponding QMgr.dll file version numbers.



| BITS version | QMgr.dll file version number |
|--------------|------------------------------|
| BITS 10.1    | 7.8.xxxx.xxxx                |
| BITS 5.0     | 7.7.xxxx.xxxx                |
| BITS 4.0     | 7.5.xxxx.xxxx                |
| BITS 3.0     | 7.0.xxxx.xxxx                |
| BITS 2.5     | 6.7.xxxx.xxxx                |
| BITS 2.0     | 6.6.xxxx.xxxx                |
| BITS 1.5     | 6.5.xxxx.xxxx                |
| BITS 1.2     | 6.2.xxxx.xxxx                |
| BITS 1.0     | 6.0.xxxx.xxxx                |



 

You can also use the symbolic class identifiers to determine the version of BITS that is registered on the computer. The following table lists the versions of BITS and their corresponding symbolic class identifiers. The **CoCreateInstance** function returns **REGDB\_E\_CLASSNOTREG** if the class is not registered.



| BITS version  | Symbolic class identifier         |
|---------------|-----------------------------------|
| BITS 10.1     | CLSID\_BackgroundCopyManager10\_1 |
| BITS 5.0      | CLSID\_BackgroundCopyManager5\_0  |
| BITS 4.0      | CLSID\_BackgroundCopyManager4\_0  |
| BITS 3.0      | CLSID\_BackgroundCopyManager3\_0  |
| BITS 2.5      | CLSID\_BackgroundCopyManager2\_5  |
| BITS 2.0      | CLSID\_BackgroundCopyManager2\_0  |
| BITS 1.5      | CLSID\_BackgroundCopyManager1\_5  |
| BITS 1.2, 1.0 | CLSID\_BackgroundCopyManager      |



 

 

 




