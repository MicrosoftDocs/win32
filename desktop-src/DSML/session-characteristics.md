---
title: Session Characteristics
description: Session Characteristics
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8abeef51-65df-4d4b-91a7-5a0dd5709092
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Session Characteristics DSML
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Session Characteristics

DSML Services for Windows maintains data about overall session characteristics as well as individual session characteristics. DSML Services for Windows monitors the following characteristics which can be configured through the dsmlv2.config configuration file:

-   Total Sessions

    The total number of outstanding active sessions. If the total number reaches the maximum, and a client requests a new session, the server will reject all subsequent new session requests until the number of outstanding active sessions is less than the maximum number specified.

    Total Sessions is controlled by the **sessionsMax** element in the dsmlv2.config configuration file.

-   Sessions per IP

    The number of sessions allowed for a given IP address. This characteristic can be useful for mitigating denial of service attacks.

    Sessions per IP is controlled by the **sessionsMaxPerIP** element in the dsmlv2.config configuration file.

-   Use IP Matching

    If enabled, the server verifies that the IP address matches the original creator of the session when the client requests a session ID.

    Use IP Matching is controlled by the **sessionsIPMatch** element in the dsmlv2.config configuration file.

-   Use Credential Matching

    If enabled, the server verifies that the user credentials match those of the original creator of the session when the client requests a session ID.

    Use Credential Matching is controlled by the **sessionsAuthMatch** element in the dsmlv2.config configuration file.

-   Time to Live (TTL)

    The amount of time, in seconds, that the session should be active before it is declared to be expired. Each client request with the session ID revitalizes the TTL. If there is no activity beyond the TTL, the session is considered to be expired.

    Time to Live is controlled by the **sessionsTTL** element in the dsmlv2.config configuration file.



| Parameter               | Configuration element | Range          | Default |
|-------------------------|-----------------------|----------------|---------|
| Total Sessions          | **sessionsMax**       | 0 - 512        | 100     |
| Sessions per IP         | **sessionsMaxPerIP**  | 0 - 512        | 5       |
| Use IP Matching         | **sessionsIPMatch**   | True/False     | True    |
| Use Credential Matching | **sessionsAuthMatch** | True/False     | True    |
| Time to Live            | **sessionsTTL**       | 1 - 2147483647 | 600     |



 

 

 




