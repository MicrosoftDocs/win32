---
title: Subentries and Multilink Connections
description: Windows NT Server 4.0 provides support for phone-book subentries, which enable multilink connections. A multilink connection combines the bandwidth of multiple connections to provide a single connection with higher bandwidth.
ms.assetid: 19cf6e1a-cdba-47e4-8d8f-d6030ed6f9e3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Subentries and Multilink Connections

Windows NT Server 4.0 provides support for phone-book subentries, which enable multilink connections. A multilink connection combines the bandwidth of multiple connections to provide a single connection with higher bandwidth.

A RAS phone-book entry can have zero or more subentries. The [**RasGetEntryProperties**](/windows/win32/Ras/nf-ras-rasgetentrypropertiesa?branch=master) function retrieves a [**RASENTRY**](/windows/win32/Ras/?branch=master) structure that includes information about the subentries of a phone-book entry. The **dwSubEntries** member of the **RASENTRY** structure indicates the number of subentries. Phone-book entries initially have no subentries. To add subentries to a phone-book entry, use the [**RasSetSubEntryProperties**](/windows/win32/Ras/nf-ras-rassetsubentrypropertiesa?branch=master) function.

The properties for each subentry include a phone number and the name and type of the TAPI device to use when dialing the subentry. In addition, a subentry can include a list of alternate phone numbers to dial if RAS cannot make a connection using the primary number. The [**RasSetSubEntryProperties**](/windows/win32/Ras/nf-ras-rassetsubentrypropertiesa?branch=master) and [**RasGetSubEntryProperties**](/windows/win32/Ras/nf-ras-rasgetsubentrypropertiesa?branch=master) functions use the [**RASSUBENTRY**](/windows/win32/Ras/?branch=master) structure to set and retrieve the properties of a specified phone-book subentry. Subentries are identified by a one-based index.

You can call the [**RasSetEntryProperties**](/windows/win32/Ras/nf-ras-rassetentrypropertiesa?branch=master) function to configure a multilink RAS entry to connect all subentries when it is first dialed. Alternatively, you can configure an entry to provide variable bandwidth. In this case, RAS connects a single subentry initially, and then connects or disconnects additional subentries as needed. For a variable-bandwidth multilink connection, you can use the [**RASDIALPARAMS**](/windows/win32/Ras/?branch=master) structure to specify the initial subentry to connect when you call the [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) function. When using the [**RasDialDlg**](/windows/win32/Rasdlg/nf-rasdlg-rasdialdlga?branch=master) function to connect a multilink entry, you can use the [**RASDIALDLG**](/windows/win32/Rasdlg/?branch=master) structure to specify the initial subentry to connect.

For a variable-bandwidth multilink connection, use the [**RASENTRY**](/windows/win32/Ras/?branch=master) structure with the [**RasSetEntryProperties**](/windows/win32/Ras/nf-ras-rassetentrypropertiesa?branch=master) function to specify the parameters for connecting and disconnecting the individual subentries. RAS connects an additional subentry when the bandwidth being used exceeds a specified percentage of the available bandwidth for a specified interval.

If you call the [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) function to establish a multilink connection, you can specify a [**RasDialFunc2**](/windows/win32/Ras/nc-ras-rasdialfunc2?branch=master) callback function to receive notifications about the connection. **RasDialFunc2** is similar to the [**RasDialFunc1**](/windows/win32/Ras/nc-ras-rasdialfunc1?branch=master) callback function, except that it provides additional information for a multilink connection, such as the index of the subentry that caused the notification. RAS calls your **RasDialFunc2** function when it connects or disconnects a subentry.

You can use an **HRASCONN** connection handle to hang up or retrieve information about a multilink connection. You can get a connection handle for each of the subentry connections that make up the multilink, as well as for the combined multilink connection. When you call the [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) function to establish a multilink connection, **RasDial** returns a handle to the combined multilink connection. Similarly, [**RasEnumConnections**](/windows/win32/Ras/nf-ras-rasenumconnectionsa?branch=master) returns the combined multilink handle when you enumerate connections. To get a handle to one of the subentry connections in a multilink connection, call the [**RasGetSubEntryHandle**](/windows/win32/Ras/nf-ras-rasgetsubentryhandlea?branch=master) function.

You can use the combined multilink connection handle and the subentry connection handles in the [**RasHangUp**](/windows/win32/Ras/nf-ras-rashangupa?branch=master), [**RasGetConnectStatus**](/windows/win32/Ras/nf-ras-rasgetconnectstatusa?branch=master), and [**RasGetProjectionInfo**](/windows/win32/Ras/nf-ras-rasgetprojectioninfoa?branch=master) functions. Calling **RasHangUp** with a combined multilink handle terminates the entire connection; calling it with a subentry handle hangs up only that subentry connection. Similarly, **RasGetConnectStatus** returns information for the combined or individual connection, depending on the handle specified. The projection information returned by **RasGetProjectionInfo** for a multilink entry is the same for each of the subentry connection handles as it is for the main connection handle.

 

 




