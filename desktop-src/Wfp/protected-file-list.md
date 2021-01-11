---
description: Protected Resource List
ms.assetid: 70413c13-3db0-4af0-b584-259cce70f084
title: Protected Resource List
ms.topic: article
ms.date: 05/31/2018
---

# Protected Resource List

Permission for full access to modify WRP-protected resources is restricted to TrustedInstaller. WRP-protected resources can be changed only using the [Supported Resource Replacement Mechanisms](supported-file-replacement-mechanisms.md) with the Windows Modules Installer service.

WRP protects files with the following extensions that are installed by Windows Server 2008 or Windows Vista: .dll, .exe, .ocx, and .sys.

WRP protects critical files that are installed by Windows Server 2008 or Windows Vista with the following extensions: .acm, .ade, .adp, .app, .asa, .asp, .aspx, .ax, .bas, .bat, .bin, .cer, .chm, .clb, .cmd, .cnt, .cnv, .com, .cpl, .cpx, .crt, .csh, .dll, .drv, .dtd, .exe, .fxp, .grp, .h1s, .hlp, .hta, .ime, .inf, .ins, .isp, .its, .js, .jse, .ksh, .lnk, .mad, .maf, .mag, .mam, .man, .maq, .mar, .mas, .mat, .mau, .mav, .maw, .mda, .mdb, .mde, .mdt, .mdw, .mdz, .msc, .msi, .msp, .mst, .mui, .nls, .ocx, .ops, .pal, .pcd, .pif, .prf, .prg, .pst, .reg, .scf, .scr, .sct, .shb, .shs, .sys, .tlb, .tsp, .url, .vb, .vbe, .vbs, .vsmacros, .vss, .vst, .vsw, .ws, .wsc, .wsf, .wsh, .xsd, and .xsl.

WRP protects critical folders. A folder containing only WRP-protected files may be locked so that only the Windows trusted installer is able to create files or subfolders in the folder. A folder may be partially locked to enable Administrators to create files and subfolders in the folder.

WRP protects essential registry keys installed by Windows Server 2008 and Windows Vista. If a key is protected by WRP, all its subkeys and values can be protected.

WRP copies files that are needed to restart Windows in the *cache directory* located at %Windir%\\winsxs\\Backup. Critical files that are not needed to restart Windows are not copied to the cache directory. The size of the cache directory and the list of files copied to cache cannot be modified.

**Windows Server 2003 and Windows XP:  **

Windows File Protection (WFP) preceded WRP.

WFP protects files that are installed by Windows with the following extensions: .dll, .exe, .ocx, and .sys. In addition, the TrueType fonts Micross.ttf, Tahoma.ttf, and Tahomabd.ttf are also protected.

At the end of the Windows installation, WFP runs a scan of all protected files to ensure they have not been modified by applications installed through unattended installation. WFP also copies verified versions of these system files to the cache directory. When an application attempts to replace a protected file, WFP can restore the original file from the cache directory.

The default value is %systemroot%\\system32\\dllcache. To specify a different location for the cache, create the following registry value: **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SFCDllCacheDir**

This must be a local path. Using a network path creates a single shared network source for cache files, provided all clients using the share are running the same service packs and hotfixes.

The default size of the cache is unlimited. To change the size of the cache, use the following registry setting: **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SFCQuota**

If the value is SFC\_QUOTA\_ALL\_FILES, all system files will be cached in the cache directory.

Due to disk space considerations, it may not be desirable to maintain cached versions of all system files in the cache directory. Depending on the size of the cache, WFP will store verified file versions in the cache directory on the system hard drive. WFP will add files to the cache until the size of the cache directory reaches the specified limit.

When an application attempts to replace a protected file that is not in the cache, WFP attempts to restore the original file from the installation source, prompting the user if necessary.

 

 



