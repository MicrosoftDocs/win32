---
title: LDAP Controls and Session Support
description: A DSML session is typically used to support LDAP controls and extended operations. The session is required to handle the multiple request-response communications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e36fadda-879b-45bc-afc5-1b8b1878726e
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- LDAP Controls and Session Support DSML
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LDAP Controls and Session Support

A DSML session is typically used to support LDAP controls and extended operations. The session is required to handle the multiple request-response communications.

To help determine when DSML sessions are required, LDAP controls and extended operations are categorized into four types:

-   Session support required

    For example, a page size control or VLV control.

-   Stateless controls

    For example, tombstone, sort, or dirsync controls.

-   Unknown controls

    Because the LDAP control mechanism is extensible, you can create a new LDAP control or an extended operation that is not recognized by the DSML V2 server.

-   Forbidden controls

    Controls not supported by the server.

The following table lists behavior that can be expected in session and stateless requests.



| Control type                      | Session request                                     | Stateless request                            |
|-----------------------------------|-----------------------------------------------------|----------------------------------------------|
| Session support required controls | Allowed.                                            | Forbidden. Error response will be generated. |
| Stateless controls                | Allowed. Behavior should be identical to stateless. | Allowed.                                     |
| Unknown controls                  | Allowed.                                            | Forbidden. Error response will be generated. |
| Forbidden controls                | Forbidden. Error response will be generated.        | Forbidden. Error response will be generated. |



 

## LDAP Controls and Extended Operations supported by Active Directory

The following table lists the set of LDAP controls and extended operations that are currently supported in Active Directory.



| LDAP OID                   | Name                                          | Description                             | Control type     |
|----------------------------|-----------------------------------------------|-----------------------------------------|------------------|
| 1.2.840.113556.1.4.319     | **LDAP\_PAGED\_RESULT\_OID\_STRING**          | Paged search control                    | Session required |
| 1.2.840.113556.1.4.417     | **LDAP\_SERVER\_SHOW\_DELETED\_OID**          | Show deleted control                    | Stateless        |
| 1.2.840.113556.1.4.473     | **LDAP\_SERVER\_SORT\_OID**                   | Server sort control                     | Stateless        |
| 1.2.840.113556.1.4.521     | **LDAP\_SERVER\_CROSSDOM\_MOVE\_TARGET\_OID** | Cross-domain move control               | Stateless        |
| 1.2.840.113556.1.4.528     | **LDAP\_SERVER\_NOTIFICATION\_OID**           | Server search notification control      | Forbidden        |
| 1.2.840.113556.1.4.529     | **LDAP\_SERVER\_EXTENDED\_DN\_OID**           | Extended DN control                     | Stateless        |
| 1.2.840.113556.1.4.619     | **LDAP\_SERVER\_LAZY\_COMMIT\_OID**           | Lazy commit control                     | Stateless        |
| 1.2.840.113556.1.4.801     | **LDAP\_SERVER\_SD\_FLAGS\_OID**              | Security descriptor flags control       | Stateless        |
| 1.2.840.113556.1.4.805     | **LDAP\_SERVER\_TREE\_DELETE\_OID**           | Tree delete control                     | Stateless        |
| 1.2.840.113556.1.4.841     | **LDAP\_SERVER\_DIRSYNC\_OID**                | Directory synchronization control       | Stateless        |
| 1.2.840.113556.1.4.970     | None                                          | Get stats control                       | Stateless        |
| 1.2.840.113556.1.4.1338    | **LDAP\_SERVER\_VERIFY\_NAME\_OID**           | Verify name control                     | Stateless        |
| 1.2.840.113556.1.4.1339    | **LDAP\_SERVER\_DOMAIN\_SCOPE\_OID**          | Domain scope control                    | Stateless        |
| 1.2.840.113556.1.4.1340    | **LDAP\_SERVER\_SEARCH\_OPTIONS\_OID**        | Search options control                  | Stateless        |
| 1.2.840.113556.1.4.1413    | **LDAP\_SERVER\_PERMISSIVE\_MODIFY\_OID**     | Permissive modify control               | Stateless        |
| 1.2.840.113556.1.4.1504    | **LDAP\_SERVER\_ASQ\_OID**                    | Attribute scoped query control          | Stateless        |
| 1.2.840.113556.1.4.1781    | **LDAP\_SERVER\_FAST\_BIND\_OID**             | Fast concurrent bind extended operation | Forbidden        |
| 1.3.6.1.4.1.1466.101.119.1 | **LDAP\_TTL\_EXTENDED\_OP\_OID**              | TTL refresh extended operation          | Stateless        |
| 1.3.6.1.4.1.1466.20037     | **LDAP\_START\_TLS\_OID**                     | Start TLS extended operation            | Forbidden        |
| 2.16.840.1.113730.3.4.9    | **LDAP\_CONTROL\_VLVREQUEST**                 | VLV request control                     | Session required |



 

 

 




