---
title: SNMPv1 Trap Types (Snmp.h)
description: The SNMPv1 trap types describe a predefined set of generic trap types that are formatted to comply with the SNMPv1 trap PDU standard.
ms.assetid: 3a652b8f-2ae1-4f8c-b0d6-388bc9171427
topic_type:
- apiref
api_name:
- SNMP_GENERICTRAP_COLDSTART
- SNMP_GENERICTRAP_WARMSTART
- SNMP_GENERICTRAP_LINKDOWN
- SNMP_GENERICTRAP_LINKUP
- SNMP_GENERICTRAP_AUTHFAILURE
- SNMP_GENERICTRAP_EGPNEIGHLOSS
- SNMP_GENERICTRAP_ENTERSPECIFIC
api_location:
- Snmp.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SNMPv1 Trap Types

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

The SNMPv1 trap types describe a predefined set of generic trap types that are formatted to comply with the SNMPv1 trap PDU standard.



| Constant                                                                                                                                                                                                          | Description                                                                                                                                                                              |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SNMP_GENERICTRAP_COLDSTART"></span><span id="snmp_generictrap_coldstart"></span><dl> <dt>**SNMP\_GENERICTRAP\_COLDSTART**</dt> </dl>             | Indicates a cold start trap. The agent is initializing protocol entities on the managed mode. It may alter objects in its view.<br/>                                               |
| <span id="SNMP_GENERICTRAP_WARMSTART"></span><span id="snmp_generictrap_warmstart"></span><dl> <dt>**SNMP\_GENERICTRAP\_WARMSTART**</dt> </dl>             | Indicates a warm start trap. The agent is reinitializing itself but it will not alter objects in its view.<br/>                                                                    |
| <span id="SNMP_GENERICTRAP_LINKDOWN"></span><span id="snmp_generictrap_linkdown"></span><dl> <dt>**SNMP\_GENERICTRAP\_LINKDOWN**</dt> </dl>                | Indicates a link-down trap. An attached interface has changed from the up state to the down state. The first variable in the variable bindings list identifies the interface.<br/> |
| <span id="SNMP_GENERICTRAP_LINKUP"></span><span id="snmp_generictrap_linkup"></span><dl> <dt>**SNMP\_GENERICTRAP\_LINKUP**</dt> </dl>                      | Indicates a link-up trap. An attached interface has changed from the down start to the up state. The first variable in the variable bindings list identifies the interface.<br/>   |
| <span id="SNMP_GENERICTRAP_AUTHFAILURE"></span><span id="snmp_generictrap_authfailure"></span><dl> <dt>**SNMP\_GENERICTRAP\_AUTHFAILURE**</dt> </dl>       | Indicates an authentication failure trap. An SNMP entity has sent an SNMP message, but it has falsely claimed to belong to a known community.<br/>                                 |
| <span id="SNMP_GENERICTRAP_EGPNEIGHLOSS"></span><span id="snmp_generictrap_egpneighloss"></span><dl> <dt>**SNMP\_GENERICTRAP\_EGPNEIGHLOSS**</dt> </dl>    | Indicates an EGP neighbor loss trap. An EGP peer has changed to the down state. The first variable in the variable bindings list identifies the IP address of the EGP peer.<br/>   |
| <span id="SNMP_GENERICTRAP_ENTERSPECIFIC"></span><span id="snmp_generictrap_enterspecific"></span><dl> <dt>**SNMP\_GENERICTRAP\_ENTERSPECIFIC**</dt> </dl> | Indicates an enterprise-specific trap. An extraordinary event has occurred. It is identified in the *specificTrap* parameter with an enterprise-specific value.<br/>               |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Snmp.h</dt> </dl> |



## See also

<dl> <dt>

[Simple Network Management Protocol (SNMP) Overview](simple-network-management-protocol-snmp-.md)
</dt> <dt>

[SNMP Reference](snmp-reference.md)
</dt> <dt>

[SNMP Constants](snmp-constants.md)
</dt> </dl>

 

