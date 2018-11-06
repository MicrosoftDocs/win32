---
title: Win32 Error Codes for ADSI 2.0
description: The following table lists the LDAP error messages for ADSI 2.0.
ms.assetid: 99d97ea8-1dcc-49f4-a2bf-36ff8076e83a
ms.tgt_platform: multiple
keywords:
- Win32 Error Codes for ADSI 2.0 ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Win32 Error Codes for ADSI 2.0

The following table lists the LDAP error messages for ADSI 2.0.



| ADSI Error Value | LDAP message                           | Win32 message                        | Description                                          |
|------------------|----------------------------------------|--------------------------------------|------------------------------------------------------|
| 0                | **LDAP\_SUCCESS**                      | **NO\_ERROR**                        | Operation succeeded.                                 |
| 0x80070002       | **LDAP\_NO\_SUCH\_OBJECT**             | **ERROR\_FILE\_NOT\_FOUND**          | Object does not exist.                               |
| 0x80070005       | **LDAP\_AUTH\_METHOD\_NOT\_SUPPORTED** | **ERROR\_ACCESS\_DENIED**            | Authentication method not supported.                 |
| 0x80070005       | **LDAP\_STRONG\_AUTH\_REQUIRED**       | **ERROR\_ACCESS\_DENIED**            | Requires strong authentication.                      |
| 0x80070005       | **LDAP\_INAPPROPRIATE\_AUTH**          | **ERROR\_ACCESS\_DENIED**            | Inappropriate authentication.                        |
| 0x80070005       | **LDAP\_INSUFFICIENT\_RIGHTS**         | **ERROR\_ACCESS\_DENIED**            | User has insufficient access rights.                 |
| 0x80070005       | **LDAP\_AUTH\_UNKNOWN**                | **ERROR\_ACCESS\_DENIED**            | Unknown authentication error occurred.               |
| 0x80070008       | **LDAP\_NO\_MEMORY**                   | **ERROR\_NOT\_ENOUGH\_MEMORY**       | System is out of memory.                             |
| 0x8007001F       | **LDAP\_OTHER**                        | **ERROR\_GEN\_FAILURE**              | Unknown error occurred.                              |
| 0x8007001F       | **LDAP\_LOCAL\_ERROR**                 | **ERROR\_GEN\_FAILURE**              | Local error occurred.                                |
| 0x80070037       | **LDAP\_UNAVAILABLE**                  | **ERROR\_DEV\_NOT\_EXIST**           | Server is not available.                             |
| 0x8007003A       | **LDAP\_SERVER\_DOWN**                 | **ERROR\_BAD\_NET\_RESP**            | Cannot contact the LDAP server.                      |
| 0x8007003B       | **LDAP\_ENCODING\_ERROR**              | **ERROR\_UNEXP\_NET\_ERR**           | Encoding error occurred.                             |
| 0x8007003B       | **LDAP\_DECODING\_ERROR**              | **ERROR\_UNEXP\_NET\_ERR**           | Decoding error occurred.                             |
| 0x80070044       | **LDAP\_ADMIN\_LIMIT\_EXCEEDED**       | **ERROR\_TOO\_MANY\_NAMES**          | Exceeded administration limit on the server.         |
| 0x80070056       | **LDAP\_INVALID\_CREDENTIALS**         | **ERROR\_INVALID\_PASSWORD**         | Credential not valid.                                |
| 0x80070057       | **LDAP\_INVALID\_DN\_SYNTAX**          | **ERROR\_INVALID\_PARAMETER**        | Distinguished name has syntax that is not valid.     |
| 0x80070057       | **LDAP\_NAMING\_VIOLATION**            | **ERROR\_INVALID\_PARAMETER**        | Naming violation.                                    |
| 0x80070057       | **LDAP\_OBJECT\_CLASS\_VIOLATION**     | **ERROR\_INVALID\_PARAMETER**        | Object class violation.                              |
| 0x80070057       | **LDAP\_FILTER\_ERROR**                | **ERROR\_INVALID\_PARAMETER**        | Search filter is bad.                                |
| 0x80070057       | **LDAP\_PARAM\_ERROR**                 | **ERROR\_INVALID\_PARAMETER**        | Bad parameter was passed to a routine.               |
| 0X8007006E       | **LDAP\_OPERATIONS\_ERROR**            | **ERROR\_OPEN\_FAILED**              | Operation error occurred.                            |
| 0x8007007A       | **LDAP\_RESULTS\_TOO\_LARGE**          | **ERROR\_INSUFFICIENT\_BUFFER**      | Results set is too large.                            |
| 0x8007007B       | **LDAP\_INVALID\_SYNTAX**              | **ERROR\_INVALID\_NAME**             | Syntax not valid.                                    |
| 0x8007007C       | **LDAP\_PROTOCOL\_ERROR**              | **ERROR\_INVALID\_LEVEL**            | Protocol error.                                      |
| 0x800700B7       | **LDAP\_ALREADY\_EXISTS**              | **ERROR\_ALREADY\_EXISTS**           | Object already exists.                               |
| 0x800700EA       | **LDAP\_PARTIAL\_RESULTS**             | **ERROR\_MORE\_DATA**                | Partial results and referrals received.              |
| 0x800700EA       | **LDAP\_BUSY**                         | **ERROR\_BUSY**                      | Server is busy.                                      |
| 0x800703EB       | **LDAP\_UNWILLING\_TO\_PERFORM**       | **ERROR\_CAN\_NOT\_COMPLETE**        | Server cannot perform operation.                     |
| 0x8007041D       | **LDAP\_TIMEOUT**                      | **ERROR\_SERVICE\_REQUEST\_TIMEOUT** | Search timed out.                                    |
| 0x800704B8       | **LDAP\_COMPARE\_FALSE**               | **ERROR\_EXTENDED\_ERROR**           | Compare yielded **FALSE**.                           |
| 0x800704B8       | **LDAP\_COMPARE\_TRUE**                | **ERROR\_EXTENDED\_ERROR**           | Compare yielded **TRUE**.                            |
| 0x800704B8       | **LDAP\_REFERRAL**                     | **ERROR\_EXTENDED\_ERROR**           | Cannot resolve referral.                             |
| 0x800704B8       | **LDAP\_UNAVAILABLE\_CRIT\_EXTENSION** | **ERROR\_EXTENDED\_ERROR**           | Critical extension is unavailable.                   |
| 0x800704B8       | **LDAP\_NO\_SUCH\_ATTRIBUTE**          | **ERROR\_EXTENDED\_ERROR**           | Requested attribute does not exist.                  |
| 0x800704B8       | **LDAP\_UNDEFINED\_TYPE**              | **ERROR\_EXTENDED\_ERROR**           | Type is not defined.                                 |
| 0x800704B8       | **LDAP\_INAPPROPRIATE\_MATCHING**      | **ERROR\_EXTENDED\_ERROR**           | There was an inappropriate matching.                 |
| 0x800704B8       | **LDAP\_CONSTRAINT\_VIOLATION**        | **ERROR\_EXTENDED\_ERROR**           | There was a constrain violation.                     |
| 0x800704B8       | **LDAP\_ATTRIBUTE\_OR\_VALUE\_EXISTS** | **ERROR\_EXTENDED\_ERROR**           | The attribute exists or the value has been assigned. |
| 0x800704B8       | **LDAP\_ALIAS\_PROBLEM**               | **ERROR\_EXTENDED\_ERROR**           | Alias is not valid.                                  |
| 0x800704B8       | **LDAP\_IS\_LEAF**                     | **ERROR\_EXTENDED\_ERROR**           | Object is a leaf.                                    |
| 0x800704B8       | **LDAP\_ALIAS\_DEREF\_PROBLEM**        | **ERROR\_EXTENDED\_ERROR**           | Cannot dereference the alias.                        |
| 0x800704B8       | **LDAP\_LOOP\_DETECT**                 | **ERROR\_EXTENDED\_ERROR**           | Loop was detected.                                   |
| 0x800704B8       | **LDAP\_NOT\_ALLOWED\_ON\_NONLEAF**    | **ERROR\_EXTENDED\_ERROR**           | Operation is not allowed on a non-leaf object.       |
| 0x800704B8       | **LDAP\_NOT\_ALLOWED\_ON\_RDN**        | **ERROR\_EXTENDED\_ERROR**           | Operation is not allowed on RDN.                     |
| 0x800704B8       | **LDAP\_NO\_OBJECT\_CLASS\_MODS**      | **ERROR\_EXTENDED\_ERROR**           | Cannot modify object class.                          |
| 0x800704B8       | **LDAP\_AFFECTS\_MULTIPLE\_DSAS**      | **ERROR\_EXTENDED\_ERROR**           | Multiple directory service agents are affected.      |
| 0x800704C7       | **LDAP\_USER\_CANCELLED**              | **ERROR\_CANCELLED**                 | User has canceled the operation.                     |
| 0x80070718       | **LDAP\_TIMELIMIT\_EXCEEDED**          | **ERROR\_NOT\_ENOUGH\_QUOTA**        | Exceeded time limit.                                 |
| 0x80070718       | **LDAP\_SIZELIMIT\_EXCEEDED**          | **ERROR\_NOT\_ENOUGH\_QUOTA**        | Exceeded size limit.                                 |



 

In ADSI 2.0, several LDAP error messages are mapped to a Win32 error code as **ERROR\_EXTENDED\_ERROR**. Call [**ADsGetLastError**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetlasterror) to retrieve the error string returned by the server. For more information, see [ADSI Extended Error Messages](adsi-extended-error-messages.md) below.

 

 




