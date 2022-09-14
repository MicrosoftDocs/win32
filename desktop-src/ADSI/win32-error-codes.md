---
title: Win32 Error Codes
description: The following table lists the LDAP error messages for ADSI.
ms.assetid: b609bd56-770a-4546-8640-26ad6e108d54
ms.tgt_platform: multiple
keywords:
- Win32 Error Codes ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Win32 Error Codes

The following table lists the LDAP error messages for ADSI.



| ADSI Error Value | LDAP message                           | Win32 message                               | Description                                      |
|------------------|----------------------------------------|---------------------------------------------|--------------------------------------------------|
| 0L               | **LDAP\_SUCCESS**                      | **NO\_ERROR**                               | Operation succeeded.                             |
| 0x80070005L      | **LDAP\_INSUFFICIENT\_RIGHTS**         | **ERROR\_ACCESS\_DENIED**                   | User has insufficient access rights.             |
| 0x80070008L      | **LDAP\_NO\_MEMORY**                   | **ERROR\_NOT\_ENOUGH\_MEMORY**              | System is out of memory.                         |
| 0x8007001fL      | **LDAP\_OTHER**                        | **ERROR\_GEN\_FAILURE**                     | Unknown error.                                   |
| 0x800700eaL      | **LDAP\_PARTIAL\_RESULTS**             | **ERROR\_MORE\_DATA**                       | Partial results and referrals received.          |
| 0x800700eaL      | **LDAP\_MORE\_RESULTS\_TO\_RETURN**    | **ERROR\_MORE\_DATA**                       | More results are to be returned.                 |
| 0x800704c7L      | **LDAP\_USER\_CANCELLED**              | **ERROR\_CANCELLED**                        | User canceled the operation.                     |
| 0x800704c9L      | **LDAP\_CONNECT\_ERROR**               | **ERROR\_CONNECTION\_REFUSED**              | Cannot establish the connection.                 |
| 0x8007052eL      | **LDAP\_INVALID\_CREDENTIALS**         | **ERROR\_LOGON\_FAILURE**                   | Supplied credential is not valid.                |
| 0x800705b4L      | **LDAP\_TIMEOUT**                      | **ERROR\_TIMEOUT**                          | Search timed out.                                |
| 0x80071392L      | **LDAP\_ALREADY\_EXISTS**              | **ERROR\_OBJECT\_ALREADY\_EXISTS**          | Object already exists.                           |
| 0x8007200aL      | **LDAP\_NO\_SUCH\_ATTRIBUTE**          | **ERROR\_DS\_NO\_ATTRIBUTE\_OR\_VALUE**     | Requested attribute does not exist.              |
| 0x8007200bL      | **LDAP\_INVALID\_SYNTAX**              | **ERROR\_DS\_INVALID\_ATTRIBUTE\_SYNTAX**   | Syntax is not valid.                             |
| 0x8007200cL      | **LDAP\_UNDEFINED\_TYPE**              | **ERROR\_DS\_ATTRIBUTE\_TYPE\_UNDEFINED**   | Type not defined.                                |
| 0x8007200dL      | **LDAP\_ATTRIBUTE\_OR\_VALUE\_EXISTS** | **ERROR\_DS\_ATTRIBUTE\_OR\_VALUE\_EXISTS** | Attribute exists or the value has been assigned. |
| 0x8007200eL      | **LDAP\_BUSY**                         | **ERROR\_DS\_BUSY**                         | Server is busy.                                  |
| 0x8007200fL      | **LDAP\_UNAVAILABLE**                  | **ERROR\_DS\_UNAVAILABLE**                  | Server is not available.                         |
| 0x80072014L      | **LDAP\_OBJECT\_CLASS\_VIOLATION**     | **ERROR\_DS\_OBJ\_CLASS\_VIOLATION**        | Object class violation.                          |
| 0x80072015L      | **LDAP\_NOT\_ALLOWED\_ON\_NONLEAF**    | **ERROR\_DS\_CANT\_ON\_NON\_LEAF**          | Operation is not allowed on a non- leaf object.  |
| 0x80072016L      | **LDAP\_NOT\_ALLOWED\_ON\_RDN**        | **ERROR\_DS\_CANT\_ON\_RDN**                | Operation is not allowed on an RDN.              |
| 0x80072017L      | **LDAP\_NO\_OBJECT\_CLASS\_MODS**      | **ERROR\_DS\_CANT\_MOD\_OBJ\_CLASS**        | Cannot modify object class.                      |
| 0x80072020L      | **LDAP\_OPERATIONS\_ERROR**            | **ERROR\_DS\_OPERATIONS\_ERROR**            | Operation error occurred.                        |
| 0x80072021L      | **LDAP\_PROTOCOL\_ERROR**              | **ERROR\_DS\_PROTOCOL\_ERROR**              | Protocol error occurred.                         |
| 0x80072022L      | **LDAP\_TIMELIMIT\_EXCEEDED**          | **ERROR\_DS\_TIMELIMIT\_EXCEEDED**          | Exceeded time limit.                             |
| 0x80072023L      | **LDAP\_SIZELIMIT\_EXCEEDED**          | **ERROR\_DS\_SIZELIMIT\_EXCEEDED**          | Exceeded size limit.                             |
| 0x80072024L      | **LDAP\_ADMIN\_LIMIT\_EXCEEDED**       | **ERROR\_DS\_ADMIN\_LIMIT\_EXCEEDED**       | Exceeded administration limit on the server.     |
| 0x80072025L      | **LDAP\_COMPARE\_FALSE**               | **ERROR\_DS\_COMPARE\_FALSE**               | Compare yielded **FALSE**.                       |
| 0x80072026L      | **LDAP\_COMPARE\_TRUE**                | **ERROR\_DS\_COMPARE\_TRUE**                | Compare yielded **TRUE**.                        |
| 0x80072027L      | **LDAP\_AUTH\_METHOD\_NOT\_SUPPORTED** | **ERROR\_DS\_AUTH\_METHOD\_NOT\_SUPPORTED** | The authentication method is not supported.      |
| 0x80072028L      | **LDAP\_STRONG\_AUTH\_REQUIRED**       | **ERROR\_DS\_STRONG\_AUTH\_REQUIRED**       | Strong authentication is required.               |
| 0x80072029L      | **LDAP\_INAPPROPRIATE\_AUTH**          | **ERROR\_DS\_INAPPROPRIATE\_AUTH**          | Authentication is inappropriate.                 |
| 0x8007202aL      | **LDAP\_AUTH\_UNKNOWN**                | **ERROR\_DS\_AUTH\_UNKNOWN**                | Unknown authentication error occurred.           |
| 0x8007202bL      | **LDAP\_REFERRAL**                     | **ERROR\_DS\_REFERRAL**                     | Cannot resolve referral.                         |
| 0x8007202cL      | **LDAP\_UNAVAILABLE\_CRIT\_EXTENSION** | **ERROR\_DS\_UNAVAILABLE\_CRIT\_EXTENSION** | Critical extension is unavailable.               |
| 0x8007202dL      | **LDAP\_CONFIDENTIALITY\_REQUIRED**    | **ERROR\_DS\_CONFIDENTIALITY\_REQUIRED**    | Confidentiality is required.                     |
| 0x8007202eL      | **LDAP\_INAPPROPRIATE\_MATCHING**      | **ERROR\_DS\_INAPPROPRIATE\_MATCHING**      | There was an inappropriate matching.             |
| 0x8007202fL      | **LDAP\_CONSTRAINT\_VIOLATION**        | **ERROR\_DS\_CONSTRAINT\_VIOLATION**        | There was a constrain violation.                 |
| 0x80072030L      | **LDAP\_NO\_SUCH\_OBJECT**             | **ERROR\_DS\_NO\_SUCH\_OBJECT**             | Object does not exist.                           |
| 0x80072031L      | **LDAP\_ALIAS\_PROBLEM**               | **ERROR\_DS\_ALIAS\_PROBLEM**               | Alias is not valid.                              |
| 0x80072032L      | **LDAP\_INVALID\_DN\_SYNTAX**          | **ERROR\_DS\_INVALID\_DN\_SYNTAX**          | Distinguished name has syntax that is not valid. |
| 0x80072033L      | **LDAP\_IS\_LEAF**                     | **ERROR\_DS\_IS\_LEAF**                     | The object is a leaf.                            |
| 0x80072034L      | **LDAP\_ALIAS\_DEREF\_PROBLEM**        | **ERROR\_DS\_ALIAS\_DEREF\_PROBLEM**        | Cannot dereference the alias.                    |
| 0x80072035L      | **LDAP\_UNWILLING\_TO\_PERFORM**       | **ERROR\_DS\_UNWILLING\_TO\_PERFORM**       | Server cannot perform operation.                 |
| 0x80072036L      | **LDAP\_LOOP\_DETECT**                 | **ERROR\_DS\_LOOP\_DETECT**                 | Loop was detected.                               |
| 0x80072037L      | **LDAP\_NAMING\_VIOLATION**            | **ERROR\_DS\_NAMING\_VIOLATION**            | There was a naming violation.                    |
| 0x80072038L      | **LDAP\_RESULTS\_TOO\_LARGE**          | **ERROR\_DS\_OBJECT\_RESULTS\_TOO\_LARGE**  | Results set is too large.                        |
| 0x80072039L      | **LDAP\_AFFECTS\_MULTIPLE\_DSAS**      | **ERROR\_DS\_AFFECTS\_MULTIPLE\_DSAS**      | Multiple directory service agents are affected.  |
| 0x8007203aL      | **LDAP\_SERVER\_DOWN**                 | **ERROR\_DS\_SERVER\_DOWN**                 | Cannot contact the LDAP server.                  |
| 0x8007203bL      | **LDAP\_LOCAL\_ERROR**                 | **ERROR\_DS\_LOCAL\_ERROR**                 | Local error occurred.                            |
| 0x8007203cL      | **LDAP\_ENCODING\_ERROR**              | **ERROR\_DS\_ENCODING\_ERROR**              | Encoding error occurred.                         |
| 0x8007203dL      | **LDAP\_DECODING\_ERROR**              | **ERROR\_DS\_DECODING\_ERROR**              | Decoding error occurred.                         |
| 0x8007203eL      | **LDAP\_FILTER\_ERROR**                | **ERROR\_DS\_FILTER\_UNKNOWN**              | The search filter is bad.                        |
| 0x8007203fL      | **LDAP\_PARAM\_ERROR**                 | **ERROR\_DS\_PARAM\_ERROR**                 | A bad parameter was passed to a function.        |
| 0x80072040L      | **LDAP\_NOT\_SUPPORTED**               | **ERROR\_DS\_NOT\_SUPPORTED**               | Feature not supported.                           |
| 0x80072041L      | **LDAP\_NO\_RESULTS\_RETURNED**        | **ERROR\_DS\_NO\_RESULTS\_RETURNED**        | Results are not returned.                        |
| 0x80072042L      | **LDAP\_CONTROL\_NOT\_FOUND**          | **ERROR\_DS\_CONTROL\_NOT\_FOUND**          | Control was not found.                           |
| 0x80072043L      | **LDAP\_CLIENT\_LOOP**                 | **ERROR\_DS\_CLIENT\_LOOP**                 | Client loop was detected.                        |
| 0x80072044L      | **LDAP\_REFERRAL\_LIMIT\_EXCEEDED**    | **ERROR\_DS\_REFERRAL\_LIMIT\_EXCEEDED**    | Exceeded referral limit.                         |



 

 

 




