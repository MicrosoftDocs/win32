---
title: DNS constants
description: The following constants are defined for DNS in host byte order.
ms.assetid: 95bc9193-7962-498a-9abd-c4718ac35f0f
ms.topic: article
ms.date: 07/13/2023
---

# DNS constants

The following constants are defined for DNS in host byte order.

## DNS record types

| Constant | Value |
|-|-|
| DNS_TYPE_A | 0x0001 |
| DNS_TYPE_NS | 0x0002 |
| DNS_TYPE_MD | 0x0003 |
| DNS_TYPE_MF | 0x0004 |
| DNS_TYPE_CNAME | 0x0005 |
| DNS_TYPE_SOA | 0x0006 |
| DNS_TYPE_MB | 0x0007 |
| DNS_TYPE_MG | 0x0008 |
| DNS_TYPE_MR | 0x0009 |
| DNS_TYPE_NULL | 0x000a |
| DNS_TYPE_WKS | 0x000b |
| DNS_TYPE_PTR | 0x000c |
| DNS_TYPE_HINFO | 0x000d |
| DNS_TYPE_MINFO | 0x000e |
| DNS_TYPE_MX | 0x000f |
| DNS_TYPE_TEXT | 0x0010 |
| DNS_TYPE_RP | 0x0011 |
| DNS_TYPE_AFSDB | 0x0012 |
| DNS_TYPE_X25 | 0x0013 |
| DNS_TYPE_ISDN | 0x0014 |
| DNS_TYPE_RT | 0x0015 |
| DNS_TYPE_NSAP | 0x0016 |
| DNS_TYPE_NSAPPTR | 0x0017 |
| DNS_TYPE_SIG | 0x0018 |
| DNS_TYPE_KEY | 0x0019 |
| DNS_TYPE_PX | 0x001a |
| DNS_TYPE_GPOS | 0x001b |
| DNS_TYPE_AAAA | 0x001c |
| DNS_TYPE_LOC | 0x001d |
| DNS_TYPE_NXT | 0x001e |
| DNS_TYPE_EID | 0x001f |
| DNS_TYPE_NIMLOC | 0x0020 |
| DNS_TYPE_SRV | 0x0021 |
| DNS_TYPE_ATMA | 0x0022 |
| DNS_TYPE_NAPTR | 0x0023 |
| DNS_TYPE_KX | 0x0024 |
| DNS_TYPE_CERT | 0x0025 |
| DNS_TYPE_A6 | 0x0026 |
| DNS_TYPE_DNAME | 0x0027 |
| DNS_TYPE_SINK | 0x0028 |
| DNS_TYPE_OPT | 0x0029 |
| DNS_TYPE_DS | 0x002B |
| DNS_TYPE_RRSIG | 0x002E |
| DNS_TYPE_NSEC | 0x002F |
| DNS_TYPE_DNSKEY | 0x0030 |
| DNS_TYPE_DHCID | 0x0031 |
| DNS_TYPE_UINFO | 0x0064 |
| DNS_TYPE_UID | 0x0065 |
| DNS_TYPE_GID | 0x0066 |
| DNS_TYPE_UNSPEC | 0x0067 |
| DNS_TYPE_ADDRS | 0x00f8 |
| DNS_TYPE_TKEY | 0x00f9 |
| DNS_TYPE_TSIG | 0x00fa |
| DNS_TYPE_IXFR | 0x00fb |
| DNS_TYPE_AXFR | 0x00fc |
| DNS_TYPE_MAILB | 0x00fd |
| DNS_TYPE_MAILA | 0x00fe |
| DNS_TYPE_ALL | 0x00ff |
| DNS_TYPE_ANY | 0x00ff |
| DNS_TYPE_WINS | 0xff01 |
| DNS_TYPE_WINSR | 0xff02 |
| DNS_TYPE_NBSTAT | DNS_TYPE_WINSR |

## DNS class types

| Constant | Value |
|-|-|
| DNS_CLASS_INTERNET | 0x0001 |
| DNS_CLASS_CSNET | 0x0002 |
| DNS_CLASS_CHAOS | 0x0003 |
| DNS_CLASS_HESIOD | 0x0004 |
| DNS_CLASS_NONE | 0x00fe |
| DNS_CLASS_ALL | 0x00ff |
| DNS_CLASS_ANY | 0x00ff |

## DNS query types

| Constant | Value |
|-|-|
| DNS_OPCODE_QUERY | 0x0000 |
| DNS_OPCODE_IQUERY | 0x0001 |
| DNS_OPCODE_SERVER_STATUS | 0x0002 |
| DNS_OPCODE_UNKNOWN | 0x0003 |
| DNS_OPCODE_NOTIFY | 0x0004 |
| DNS_OPCODE_UPDATE | 0x0005 |

## DNS record flags

The following flags refer to a resource record's (RR) section within a DNS message:

| Constant | Value | Meaning |
|-|-|-|
| DNSREC_QUESTION | 0x00000000 | RR is in the question section |
| DNSREC_ANSWER | 0x00000001 | RR is in the answer section |
| DNSREC_AUTHORITY | 0x00000002 | RR is in the authority section |
| DNSREC_ADDITIONAL | 0x00000003 | RR is in the additional section |

The following flags refer to an RR's section within an update DNS message per [RFC 2136](https://www.ietf.org/rfc/rfc2136.txt):

| Constant | Value | Meaning |
|-|-|-|
| DNSREC_ZONE | 0x00000000 | RR is in the zone section |
| DNSREC_PREREQ | 0x00000001 | RR is in the prerequisite section |
| DNSREC_UPDATE | 0x00000002 | RR is in the update section |

The following flags are mutually exclusive:

| Constant | Value | Meaning |
|-|-|-|
| DNSREC_DELETE | 0x00000004 | Delete a RR. Used in conjunction with DNSREC_UPDATE |
| DNSREC_NOEXIST | 0x00000004 | RR does not exist. Used in conjunction with DNSREC_PREREQ |

## DNS query options

| Constant | Value | Meaning |
|-|-|-|
| DNS_QUERY_STANDARD | 0x00000000 | Standard query. |
| DNS_QUERY_ACCEPT_TRUNCATED_RESPONSE | 0x00000001 | Returns truncated results. Does not retry under TCP. |
| DNS_QUERY_USE_TCP_ONLY | 0x00000002 | Uses TCP only for the query. |
| DNS_QUERY_NO_RECURSION | 0x00000004 | Directs the DNS server to perform an iterative query (specifically directs the DNS server not to perform recursive resolution to resolve the query). |
| DNS_QUERY_BYPASS_CACHE | 0x00000008 | Bypasses the [*resolver*](r-gly.md) cache on the lookup. |
| DNS_QUERY_NO_WIRE_QUERY | 0x00000010 | Directs DNS to perform a query on the local cache only.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported. For similar functionality, use **DNS_QUERY_CACHE_ONLY**. |
| DNS_QUERY_NO_LOCAL_NAME | 0x00000020 | Directs DNS to ignore the local name.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported. |
| DNS_QUERY_NO_HOSTS_FILE | 0x00000040 | Prevents the DNS query from consulting the HOSTS file.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported. |
| DNS_QUERY_NO_NETBT | 0x00000080 | Prevents the DNS query from using NetBT for resolution.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported. |
| DNS_QUERY_WIRE_ONLY | 0x00000100 | Directs DNS to perform a query using the network only, bypassing local information.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported. |
| DNS_QUERY_RETURN_MESSAGE | 0x00000200 | Directs DNS to return the entire DNS response message.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported. |
| DNS_QUERY_MULTICAST_ONLY | 0x00000400 | Prevents the query from using DNS and uses only Local Link Multicast Name Resolution (LLMNR).**Windows Vista and Windows Server 2008 or later.:** This value is supported. |
| DNS_QUERY_NO_MULTICAST | 0x00000800 | |
| DNS_QUERY_TREAT_AS_FQDN | 0x00001000 | Prevents the DNS response from attaching suffixes to the submitted name in a name resolution process. |
| DNS_QUERY_ADDRCONFIG | 0x00002000 | Windows 7 only: Do not send [**A**](/windows/win32/api/windns/ns-windns-dns_a_data) type queries if IPv4 addresses are not available on an interface and do not send [**AAAA**](/windows/win32/api/windns/ns-windns-dns_aaaa_data) type queries if IPv6 addresses are not available. |
| DNS_QUERY_DUAL_ADDR | 0x00004000 | Windows 7 only: Query both [**AAAA**](/windows/win32/api/windns/ns-windns-dns_aaaa_data) and [**A**](/windows/win32/api/windns/ns-windns-dns_a_data) type records and return results for each. Results for **A** type records are mapped into **AAAA** type. |
| DNS_QUERY_MULTICAST_WAIT | 0x00020000 | Waits for a full timeout to collect all the responses from the Local Link. If not set, the default behavior is to return with the first response.**Windows Vista and Windows Server 2008 or later.:** This value is supported. |
| DNS_QUERY_MULTICAST_VERIFY | 0x00040000 | Directs a test using the local machine hostname to verify name uniqueness on the same Local Link. Collects all responses even if normal LLMNR Sender behavior is not enabled.**Windows Vista and Windows Server 2008 or later.:** This value is supported. |
| DNS_QUERY_DONT_RESET_TTL_VALUES | 0x00100000 | If set, and if the response contains multiple records, records are stored with the TTL corresponding to the minimum value TTL from among all records. When this option is set, "Do not change the TTL of individual records" in the returned record set is not modified. |
| DNS_QUERY_DISABLE_IDN_ENCODING | 0x00200000 | Disables International Domain Name (IDN) encoding support in the [**DnsQuery**](/windows/desktop/api/Windns/nf-windns-dnsquery_a), [**DnsQueryEx**](/windows/desktop/api/Windns/nf-windns-dnsqueryex), [**DnsModifyRecordsInSet**](/windows/desktop/api/Windns/nf-windns-dnsmodifyrecordsinset_a), and [**DnsReplaceRecordSet**](/windows/desktop/api/Windns/nf-windns-dnsreplacerecordseta) APIs. All punycode names are treated as ASCII and will be ASCII encoded on the wire. All non-ASCII names are encoded in UTF8 on the wire. **Windows 8 or later.:** This value is supported. |
| DNS_QUERY_APPEND_MULTILABEL | 0x00800000 | |
| DNS_QUERY_RESERVED | 0xf0000000 | Reserved. |

## DNS update options

| Constant | Value | Meaning |
|-|-|-|
| DNS_UPDATE_SECURITY_USE_DEFAULT | 0x00000000 | Uses the default behavior, which is specified in the registry, for secure dynamic DNS updates. |
| DNS_UPDATE_SECURITY_OFF | 0x00000010 | Does not attempt secure dynamic updates. |
| DNS_UPDATE_SECURITY_ON | 0x00000020 | Attempts non-secure dynamic update; if refused, attempts secure dynamic update. |
| DNS_UPDATE_SECURITY_ONLY | 0x00000100 | Attempts secure dynamic updates only. |
| DNS_UPDATE_CACHE_SECURITY_CONTEXT | 0x00000200 | Caches the security context for use in future transactions. |
| DNS_UPDATE_TEST_USE_LOCAL_SYS_ACCT | 0x00000400 | Uses credentials of the local computer account. |
| DNS_UPDATE_FORCE_SECURITY_NEGO | 0x00000800 | Does not use cached security context. |
| DNS_UPDATE_TRY_ALL_MASTER_SERVERS | 0x00001000 | Sends DNS updates to all multi-master DNS servers. |
| DNS_UPDATE_SKIP_NO_UPDATE_ADAPTERS | 0x00002000 | Do not update adapters where dynamic DNS updates are disabled.**Windows 2000 Server with SP2 or later.:** This value is supported. |
| DNS_UPDATE_REMOTE_SERVER | 0x00004000 | Register CNAME records on a remote server in addition to the local DNS server.**Windows 2000 Server with SP2 or later.:** This value is supported. |
| DNS_UPDATE_RESERVED | 0xffff0000 | Reserved for future use. |

## DNS response codes

| Error | Meaning |
|-|-|
| DNS_RCODE_NOERROR | No error |
| DNS_RCODE_FORMERR | Format error |
| DNS_RCODE_SERVFAIL | Server failure |
| DNS_RCODE_NXDOMAIN | Name error |
| DNS_RCODE_NOTIMPL | Not implemented |
| DNS_RCODE_REFUSED | Connection refused |
| DNS_RCODE_YXDOMAIN | Domain name should not exist |
| DNS_RCODE_YXRRSET | Resource Record (RR) set should not exist |
| DNS_RCODE_NXRRSET | RR set does not exist |
| DNS_RCODE_NOTAUTH | Not authoritative for zone |
| DNS_RCODE_NOTZONE | Name not in zone |
| DNS_RCODE_BADVERS | Bad Extension Mechanism for DNS (EDNS) version |
| DNS_RCODE_BADSIG | Bad signature |
| DNS_RCODE_BADKEY | Bad key |
| DNS_RCODE_BADTIME | Bad timestamp |

## DNS protocols

| Constant | Value | Meaning |
|-|-|-|
| DNS_PROTOCOL_UNSPECIFIED | 0 |  |
| DNS_PROTOCOL_UDP | 1 |  |
| DNS_PROTOCOL_TCP | 2 |  |
| DNS_PROTOCOL_DOH | 3 |  |
| DNS_PROTOCOL_DOT | 4 |  |
| DNS_PROTOCOL_NO_WIRE | 5 |  |

## Other constants

| Constant | Value | Meaning |
|-|-|-|
| DNS_QUERY_RAW_RESULTS_VERSION1 | 0x1 |  |
| DNS_QUERY_RAW_REQUEST_VERSION1 | 0x1 |  |
| DNS_QUERY_RAW_OPTION_BEST_EFFORT_PARSE | 0x1 |  |
