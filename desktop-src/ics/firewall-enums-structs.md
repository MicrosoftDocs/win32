---
title: Windows Firewall with Advanced Security enums and structs
description: Windows Firewall with Advanced Security contains the following enums and structs.
keywords:
- Windows Firewall with Advanced Security, enums, structs
ms.topic: reference
ms.date: 11/14/2025
---

# Windows Firewall with Advanced Security enums and structs

Windows Firewall with Advanced Security contains the following enums and structs.

* [FW_RULE structure](./firewall/ns-firewall-fw_rule.md)

```cpp
#define FW_VERSION(major,minor) \
        ((WORD)(((BYTE)(minor)) | ((WORD)((BYTE)(major))) << 8))

#define FW_CURRENT_BINARY_VERSION FW_VERSION(2,27)

enum FW_POLICY_STORE_FLAGS
{
    FW_POLICY_STORE_FLAGS_NONE = 0x0000,
    FW_POLICY_STORE_FLAGS_DELETE_DYNAMIC_RULES_AFTER_CLOSE = 0x0001,
    FW_POLICY_STORE_FLAGS_OPEN_GP_CACHE = 0x0002,
    FW_POLICY_STORE_FLAGS_USE_GP_CACHE = 0x0004,
    FW_POLICY_STORE_FLAGS_SAVE_GP_CACHE = 0x0008,
    FW_POLICY_STORE_FLAGS_NOT_USED_VALUE_16 = 0x0010,
    FW_POLICY_STORE_FLAGS_COALESCE_NETISO = FW_POLICY_STORE_FLAGS_NOT_USED_VALUE_16,
    FW_POLICY_STORE_FLAGS_MAX = 0x0020
};

enum FW_STORE_TYPE
{
	FW_STORE_TYPE_INVALID = 0,
	FW_STORE_TYPE_GP_RSOP = 1, //read-only
	FW_STORE_TYPE_LOCAL = 2,
	FW_STORE_TYPE_NOT_USED_VALUE_3 = 3, //read-only
	FW_STORE_TYPE_NOT_USED_VALUE_4 = 4,
	FW_STORE_TYPE_DYNAMIC = 5,
	FW_STORE_TYPE_GPO = 6,
	FW_STORE_TYPE_DEFAULTS = 7,
	FW_STORE_TYPE_NOT_USED_VALUE_8 = 8,
	FW_STORE_TYPE_NOT_USED_VALUE_9 = 9,
	FW_STORE_TYPE_NOT_USED_VALUE_10 = 10,
	FW_STORE_TYPE_NOT_USED_VALUE_11 = 11,
	FW_STORE_TYPE_NOT_USED_VALUE_12 = 12,
	FW_STORE_TYPE_MAX = 13,
	FW_STORE_TYPE_WSH_STATIC = FW_STORE_TYPE_NOT_USED_VALUE_3, //read-only
	FW_STORE_TYPE_WSH_CONFIGURABLE = FW_STORE_TYPE_NOT_USED_VALUE_4,
	FW_STORE_TYPE_IF_ISO = FW_STORE_TYPE_NOT_USED_VALUE_8, //read-only
	FW_STORE_TYPE_IF_ISO_DYNAMIC = FW_STORE_TYPE_NOT_USED_VALUE_9,
	FW_STORE_TYPE_APP_ISO = FW_STORE_TYPE_NOT_USED_VALUE_10,
	FW_STORE_TYPE_MDM = FW_STORE_TYPE_NOT_USED_VALUE_11,
	FW_STORE_TYPE_TENANT_RESTRICTIONS = FW_STORE_TYPE_NOT_USED_VALUE_12
};

enum FW_PROFILE_TYPE
{
	FW_PROFILE_TYPE_INVALID = 0,
	FW_PROFILE_TYPE_DOMAIN = 0x001,
	FW_PROFILE_TYPE_STANDARD = 0x002,
	FW_PROFILE_TYPE_PRIVATE = FW_PROFILE_TYPE_STANDARD,
	FW_PROFILE_TYPE_PUBLIC = 0x004,
	FW_PROFILE_TYPE_ALL = 0x7FFFFFFF,
	FW_PROFILE_TYPE_CURRENT = 0x80000000,
	FW_PROFILE_TYPE_NONE = FW_PROFILE_TYPE_CURRENT + 1
};

enum FW_POLICY_ACCESS_RIGHT
{
	FW_POLICY_ACCESS_RIGHT_INVALID,
	FW_POLICY_ACCESS_RIGHT_READ,
	FW_POLICY_ACCESS_RIGHT_READ_WRITE,
	FW_POLICY_ACCESS_RIGHT_MAX
};

struct FW_IPV4_SUBNET
{
	DWORD dwAddress;
	DWORD dwSubNetMask;
};

struct FW_IPV4_SUBNET_LIST
{
	DWORD dwNumEntries;
	FW_IPV4_SUBNET* pSubNets;
};

struct FW_IPV6_SUBNET
{
	BYTE Address[16];
	DWORD dwNumPrefixBits;
};

struct FW_IPV6_SUBNET_LIST
{
	DWORD dwNumEntries;
	FW_IPV6_SUBNET* pSubNets;
};

struct FW_IPV4_ADDRESS_RANGE
{
	DWORD dwBegin;
	DWORD dwEnd;
};

struct FW_IPV6_ADDRESS_RANGE
{
	BYTE Begin[16];
	BYTE End[16];
};

struct FW_IPV4_RANGE_LIST
{
	DWORD dwNumEntries;
	FW_IPV4_ADDRESS_RANGE* pRanges;
};

struct FW_IPV6_RANGE_LIST
{
	DWORD dwNumEntries;
	FW_IPV6_ADDRESS_RANGE* pRanges;
};

struct FW_PORT_RANGE
{
	WORD wBegin;
	WORD wEnd;
};

struct FW_PORT_RANGE_LIST
{
	DWORD dwNumEntries;
	FW_PORT_RANGE* pPorts;
};

enum FW_PORT_KEYWORD
{
	FW_PORT_KEYWORD_NONE = 0x00,
	FW_PORT_KEYWORD_DYNAMIC_RPC_PORTS = 0x01,
	FW_PORT_KEYWORD_RPC_EP = 0x02,
	FW_PORT_KEYWORD_TEREDO_PORT = 0x04,
	FW_PORT_KEYWORD_IP_TLS_IN = 0x08,
	FW_PORT_KEYWORD_IP_TLS_OUT = 0x10,
	FW_PORT_KEYWORD_DHCP = 0x20,
	FW_PORT_KEYWORD_PLAYTO_DISCOVERY = 0x40,
	FW_PORT_KEYWORD_MDNS = 0x80,
	FW_PORT_KEYWORD_CORTANA_OUT = 0x100,
	FW_PORT_KEYWORD_PROXIMAL_TCP_CDP = 0x200,
	FW_PORT_KEYWORD_MAX = 0x400,
	FW_PORT_KEYWORD_IP_HTTPS_IN = FW_PORT_KEYWORD_IP_TLS_IN,
	FW_PORT_KEYWORD_IP_HTTPS_OUT = FW_PORT_KEYWORD_IP_TLS_OUT,
	FW_PORT_KEYWORD_MAX_V2_1 = 0x08,
	FW_PORT_KEYWORD_MAX_V2_10 = 0x20,
	FW_PORT_KEYWORD_MAX_V2_20 = 0x80,
	FW_PORT_KEYWORD_MAX_V2_24 = 0x100,
	FW_PORT_KEYWORD_MAX_V2_25 = 0x200,
};

struct FW_PORTS
{
	WORD wPortKeywords; // Bit-flags from FW_PORT_KEYWORD
	FW_PORT_RANGE_LIST Ports;
};

#define FW_ICMP_CODE_ANY       256
#define FW_IP_PROTOCOL_ANY     256

struct FW_ICMP_TYPE_CODE
{
	BYTE bType;
	WORD wCode;
};

struct FW_ICMP_TYPE_CODE_LIST
{
	DWORD dwNumEntries;
	FW_ICMP_TYPE_CODE* pEntries;
};

struct FW_INTERFACE_LUIDS
{
	DWORD dwNumLUIDs;
	GUID* pLUIDs;
};

enum FW_DIRECTION
{
	FW_DIR_INVALID = 0,
	FW_DIR_IN,
	FW_DIR_OUT,
	FW_DIR_MAX
};

// Interface Types bitmap.
enum FW_INTERFACE_TYPE
{
	FW_INTERFACE_TYPE_ALL = 0x0000,
	FW_INTERFACE_TYPE_LAN = 0x0001,
	FW_INTERFACE_TYPE_WIRELESS = 0x0002,
	FW_INTERFACE_TYPE_REMOTE_ACCESS = 0x0004,
	FW_INTERFACE_TYPE_MOBILE_BBAND = 0x0008,
	FW_INTERFACE_TYPE_MAX = 0x0010,
	FW_INTERFACE_TYPE_MAX_V2_23 = 0x0008,
};

enum FW_ADDRESS_KEYWORD
{
	FW_ADDRESS_KEYWORD_NONE = 0x0000,
	FW_ADDRESS_KEYWORD_LOCAL_SUBNET = 0x0001,
	FW_ADDRESS_KEYWORD_DNS = 0x0002,
	FW_ADDRESS_KEYWORD_DHCP = 0x0004,
	FW_ADDRESS_KEYWORD_WINS = 0x0008,
	FW_ADDRESS_KEYWORD_DEFAULT_GATEWAY = 0x0010,
	FW_ADDRESS_KEYWORD_INTRANET = 0x0020,
	FW_ADDRESS_KEYWORD_INTERNET = 0x0040,
	FW_ADDRESS_KEYWORD_PLAYTO_RENDERERS = 0x0080,
	FW_ADDRESS_KEYWORD_REMOTE_INTRANET = 0x0100,
	FW_ADDRESS_KEYWORD_CAPTIVE_PORTAL = 0x0200,
	// This flag is internal use only.
	FW_ADDRESS_KEYWORD_INTERNAL_LOCAL_ADDRESSES = 0x0400,
	FW_ADDRESS_KEYWORD_MAX_V2_10 = 0x0020,
	FW_ADDRESS_KEYWORD_MAX = 0x0800,
};

struct FW_ADDRESSES
{
	DWORD dwV4AddressKeywords; // Bit flags from FW_ADDRESS_KEYWORD
	DWORD dwV6AddressKeywords; // Bit flags from FW_ADDRESS_KEYWORD

	FW_IPV4_SUBNET_LIST V4SubNets;
	FW_IPV4_RANGE_LIST V4Ranges;
	FW_IPV6_SUBNET_LIST V6SubNets;
	FW_IPV6_RANGE_LIST V6Ranges;
};

enum FW_RULE_STATUS
{
	FW_RULE_STATUS_OK = 0x00010000,
	// The rule was parsed successfully from the store.

	FW_RULE_STATUS_PARTIALLY_IGNORED = 0x00020000,
	// The rule is from a later version of the service. Some fields
	// were not understood and have been ignored. This may cause the
	// rule to be less restrictive than on the version where it was
	// created. To mitigate any risk from this fallback behavior,
	// ensure that the original rule is as specific as possible. To
	// avoid this fallback behavior, create version-specific GPO's, or
	// apply a Platform condition to the rule.

	FW_RULE_STATUS_IGNORED = 0x00040000,
	// The rule is from a newer schema version than the service, and
	// the unknown fields could not be ignored.  The whole rule was
	// ignored.

	FW_RULE_STATUS_PARSING_ERROR = 0x00080000,
	// The service was unable to parse the rule.

	FW_RULE_STATUS_PARSING_ERROR_NAME = 0x00080001,
	// The name contains invalid characters, or is an invalid length.

	FW_RULE_STATUS_PARSING_ERROR_DESC = 0x00080002,
	// The description contains invalid characters, or is an invalid
	// length.

	FW_RULE_STATUS_PARSING_ERROR_APP = 0x00080003,
	// The application contains invalid characters, or is an invalid
	// length.

	FW_RULE_STATUS_PARSING_ERROR_SVC = 0x00080004,
	// The service contains invalid characters, or is an invalid length.

	FW_RULE_STATUS_PARSING_ERROR_RMA = 0x00080005,
	// The authorized remote machines list contains invalid characters,
	// or is an invalid length.

	FW_RULE_STATUS_PARSING_ERROR_RUA = 0x00080006,
	// The authorized remote users list contains invalid characters, or
	// is an invalid length.

	FW_RULE_STATUS_PARSING_ERROR_EMBD = 0x00080007,
	// The group (sometimes called the embedded context) contains
	// invalid characters, or is an invalid length.

	FW_RULE_STATUS_PARSING_ERROR_RULE_ID = 0x00080008,
	// The rule ID contains invalid characters, or is an invalid length.

	FW_RULE_STATUS_PARSING_ERROR_PHASE1_AUTH = 0x00080009,
	// The phase 1 auth set ID contains invalid characters, or is an
	// invalid length.

	FW_RULE_STATUS_PARSING_ERROR_PHASE2_CRYPTO = 0x0008000A,
	// The quick mode crypto set ID contains invalid characters, or is
	// an invalid length.

	FW_RULE_STATUS_PARSING_ERROR_PHASE2_AUTH = 0x0008000B,
	// The main mode crypto set ID contains invalid characters, or is
	// an invalid length.

	FW_RULE_STATUS_PARSING_ERROR_RESOLVE_APP = 0x0008000C,
	// The application name could not be resolved.

	FW_RULE_STATUS_PARSING_ERROR_MAINMODE_ID = 0x0008000D,
	// This error value is not used.

	FW_RULE_STATUS_PARSING_ERROR_PHASE1_CRYPTO = 0x0008000E,
	// The phase 2 auth set ID contains invalid characters, or is an
	// invalid length.

	FW_RULE_STATUS_PARSING_ERROR_REMOTE_ENDPOINTS = 0x0008000F,
	// The remote endpoints are invalid.

	FW_RULE_STATUS_PARSING_ERROR_REMOTE_ENDPOINT_FQDN = 0x00080010,
	// The remote endpoint FQDN is invalid.

	FW_RULE_STATUS_PARSING_ERROR_KEY_MODULE = 0x00080011,
	// The choice of key modules is invalid.

	FW_RULE_STATUS_PARSING_ERROR_LUA = 0x00080012,
	// The local user authorization list contains invalid characters,
	// or is an invalid length.

	FW_RULE_STATUS_PARSING_ERROR_FWD_LIFETIME = 0x00080013,
	// The forward path SA lifetime is invalid.

	FW_RULE_STATUS_PARSING_ERROR_TRANSPORT_MACHINE_AUTHZ_SDDL = 0x00080014,
	// The transport rule machine SDDL is not valid.

	FW_RULE_STATUS_PARSING_ERROR_TRANSPORT_USER_AUTHZ_SDDL = 0x00080015,
	// The transport rule user SDDL is not valid.

	FW_RULE_STATUS_PARSING_ERROR_NETNAMES_STRING = 0x00080016,
	// A string of the network name structure is invalid.

	FW_RULE_STATUS_PARSING_ERROR_SECURITY_REALM_ID_STRING = 0x00080017,
	// A string for the security realm Id is invalid.

	FW_RULE_STATUS_PARSING_ERROR_FQBN_STRING = 0x00080018,
	// A string for the FQBN is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR = 0x00100000,
	// The rule was parsed successfully, but there was an unknown
	// semantic error when processing the rule.

	FW_RULE_STATUS_SEMANTIC_ERROR_RULE_ID = 0x00100010,
	// The Rule ID was not specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_PORTS = 0x00100020,
	// Mismatch in number of ports and ports buffer.

	FW_RULE_STATUS_SEMANTIC_ERROR_PORT_KEYW = 0x00100021,
	// One of the port keywords is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PORT_RANGE = 0x00100022,
	// An invalid port range was specified, or 0 was used as a port
	// number.

	FW_RULE_STATUS_SEMANTIC_ERROR_PORTRANGE_RESTRICTION = 0x00100023,
	// Port ranges are only allowed in connection security rules when
	// the action is Do Not Secure.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_V4_SUBNETS = 0x00100040,
	// Mismatch in number of V4 address subnets and subnets buffer.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_V6_SUBNETS = 0x00100041,
	// Mismatch in number of V6 address subnets and subnets buffer.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_V4_RANGES = 0x00100042,
	// Mismatch in number of V4 address ranges and ranges buffer.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_V6_RANGES = 0x00100043,
	// Mismatch in number of V6 address ranges and ranges buffer.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_RANGE = 0x00100044,
	// The address range is invalid.  The end address is less than the
	// beginning address.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_MASK = 0x00100045,
	// One or more of the subnet masks is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_PREFIX = 0x00100046,
	// One or more of the address prefixes is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_KEYW = 0x00100047,
	// One or more of the address keywords are invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_LADDR_PROP = 0x00100048,
	// Some of the keywords specified on the local address are only
	// valid on the remote address.

	FW_RULE_STATUS_SEMANTIC_ERROR_RADDR_PROP = 0x00100049,
	// Some of the keywords specified on the remote address are only
	// valid on the local address.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_V6 = 0x0010004A,
	// An unspecified, multicast, broadcast, or loopback IPv6 address
	// was specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_LADDR_INTF = 0x0010004B,
	// A local address cannot be used in conjunction with an interface
	// or interface type condition.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_V4 = 0x0010004C,
	// An unspecified, multicast, broadcast, or loopback IPv4 address
	// was specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_TUNNEL_ENDPOINT_ADDR = 0x0010004D,
	// Endpoint 'any' cannot be specified for a tunnel-mode rule.

	FW_RULE_STATUS_SEMANTIC_ERROR_DTE_VER = 0x0010004E,
	// The target schema version does not support dynamic endpoints.

	FW_RULE_STATUS_SEMANTIC_ERROR_DTE_MISMATCH_ADDR = 0x0010004F,
	// When specifying tunnel endpoints in both IPv4 and IPv6, a tunnel
	// endpoint may not be dynamic for one address family and explicit
	// for the other.  (A dynamic tunnel endpoint is one set to "Any".)

	FW_RULE_STATUS_SEMANTIC_ERROR_PROFILE = 0x00100050,
	// The profile type is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_ICMP = 0x00100060,
	// Mismatch in number of ICMP and ICMP buffer.

	FW_RULE_STATUS_SEMANTIC_ERROR_ICMP_CODE = 0x00100061,
	// Invalid ICMP code specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_IF_ID = 0x00100070,
	// Number of interfaces and interface buffer don't match.

	FW_RULE_STATUS_SEMANTIC_ERROR_IF_TYPE = 0x00100071,
	// The interface type is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_ACTION = 0x00100080,
	// The action is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_ALLOW_BYPASS = 0x00100081,
	// Allow-Bypass action specified, but the rule does not meet
	// allow-bypass criteria (inbound, authenticate/encrypt flags set,
	// remote machine auth list specified)

	FW_RULE_STATUS_SEMANTIC_ERROR_DO_NOT_SECURE = 0x00100082,
	// If the action is Do Not Secure, the auth and crypto sets must be
	// null.

	FW_RULE_STATUS_SEMANTIC_ERROR_ACTION_BLOCK_IS_ENCRYPTED_SECURE = 0x00100083,
	// Block action was specified in conjunction with require security
	// or require encryption.

	FW_RULE_STATUS_SEMANTIC_ERROR_INCOMPATIBLE_FLAG_OR_ACTION_WITH_SECURITY_REALM = 0x00100084,
	// Firewall Rules with security realm Id field would require authentication
	// and encryption, and action should be Allow.

	FW_RULE_STATUS_SEMANTIC_ERROR_DIR = 0x00100090,
	// The direction is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PROT = 0x001000A0,
	// The protocol number is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PROT_PROP = 0x001000A1,
	// The protocol-specific options do not match the protocol that was
	// chosen.

	FW_RULE_STATUS_SEMANTIC_ERROR_DEFER_EDGE_PROP = 0x001000A2,
	// The edge traversal flags are inconsistent.  Defer To App must be
	// set without Edge Traversal, but Defer To User must be set with
	// Edge Traversal.

	FW_RULE_STATUS_SEMANTIC_ERROR_ALLOW_BYPASS_OUTBOUND = 0x001000A3,
	// Allow-Bypass action specified, but the rule does not meet
	// allow-bypass criteria (authenticate/encrypt flags set)

	FW_RULE_STATUS_SEMANTIC_ERROR_DEFER_USER_INVALID_RULE = 0x001000A4,
	// Defer to user' setting can only be used in a firewall rule where
	// program path and TCP/UDP protocol are specified with no
	// additional conditions.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS = 0x001000B0,
	// Invalid flags specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_AUTO_AUTH = 0x001000B1,
	// Autogenerate flag is set but Authenticate / Authenticate-encrypt
	// flags are not set.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_AUTO_BLOCK = 0x001000B2,
	// Autogenerate flag is set but the action is block.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_AUTO_DYN_RPC = 0x001000B3,
	// Autogenerate flag is set along with Dynamic RPC flag.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_AUTHENTICATE_ENCRYPT = 0x001000B4,
	// The Authentication and Authentication & Encryption flags cannot
	// be used together.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_AUTH_WITH_ENC_NEGOTIATE_VER = 0x001000B5,
	// The target schema version does not support Authentication
	// (Dynamic Encryption).

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_AUTH_WITH_ENC_NEGOTIATE = 0x001000B6,
	// When the Authentication (Dynamic Encryption) flag is set, the
	// Authentication & Encryption flag must be set as well.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_ESP_NO_ENCAP_VER = 0x001000B7,
	// The target schema version does not support Authentication (No
	// Encapsulation).

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_ESP_NO_ENCAP = 0x001000B8,
	// When the Authentication (No Encapsulation) flag is set, the
	// Authentication flag must be set as well.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_TUNNEL_AUTH_MODES_VER = 0x001000B9,
	// The target schema version does not support tunnel authentication
	// modes.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_TUNNEL_AUTH_MODES = 0x001000BA,
	// The target schema version does not support tunnel authentication
	// modes.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_IP_HTTPS_VER = 0x001000BB,
	// The target schema version does not support the IP_HTTPS keyword.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_IP_TLS_VER = 0x001000BB,
	// The target schema version does not support the IP_TLS keyword.

	FW_RULE_STATUS_SEMANTIC_ERROR_PORTRANGE_VER = 0x001000BC,
	// The target schema version does not support port ranges.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_ADDRS_TRAVERSE_DEFER_VER = 0x001000BD,
	// The target schema version does not support dynamic edge
	// traversal.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_AUTH_WITH_ENC_NEGOTIATE_OUTBOUND = 0x001000BE,
	// The Authentication (Dynamic Encryption) flag cannot be used when
	// direction is Outbound.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_AUTHENTICATE_WITH_OUTBOUND_BYPASS_VER = 0x001000BF,
	// The target schema version does not support outbound Allow-Bypass
	// rules.

	FW_RULE_STATUS_SEMANTIC_ERROR_REMOTE_AUTH_LIST = 0x001000C0,
	// Authorization lists can only be used if authentication is
	// required on the rule.

	FW_RULE_STATUS_SEMANTIC_ERROR_REMOTE_USER_LIST = 0x001000C1,
	// Remote user authorization can only be applied to inbound rules.

	FW_RULE_STATUS_SEMANTIC_ERROR_LOCAL_USER_LIST = 0x001000C2,
	// The authorized local user list may not be used in conjunction
	// with a service SID.

	FW_RULE_STATUS_SEMANTIC_ERROR_LUA_VER = 0x001000C3,
	// The target schema version does not support the authorized local
	// user list.

	FW_RULE_STATUS_SEMANTIC_ERROR_LOCAL_USER_OWNER = 0x001000C4,
	// The local user owner field may not be used in conjunction with a
	// service SID.

	FW_RULE_STATUS_SEMANTIC_ERROR_LOCAL_USER_OWNER_VER = 0x001000C5,
	// The target schema version does not support the local user owner
	// field.

	FW_RULE_STATUS_SEMANTIC_ERROR_LUA_CONDITIONAL_VER = 0x001000C6,
	// The target schema version does not support the authorized local
	// user list containing conditional aces (e.g. aces with claims).

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_SYSTEMOS_GAMEOS = 0x001000C7,
	// The Sytem OS Only and Game OS Only flags cannot
	// be used together.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_CORTANA_VER = 0x001000C8,
	// The Sytem OS Only and Game OS Only flags cannot
	// be used together.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_REMOTENAME = 0x001000C9,
	// The Sytem OS Only and Game OS Only flags cannot
	// be used together.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_ALLOW_PROFILE_CROSSING_VER = 0x001000D0,
	// The target schema version does not support profile crossing.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_LOCAL_ONLY_MAPPED_VER = 0x001000D1,
	// The target schema version does not support local only mapping.

	FW_RULE_STATUS_SEMANTIC_ERROR_PLATFORM = 0x001000E0,
	// Number of valid OS Platforms and the list of valid OS Platforms
	// don't match

	FW_RULE_STATUS_SEMANTIC_ERROR_PLATFORM_OP_VER = 0x001000E1,
	// The target schema version does not support the platform operator
	// specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_PLATFORM_OP = 0x001000E2,
	// One of the platform operators is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_DTE_NOANY_ADDR = 0x001000F0,
	// The DTM flag requires at least one dynamic endpoint.

	FW_RULE_STATUS_SEMANTIC_ERROR_TUNNEL_EXEMPT_WITH_GATEWAY = 0x001000F1,
	// A dynamic tunnel-mode exemption rule cannot have tunnel
	// endpoints.

	FW_RULE_STATUS_SEMANTIC_ERROR_TUNNEL_EXEMPT_VER = 0x001000F2,
	// The target schema version does not support tunnel-mode
	// exemptions.

	FW_RULE_STATUS_SEMANTIC_ERROR_ADDR_KEYWORD_VER = 0x001000F3,
	// The target schema version does not support one or more of the
	// address keywords given.

	FW_RULE_STATUS_SEMANTIC_ERROR_KEY_MODULE_VER = 0x001000F4,
	// The target schema version does not support custom key module
	// preferences.

	FW_RULE_STATUS_SEMANTIC_ERROR_APP_CONTAINER_PACKAGE_ID = 0x00100100,
	// The application package SID is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_APP_CONTAINER_PACKAGE_ID_VER = 0x00100101,
	// The target schema version does not support application package
	// SIDs.

	FW_RULE_STATUS_SEMANTIC_ERROR_TRUST_TUPLE_KEYWORD_INCOMPATIBLE = 0x00100200,
	// Logical endpoints (trust tuples) cannot be combined with
	// specific addresses or ports.

	FW_RULE_STATUS_SEMANTIC_ERROR_TRUST_TUPLE_KEYWORD_INVALID = 0x00100201,
	// One or more of the logical endpoints (trust tuples) are invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_TRUST_TUPLE_KEYWORD_VER = 0x00100202,
	// The target schema version does not support logical endpoints
	// (trust tuples).

	FW_RULE_STATUS_SEMANTIC_ERROR_INTERFACE_TYPES_VER = 0x00100301,
	// The target schema version does not support the specified
	// local interface type

	FW_RULE_STATUS_SEMANTIC_ERROR_NETNAMES_VER = 0x00100401,
	// The target schema version does not support the specified
	// local interface type

	FW_RULE_STATUS_SEMANTIC_ERROR_SECURITY_REALM_ID_VER = 0x00100402,
	// The target schema version does not support security realm Id

	FW_RULE_STATUS_SEMANTIC_ERROR_SYSTEMOS_GAMEOS_VER = 0x00100403,
	// The target schema version does not support specifying System OS or Game OS flag

	FW_RULE_STATUS_SEMANTIC_ERROR_DEVMODE_VER = 0x00100404,
	// The target schema version does not support specifying Development mode flag

	FW_RULE_STATUS_SEMANTIC_ERROR_REMOTE_SERVERNAME_VER = 0x00100405,
	// The target schema version does not support specifying Remote Server Name attributes

	FW_RULE_STATUS_SEMANTIC_ERROR_FQBN_VER = 0x00100406,
	// The target schema version does not support specifying fqbn

	FW_RULE_STATUS_SEMANTIC_ERROR_COMPARTMENT_ID_VER = 0x00100407,
	// The target schema version does not support specifying compartment Id

	FW_RULE_STATUS_SEMANTIC_ERROR_CALLOUT_AND_AUDIT_VER = 0x00100408,
	// The target schema version does not support specifying callout and audit flag

	FW_RULE_STATUS_SEMANTIC_ERROR_APPCONTAINER_LOOPBACK_VER = 0x00100409,
	// The target schema version does not support specifying app container loopback flag

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_AUTH_SET_ID = 0x00100500,
	// The phase 1 auth set ID must be specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_CRYPTO_SET_ID = 0x00100510,
	// The quick mode crypto set ID must be specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_SET_ID = 0x00100511,
	// The main mode crypto set ID must be specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_KEY_MANAGER_DICTATE_VER = 0x00100512,
	// The target schema version does not support the Key Manager
	// Dictation flag.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_KEY_MANAGER_NOTIFY_VER = 0x00100513,
	// The target schema version does not support the Key Manager
	// Notification flag.

	FW_RULE_STATUS_SEMANTIC_ERROR_TRANSPORT_MACHINE_AUTHZ_VER = 0x00100514,
	// The target schema version does not support transport rule
	// machine authorization lists.

	FW_RULE_STATUS_SEMANTIC_ERROR_TRANSPORT_USER_AUTHZ_VER = 0x00100515,
	// The target schema version does not support transport rule user
	// authorization lists.

	FW_RULE_STATUS_SEMANTIC_ERROR_TRANSPORT_MACHINE_AUTHZ_ON_TUNNEL = 0x00100516,
	// Transport machine authorization SDDL specified on tunnel-mode
	// rule.

	FW_RULE_STATUS_SEMANTIC_ERROR_TRANSPORT_USER_AUTHZ_ON_TUNNEL = 0x00100517,
	// Transport user authorization SDDL specified on tunnel-mode rule.

	FW_RULE_STATUS_SEMANTIC_ERROR_PER_RULE_AND_GLOBAL_AUTHZ = 0x00100518,
	// The Apply Global Authorization flag cannot be used when a
	// per-rule authorization list is also specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_FLAGS_SECURITY_REALM = 0x00100519,
	// The target schema version does not support security realm flag.

	FW_RULE_STATUS_SEMANTIC_ERROR_SET_ID = 0x00101000,
	// The Set ID was not specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_IPSEC_PHASE = 0x00101010,
	// The IPsec phase is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_EMPTY_SUITES = 0x00101020,
	// No suites specified in the set.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_AUTH_METHOD = 0x00101030,
	// One of the phase 1 auth methods is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_AUTH_METHOD = 0x00101031,
	// One of the phase 2 auth methods is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_METHOD_ANONYMOUS = 0x00101032,
	// Anonymous cannot be the only authentication method.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_METHOD_DUPLICATE = 0x00101033,
	// The same authentication method cannot be used more than once
	// within a set.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_METHOD_VER = 0x00101034,
	// The target schema version does not support one or more of the
	// authentication methods given.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_SUITE_FLAGS = 0x00101040,
	// Invalid auth suite flags specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_HEALTH_CERT = 0x00101041,
	// Machine certificates can only be used in phase 2 auth if they
	// are machine health certificates.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_SIGNCERT_VER = 0x00101042,
	// The target schema version does not support the requested
	// certificate signing algorithm.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_INTERMEDIATE_CA_VER = 0x00101043,
	// The target schema version does not support targeting
	// Intermediate CA's.

	FW_RULE_STATUS_SEMANTIC_ERROR_MACHINE_SHKEY = 0x00101050,
	// Machine Preshared Key was selected as an authentication type,
	// but no key string was specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_CA_NAME = 0x00101060,
	// The certificate authority name is required, and must be
	// formatted as an X.509 distinguished name.

	FW_RULE_STATUS_SEMANTIC_ERROR_MIXED_CERTS = 0x00101061,
	// Machine health certificates and regular certificates cannot both
	// be proposed within the same authentication set.

	FW_RULE_STATUS_SEMANTIC_ERROR_NON_CONTIGUOUS_CERTS = 0x00101062,
	// When specifying multiple certificate authentication proposals,
	// all the certificate proposals with the same signing method must
	// must be grouped together within the set.

	FW_RULE_STATUS_SEMANTIC_ERROR_MIXED_CA_TYPE_IN_BLOCK = 0x00101063,
	// This error value is not used.

	FW_RULE_STATUS_SEMANTIC_ERROR_MACHINE_USER_AUTH = 0x00101070,
	// Both machine and user auth cannot be proposed within the same
	// authentication set.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_CERT_CRITERIA_VER = 0x00101071,
	// The target schema version does not support certificate criteria.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_CERT_CRITERIA_VER_MISMATCH = 0x00101072,
	// Certificate criteria version does not match schema version.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_CERT_CRITERIA_RENEWAL_HASH = 0x00101073,
	// The certificate criteria are invalid.  A thumbprint hash must be
	// specified when FollowRenewal is used.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_CERT_CRITERIA_INVALID_HASH = 0x00101074,
	// The certificate criteria are invalid.  The thumbprint hash is
	// invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_CERT_CRITERIA_INVALID_EKU = 0x00101075,
	// The certificate criteria are invalid.  One or more of the EKU's
	// are invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_CERT_CRITERIA_INVALID_NAME_TYPE = 0x00101076,
	// The certificate criteria are invalid.  The name type is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_CERT_CRITERIA_INVALID_NAME = 0x00101077,
	// The certificate criteria are invalid.  The subject name is not
	// valid.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_CERT_CRITERIA_INVALID_CRITERIA_TYPE = 0x00101078,
	// The certificate criteria are invalid.  The criteria type flags
	// are invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_CERT_CRITERIA_MISSING_CRITERIA = 0x00101079,
	// The certificate criteria are invalid.  You need to specify at
	// least one set of validation criteria and one set of selection
	// criteria.

	FW_RULE_STATUS_SEMANTIC_ERROR_PROXY_SERVER = 0x00101080,
	// The Kerberos proxy name must be a fully qualified domain name
	// (FQDN). For example: kerbproxy.contoso.com

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_PROXY_SERVER_VER = 0x00101081,
	// The target schema version does not support kerberos proxy
	// servers.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_NON_DEFAULT_ID = 0x00105000,
	// The main mode crypto set ID should be the global main mode
	// crypto set ID.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_FLAGS = 0x00105001,
	// The phase 1 crypto set flags are invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_TIMEOUT_MINUTES = 0x00105002,
	// The main mode lifetime, in minutes, is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_TIMEOUT_SESSIONS = 0x00105003,
	// The main mode lifetime, in sessions, is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_KEY_EXCHANGE = 0x00105004,
	// One of the main mode key exchange algorithms is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_ENCRYPTION = 0x00105005,
	// One of the main mode encryption algorithms is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_HASH = 0x00105006,
	// One of the main mode hash algorithms is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_ENCRYPTION_VER = 0x00105007,
	// The target schema version does not support one of the main mode
	// encryption algorithms chosen.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_HASH_VER = 0x00105008,
	// The target schema version does not support one of the main mode
	// hash algorithms chosen.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE1_CRYPTO_KEY_EXCH_VER = 0x00105009,
	// The target schema version does not support one of the main mode
	// key exchange algorithms chosen.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_CRYPTO_PFS = 0x00105020,
	// One of the quick mode key exchange algorithms is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_CRYPTO_PROTOCOL = 0x00105021,
	// One of the quick mode encapsulation types is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_CRYPTO_ENCRYPTION = 0x00105022,
	// One of the quick mode encryption algorithms is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_CRYPTO_HASH = 0x00105023,
	// One of the quick mode hash algorithms is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_CRYPTO_TIMEOUT_MINUTES = 0x00105024,
	// The quick mode lifetime, in minutes, is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_CRYPTO_TIMEOUT_KBYTES = 0x00105025,
	// The quick mode lifetime, in kilobytes, is invalid.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_CRYPTO_ENCRYPTION_VER = 0x00105026,
	// The target schema version does not support one of the quick mode
	// encryption algorithms chosen.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_CRYPTO_HASH_VER = 0x00105027,
	// The target schema version does not support one of the quick mode
	// hash algorithms chosen.

	FW_RULE_STATUS_SEMANTIC_ERROR_PHASE2_CRYPTO_PFS_VER = 0x00105028,
	// The target schema version does not support one of the quick mode
	// key exchange algorithms chosen.

	FW_RULE_STATUS_SEMANTIC_ERROR_CRYPTO_ENCR_HASH = 0x00105040,
	// Either Encryption or Hash must be specified.

	FW_RULE_STATUS_SEMANTIC_ERROR_CRYPTO_ENCR_HASH_COMPAT = 0x00105041,
	// The encryption and hash algorithms specified are incompatible.

	FW_RULE_STATUS_SEMANTIC_ERROR_SCHEMA_VERSION = 0x00105050,
	// The target schema version specified is not supported.

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_OR_AND_CONDITIONS = 0x00106000,
	// Malformed query: Mismatch in the number of ORed terms and the
	// terms array

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_AND_CONDITIONS = 0x00106001,
	// Malformed query: Mismatch in the number of ANDed conditions and
	// conditions array

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_CONDITION_KEY = 0x00106002,
	// Malformed query: Invalid confition match key

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_CONDITION_MATCH_TYPE = 0x00106003,
	// Malformed query: Invalid condition match type

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_CONDITION_DATA_TYPE = 0x00106004,
	// Malformed query: Invalid condition data type

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_CONDITION_KEY_AND_DATA_TYPE = 0x00106005,
	// Malformed query: Invalid key and data type combination

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_KEYS_PROTOCOL_PORT = 0x00106006,
	// Malformed query: Protocol condition present without a protocol
	// condition

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_KEY_PROFILE = 0x00106007,
	// Malformed query: Profile Key unavailable for this object type
	// queried

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_KEY_STATUS = 0x00106008,
	// Malformed query: Status Key unavailable for this object type
	// queried

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_KEY_FILTERID = 0x00106009,
	// Malformed query: FilterID Key unavailable for this object type
	// queried

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_KEY_APP_PATH = 0x00106010,
	// Malformed query: Application Key unavailable for this object
	// type queried

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_KEY_PROTOCOL = 0x00106011,
	// Malformed query: Protocol Key unavailable for this object type
	// queried

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_KEY_LOCAL_PORT = 0x00106012,
	// Malformed query: Local Port Key unavailable for this object type
	// queried

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_KEY_REMOTE_PORT = 0x00106013,
	// Malformed query: Remote Port Key unavailable for this object
	// type queried

	FW_RULE_STATUS_SEMANTIC_ERROR_QUERY_KEY_SVC_NAME = 0x00106015,
	// Malformed query: Service Name Key unavailable for this object
	// type queried

	FW_RULE_STATUS_SEMANTIC_ERROR_REQUIRE_IN_CLEAR_OUT_ON_TRANSPORT = 0x00107000,
	// Authentication mode,"Require inbound and clear outbound" can
	// only be set when using IPsec tunneling.

	FW_RULE_STATUS_SEMANTIC_ERROR_BYPASS_TUNNEL_IF_SECURE_ON_TRANSPORT = 0x00107001,
	// Bypass Tunnel If Secure may not be set on Transport-Mode rules.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_NOENCAP_ON_TUNNEL = 0x00107002,
	// Authentication (No Encapsulation) may not be used on tunnel-mode
	// rules.

	FW_RULE_STATUS_SEMANTIC_ERROR_AUTH_NOENCAP_ON_PSK = 0x00107003,
	// Authentication (No Encapsulation) may not be used on rules that
	// contain preshared keys.

	FW_RULE_STATUS_SEMANTIC_ERROR_REMOTE_DYNAMIC_KEYWORD_ADDRESSES = 0x00107004,
	// The target schema version does not support remote dynamic keyword addresses.

	FW_RULE_STATUS_SEMANTIC_ERROR_PACKAGE_FAMILY_NAME_FIELD_NOT_FOUND = 0x00107005,
	// The target schema version does not support package family names.

	FW_RULE_STATUS_RUNTIME_ERROR = 0x00200000,
	// A runtime error occurred while trying to enforce the rule.

	FW_RULE_STATUS_RUNTIME_ERROR_PHASE1_AUTH_NOT_FOUND = 0x00200001,
	// The phase 1 authentication set was not found.

	FW_RULE_STATUS_RUNTIME_ERROR_PHASE2_AUTH_NOT_FOUND = 0x00200002,
	// The phase 2 authentication set was not found.

	FW_RULE_STATUS_RUNTIME_ERROR_PHASE2_CRYPTO_NOT_FOUND = 0x00200003,
	// The quick mode cryptographic set was not found.

	FW_RULE_STATUS_RUNTIME_ERROR_AUTH_MCHN_SHKEY_MISMATCH = 0x00200004,
	// A conflict was detected between the phase 1 and phase 2
	// authentication sets. When preshared keys are used in phase 1,
	// there cannot be a phase 2 authentication set.

	FW_RULE_STATUS_RUNTIME_ERROR_PHASE1_CRYPTO_NOT_FOUND = 0x00200005,
	// The main mode cryptographic set was not found.

	FW_RULE_STATUS_RUNTIME_ERROR_AUTH_NOENCAP_ON_TUNNEL = 0x00200006,
	// Authentication (No Encapsulation) cannot be specified on a
	// tunnel-mode rule.

	FW_RULE_STATUS_RUNTIME_ERROR_AUTH_NOENCAP_ON_PSK = 0x00200007,
	// Authentication (No Encapsulation) cannot be specified on a rule
	// that uses a preshared key.

	FW_RULE_STATUS_RUNTIME_ERROR_KEY_MODULE_AUTH_MISMATCH = 0x00200008,
	// The key module in the rule is incompatible with the
	// authentication methods specified in the associated
	// authentication sets.

	FW_RULE_STATUS_ERROR = FW_RULE_STATUS_PARSING_ERROR | FW_RULE_STATUS_SEMANTIC_ERROR | FW_RULE_STATUS_RUNTIME_ERROR,
	// An error occurred.

	FW_RULE_STATUS_ALL = 0xFFFF0000
	// Enumerate all rules, regardless of status.
};

//rule status bitflags
enum FW_RULE_STATUS_CLASS
{
	FW_RULE_STATUS_CLASS_OK = FW_RULE_STATUS_OK, // The rule was parsed successfully from the store
	FW_RULE_STATUS_CLASS_PARTIALLY_IGNORED = FW_RULE_STATUS_PARTIALLY_IGNORED, // The rule has fields that the service can successfully ignore
	FW_RULE_STATUS_CLASS_IGNORED = FW_RULE_STATUS_IGNORED, // The rule has a higher version that the service must ignore
	FW_RULE_STATUS_CLASS_PARSING_ERROR = FW_RULE_STATUS_PARSING_ERROR, // The rule failed to be parsed correctly
	FW_RULE_STATUS_CLASS_SEMANTIC_ERROR = FW_RULE_STATUS_SEMANTIC_ERROR,
	//There is a semantic error when considering the fields of the rule in conjunction
	FW_RULE_STATUS_CLASS_RUNTIME_ERROR = FW_RULE_STATUS_RUNTIME_ERROR,
	// There is a runtime error when the object is considered in conjuntion with other Policy Objects.

	FW_RULE_STATUS_CLASS_ERROR = FW_RULE_STATUS_ERROR, // An Error occurred

	FW_RULE_STATUS_CLASS_ALL = FW_RULE_STATUS_ALL // All the status. (Used to enum ALL the rules, regardless the status.)
};

enum FW_ENFORCEMENT_STATE
{
	FW_ENFORCEMENT_STATE_INVALID,
	FW_ENFORCEMENT_STATE_FULL,
	FW_ENFORCEMENT_STATE_WF_OFF_IN_PROFILE,
	FW_ENFORCEMENT_STATE_CATEGORY_OFF,
	FW_ENFORCEMENT_STATE_DISABLED_OBJECT,
	FW_ENFORCEMENT_STATE_INACTIVE_PROFILE,
	FW_ENFORCEMENT_STATE_LOCAL_ADDRESS_RESOLUTION_EMPTY,
	FW_ENFORCEMENT_STATE_REMOTE_ADDRESS_RESOLUTION_EMPTY,
	FW_ENFORCEMENT_STATE_LOCAL_PORT_RESOLUTION_EMPTY,
	FW_ENFORCEMENT_STATE_REMOTE_PORT_RESOLUTION_EMPTY,
	FW_ENFORCEMENT_STATE_INTERFACE_RESOLUTION_EMPTY,
	FW_ENFORCEMENT_STATE_APPLICATION_RESOLUTION_EMPTY,
	FW_ENFORCEMENT_STATE_REMOTE_MACHINE_EMPTY,
	FW_ENFORCEMENT_STATE_REMOTE_USER_EMPTY,
	FW_ENFORCEMENT_STATE_LOCAL_GLOBAL_OPEN_PORTS_DISALLOWED,
	FW_ENFORCEMENT_STATE_LOCAL_AUTHORIZED_APPLICATIONS_DISALLOWED,
	FW_ENFORCEMENT_STATE_LOCAL_FIREWALL_RULES_DISALLOWED,
	FW_ENFORCEMENT_STATE_LOCAL_CONSEC_RULES_DISALLOWED,
	FW_ENFORCEMENT_STATE_MISMATCHED_PLATFORM,
	FW_ENFORCEMENT_STATE_OPTIMIZED_OUT,
	FW_ENFORCEMENT_STATE_LOCAL_USER_EMPTY,
	FW_ENFORCEMENT_STATE_TRANSPORT_MACHINE_SD_EMPTY,
	FW_ENFORCEMENT_STATE_TRANSPORT_USER_SD_EMPTY,
	FW_ENFORCEMENT_STATE_TUPLE_RESOLUTION_EMPTY,
	FW_ENFORCEMENT_STATE_NETNAME_RESOLUTION_EMPTY,
	FW_ENFORCEMENT_STATE_DUPLICATE,
	FW_ENFORCEMENT_STATE_MAX
};

struct FW_OBJECT_METADATA
{
	UINT64 qwFilterContextID;

	DWORD dwNumEntries;
	FW_ENFORCEMENT_STATE* pEnforcementStates;
};

// Values for platform, major and minor versions correspond to values in the OSVERSIONINFOEX structure
struct FW_OS_PLATFORM
{
	BYTE bPlatform;
	BYTE bMajorVersion;
	BYTE bMinorVersion;
	BYTE Reserved;
};

struct FW_OS_PLATFORM_LIST
{
	DWORD dwNumEntries;
	FW_OS_PLATFORM* pPlatforms;
};

struct FW_NETWORK_NAMES
{
	DWORD dwNumEntries;
	LPWSTR* wszNames;
};

enum FW_RULE_ORIGIN_TYPE
{
	FW_RULE_ORIGIN_INVALID,
	FW_RULE_ORIGIN_LOCAL,
	FW_RULE_ORIGIN_GP,
	FW_RULE_ORIGIN_DYNAMIC,
	FW_RULE_ORIGIN_AUTOGEN,
	FW_RULE_ORIGIN_HARDCODED,
	FW_RULE_ORIGIN_MDM,
	FW_RULE_ORIGIN_MAX,
	// Hyper-V rule origins for host translated rules
	FW_RULE_ORIGIN_HOST_LOCAL,
	FW_RULE_ORIGIN_HOST_GP,
	FW_RULE_ORIGIN_HOST_DYNAMIC,
	FW_RULE_ORIGIN_HOST_MDM,
	FW_RULE_ORIGIN_HOST_MAX,
};

enum FW_ENUM_RULES_FLAGS
{
	FW_ENUM_RULES_FLAG_NONE = 0x0000,
	FW_ENUM_RULES_FLAG_RESOLVE_NAME = 0x0001, // Resolves rule name if in the format of '@file.dll,-<resID>'
	FW_ENUM_RULES_FLAG_RESOLVE_DESCRIPTION = 0x0002, // Resolves rule descriptions if in the format of '@file.dll,-<resID>'
	FW_ENUM_RULES_FLAG_RESOLVE_APPLICATION = 0x0004, // Resolves environment variables in the application string
	FW_ENUM_RULES_FLAG_RESOLVE_KEYWORD = 0x0008, // Resolves Keywords in addresses and ports to the actual addresses and ports (dynamic store only)
	FW_ENUM_RULES_FLAG_RESOLVE_GPO_NAME = 0x0010, // Resolves GPO name for the GP_RSOP rules
	FW_ENUM_RULES_FLAG_EFFECTIVE = 0x0020, // Enum Rules only if we attempted to push them to BFE (dynamic store only)
	FW_ENUM_RULES_FLAG_INCLUDE_METADATA = 0x0040, // Inlude Object MetaData in the Enumerated Object.
	FW_ENUM_RULES_FLAG_MAX = 0x0080
};

//ordered by priority - highest on top
enum FW_RULE_ACTION
{
	FW_RULE_ACTION_INVALID = 0,
	FW_RULE_ACTION_ALLOW_BYPASS,
	FW_RULE_ACTION_BLOCK,
	FW_RULE_ACTION_ALLOW,
	FW_RULE_ACTION_MAX
};

enum FW_RULE_FLAG
{
	FW_RULE_FLAGS_NONE = 0x0000,
	FW_RULE_FLAGS_ACTIVE = 0x0001,
	FW_RULE_FLAGS_AUTHENTICATE = 0x0002,
	FW_RULE_FLAGS_AUTHENTICATE_WITH_ENCRYPTION = 0x0004,
	FW_RULE_FLAGS_ROUTEABLE_ADDRS_TRAVERSE = 0x0008,
	FW_RULE_FLAGS_LOOSE_SOURCE_MAPPED = 0x00010,
	FW_RULE_FLAGS_MAX_V2_1 = 0x0020,
	// This is the new "NoEncapsulation" flag in Win7
	FW_RULE_FLAGS_AUTH_WITH_NO_ENCAPSULATION = 0x0020,
	FW_RULE_FLAGS_MAX_V2_9 = 0x0040,
	// these are the new flags added for SSP in Win 7.
	FW_RULE_FLAGS_AUTH_WITH_ENC_NEGOTIATE = 0x0040,
	FW_RULE_FLAGS_ROUTEABLE_ADDRS_TRAVERSE_DEFER_APP = 0x0080,
	FW_RULE_FLAGS_ROUTEABLE_ADDRS_TRAVERSE_DEFER_USER = 0x0100,
	FW_RULE_FLAGS_AUTHENTICATE_BYPASS_OUTBOUND = 0x0200,
	FW_RULE_FLAGS_MAX_V2_10 = 0x0400,
	// This is the new flag in Windws 8 to allow profile crossings for clusters
	FW_RULE_FLAGS_ALLOW_PROFILE_CROSSING = 0x0400,
	// This is the new flag in Windws 8 to allow LOM on flows.
	FW_RULE_FLAGS_LOCAL_ONLY_MAPPED = 0x0800,
	FW_RULE_FLAGS_MAX_V2_20 = 0x1000,
	FW_RULE_FLAGS_LUA_CONDITIONAL_ACE = 0x1000,
	FW_RULE_FLAGS_BIND_TO_INTERFACE = 0x2000,
	FW_RULE_FLAGS_MAX = 0x4000,
	FW_RULE_FLAGS_AUTOGENERATE_CONNECTION_SECURITY_RULE = 0x0020,
};

enum FW_RULE_FLAGS2
{
	FW_RULE_FLAGS2_NONE = 0x0000,
	FW_RULE_FLAGS2_SYSTEMOS_ONLY = 0x0001,
	FW_RULE_FLAGS2_GAMEOS_ONLY = 0x0002,
	FW_RULE_FLAGS2_DEVMODE = 0x0004,
	FW_RULE_FLAGS_MAX_V2_26 = 0x0008,
	FW_RULE_FLAGS2_NOT_USED_VALUE_8 = 0x0008,
	FW_RULE_FLAGS2_EMPTY_REMOTENAME = 0x0010,
	FW_RULE_FLAGS2_NOT_REMOTENAME = 0x0020,
	FW_RULE_FLAGS2_NOT_USED_VALUE_64 = 0x0040,
	FW_RULE_FLAGS2_CALLOUT_AND_AUDIT = 0x0080,
	FW_RULE_FLAGS2_APP_LOOPBACK = 0x0100,
	FW_RULE_FLAGS2_NOT_USED_VALUE_512 = 0x0200,
	FW_RULE_FLAGS2_NOT_USED_VALUE_1024 = 0x0400,
	FW_RULE_FLAGS2_NOT_USED_VALUE_2048 = 0x0800,
	FW_RULE_FLAGS2_INDIRECT_NAME_RESOLVED = 0x1000,
	FW_RULE_FLAGS2_INDIRECT_DESCRIPTION_RESOLVED = 0x2000,
	FW_RULE_FLAGS2_DELAY_ENFORCE = FW_RULE_FLAGS2_NOT_USED_VALUE_8,
	FW_RULE_FLAGS2_AVOID_NETID = FW_RULE_FLAGS2_NOT_USED_VALUE_64,
	FW_RULE_FLAGS2_LOOPBACK = FW_RULE_FLAGS2_NOT_USED_VALUE_512,
	FW_RULE_FLAGS2_EDP = FW_RULE_FLAGS2_NOT_USED_VALUE_1024,
	FW_RULE_FLAGS2_TENANT_RESTRICTIONS_HIGH_WEIGHT = FW_RULE_FLAGS2_NOT_USED_VALUE_2048,

	FW_RULE_FLAGS2_MAX = 0x2000
};

using FW_POLICY_STORE_HANDLE = HANDLE;
```
