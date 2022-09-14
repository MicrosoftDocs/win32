---
title: AutoDial Mapping Database
description: The AutoDial mapping database maps network addresses to RAS phone-book entries.
ms.assetid: 4589d1e5-eec3-46ac-a10f-f20ae9f7b543
ms.topic: article
ms.date: 05/31/2018
---

# AutoDial Mapping Database

The AutoDial mapping database maps network addresses to RAS phone-book entries. The database can include IP addresses (for example, "172.21.167.35"), Internet host names (for example, "www.microsoft.com"), or NetBIOS names (for example, "products1"). Associated with each address in the AutoDial database is a set of one or more [**RASAUTODIALENTRY**](/previous-versions/windows/desktop/legacy/aa376721(v=vs.85)) entries. Each of these entries specifies a phone-book entry that RAS can dial to connect to the address from a particular Telephony Application Programming Interface (TAPI) dialing location. For more information about TAPI dialing locations, see the TAPI documentation.

AutoDial automatically creates entries in the AutoDial mapping database in two situations:

-   When an attempt to connect to a network address fails

    If there is no entry for the address in the mapping database, and the computer is not connected to a network, either directly or through RAS, AutoDial prompts the user to specify the information necessary to establish a dial-up connection. If the user provides the information and the dial-up connection operation is successful, AutoDial stores the information in the mapping database.

-   When the computer is connected to a network through RAS

    Whenever the user connects to a network address, AutoDial creates an entry in the database. The entry maps the network address to the phone-book entry that was used to establish the RAS connection.

You can use the [**RasSetAutodialAddress**](/windows/desktop/api/Ras/nf-ras-rassetautodialaddressa) function to add an address to the AutoDial mapping database, delete an address from the database, or change the AutoDial entries associated with an existing address in the database. You can use the [**RasGetAutodialAddress**](/windows/desktop/api/Ras/nf-ras-rasgetautodialaddressa) function to retrieve the AutoDial entries associated with a specified network address in the AutoDial mapping database. The [**RasEnumAutodialAddresses**](/windows/desktop/api/Ras/nf-ras-rasenumautodialaddressesa) function returns a list of all addresses in the AutoDial mapping database.

 

 