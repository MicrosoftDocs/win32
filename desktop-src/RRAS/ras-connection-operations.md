---
title: RAS Connection Operations
description: Windows NT and later versions provide the RasPhonebookDlg and RasDialDlg functions that display the built-in user interface for starting a RAS connection operation.
ms.assetid: 1e0f82e1-5995-4b47-970b-e6a7ff6d52e0
keywords:
- Connection Operations, RAS
ms.topic: article
ms.date: 05/31/2018
---

# RAS Connection Operations

Windows NT and later versions provide the [**RasPhonebookDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasphonebookdlga) and [**RasDialDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasdialdlga) functions that display the built-in user interface for starting a RAS connection operation. For most applications, this is the preferred way to start a RAS connection operation. Windows 95 does not currently support these functions.

The remainder of this section describes the low-level functions for starting a RAS connection. These functions are available on bothWindows NT 4.0 (and later versions), and Windows 95.

A RAS client application uses the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function to establish a connection to a RAS server. The **RasDial** function starts the connection operation, which is then carried out by the Remote Access Connection Manager.

The Remote Access Connection Manager is a service that handles the details of establishing the connection to the remote server. This service also provides the client with status information during the connection operation. The Remote Access Connection Manager starts automatically when an application loads the RASAPI32.DLL.

The [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call specifies the following information when it starts a connection operation:

-   The [connection information](phone-book-files-and-connection-information.md) that the Remote Access Connection Manager needs to establish the connection.
-   An optional [notification handler](notification-handlers.md) that receives progress notifications during the connection operation. If the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call specifies a notification handler, the call is [asynchronous](asynchronous-operations.md); otherwise, it is [synchronous](synchronous-operations.md).
-   An optional [**RASDIALEXTENSIONS**](/previous-versions/windows/desktop/legacy/aa377029(v=vs.85)) structure to enable or disable extensions to the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) operation. The extensions permit a RAS client to directly enable some modem settings, to control whether RAS uses the prefixes and suffixes in a phone-book entry, and to support [paused states](paused-states.md) during the connection operation.

 

 