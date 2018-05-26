---
Description: Unless you are developing an application that is intended to manage device maintenance, your application does not have to address drive cleaning. RSM is designed to manage device maintenance.
ms.assetid: 8e453d20-d03b-40eb-9a1e-2634d50abea3
title: Cleaning Drives in RSM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cleaning Drives in RSM

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

Unless you are developing an application that is intended to manage device maintenance, your application does not have to address drive cleaning. RSM is designed to manage device maintenance.

In the RSM model of device maintenance, each library unit can contain one cleaner cartridge. Administrators can use the RSM MMC snap-in to place a cleaning cartridge in a library, clean a dirty drive or remove an exhausted cleaning cartridge.

RSM maintains a usage count for each cleaner cartridge. When a cleaner reaches its maximum usage count, RSM generates an operator request. If you are developing an application that manages device maintenance, you can use the following RSM functions to implement drive cleaning functionality.

-   [**CleanNtmsDrive**](/windows/win32/Ntmsapi/nf-ntmsapi-cleanntmsdrive?branch=master)
-   [**EjectNtmsCleaner**](/windows/win32/Ntmsapi/nf-ntmsapi-ejectntmscleaner?branch=master)
-   [**InjectNtmsCleaner**](/windows/win32/Ntmsapi/nf-ntmsapi-injectntmscleaner?branch=master)
-   [**ReleaseNtmsCleanerSlot**](/windows/win32/Ntmsapi/nf-ntmsapi-releasentmscleanerslot?branch=master)
-   [**ReserveNtmsCleanerSlot**](/windows/win32/Ntmsapi/nf-ntmsapi-reserventmscleanerslot?branch=master)

If your application calls [**EjectNtmsCleaner**](/windows/win32/Ntmsapi/nf-ntmsapi-ejectntmscleaner?branch=master), it must first call [**ReserveNtmsCleanerSlot**](/windows/win32/Ntmsapi/nf-ntmsapi-reserventmscleanerslot?branch=master) in order to have a place in the library to put the cleaning cartridge.

 

 



