---
title: Graphics driver migration to Windows 10
description: Windows 10 Media and Windows 10, like its predecessor, Windows 8.1, does not have any 3rd party graphics drivers in the Windows media kit or “In Box”.
ms.assetid: E6240CF0-5A65-4A66-98AE-856C783EB320
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Graphics driver migration to Windows 10

Windows 10 Media and Windows 10, like its predecessor, Windows 8.1, does not have any 3rd party graphics drivers in the Windows media kit or “In Box”. Instead, the graphics drivers for a broad range of devices are provisioned on WU, which allows hardware vendors to update drivers without requiring a change to the operating system image. Also, existing drivers are not migrated to Windows 10 during an OS upgrade to Windows 10 from Windows 7, Windows 8 or Windows 8.1. This also impacts upgrades from Windows Server 2012.

## Upgrades and installation

For upgrades and new installations, the graphics drivers must be obtained from Windows Update (WU) or the IHV/OEM web site for the relevant hardware. This requires an Internet connection. The drivers on WU are injected into the OS setup by Dynamic Update (DU) when a user upgrades their Windows 7 or Windows 8.x system to Windows 10.

> [!Note]  
> This does not apply to systems which come with Windows pre-installed, e.g. off-the-shelf computers purchased in a retail store. These systems already have the graphics drivers installed by the OEM. The OEM might also supply a DVD (for re-installing the OS) which includes the drivers.

 

After upgrading to Windows 10, users might find that there are no graphics drivers installed on their PC. This can happen for a few reasons:

-   The user elected to do a clean install, i.e. not an upgrade.
-   The user de-selected the option to check for updates during the upgrade, i.e. effectively disabled Dynamic Update (DU).
-   The Internet connection was not working during the upgrade.
-   The driver installation failed.

After a clean install of the OS, there will not be any graphics drivers on the PC until the WU client runs automatically and downloads the applicable drivers. In the interim the PC will be running the Microsoft Basic Display Adapter (MSBDA), which has limited capabilities, e.g. no support for multiple monitors, and the user might also experience poor performance compared to a hardware driver, e.g. slow frame rate or tearing on video playback.

## Manifestations

For older PCs (typically built prior to Windows 7), it is possible that there are no drivers for Windows 10 on WU because the graphics adapters have reached End-Of-Life (EOL) and are no longer supported by the hardware vendors. Even systems currently running Windows 7 or 8.x might have been upgraded from a previous OS and could have EOL graphics adapters.

Newer PCs might not have drivers available because the graphics adapter was transferred from an older computer, e.g. during a hardware upgrade. This most often happens for computers with multiple graphics adapters where the user kept an old graphics card when purchasing a new machine in order to use multiple displays.

Another possibility for a small percentage of machines is that Windows Update only has “coverage” drivers. These are generic drivers that lack OEM customizations. A user who is delivered one of these drivers after upgrading to Windows 10 might see that some functionality is missing, e.g. function keys for controlling screen brightness no longer work.

## Mitigations

-   Suitable graphics drivers should be delivered either by DU during the upgrade process or by WU soon after the upgrade completes. OEMs must ensure that the appropriate graphics drivers are included in the system images used for factory installation of Windows 10 on their computers.
-   After an upgrade, the user can explicitly check Settings \\ Windows Update for drivers although this should not be necessary. Users who force a check while a driver is being automatically installed in the background might see a driver installation failure if the automatic installation completes first. This can be ignored.
-   Users who intend to do a clean install of Windows 10 should obtain the relevant drivers before installing or rely on Windows Update to supply the drivers later, in which case they must ensure that their Internet connection is working.
-   For computers that receive a coverage driver there is no mitigation for missing functionality. However, this should only happen in cases where the hardware supplier no longer maintains the drivers, i.e. computers that are several years old.

> [!Note]  
> For systems with a single display, e.g. a laptop, many users find that MSBDA is acceptable and do not notice the lack of a hardware driver. No mitigation is required in this case.

 

## Solutions

It is critical that IHVs and OEMs upload their Windows 10 graphics drivers to WU for any hardware that they intend to support.

Users should leave “Check for Updates” selected (the default setting) when upgrading. Depending on the speed of the network connection and the load on the WU servers, this can mean that the drivers do not get installed until after OOBE has completed and the user has logged in for the first time. In the meantime, the user might notice some limited functionality or poor performance.

Users must ensure that their Internet connection is working before starting an upgrade even if they are upgrading using media (DVD or Flash Drive).

-   If the PC is connected to the Internet, the appropriate drivers should be downloaded and installed automatically. The user is not required to take any action.
-   If the PC is not connected to the Internet, the drivers must be downloaded from the IHV or OEM web site using an Internet-connected computer; transferred to the target machine using a Flash Drive or CD/DVD; and then installed manually.

 

 




