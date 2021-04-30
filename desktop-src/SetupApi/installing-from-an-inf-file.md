---
description: After you retrieve installation information from an INF file, there are several file-handling functions that you can use to install the files listed in an INF section.
ms.assetid: 4e6042a0-36a9-4f74-b6cc-554e7f7aa2d9
title: Installing From an INF File
ms.topic: article
ms.date: 05/31/2018
---

# Installing From an INF File

After you retrieve installation information from an INF file, there are several file-handling functions that you can use to install the files listed in an INF section. Low-level functions such as [**SetupInstallFile**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfilea) and [**SetupInstallFileEx**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfileexa) install a single file.

There are also functions to handle compressed files. The [**SetupGetFileCompressionInfo**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetfilecompressioninfoa) function returns information about compressed files. This information can then be used by [**SetupDecompressOrCopyFile**](/windows/desktop/api/Setupapi/nf-setupapi-setupdecompressorcopyfilea) to copy and, if necessary, expand the file.

High-level functions such as [**SetupInstallFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfrominfsectiona), [**SetupInstallFilesFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfilesfrominfsectiona), and [**SetupInstallServicesFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallservicesfrominfsectiona) process the installation operations in an **Install** or **Service** section. Of these, **SetupInstallFromInfSection** is the most versatile because it can perform any type of installation operation listed in the **Install** section of an INF file. This includes the registry and INI operations listed in the **AddReg**, **DelReg**, **UpdateInis**, or **UpdateIniField** lines of an **Install** section.

The [**SetupInstallFilesFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfilesfrominfsectiona) and [**SetupInstallServicesFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallservicesfrominfsectiona) functions queue operations from an **Install** or **Service** section, respectively, to an existing file queue. Note that you must call SetupInstallFromInfSection and SetupInstallServicesFromInfSection separately to queue operations and services. For more information, see [File Queues](file-queues.md).

In contrast, the [**SetupInstallFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfrominfsectiona) function creates and destroys its own internal queue. A common use for **SetupInstallFromInfSection** is to call it after all files have been successfully copied to perform the registry and INI transactions.

On Windows 2000, DLL files may be self-registered by calling [**SetupInstallFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfrominfsectiona) on an INF file that includes the **RegisterDlls** directive in its **Install** section. **SetupInstallFromInfSection** can also self-register 32-bit DLLs from a 64-bit process.

On 64-bit operating systems, [**SetupInstallFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfrominfsectiona) may be called to perform operations on the 32-bit portion of the registry. To add a registry key to the 32-bit portion of the registry, include the FLG\_ADDREG\_32BITKEY flag in the **AddReg** line of the INF. To delete a registry key only in the 32-bit portion of the registry, include the FLG\_DELREG\_32BITKEY key in the **DelReg** line. To set or clear a binary value only in the 32-bit portion of the registry, include the FLG\_BITREG\_32BITKEY in the **BitReg** line.

In addition to the functions previously listed, the Setup API includes functions that queue file installation operations, either by file, or by INF section. For more information, see [File Queues](file-queues.md).

 

 



