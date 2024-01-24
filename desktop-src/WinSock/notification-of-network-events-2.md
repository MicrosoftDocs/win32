---
description: One of the most important responsibilities of a data transport service provider is that of providing indications to the client when certain network events have occurred.
ms.assetid: 7b60a775-ed20-4048-bd0b-9d43d090f82c
title: Notification of Network Events
ms.topic: article
ms.date: 05/31/2018
---

# Notification of Network Events

One of the most important responsibilities of a data transport service provider is that of providing indications to the client when certain network events have occurred. The list of defined network events consists of the following:

-   **FD\_CONNECT**— A connection to a remote host or to a multicast session has been completed.
-   **FD\_ACCEPT**— A remote host is making a connection request.
-   **FD\_READ**— Network data has arrived which is available to be read.
-   **FD\_WRITE**— Space has become available in the service provider's buffers so that additional data may now be sent.
-   **FD\_OOB**— Out of band data is available to be read.
-   **FD\_CLOSE**— The remote host has closed down the connection.
-   **FD\_QOS**— A change has occurred in negotiated QoS levels.
-   **FD\_GROUP\_QOS**— Reserved.
-   **FD\_ROUTING\_INTERFACE\_CHANGE**— A local interface that should be used to reach the destination specified in **SIO\_ROUTING\_INTERFACE\_CHANGE IOCTL** has changed.
-   **FD\_ADDRESS\_LIST\_CHANGE**— The list of local addresses to which application can bind has changed.

The set of network events enumerated above is sometimes referred to as the **FD\_XXX** events. Indication of the occurrence of one or more of such network events may be given in a number of ways depending on how the client requests notification.

 

 



