---
title: FW_RULE
description: Represents a firewall rule.
ms.topic: reference
ms.date: 11/19/2025
tech.root: ics
topic_type:
- APIRef
- kbSyntax
api_type:
 - HeaderDef
api_location:
api_name:
- FW_RULE
targetos: Windows
ms.localizationpriority: low
req.header:
req.target-type: Windows
req.typenames: FW_RULE
---

# FW_RULE structure

Represents a firewall rule (appropriate for use by binary policy version 2.27 servers and clients). Also see [FW_RULE](/openspecs/windows_protocols/ms-fasp/8c008258-166d-46d4-9090-f2ffaa01be4b) and [Windows Firewall with Advanced Security enums and structs](../firewall-enums-structs.md).

## Syntax

```cpp
struct FW_RULE
{
	FW_RULE* pNext;
	WORD wSchemaVersion;

	LPWSTR wszRuleId;
	LPWSTR wszName;
	LPWSTR wszDescription;

	DWORD dwProfiles;

	FW_DIRECTION Direction;
	WORD wIpProtocol;
	union
	{
		struct
		{
			FW_PORTS LocalPorts;
			FW_PORTS RemotePorts;
		};

		FW_ICMP_TYPE_CODE_LIST V4TypeCodeList;
		FW_ICMP_TYPE_CODE_LIST V6TypeCodeList;
	};

	FW_ADDRESSES LocalAddresses;
	FW_ADDRESSES RemoteAddresses;
	FW_INTERFACE_LUIDS LocalInterfaceIds;
	DWORD dwLocalInterfaceTypes;
	LPWSTR wszLocalApplication;
	LPWSTR wszLocalService;

	FW_RULE_ACTION Action;
	WORD wFlags;

	LPWSTR wszRemoteMachineAuthorizationList;
	LPWSTR wszRemoteUserAuthorizationList;

	LPWSTR wszEmbeddedContext;
	FW_OS_PLATFORM_LIST PlatformValidityList;

	FW_RULE_STATUS Status;
	FW_RULE_ORIGIN_TYPE Origin;
	LPWSTR wszGPOName;
	DWORD Reserved;

	FW_OBJECT_METADATA* pMetaData;

	WCHAR* wszLocalUserAuthorizationList;

	WCHAR* wszPackageId;

	WCHAR* wszLocalUserOwner;

	DWORD dwTrustTupleKeywords;

	FW_NETWORK_NAMES OnNetworkNames;

    WCHAR* wszSecurityRealmId;

	WORD wFlags2;

	FW_NETWORK_NAMES RemoteOutServerNames;

	WCHAR* wszFqbn;

	DWORD compartmentId;
};
```

## Members

`pNext`

Points to the next **FW_RULE** structure in a linked list.

`wSchemaVersion`

Specifies the version of the rule.

`wszRuleId`

A pointer to a Unicode string that uniquely identifies the rule.

`wszName`

A pointer to a Unicode string that provides a friendly name for the rule.

`wszDescription`

A pointer to a Unicode string that provides a friendly description for the rule.

`dwProfiles`

A bitmask of the [FW_PROFILE_TYPE](../firewall-enums-structs.md) flags. It is a condition that matches traffic on the specified profiles.

`Direction`

An **FW_DIRECTION** structure.

`wIpProtocol`

A **WORD** value in the range 0-255, or **FW_IP_PROTOCOL_ANY**.

`LocalPorts`

Ports specified if *wIpProtocol* has the value 6 (TCP) or 17 (UDP).

`RemotePorts`

Ports specified if *wIpProtocol* has the value 6 (TCP) or 17 (UDP).

`V4TypeCodeList`

ICMP types/codes specified if *wIpProtocol* has the value of 1 (ICMPv4) or 58 (ICMPv6).

`V6TypeCodeList`

ICMP types/codes specified if *wIpProtocol* has the value of 1 (ICMPv4) or 58 (ICMPv6).

`LocalAddresses`

A condition that specifies the addresses of the local host of the traffic that the rule matches. An empty [FW_ADDRESSES](../firewall-enums-structs.md) structure means that this condition is not applied.

`RemoteAddresses`

A condition that specifies the addresses of the remote host of the traffic that the rule matches. An empty [FW_ADDRESSES](../firewall-enums-structs.md) structure means that this condition is not applied.

`LocalInterfaceIds`

A condition that specifies the list of specific network interfaces used by the traffic that the rule matches. An [FW_INTERFACE_LUIDS](../firewall-enums-structs.md) field with no interface GUID specified means that the rule applies to all interfaces; that is, the condition is not applied.

`dwLocalInterfaceTypes`

Bit flags from **FW_INTERFACE_TYPE**.

`wszLocalApplication`

A pointer to a Unicode string. It is a condition that specifies a file path name to the executable that uses the traffic that the rule matches. A null in this field means that the rule applies to all processes in the host.

`wszLocalService`

A pointer to a Unicode string. It is a condition that specifies the service name of the service that uses the traffic that the rule matches. An L"*" string in this field means that the rule applies to all services in the system. A null in this field means that the rule applies to all processes.

`Action`

The action that the rule will take for the traffic matches.

`wFlags`

Bit flags from **FW_RULE_FLAGS**.

`wszRemoteMachineAuthorizationList`

Authorized remote machines SDDL.

`wszRemoteUserAuthorizationList`

Authorized remote users SDDL.

`wszEmbeddedContext`

A pointer to a Unicode string. It specifies a group name for this rule. Other components in the system use this string to enable or disable groups of rules by verifying that they all have the same group name.

`PlatformValidityList`

A condition in a rule that determines whether or not the rule is enforced by the local computer based on the local computer's platform information. The rule is enforced only if the local computer's operating system platform is an element of the set described as follows. Windows uses the three fields of the [FW_OS_PLATFORM](../firewall-enums-structs.md) data type to identify Windows platform types. The fields in that data type correspond to the fields of the Windows OSVERSIONINFOEX data type (for more info, see [MSDN-OSVERSIONINFOEX](/windows/win32/api/winnt/ns-winnt-osversioninfoexa)). The Windows firewall and advanced security components extract the **OSVERSIONINFOEX** values, and use them to enforce PlatformValidityList conditions in **FW_RULE** and **FW_CS_RULE** rules.

`Status`

Parsing error if any, filled on return. On input, set this to **FW_RULE_STATUS_OK**.

`Origin`

Rule origin, filled on enumerated rules. Ignored on input.

`wszGPOName`

Name of originating GPO, if rule origin is GP.

`Reserved`

Reserved; don't use.

`pMetaData`

A pointer to an [FW_OBJECT_METADATA](/windows/win32/api/winnt/ns-winnt-osversioninfoexa) structure that contains specific metadata about the current state of the firewall rule.

`wszLocalUserAuthorizationList`

Authorized local users SDDL.

`wszPackageId`

Application Container Package Id Sid.

`wszLocalUserOwner`

User owner of the rule.

`dwTrustTupleKeywords`

Trust tuple keywords.

`OnNetworkNames`

Specifies the networks, identified by name, in which the rule must be enforced.

`wszSecurityRealmId`

Security realm identifier.

`wFlags2`

Bit flags from **FW_RULE_FLAGS2**.

`RemoteOutServerNames`

This value is not used over the wire.

`wszFqbn`

A string that is formatted as a fully qualified binary name (FQBN).

`compartmentId`

The ID of the compartment or Windows Server Container.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 11, version 23H2 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |

## See also

* [Windows Firewall with Advanced Security enums and structs](../firewall-enums-structs.md)
