---
title: Logging With Network Policy Server
description: Logging With Network Policy Server
ms.assetid: 903d89bd-c223-4f29-9eaf-1dc28d27a32a
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Logging With Network Policy Server

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

The following table describes only the most important aspects of the RADIUS accounting packets. The RADIUS Accounting Request for Comments document ([RFC 2866](https://www.ietf.org/rfc/rfc2866.txt)) provides detailed information on these packets.

RADIUS accounting packets can be divided into the following categories.



| Accounting packet  | Description                                                                                                                                                                                                                |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accounting-On      | Sent by the Network Access Server (NAS) to indicate that it has restarted.<br/> Contains nas-identifier/ipaddress.<br/>                                                                                        |
| Accounting-Off     | Sent by the NAS to indicate that it is being shutdown.<br/> Contains nas-identifier/ipaddress.<br/>                                                                                                            |
| Accounting-Start   | Sent by the NAS, after the user was authenticated and authorized, to indicate the start of a user session. <br/> Contains userid, nas-identifier/ipaddress, plus other information received from the NAS.<br/> |
| Accounting-Stop    | Sent by the NAS to indicate the end of a user session.<br/> Contains userid, nas-identifier/ipaddress, plus other information received from the NAS.<br/>                                                      |
| Accounting-Interim | Could be sent periodically by the NAS for each user that is logged on at the NAS. <br/> This feature is generally supported in newer versions of NAS.<br/>                                                     |



 

The following issues are important to consider when collecting accounting information made available through RADIUS:

-   In rare cases, packets could be lost during transmission and may never reach the RADIUS server.
-   The RADIUS server is not notified if the NAS aborts.
-   ISDN supports multiple sessions and each session generates an Accounting-Start/-Stop pair of packets. There is an accounting attribute called multi-session identifier that clearly identifies such multi-session packets. Check for the multi-session identifier in addition to the session identifier to calculate the number of sessions.

## Requests Logged by NPS

By default, NPS does not log any data. NPS can be configured, using the NPS user interface (nps.msc), to log the following requests.



| Logged packet          | Description                                                                                                                                  |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Accounting Request     | Any of the accounting packets described in the previous table.<br/>                                                                    |
| Authentication Request | Sent by the NAS on behalf of the connecting user.<br/> The log entries contain only incoming attributes.<br/>                    |
| Authentication Accept  | Sent by NPS to indicate that the user connection should be accepted.<br/> The log entries contain only outgoing attributes.<br/> |
| Authentication Reject  | Sent by NPS to indicate that the user connection should be rejected.<br/> The log entries contain only outgoing attributes.<br/> |



 

Data logged by NPS can go to a text file on the NPS server or to a central SQL database. For more information on NPS SQL logging, see [SQL Programmability](sql-programmability.md).

## Related topics

<dl> <dt>

[Internet Authentication Service and Network Policy Server](internet-authentication-service-vs-network-policy-server.md)
</dt> <dt>

[RADIUS Authentication, Authorization, and Accounting](/windows/desktop/Nps/ias-radius-authentication-and-accounting)
</dt> <dt>

[Working with a State Server](/windows/desktop/Nps/ias-working-with-a-state-server)
</dt> </dl>

 

