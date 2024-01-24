---
description: Qualifiers contain implementation-specific context information and transport properties that define how the SNMP Provider accesses an SNMP agent. The following lists the qualifiers unique to the SNMP Provider.
ms.assetid: f2ac107c-e201-4670-96d1-883419787377
ms.tgt_platform: multiple
title: Qualifiers Specific to the SNMP Provider
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Qualifiers
api_type: 
- NA
api_location: 
---

# Qualifiers Specific to the SNMP Provider

Qualifiers contain implementation-specific context information and transport properties that define how the SNMP Provider accesses an SNMP agent. The following lists the qualifiers unique to the SNMP Provider.

<dt>

<span id="AgentAddress_"></span><span id="agentaddress_"></span><span id="AGENTADDRESS_"></span>**AgentAddress** 
</dt> <dd>

Data type: **CIM\_STRING**

Transport address associated with the SNMP agent, such as an IP address or DNS name. You should set **AgentAddress** to a valid unicast host address or a domain host name that can be resolved through the operating system's domain-name resolution process. **AgentAddress** has no default value.

</dd> <dt>

<span id="AgentFlowControlWindowSize_"></span><span id="agentflowcontrolwindowsize_"></span><span id="AGENTFLOWCONTROLWINDOWSIZE_"></span>**AgentFlowControlWindowSize** 
</dt> <dd>

Data type: **CIM\_SINT32**

Maximum number of concurrently outstanding SNMP requests that can be sent to this agent while a response has not yet been received. An SNMP request is considered outstanding until a PDU response has been received or it has timed out. A large window size generally improves performance, but some agents might not work well under a heavy load. **AgentFlowControlWindowSize** can be set to 0 to indicate an infinite window size or to an integer between 1 and 2^32-1. The default value is 10. This qualifier is optional.

</dd> <dt>

<span id="AgentReadCommunityName_"></span><span id="agentreadcommunityname_"></span><span id="AGENTREADCOMMUNITYNAME_"></span>**AgentReadCommunityName** 
</dt> <dd>

Data type: **CIM\_STRING**

Variable-length octet string that is used by the SNMP agent to authenticate an SNMP Protocol Data Unit (PDU) during a read operation (SNMP GET/GET NEXT requests). The community name must be mapped to a Unicode string and is limited to alphanumeric characters. The default value is public. This qualifier is optional.

</dd> <dt>

<span id="AgentRetryCount_"></span><span id="agentretrycount_"></span><span id="AGENTRETRYCOUNT_"></span>**AgentRetryCount** 
</dt> <dd>

Data type: **CIM\_SINT32**

Number of times a single SNMP request can be retried when there is no response from the SNMP agent before the request is deemed to have failed. **AgentRetryCount** must be set to an integer between 0 and 2^32-1. The default value is 1. This qualifier is optional.

</dd> <dt>

<span id="AgentRetryTimeout_"></span><span id="agentretrytimeout_"></span><span id="AGENTRETRYTIMEOUT_"></span>**AgentRetryTimeout** 
</dt> <dd>

Data type: **CIM\_SINT32**

Time in milliseconds before the SNMP Protocol Data Unit (PDU) is considered to have been dropped. This is the number of milliseconds to wait for a response to an SNMP request sent to the SNMP agent. **AgentRetryTimeout** must be set to an integer between 0 and 2^32-1. The default value is 500. This qualifier is optional.

</dd> <dt>

<span id="AgentSNMPVersion_"></span><span id="agentsnmpversion_"></span><span id="AGENTSNMPVERSION_"></span>**AgentSNMPVersion** 
</dt> <dd>

Data type: **CIM\_STRING**

Version of the SNMP protocol to be used when communicating with the SNMP agent. Currently, the only valid values are 1 (for SNMPv1) and 2C (for SNMPv2C). The default value is 1. This qualifier is optional.

</dd> <dt>

<span id="AgentTransport_"></span><span id="agenttransport_"></span><span id="AGENTTRANSPORT_"></span>**AgentTransport** 
</dt> <dd>

Data type: **CIM\_STRING**

Transport protocol used to communicate with the SNMP agent. Currently the only valid values are Internet Protocol (IP) and Internet Packet Exchange (IPX). The default value is IP. This qualifier is optional.

</dd> <dt>

<span id="AgentVarBindsPerPdu_"></span><span id="agentvarbindsperpdu_"></span><span id="AGENTVARBINDSPERPDU_"></span>**AgentVarBindsPerPdu** 
</dt> <dd>

Data type: **CIM\_SINT32**

Maximum number of variable bindings contained within a single SNMP PDU. Every SNMP request sent to the SNMP agent contains one or more SNMP variables. This parameter specifies the largest number of variables that can be included in a single request. **AgentVarBindsPerPdu** can be set to 0 (zero) to cause the implementation to determine the optimal variable bindings or to an integer between 1 and 2^32-1. Note that while increasing this value can improve performance, some agents and networks cannot deal with the resulting request. The default value is 10. This qualifier is optional.

</dd> <dt>

<span id="AgentWriteCommunityName_"></span><span id="agentwritecommunityname_"></span><span id="AGENTWRITECOMMUNITYNAME_"></span>**AgentWriteCommunityName** 
</dt> <dd>

Data type: **CIM\_STRING**

Variable-length octet string that is used by the SNMP agent to authenticate an SNMP Protocol Data Unit (PDU) during a write operation (SNMP SET request). The community name must be mapped to a Unicode string and is limited to alphanumeric characters. The default value is public. This qualifier is optional.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



 

 




