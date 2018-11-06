---
title: Availability of applicable graphics drivers on Windows Update
description: The availability of these drivers on Windows Update (WU) will determine whether a user is automatically offered an upgrade from Windows 7, Windows 8 or Windows 8.1 to Windows 10.
ms.assetid: 166C0FE3-CB9D-4895-91AC-6E57EC1D8B21
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Availability of applicable graphics drivers on Windows Update

The availability of these drivers on Windows Update (WU) will determine whether a user is automatically offered an upgrade from Windows 7, Windows 8 or Windows 8.1 to Windows 10. If hardware scans showed that there was no graphics driver available on Windows Update for the graphics adapter in the PC, users were not offered the updated Windows 10 OS. However, users can still obtain Windows 10 through other sources and manually perform the upgrade.

Some users were unsure of why they were not offered the upgrade when other people were, even though the Upgrade Advisor explained that there was no graphics driver available for their hardware.

Additionally, some users forced an upgrade and then found that their graphics functionality and performance suffered due to the lack of a hardware driver.

## Mitigations

To mitigate this, users can manually install an older driver, i.e. from Windows 7, Windows 8 or Windows 8.1, by going to the IHV or OEM web site and downloading a driver explicitly. This must be done after the upgrade and is not guaranteed to work. There is no supported solution if a suitable graphics driver is not available on WU. The user must decide whether to:

-   Remain on the previous OS;
-   Accept the limitations of the software driver, Microsoft Basic Display Adapter (MSBDA); or
-   Buy a new graphics card that has a supported Windows 10 driver.

## Solutions

It’s critical that IHVs and OEMs upload their Windows 10 graphics drivers to WU for any hardware that they intend to support.

Note that hardware that has reached End-Of-Live (EOL) might not have drivers on WU. There is no solution in this case – the user must choose one of the options under Mitigations above.

 

 




