---
title: Point-to-Point Protocol over Ethernet Connections
description: Windows Server 2003, Windows XP, and later operating systems provide support for Point-to-Point Protocol over Ethernet (PPPoE). For a PPPoE connection, set the following values in the RASENTRY structure.
ms.assetid: abdbf22c-abeb-4363-bfa6-e0002d1637f4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Point-to-Point Protocol over Ethernet Connections

Windows Server 2003, Windows XP, and later operating systems provide support for Point-to-Point Protocol over Ethernet (PPPoE). For a PPPoE connection, set the following values in the [**RASENTRY**](/windows/win32/Ras/?branch=master) structure.



| Member                      | Value             |
|-----------------------------|-------------------|
| RASENTRY.dwType             | RASET\_Broadband  |
| RAENTRY.szDeviceType        | RASDT\_PPPoE      |
| RASENTRY.szLocalPhoneNumber | The service name. |



 

Use the [**RasSetEntryProperties**](/windows/win32/Ras/nf-ras-rassetentrypropertiesa?branch=master) function to set these values.

You can also use [**RasEntryDlg**](/windows/win32/Rasdlg/nf-rasdlg-rasentrydlga?branch=master) and the RASEDFLAG\_NewBroadbandEntry flag for [**RASENTRYDLG**](/windows/win32/Rasdlg/nf-rasdlg-rasentrydlga?branch=master) to display a wizard for creating a PPPoE phonebook entry.

 

 




