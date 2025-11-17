---
title: FW_RULE
description: TBD
ms.topic: reference
ms.date: 11/14/2025
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

Represents a firewall rule (appropriate for use by binary policy version 2.27 servers and clients). Also see [FW_GLOBAL_CONFIG](/openspecs/windows_protocols/ms-fasp/faf4ffbe-1d51-40ad-ae90-2230f2c0b6a9) and [FW_RULE](/openspecs/windows_protocols/ms-fasp/8c008258-166d-46d4-9090-f2ffaa01be4b).

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

TBD

`wszRuleId`

TBD

`wszName`

TBD

`wszDescription`

TBD

`dwProfiles`

TBD

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

TBD

`RemoteAddresses`

TBD

`LocalInterfaceIds`

TBD

`dwLocalInterfaceTypes`

Bit flags from **FW_INTERFACE_TYPE**.

`wszLocalApplication`

TBD

`wszLocalService`

TBD

`Action`

TBD

`wFlags`

Bit flags from **FW_RULE_FLAGS**.

`wszRemoteMachineAuthorizationList`

Authorized remote machines SDDL.

`wszRemoteUserAuthorizationList`

Authorized remote users SDDL.

`wszEmbeddedContext`

TBD

`PlatformValidityList`

TBD

`Status`

Parsing error if any, filled on return. On input, set this to **FW_RULE_STATUS_OK**.

`Origin`

Rule origin, filled on enumerated rules. Ignored on input.

`wszGPOName`

Name of originating GPO, if rule origin is GP.

`Reserved`

Reserved; don't use.

`pMetaData`

TBD

`wszLocalUserAuthorizationList`

Authorized local users SDDL.

`wszPackageId`

Application Container Package Id Sid.

`wszLocalUserOwner`

User owner of the rule.

`dwTrustTupleKeywords`

Trust tuple keywords.

`OnNetworkNames`

TBD

`wszSecurityRealmId`

Security realm identifier.

`wFlags2`

Bit flags from **FW_RULE_FLAGS2**.

`RemoteOutServerNames`

TBD

`wszFqbn`

TBD

`compartmentId`

TBD

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 11, version 23H2 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |

## See also

* [Windows Firewall with Advanced Security enums and structs](../firewall-enums-structs.md)
