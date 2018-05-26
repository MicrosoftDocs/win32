---
Description: Active Directory Rights Management Services (AD RMS) requires applications that use a lockbox to also use a manifest to identify the files that can or must be loaded into a process space and files that must not be loaded.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7dafa3de-8fa3-4c64-adda-a540755ad2fb
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Malicious Software
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Malicious Software

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Active Directory Rights Management Services (AD RMS) requires applications that use a lockbox to also use a manifest to identify the files that can or must be loaded into a process space and files that must not be loaded. This helps prevent other applications, namely viruses, from running in the same space as your application. It also helps prevent an attacker from surreptitiously replacing DLLs with malicious modules. Microsoft has defined minimum required standards that your application must meet to protect content from malicious software.

-   [Loading Unprotected Libraries](#loading-unprotected-libraries)
-   [Importing Malicious Software by Using Address Tables](#importing-malicious-software-by-using-address-tables)
-   [Related topics](#related-topics)

## Loading Unprotected Libraries

An application can load external libraries in a variety of ways. However, an AD RMS application should only load libraries enumerated in a manifest and only by calling AD RMS functions. That is, you can load libraries by calling [**DRMInitEnvironment**](/windows/previous-versions/Msdrm/nf-msdrm-drminitenvironment?branch=master) once when initializing a secure environment or by calling [**DRMLoadLibrary**](/windows/previous-versions/Msdrm/nf-msdrm-drmloadlibrary?branch=master) multiple times during program execution.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Standard level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Minimum standard</td>
<td>Use AD RMS functions, when possible, to load DLLs, executable files, and libraries enumerated in the manifest. Include in the manifest your primary process and any module that calls into Msdrm.dll. This is required unless you use a lockbox, and we recommend it even then.</td>
</tr>
<tr class="even">
<td>Recommended standard</td>
<td>Include in your manifest modules that manipulate protected content. If your application sends decrypted content to a system DLL or places the content in a location prescribed by a system DLL, that DLL should be included in the module list section of the manifest. If the DLL is signed in a system catalog (.cat) file, it is sufficient to include the Microsoft catalog file signing certificates in the policy section of the manifest.When loading libraries, use only the AD RMS [<strong>DRMInitEnvironment</strong>](/windows/previous-versions/Msdrm/nf-msdrm-drminitenvironment?branch=master) or [<strong>DRMLoadLibrary</strong>](/windows/previous-versions/Msdrm/nf-msdrm-drmloadlibrary?branch=master) functions, not the [<strong>LoadLibrary</strong>](https://msdn.microsoft.com/library/windows/desktop/ms684175) or [<strong>CoCreateInstance</strong>](_com_cocreateinstance) methods.<br/> Specify in the manifest any library that accesses content, including any third-party plug-in called by your application.<br/> The following recommendations help ensure that malicious software cannot be injected into the environment where decrypted information is available:
<ul>
<li>When any optional module (such as a module loaded by the [<strong>LoadLibrary</strong>](https://msdn.microsoft.com/library/windows/desktop/ms684175) or [<strong>CoCreateInstance</strong>](_com_cocreateinstance) methods) is loaded in the AD RMS environment after the environment is created, you should notify AD RMS by calling [<strong>DRMLoadLibrary</strong>](/windows/previous-versions/Msdrm/nf-msdrm-drmloadlibrary?branch=master) for that module.</li>
<li>Prior to unloading a module loaded by using [<strong>DRMLoadLibrary</strong>](/windows/previous-versions/Msdrm/nf-msdrm-drmloadlibrary?branch=master), you must notify AD RMS by calling [<strong>DRMCloseHandle</strong>](/windows/previous-versions/Msdrm/nf-msdrm-drmclosehandle?branch=master).</li>
</ul>
<br/></td>
</tr>
<tr class="odd">
<td>Preferred standard</td>
<td>None at this time.</td>
</tr>
</tbody>
</table>



 

## Importing Malicious Software by Using Address Tables

AD RMS does not support code modification at run time or modification of the import address table (IAT). An import address table is created for every DLL loaded in your process space. It specifies the addresses of all functions that your application imports. One common attack is to modify the IAT entries within an application to, for example, point to malicious software. AD RMS stops the application when it detects this type of attack.



| Standard level       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum standard     | You cannot modify the import address table in the application process during execution.Your application specifies many of the functions called at run time by using address tables, and these cannot be altered during or after run time. Among other things, this means you cannot perform code-profiling on an application signed by using the production certificate.<br/> You cannot call the [**DebugBreak**](https://msdn.microsoft.com/library/windows/desktop/ms679297) function from within any DLL specified in the manifest.<br/> You cannot call [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) with the **DONT\_RESOLVE\_DLL\_REFERENCES** flag set. This flag tells the loader to skip binding to the imported modules, thereby modifying the import address table.<br/> You cannot alter delayed loading by making run-time or subsequent changes to the **/DELAYLOAD** linker switch.<br/> You cannot alter delayed loading by providing your own version of the Delayimp.lib helper function.<br/> You cannot unload modules that have been delay-loaded by authenticated modules while the AD RMS environment exists. You cannot use the **/DELAY:UNLOAD** linker switch to enable unloading of delayed modules.<br/> |
| Recommended standard | None at this time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Preferred standard   | None at this time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Required Application Security Standards](required-application-security-standards.md)
</dt> </dl>

 

 




