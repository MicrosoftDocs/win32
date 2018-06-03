---
title: QOS Event Codes
description: Applications that use the FD\_QOS event suite to monitor QOS events have access to status and error codes associated with the event, as well as updated QOS parameters (in the QOS structure associated with the event).
ms.assetid: 348f7e3b-e9a5-4244-8817-7bdf65562d14
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QOS Event Codes

Applications that use the FD\_QOS event suite to monitor QOS events have access to status and error codes associated with the event, as well as updated QOS parameters (in the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure associated with the event). The following is a list of common QOS-related Windows Sockets 2 status and error codes.



| Event or error code            | Definition                                                  |
|--------------------------------|-------------------------------------------------------------|
| WSA\_QOS\_RECEIVERS            | One or more RESV message has arrived.                       |
| WSA\_QOS\_SENDERS              | One or more PATH message has arrived.                       |
| WSA\_QOS\_NO\_SENDERS          | There are no senders.                                       |
| WSA\_QOS\_NO\_RECEIVERS        | There are no receivers.                                     |
| WSA\_QOS\_REQUEST\_CONFIRMED   | Reservation has been confirmed.                             |
| WSA\_QOS\_ADMISSION\_FAILURE   | Error due to lack of resources.                             |
| WSA\_QOS\_POLICY\_FAILURE      | Rejected for administrative reasons.                        |
| WSA\_QOS\_BAD\_STYLE           | Unknown or conflicting style.                               |
| WSA\_QOS\_BAD\_OBJECT          | Problem with some part of the [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec). |
| WSA\_QOS\_TRAFFIC\_CTRL\_ERROR | Problem with some part of the filter specification.         |
| WSA\_QOS\_GENERIC\_ERROR       | General error.                                              |



 

 

For additional status and error codes, consult the Winsock2.h header file.

 

 




