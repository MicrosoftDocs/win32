---
Description: The hardware configuration functions retrieve information such as processor, hardware profile, and keyboard information.
ms.assetid: c6245571-428a-4965-b58c-24645ddca70d
title: Hardware Configuration
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Hardware Configuration

The hardware configuration functions retrieve information such as processor, hardware profile, and keyboard information.

The [**GetSystemInfo**](/windows/win32/Winbase/?branch=master) function retrieves processor and memory information, such as the page size, original equipment manufacturer (OEM) identifier, number and type of processors, application address range, and so on. The [**IsProcessorFeaturePresent**](isprocessorfeaturepresent.md) function retrieves information about the floating-point operations and instruction sets supported by the processor.

The [**GetCurrentHwProfile**](/windows/win32/Winbase/nf-winbase-getcurrenthwprofilea?branch=master) function retrieves information about the hardware profile. The hardware profile includes information such as the docking state, globally unique identifier (GUID), and display name for the profile. The [**GetKeyboardType**](https://msdn.microsoft.com/library/windows/desktop/ms724336) function retrieves such information as the type of keyboard and the number of function keys on the current keyboard.

 

 



