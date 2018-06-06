---
Description: When the computer system is started, the Local Security Authority (LSA) automatically loads all registered security support provider/authentication package (SSP/AP) DLLs into its process space. The following illustrations show the initialization process.
ms.assetid: 2d52cbbf-9e28-4c6f-8b4c-448b73c6dbf8
title: LSA Mode Initialization
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LSA Mode Initialization

When the computer system is started, the [*Local Security Authority*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f) (LSA) automatically loads all registered [*security support provider*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50)/[*authentication package*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) (SSP/AP) DLLs into its process space. The following illustrations show the initialization process.

> [!Note]  
> "Kerberos" represents the Microsoft [*Kerberos*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33) SSP/AP, and "My SSP/AP" represents a custom SSP/AP that contains two custom security packages.

 

![lsa mode initialization](images/lsamode1.png)

At startup, the LSA calls the [**SpLsaModeInitialize**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-splsamodeinitializefn) function in each SSP/AP to obtain pointers to the functions implemented by each [*security package*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) in the DLL. The function pointers are passed to the LSA in an array of [**SECPKG\_FUNCTION\_TABLE**](/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-_secpkg_function_table) structures.

![the lsa calls splsamodeinitialize to get function pointers](images/lsamode2.png)

After receiving the set of [**SECPKG\_FUNCTION\_TABLE**](/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-_secpkg_function_table) structures, the LSA calls each security package's [**SpInitialize**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spinitializefn) function. The LSA uses this function call to pass each security package an [**LSA\_SECPKG\_FUNCTION\_TABLE**](/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-_lsa_secpkg_function_table) structure, which contains pointers to the LSA support functions available to security packages. In addition to storing the pointers to the LSA support functions, custom security packages should use their implementation of the **SpInitialize** function to perform any initialization-related processing.

For a list of the LSA support functions available to LSA-mode security packages, see [LSA Functions Called by SSP/APs](authentication-functions.md).

For information about registering an SSP/AP DLL, see [Registering SSP/AP DLLs](registering-ssp-ap-dlls.md).

 

 



