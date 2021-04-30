---
title: ms-DS-Repl-Authentication-Mode attribute
description: The ms-DS-Repl-Authentication-Mode attribute is used to specify which authentication method is used to authenticate replication partners.
ms.assetid: b7e77b40-7aa7-4990-93fd-c8068e35fcf9
ms.tgt_platform: multiple
keywords:
- ms-DS-Repl-Authentication-Mode attribute AD Schema
- msDS-ReplAuthenticationMode attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-Repl-Authentication-Mode
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-Repl-Authentication-Mode attribute

The **ms-DS-Repl-Authentication-Mode** attribute is used to specify which authentication method is used to authenticate replication partners. This attribute applies to the configuration partition of an ADAM instance.

The following values are the possible values for this attribute.

| Value        | Authentication method                          | Description                                                                                                                                                                    |
|--------------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0<br/> | Negotiated pass-through<br/>             | All ADAM instances in the configuration set use an identical account name and password as the ADAM service account.<br/>                                                 |
| 1<br/> | Negotiated<br/>                          | Kerberos authentication (using SPNs) is attempted first. If Kerberos fails, NTLM authentication is attempted. If NTLM fails, the ADAM instances will not replicate.<br/> |
| 2<br/> | Mutual authentication with Kerberos<br/> | Kerberos authentication, using service principal names (SPNs), is required. If Kerberos authentication fails, the ADAM instances will not replicate.<br/>                |



 

The following table contains the programmatic identifiers for the values of this attribute.

| Value        | Identifier (from Ntdsapi.h)                                               |
|--------------|---------------------------------------------------------------------------|
| 0<br/> | **ADAM\_REPL\_AUTHENTICATION\_MODE\_NEGOTIATE\_PASS\_THROUGH**<br/> |
| 1<br/> | **ADAM\_REPL\_AUTHENTICATION\_MODE\_NEGOTIATE**<br/>                |
| 2<br/> | **ADAM\_REPL\_AUTHENTICATION\_MODE\_MUTUAL\_AUTH\_REQUIRED**<br/>   |



 



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | ms-DS-Repl-Authentication-Mode       |
| Ldap-Display-Name | msDS-ReplAuthenticationMode          |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.1861              |
| System-Id-Guid    | 6e124d4f-1a3f-4cc6-8e09-4a54c81b1d50 |
| Syntax            | [**Enumeration**](s-enumeration.md) |



## Implementations

-   [**ADAM**](#adam)

## ADAM



| Entry | Value |
|------------------------|-----------------------------------------------------|
| Link-Id                | \-                                                  |
| MAPI-Id                | \-                                                  |
| System-Only            | False                                               |
| Is-Single-Valued       | True                                                |
| Is Indexed             | False                                               |
| In Global Catalog      | False                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                        |
| Range-Lower            | \-                                                  |
| Range-Upper            | \-                                                  |
| Search-Flags           | 0x00000000                                          |
| System-Flags           | 0x00000010                                          |
| Classes used in        | [**Configuration**](c-configuration.md)<br/> |



 

 





