---
title: AutoDial Connection Operations
description: When an attempt to connect to a network address fails because the host cannot be reached, the system searches the AutoDial mapping database for the address.
ms.assetid: 343ee69e-1ff5-4107-9ddb-4245c3b4a54d
ms.topic: article
ms.date: 05/31/2018
---

# AutoDial Connection Operations

When an attempt to connect to a network address fails because the host cannot be reached, the system searches the AutoDial mapping database for the address. If the address is in the database, the system initiates an AutoDial operation for the [**RASAUTODIALENTRY**](/previous-versions/windows/desktop/legacy/aa376721(v=vs.85)), if any, that corresponds to the local TAPI dialing location.

The RAS API provides functions that enable you to set and query AutoDial parameters that control AutoDial connections. You can call the [**RasSetAutodialEnable**](/windows/desktop/api/Ras/nf-ras-rassetautodialenablea) function to enable or disable the AutoDial feature for a specified TAPI dialing location. The [**RasGetAutodialEnable**](/windows/desktop/api/Ras/nf-ras-rasgetautodialenablea) function indicates whether the AutoDial feature is enabled for a specified TAPI dialing location. For more information about TAPI dialing locations, see the TAPI documentation. You can call the [**RasSetAutodialParam**](/windows/desktop/api/Ras/nf-ras-rassetautodialparama) function to set other AutoDial connection parameters. For example, you can disable AutoDial connections for the current logon session. Call the [**RasGetAutodialParam**](/windows/desktop/api/Ras/nf-ras-rasgetautodialparama) function to determine the current value of the AutoDial connection parameters.

The system provides a default user interface for AutoDial dialing operations. However, you can create an AutoDial dynamic-link library (DLL) to provide a custom user interface for AutoDial dialing operations involving specified phone-book entries. Your AutoDial DLL must export both an ANSI and a Unicode version of a [**RASADFunc**](/windows/desktop/api/Ras/nc-ras-rasadfunca) AutoDial handler.

To enable your custom AutoDial handler for a phone-book entry, call the [**RasSetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rassetentrypropertiesa) function to set the properties for that entry. The **szAutodialDll** and **szAutodialFunc** members of the [**RASENTRY**](/previous-versions/windows/desktop/legacy/aa377274(v=vs.85)) structure passed to **RasSetEntryProperties** specify the name of your AutoDial DLL and the name of your [**RASADFunc**](/windows/desktop/api/Ras/nc-ras-rasadfunca) function, excluding the "A" or "W" suffix.

When the system starts an AutoDial operation for a phone-book entry with a custom AutoDial handler, it calls the specified [**RASADFunc**](/windows/desktop/api/Ras/nc-ras-rasadfunca). The **RASADFunc** function receives a pointer to a [**RASADPARAMS**](/previous-versions/windows/desktop/legacy/aa376719(v=vs.85)) structure that indicates the location and parent window for the window of your user interface. Your **RASADFunc** can start a thread to perform the custom dialing operation. The **RASADFunc** function returns **TRUE** to indicate that it took over the dialing, or **FALSE** to allow the system to perform the dialing. Your custom dialing operation must use the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function to do the actual dialing. When the dialing operation has been completed, the custom dialing operation indicates success or failure by setting the variable pointed to by the *lpdwRetCode* parameter passed to [**RASADFunc**](/windows/desktop/api/Ras/nc-ras-rasadfunca).

 

 