---
title: Point-to-Point Protocol over Ethernet Connections
description: Windows Server 2003, Windows XP, and later operating systems provide support for Point-to-Point Protocol over Ethernet (PPPoE). For a PPPoE connection, set the following values in the RASENTRY structure.
ms.assetid: abdbf22c-abeb-4363-bfa6-e0002d1637f4
ms.topic: article
ms.date: 05/31/2018
---

# Point-to-Point Protocol over Ethernet Connections

Windows Server 2003, Windows XP, and later operating systems provide support for Point-to-Point Protocol over Ethernet (PPPoE). For a PPPoE connection, set the following values in the [**RASENTRY**](/previous-versions/windows/desktop/legacy/aa377274(v=vs.85)) structure.



| Member                      | Value             |
|-----------------------------|-------------------|
| RASENTRY.dwType             | RASET\_Broadband  |
| RAENTRY.szDeviceType        | RASDT\_PPPoE      |
| RASENTRY.szLocalPhoneNumber | The service name. |



 

Use the [**RasSetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rassetentrypropertiesa) function to set these values.

You can also use [**RasEntryDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasentrydlga) and the RASEDFLAG\_NewBroadbandEntry flag for [**RASENTRYDLG**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasentrydlga) to display a wizard for creating a PPPoE phonebook entry.

 

 