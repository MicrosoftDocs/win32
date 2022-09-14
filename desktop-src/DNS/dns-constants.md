---
title: DNS Constants
description: The following constants are defined for DNS in host byte order.
ms.assetid: 95bc9193-7962-498a-9abd-c4718ac35f0f
ms.topic: article
ms.date: 05/31/2018
---

# DNS Constants

The following constants are defined for DNS in host byte order.

## DNS Record Types



| Constant           | Value            |
|--------------------|------------------|
| DNS\_TYPE\_A       | 0x0001           |
| DNS\_TYPE\_NS      | 0x0002           |
| DNS\_TYPE\_MD      | 0x0003           |
| DNS\_TYPE\_MF      | 0x0004           |
| DNS\_TYPE\_CNAME   | 0x0005           |
| DNS\_TYPE\_SOA     | 0x0006           |
| DNS\_TYPE\_MB      | 0x0007           |
| DNS\_TYPE\_MG      | 0x0008           |
| DNS\_TYPE\_MR      | 0x0009           |
| DNS\_TYPE\_NULL    | 0x000a           |
| DNS\_TYPE\_WKS     | 0x000b           |
| DNS\_TYPE\_PTR     | 0x000c           |
| DNS\_TYPE\_HINFO   | 0x000d           |
| DNS\_TYPE\_MINFO   | 0x000e           |
| DNS\_TYPE\_MX      | 0x000f           |
| DNS\_TYPE\_TEXT    | 0x0010           |
| DNS\_TYPE\_RP      | 0x0011           |
| DNS\_TYPE\_AFSDB   | 0x0012           |
| DNS\_TYPE\_X25     | 0x0013           |
| DNS\_TYPE\_ISDN    | 0x0014           |
| DNS\_TYPE\_RT      | 0x0015           |
| DNS\_TYPE\_NSAP    | 0x0016           |
| DNS\_TYPE\_NSAPPTR | 0x0017           |
| DNS\_TYPE\_SIG     | 0x0018           |
| DNS\_TYPE\_KEY     | 0x0019           |
| DNS\_TYPE\_PX      | 0x001a           |
| DNS\_TYPE\_GPOS    | 0x001b           |
| DNS\_TYPE\_AAAA    | 0x001c           |
| DNS\_TYPE\_LOC     | 0x001d           |
| DNS\_TYPE\_NXT     | 0x001e           |
| DNS\_TYPE\_EID     | 0x001f           |
| DNS\_TYPE\_NIMLOC  | 0x0020           |
| DNS\_TYPE\_SRV     | 0x0021           |
| DNS\_TYPE\_ATMA    | 0x0022           |
| DNS\_TYPE\_NAPTR   | 0x0023           |
| DNS\_TYPE\_KX      | 0x0024           |
| DNS\_TYPE\_CERT    | 0x0025           |
| DNS\_TYPE\_A6      | 0x0026           |
| DNS\_TYPE\_DNAME   | 0x0027           |
| DNS\_TYPE\_SINK    | 0x0028           |
| DNS\_TYPE\_OPT     | 0x0029           |
| DNS\_TYPE\_DS      | 0x002B           |
| DNS\_TYPE\_RRSIG   | 0x002E           |
| DNS\_TYPE\_NSEC    | 0x002F           |
| DNS\_TYPE\_DNSKEY  | 0x0030           |
| DNS\_TYPE\_DHCID   | 0x0031           |
| DNS\_TYPE\_UINFO   | 0x0064           |
| DNS\_TYPE\_UID     | 0x0065           |
| DNS\_TYPE\_GID     | 0x0066           |
| DNS\_TYPE\_UNSPEC  | 0x0067           |
| DNS\_TYPE\_ADDRS   | 0x00f8           |
| DNS\_TYPE\_TKEY    | 0x00f9           |
| DNS\_TYPE\_TSIG    | 0x00fa           |
| DNS\_TYPE\_IXFR    | 0x00fb           |
| DNS\_TYPE\_AXFR    | 0x00fc           |
| DNS\_TYPE\_MAILB   | 0x00fd           |
| DNS\_TYPE\_MAILA   | 0x00fe           |
| DNS\_TYPE\_ALL     | 0x00ff           |
| DNS\_TYPE\_ANY     | 0x00ff           |
| DNS\_TYPE\_WINS    | 0xff01           |
| DNS\_TYPE\_WINSR   | 0xff02           |
| DNS\_TYPE\_NBSTAT  | DNS\_TYPE\_WINSR |



 

## DNS Class Types



| Constant             | Value  |
|----------------------|--------|
| DNS\_CLASS\_INTERNET | 0x0001 |
| DNS\_CLASS\_CSNET    | 0x0002 |
| DNS\_CLASS\_CHAOS    | 0x0003 |
| DNS\_CLASS\_HESIOD   | 0x0004 |
| DNS\_CLASS\_NONE     | 0x00fe |
| DNS\_CLASS\_ALL      | 0x00ff |
| DNS\_CLASS\_ANY      | 0x00ff |



 

## DNS Query Types



| Constant                    | Value  |
|-----------------------------|--------|
| DNS\_OPCODE\_QUERY          | 0x0000 |
| DNS\_OPCODE\_IQUERY         | 0x0001 |
| DNS\_OPCODE\_SERVER\_STATUS | 0x0002 |
| DNS\_OPCODE\_UNKNOWN        | 0x0003 |
| DNS\_OPCODE\_NOTIFY         | 0x0004 |
| DNS\_OPCODE\_UPDATE         | 0x0005 |



 

## DNS Record Flags

The following flags refer to a resource record's (RR) section within a DNS message:



| Constant           | Value      | Meaning                         |
|--------------------|------------|---------------------------------|
| DNSREC\_QUESTION   | 0x00000000 | RR is in the question section   |
| DNSREC\_ANSWER     | 0x00000001 | RR is in the answer section     |
| DNSREC\_AUTHORITY  | 0x00000002 | RR is in the authority section  |
| DNSREC\_ADDITIONAL | 0x00000003 | RR is in the additional section |



 

The following flags refer to a RR's section within an update DNS message per [RFC 2136](https://www.ietf.org/rfc/rfc2136.txt):



| Constant       | Value      | Meaning                           |
|----------------|------------|-----------------------------------|
| DNSREC\_ZONE   | 0x00000000 | RR is in the zone section         |
| DNSREC\_PREREQ | 0x00000001 | RR is in the prerequisite section |
| DNSREC\_UPDATE | 0x00000002 | RR is in the update section       |



 

The following flags are mutually exclusive:



| Constant        | Value      | Meaning                                                    |
|-----------------|------------|------------------------------------------------------------|
| DNSREC\_DELETE  | 0x00000004 | Delete a RR. Used in conjunction with DNSREC\_UPDATE       |
| DNSREC\_NOEXIST | 0x00000004 | RR does not exist. Used in conjunction with DNSREC\_PREREQ |



 

## DNS Query Options



| Constant                                | Value      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DNS\_QUERY\_STANDARD                    | 0x00000000 | Standard query.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DNS\_QUERY\_ACCEPT\_TRUNCATED\_RESPONSE | 0x00000001 | Returns truncated results. Does not retry under TCP.                                                                                                                                                                                                                                                                                                                                                                                                   |
| DNS\_QUERY\_USE\_TCP\_ONLY              | 0x00000002 | Uses TCP only for the query.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DNS\_QUERY\_NO\_RECURSION               | 0x00000004 | Directs the DNS server to perform an iterative query (specifically directs the DNS server not to perform recursive resolution to resolve the query).                                                                                                                                                                                                                                                                                                   |
| DNS\_QUERY\_BYPASS\_CACHE               | 0x00000008 | Bypasses the [*resolver*](r-gly.md) cache on the lookup.                                                                                                                                                                                                                                                                                                                                                                            |
| DNS\_QUERY\_NO\_WIRE\_QUERY             | 0x00000010 | Directs DNS to perform a query on the local cache only.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported. For similar functionality, use **DNS\_QUERY\_CACHE\_ONLY**.<br/>                                                                                                                                                                                                                                      |
| DNS\_QUERY\_NO\_LOCAL\_NAME             | 0x00000020 | Directs DNS to ignore the local name.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported.<br/>                                                                                                                                                                                                                                                                                                                    |
| DNS\_QUERY\_NO\_HOSTS\_FILE             | 0x00000040 | Prevents the DNS query from consulting the HOSTS file.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported.<br/>                                                                                                                                                                                                                                                                                                   |
| DNS\_QUERY\_NO\_NETBT                   | 0x00000080 | Prevents the DNS query from using NetBT for resolution.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported.<br/>                                                                                                                                                                                                                                                                                                  |
| DNS\_QUERY\_WIRE\_ONLY                  | 0x00000100 | Directs DNS to perform a query using the network only, bypassing local information.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported.<br/>                                                                                                                                                                                                                                                                      |
| DNS\_QUERY\_RETURN\_MESSAGE             | 0x00000200 | Directs DNS to return the entire DNS response message.**Windows 2000 Server and Windows 2000 Professional:** This value is not supported.<br/>                                                                                                                                                                                                                                                                                                   |
| DNS\_QUERY\_MULTICAST\_ONLY             | 0x00000400 | Prevents the query from using DNS and uses only Local Link Multicast Name Resolution (LLMNR).**Windows Vista and Windows Server 2008 or later.:** This value is supported.<br/>                                                                                                                                                                                                                                                                  |
| DNS\_QUERY\_NO\_MULTICAST               | 0x00000800 |                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DNS\_QUERY\_TREAT\_AS\_FQDN             | 0x00001000 | Prevents the DNS response from attaching suffixes to the submitted name in a name resolution process.                                                                                                                                                                                                                                                                                                                                                  |
| DNS\_QUERY\_ADDRCONFIG                  | 0x00002000 | Windows 7 only: Do not send [**A**](/windows/win32/api/windns/ns-windns-dns_a_data) type queries if IPv4 addresses are not available on an interface and do not send [**AAAA**](/windows/win32/api/windns/ns-windns-dns_aaaa_data) type queries if IPv6 addresses are not available.                                                                                                                                                                                                                                   |
| DNS\_QUERY\_DUAL\_ADDR                  | 0x00004000 | Windows 7 only: Query both [**AAAA**](/windows/win32/api/windns/ns-windns-dns_aaaa_data) and [**A**](/windows/win32/api/windns/ns-windns-dns_a_data) type records and return results for each. Results for **A** type records are mapped into **AAAA** type.                                                                                                                                                                                                                                                           |
| DNS\_QUERY\_MULTICAST\_WAIT             | 0x00020000 | Waits for a full timeout to collect all the responses from the Local Link. If not set, the default behavior is to return with the first response.**Windows Vista and Windows Server 2008 or later.:** This value is supported.<br/>                                                                                                                                                                                                              |
| DNS\_QUERY\_MULTICAST\_VERIFY           | 0x00040000 | Directs a test using the local machine hostname to verify name uniqueness on the same Local Link. Collects all responses even if normal LLMNR Sender behavior is not enabled.**Windows Vista and Windows Server 2008 or later.:** This value is supported.<br/>                                                                                                                                                                                  |
| DNS\_QUERY\_DONT\_RESET\_TTL\_VALUES    | 0x00100000 | If set, and if the response contains multiple records, records are stored with the TTL corresponding to the minimum value TTL from among all records. When this option is set, "Do not change the TTL of individual records" in the returned record set is not modified.                                                                                                                                                                               |
| DNS\_QUERY\_DISABLE\_IDN\_ENCODING      | 0x00200000 | Disables International Domain Name (IDN) encoding support in the [**DnsQuery**](/windows/desktop/api/Windns/nf-windns-dnsquery_a), [**DnsQueryEx**](/windows/desktop/api/Windns/nf-windns-dnsqueryex), [**DnsModifyRecordsInSet**](/windows/desktop/api/Windns/nf-windns-dnsmodifyrecordsinset_a), and [**DnsReplaceRecordSet**](/windows/desktop/api/Windns/nf-windns-dnsreplacerecordseta) APIs. All punycode names are treated as ASCII and will be ASCII encoded on the wire. All non-ASCII names are encoded in UTF8 on the wire. **Windows 8 or later.:** This value is supported.<br/> |
| DNS\_QUERY\_APPEND\_MULTILABEL          | 0x00800000 |                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DNS\_QUERY\_RESERVED                    | 0xf0000000 | Reserved.                                                                                                                                                                                                                                                                                                                                                                                                                                              |



 

## DNS Update Options



| Constant                                 | Value      | Meaning                                                                                                                                                       |
|------------------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DNS\_UPDATE\_SECURITY\_USE\_DEFAULT      | 0x00000000 | Uses the default behavior, which is specified in the registry, for secure dynamic DNS updates.                                                                |
| DNS\_UPDATE\_SECURITY\_OFF               | 0x00000010 | Does not attempt secure dynamic updates.                                                                                                                      |
| DNS\_UPDATE\_SECURITY\_ON                | 0x00000020 | Attempts non-secure dynamic update; if refused, attempts secure dynamic update.                                                                               |
| DNS\_UPDATE\_SECURITY\_ONLY              | 0x00000100 | Attempts secure dynamic updates only.                                                                                                                         |
| DNS\_UPDATE\_CACHE\_SECURITY\_CONTEXT    | 0x00000200 | Caches the security context for use in future transactions.                                                                                                   |
| DNS\_UPDATE\_TEST\_USE\_LOCAL\_SYS\_ACCT | 0x00000400 | Uses credentials of the local computer account.                                                                                                               |
| DNS\_UPDATE\_FORCE\_SECURITY\_NEGO       | 0x00000800 | Does not use cached security context.                                                                                                                         |
| DNS\_UPDATE\_TRY\_ALL\_MASTER\_SERVERS   | 0x00001000 | Sends DNS updates to all multi-master DNS servers.                                                                                                            |
| DNS\_UPDATE\_SKIP\_NO\_UPDATE\_ADAPTERS  | 0x00002000 | Do not update adapters where dynamic DNS updates are disabled.**Windows 2000 Server with SP2 or later.:** This value is supported.<br/>                 |
| DNS\_UPDATE\_REMOTE\_SERVER              | 0x00004000 | Register CNAME records on a remote server in addition to the local DNS server.**Windows 2000 Server with SP2 or later.:** This value is supported.<br/> |
| DNS\_UPDATE\_RESERVED                    | 0xffff0000 | Reserved for future use.                                                                                                                                      |



 

## DNS Response Codes



| Error                | Meaning                                        |
|----------------------|------------------------------------------------|
| DNS\_RCODE\_NOERROR  | No error                                       |
| DNS\_RCODE\_FORMERR  | Format error                                   |
| DNS\_RCODE\_SERVFAIL | Server failure                                 |
| DNS\_RCODE\_NXDOMAIN | Name error                                     |
| DNS\_RCODE\_NOTIMPL  | Not implemented                                |
| DNS\_RCODE\_REFUSED  | Connection refused                             |
| DNS\_RCODE\_YXDOMAIN | Domain name should not exist                   |
| DNS\_RCODE\_YXRRSET  | Resource Record (RR) set should not exist      |
| DNS\_RCODE\_NXRRSET  | RR set does not exist                          |
| DNS\_RCODE\_NOTAUTH  | Not authoritative for zone                     |
| DNS\_RCODE\_NOTZONE  | Name not in zone                               |
| DNS\_RCODE\_BADVERS  | Bad Extension Mechanism for DNS (EDNS) version |
| DNS\_RCODE\_BADSIG   | Bad signature                                  |
| DNS\_RCODE\_BADKEY   | Bad key                                        |
| DNS\_RCODE\_BADTIME  | Bad timestamp                                  |



 

 

 





