---
description: Contains definitions of security terms that begin with the letter L.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 65dd9a04-fc7c-4179-95ff-dac7dad4668f
title: L (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# L (Security Glossary)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J [K](k-gly.md) L [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_ldap_gly"></span><span id="_SECURITY_LDAP_GLY"></span>**LDAP**
</dt> <dd>

See *Lightweight Directory Access Protocol*

</dd> <dt>

<span id="_security_lightweight_directory_access_protocol_gly"></span><span id="_SECURITY_LIGHTWEIGHT_DIRECTORY_ACCESS_PROTOCOL_GLY"></span>**Lightweight Directory Access Protocol**
</dt> <dd>

A more easily implemented subset of the X.500 DAP standard for directory services.

</dd> <dt>

<span id="_security_little_endian_gly"></span><span id="_SECURITY_LITTLE_ENDIAN_GLY"></span>**little-endian**
</dt> <dd>

A memory or data format in which the least significant byte is stored at the lower address or arrives first.

See also [*big-endian*](b-gly.md).

</dd> <dt>

<span id="_security_locally_unique_identifier_gly"></span><span id="_SECURITY_LOCALLY_UNIQUE_IDENTIFIER_GLY"></span>**locally unique identifier**
</dt> <dd>

(LUID) A 64-bit value that is guaranteed to be unique on the operating system that generated it until the system is restarted.

</dd> <dt>

<span id="_security_local_registration_authority_gly"></span><span id="_SECURITY_LOCAL_REGISTRATION_AUTHORITY_GLY"></span>**local registration authority**
</dt> <dd>

(LRA) An intermediary between a publisher and a [*certification authority*](c-gly.md) (CA). The LRA can, for example, verify a publisher's credentials before sending them to the CA.

</dd> <dt>

<span id="_security_local_security_authority_gly"></span><span id="_SECURITY_LOCAL_SECURITY_AUTHORITY_GLY"></span>**Local Security Authority**
</dt> <dd>

(LSA) A protected subsystem that authenticates and logs users onto the local system. LSA also maintains information about all aspects of local security on a system, collectively known as the Local Security Policy of the system.

</dd> <dt>

<span id="_security_logical_store_gly"></span><span id="_SECURITY_LOGICAL_STORE_GLY"></span>**logical store**
</dt> <dd>

See [*virtual store*](v-gly.md).

</dd> <dt>

<span id="_security_logon_data_gly"></span><span id="_SECURITY_LOGON_DATA_GLY"></span>**logon data**
</dt> <dd>

Information presented to the system by a [*security principal*](s-gly.md) for authentication.

</dd> <dt>

<span id="_security_logon_identifier_gly"></span><span id="_SECURITY_LOGON_IDENTIFIER_GLY"></span>**logon identifier**
</dt> <dd>

An LUID that identifies a *logon session*. A logon ID is valid until the user logs off. A logon ID is unique while the computer is running; no other logon session will have the same logon ID. However, the set of possible logon IDs is reset when the computer starts up. To retrieve the logon ID from an [*access token*](a-gly.md), call the **GetTokenInformation** function for TokenStatistics; the logon ID is in the **AuthenticationId** member.

</dd> <dt>

<span id="_security_logon_session_gly"></span><span id="_SECURITY_LOGON_SESSION_GLY"></span>**logon session**
</dt> <dd>

A logon session begins whenever a user logs on to a computer. All processes in a logon session have the same primary [*access token*](a-gly.md). The access token contains information about the security context of the logon session, including the user's SID, the *logon identifier*, and the *logon SID*.

</dd> <dt>

<span id="_security_logon_sid_gly"></span><span id="_SECURITY_LOGON_SID_GLY"></span>**logon SID**
</dt> <dd>

A [*security identifier*](s-gly.md) (SID) that identifies a *logon session*. You can use the logon SID in a [*DACL*](d-gly.md) to control access during a logon session. A logon SID is valid until the user logs off. A logon SID is unique while the computer is running; no other logon session will have the same logon SID. However, the set of possible logon SIDs is reset when the computer starts up. To retrieve the logon SID from an [*access token*](a-gly.md), call the **GetTokenInformation** function for TokenGroups.

</dd> <dt>

<span id="_security_low_level_message_functions_gly"></span><span id="_SECURITY_LOW_LEVEL_MESSAGE_FUNCTIONS_GLY"></span>**low-level message functions**
</dt> <dd>

Message management functions that operate at a higher level than the base cryptographic functions. These functions provide functionality for encoding data for transmission and for decoding data that has been received. Low-level message functions provide more flexibility than simplified message functions, but require more function calls.

See also [*simplified message functions*](s-gly.md).

</dd> <dt>

<span id="_security_lsa_gly"></span><span id="_SECURITY_LSA_GLY"></span>**LSA**
</dt> <dd>

See *Local Security Authority*.

</dd> <dt>

<span id="_security_luid_gly"></span><span id="_SECURITY_LUID_GLY"></span>**LUID**
</dt> <dd>

See *locally unique identifier*.

</dd> </dl>

 

 



