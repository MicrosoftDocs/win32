---
Description: Windows Update Agent (WUA) automatically updates itself when it is connected to a Windows Server Update Services (WSUS) server or to Windows Update.
ms.assetid: 829112ab-b240-4cc4-8053-18b484934886
title: Updating Windows Update Agent
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Updating Windows Update Agent

Windows Update Agent (WUA) automatically updates itself when it is connected to a Windows Server Update Services (WSUS) server or to Windows Update. You can also use a signed installation package that is available from Microsoft to manually update WUA. You can use this installation package to install the latest released versions of WUA or the latest released versions of the Muauth.cab file. Here we explain how you can programmatically determine whether the version of WUA that is running on the computer meets your needs, that is, whether the version is the latest or at least current enough.

You can call the [**IWindowsUpdateAgentInfo::GetInfo**](/windows/desktop/api/Wuapi/nf-wuapi-iwindowsupdateagentinfo-getinfo) method to get current version info about WUA, but you can't determine if that version is the latest. If you receive a **WU\_E\_SELFUPDATE\_REQUIRED** error message when you use the WUA API to perform a scan, download, or install, this error tells you that the version of WUA is out of date. But even if you know the version of WUA is out of date, you can't use the WUA API to force a self-update. Additionally, if Windows Update on the computer is in such a state that automatic self-updates are failing, you can't use the WUA API to recover from that state. When necessary, to ensure that users have the latest WUA, prompt them to install [KB949104](http://support.microsoft.com/kb/949104) or the latest WUA.

Follow these steps in your app to determine whether or not the running version of WUA is the most recent one (or at least a current one). If the running version of WUA is too old or if WUA isn't running at all, install the most recent version of WUA (or at least a current version of WUA).

**To ensure that an appropriate version of WUA is installed**

1.  Use the [WinHTTP](https://msdn.microsoft.com/library/Aa384273(v=VS.85).aspx) APIs to download [Wuredist.cab](http://update.microsoft.com/redist/wuredist.cab).
2.  Use the [Cryptography Functions](https://msdn.microsoft.com/library/Aa380252(v=VS.85).aspx) to verify that the downloaded copy of [Wuredist.cab](http://update.microsoft.com/redist/wuredist.cab) has a digital signature from Microsoft. If you can't verify the digital signature, stop.
3.  Use the [File Decompression Interface](https://msdn.microsoft.com/en-us/library/Ff797921(v=VS.85).aspx) APIs to extract the XML file from [Wuredist.cab](http://update.microsoft.com/redist/wuredist.cab).
4.  Use the Microsoft XML Core Services ([MSXML](https://msdn.microsoft.com/en-us/library/ms763742(v=VS.85).aspx)) APIs to load the XML file and locate the WURedist/StandaloneRedist/architecture node for the computer's architecture. For example, for x86, locate the WURedist/StandaloneRedist/architecture node with the **name** attribute of x86.
5.  Call [**IWindowsUpdateAgentInfo::GetInfo**](/windows/desktop/api/Wuapi/nf-wuapi-iwindowsupdateagentinfo-getinfo) to determine the current version of WUA. If **IWindowsUpdateAgentInfo::GetInfo** returns a version number that is at least as high as the **clientVersion** attribute in the architecture node you located, stop.
6.  Use the [MSXML](https://msdn.microsoft.com/en-us/library/ms763742(v=VS.85).aspx) APIs to read the **downloadUrl** attribute from the architecture node that you located. **downloadUrl** gives you the download URL for the appropriate WUA installer for the computer's architecture.
7.  Use the [WinHTTP](https://msdn.microsoft.com/library/Aa384273(v=VS.85).aspx) APIs to download the appropriate installer.
8.  Use the [**CreateProcess**](https://msdn.microsoft.com/library/ms682425(v=VS.85).aspx) function or a similar API to execute the downloaded installer.

 

 



