---
description: Determine the version of Windows Update Agent (WUA) before you use it.
ms.assetid: fc915535-f87d-43fb-8755-fa6c80fedea5
title: Determining the Current Version of WUA
ms.topic: article
ms.date: 05/31/2018
---

# Determining the Current Version of WUA

For general information on updating the WUA, including step by step instructions to programmatically determine from within your app whether the version of WUA that is running on the computer meets your needs, see [Updating the Windows Update Agent](updating-the-windows-update-agent.md).

On versions of Windows prior to Windows 7 and Windows Server 2008 R2, you should determine the installed version of Windows Update Agent (WUA) before you use it. The current version of WUA is determined by the version of the Wuaueng.dll that is running in the \\System32 subdirectory of the current Windows installation. If the version of Wuaueng.dll is version 5.4.3790.1000 or a later version, WUA is installed. A version that is earlier than 5.4.3790.1000 indicates that Software Update Services (SUS) 1.0 is installed.

When a call is made to SUS 1.0 by using the WUA API, an **HRESULT** of WU\_E\_AU\_LEGACYSERVER is returned.

You can also use the [**IWindowsUpdateAgentInfo::GetInfo**](/windows/desktop/api/Wuapi/nf-wuapi-iwindowsupdateagentinfo-getinfo) method to retrieve the current file version of Wuapi.dll that is running on a computer. The [**IWindowsUpdateAgentInfo**](/windows/desktop/api/Wuapi/nn-wuapi-iwindowsupdateagentinfo) interface is not supported in WUA 1.0.
