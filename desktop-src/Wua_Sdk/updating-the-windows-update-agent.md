---
description: Windows Update Agent (WUA) automatically updates itself when it is connected to a Windows Server Update Services (WSUS) server or to Windows Update.
ms.assetid: 829112ab-b240-4cc4-8053-18b484934886
title: Updating Windows Update Agent
ms.topic: article
ms.date: 05/31/2018
---

# Updating Windows Update Agent

Windows Update Agent (WUA) updates itself through various means, depending on the version of Windows running on the device. Old versions of WUA may not be able to connect to current update services, may not be compatible with all updates, and may not support all documented APIs. Here is how to insure that WUA is fully updated and compatible.

**On versions of Windows beginning with Windows 7 and Windows Server 2008 R2**

Windows Update Agent (WUA) updates are included in the regular periodic updates to Windows distributed through Windows Update or to Windows Server Update Services (WSUS). You do not need to take any special steps to update WUA on these Windows versions.

**On versions of Windows prior to Windows 7 and Windows Server 2008 R2**

WUA automatically updates itself when Automatic Updates connects to Windows Update or to WSUS.

If Automatic Updates has not yet successfully run, it is possible that a device running these Windows versions will be running an older version of WUA that does not support all the documented APIs. If you receive a WU_E_SELFUPDATE_REQUIRED result when you use the WUA API to perform a scan, download, or install, this error tells you that the installed version of WUA is too old to connect to current Windows Update services. You cannot use the normal WUA APIs to update WUA on these operating systems. 

A user can manually update WUA to a current version by opening the Windows Update control panel, selecting Check for Updates, then accepting the self-update that appears. Alternately, you can update WUA programmatically.

**To programmatically update WUA on versions of Windows prior to Windows 7 and Windows Server 2008 R2**

1.  Use the [WinHTTP](../winhttp/winhttp-start-page.md) APIs to download [Wuredist.cab](https://update.microsoft.com/redist/wuredist.cab).
2.  Use the [Cryptography Functions](../seccrypto/cryptography-functions.md) to verify that the downloaded copy of [Wuredist.cab](https://update.microsoft.com/redist/wuredist.cab) has a digital signature from Microsoft. If you can't verify the digital signature, stop.
3.  Use the [File Decompression Interface](../devnotes/cabinet-api-functions.md) APIs to extract the XML file from [Wuredist.cab](https://update.microsoft.com/redist/wuredist.cab).
4.  Use the Microsoft XML Core Services ([MSXML](/previous-versions/windows/desktop/ms763742(v=vs.85))) APIs to load the XML file and locate the WURedist/StandaloneRedist/architecture node for the computer's architecture. For example, for x86, locate the WURedist/StandaloneRedist/architecture node with the **name** attribute of x86.
5.  Call [**IWindowsUpdateAgentInfo::GetInfo**](/windows/desktop/api/Wuapi/nf-wuapi-iwindowsupdateagentinfo-getinfo) to determine the current version of WUA. If **IWindowsUpdateAgentInfo::GetInfo** returns a version number that is at least as high as the **clientVersion** attribute in the architecture node you located, stop.
6.  Use the [MSXML](/previous-versions/windows/desktop/ms763742(v=vs.85)) APIs to read the **downloadUrl** attribute from the architecture node that you located. **downloadUrl** gives you the download URL for the appropriate WUA installer for the computer's architecture.
7.  Use the [WinHTTP](../winhttp/winhttp-start-page.md) APIs to download the appropriate installer.
8.  Use the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function or a similar API to execute the downloaded installer.

 

 
