---
title: Subentries and Multilink Connections
description: Windows NT Server 4.0 provides support for phone-book subentries, which enable multilink connections. A multilink connection combines the bandwidth of multiple connections to provide a single connection with higher bandwidth.
ms.assetid: 19cf6e1a-cdba-47e4-8d8f-d6030ed6f9e3
ms.topic: article
ms.date: 05/31/2018
---

# Subentries and Multilink Connections

Windows NT Server 4.0 provides support for phone-book subentries, which enable multilink connections. A multilink connection combines the bandwidth of multiple connections to provide a single connection with higher bandwidth.

A RAS phone-book entry can have zero or more subentries. The [**RasGetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rasgetentrypropertiesa) function retrieves a [**RASENTRY**](/previous-versions/windows/desktop/legacy/aa377274(v=vs.85)) structure that includes information about the subentries of a phone-book entry. The **dwSubEntries** member of the **RASENTRY** structure indicates the number of subentries. Phone-book entries initially have no subentries. To add subentries to a phone-book entry, use the [**RasSetSubEntryProperties**](/windows/desktop/api/Ras/nf-ras-rassetsubentrypropertiesa) function.

The properties for each subentry include a phone number and the name and type of the TAPI device to use when dialing the subentry. In addition, a subentry can include a list of alternate phone numbers to dial if RAS cannot make a connection using the primary number. The [**RasSetSubEntryProperties**](/windows/desktop/api/Ras/nf-ras-rassetsubentrypropertiesa) and [**RasGetSubEntryProperties**](/windows/desktop/api/Ras/nf-ras-rasgetsubentrypropertiesa) functions use the [**RASSUBENTRY**](/previous-versions/windows/desktop/legacy/aa377839(v=vs.85)) structure to set and retrieve the properties of a specified phone-book subentry. Subentries are identified by a one-based index.

You can call the [**RasSetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rassetentrypropertiesa) function to configure a multilink RAS entry to connect all subentries when it is first dialed. Alternatively, you can configure an entry to provide variable bandwidth. In this case, RAS connects a single subentry initially, and then connects or disconnects additional subentries as needed. For a variable-bandwidth multilink connection, you can use the [**RASDIALPARAMS**](/previous-versions/windows/desktop/legacy/aa377238(v=vs.85)) structure to specify the initial subentry to connect when you call the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function. When using the [**RasDialDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasdialdlga) function to connect a multilink entry, you can use the [**RASDIALDLG**](/previous-versions/windows/desktop/legacy/aa377023(v=vs.85)) structure to specify the initial subentry to connect.

For a variable-bandwidth multilink connection, use the [**RASENTRY**](/previous-versions/windows/desktop/legacy/aa377274(v=vs.85)) structure with the [**RasSetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rassetentrypropertiesa) function to specify the parameters for connecting and disconnecting the individual subentries. RAS connects an additional subentry when the bandwidth being used exceeds a specified percentage of the available bandwidth for a specified interval.

If you call the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function to establish a multilink connection, you can specify a [**RasDialFunc2**](/windows/desktop/api/Ras/nc-ras-rasdialfunc2) callback function to receive notifications about the connection. **RasDialFunc2** is similar to the [**RasDialFunc1**](/windows/desktop/api/Ras/nc-ras-rasdialfunc1) callback function, except that it provides additional information for a multilink connection, such as the index of the subentry that caused the notification. RAS calls your **RasDialFunc2** function when it connects or disconnects a subentry.

You can use an **HRASCONN** connection handle to hang up or retrieve information about a multilink connection. You can get a connection handle for each of the subentry connections that make up the multilink, as well as for the combined multilink connection. When you call the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function to establish a multilink connection, **RasDial** returns a handle to the combined multilink connection. Similarly, [**RasEnumConnections**](/windows/desktop/api/Ras/nf-ras-rasenumconnectionsa) returns the combined multilink handle when you enumerate connections. To get a handle to one of the subentry connections in a multilink connection, call the [**RasGetSubEntryHandle**](/windows/desktop/api/Ras/nf-ras-rasgetsubentryhandlea) function.

You can use the combined multilink connection handle and the subentry connection handles in the [**RasHangUp**](/windows/desktop/api/Ras/nf-ras-rashangupa), [**RasGetConnectStatus**](/windows/desktop/api/Ras/nf-ras-rasgetconnectstatusa), and [**RasGetProjectionInfo**](/previous-versions/windows/embedded/ms897107(v=msdn.10)) functions. Calling **RasHangUp** with a combined multilink handle terminates the entire connection; calling it with a subentry handle hangs up only that subentry connection. Similarly, **RasGetConnectStatus** returns information for the combined or individual connection, depending on the handle specified. The projection information returned by **RasGetProjectionInfo** for a multilink entry is the same for each of the subentry connection handles as it is for the main connection handle.

 

 