---
title: Managing DNS Resource Records
description:  Learn about managing resource records. A resource record is the unit of information entry in DNS zone files, which used to resolve all DNS queries.
ms.assetid: 'ddad5f14-5a2d-4966-87b7-b354666f9e24'
ms.topic: article
ms.date: 05/31/2018
---

# Managing DNS Resource Records

A resource record, commonly referred to as an RR, is the unit of information entry in DNS zone files; RRs are the basic building blocks of host-name and IP information and are used to resolve all DNS queries. Resource records come in a fairly wide variety of types in order to provide extended name-resolution services.

Different types of RRs have different formats, as they contain different data. Many RRs share a common format. Each DNS Server contains RRs for the portion of the name space for which it is authoritative.

The DNS WMI Provider currently supports the following RR types. Click the name of the resource record to jump to its reference page.



| Resource Record (in provider)                             | Description                                                  |
|-----------------------------------------------------------|--------------------------------------------------------------|
| [**MicrosoftDNS\_AType**](microsoftdns-atype.md)         | Name to address mapping record                               |
| [**MicrosoftDNS\_AAAAType**](microsoftdns-aaaatype.md)   | Host to Ipv6 address record                                  |
| [**MicrosoftDNS\_AFSDBType**](microsoftdns-afsdbtype.md) | Andrew File System Database Server record                    |
| [**MicrosoftDNS\_ATMAType**](microsoftdns-atmatype.md)   | ATM address-to-name record                                   |
| [**MicrosoftDNS\_CNAMEType**](microsoftdns-cnametype.md) | [*Canonical Name*](c-gly.md) record |
| [**MicrosoftDNS\_HINFOType**](microsoftdns-hinfotype.md) | Host Information record                                      |
| [**MicrosoftDNS\_ISDNType**](microsoftdns-isdntype.md)   | Integrated services digital network record                   |
| [**MicrosoftDNS\_KEYType**](microsoftdns-keytype.md)     | KEY record. See RFC 2535                                     |
| [**MicrosoftDNS\_MBType**](microsoftdns-mbtype.md)       | Mailbox record                                               |
| [**MicrosoftDNS\_MDType**](microsoftdns-mdtype.md)       | Mail agent for the domain record                             |
| [**MicrosoftDNS\_MFType**](microsoftdns-mftype.md)       | Mail forwarding agent for the domain record                  |
| [**MicrosoftDNS\_MGType**](microsoftdns-mgtype.md)       | Mail group record                                            |
| [**MicrosoftDNS\_MINFOType**](microsoftdns-minfotype.md) | Mail information record                                      |
| [**MicrosoftDNS\_MRType**](microsoftdns-mrtype.md)       | Mailbox rename record                                        |
| [**MicrosoftDNS\_MXType**](microsoftdns-mxtype.md)       | Mail exchanger record                                        |
| [**MicrosoftDNS\_NSType**](microsoftdns-nstype.md)       | Name server record                                           |
| [**MicrosoftDNS\_NXTType**](microsoftdns-nxttype.md)     | Next record                                                  |
| [**MicrosoftDNS\_PTRType**](microsoftdns-ptrtype.md)     | Address to name mapping record                               |
| [**MicrosoftDNS\_RPType**](microsoftdns-rptype.md)       | Responsible person record                                    |
| [**MicrosoftDNS\_RTType**](microsoftdns-rttype.md)       | Route through record                                         |
| [**MicrosoftDNS\_SIGType**](microsoftdns-sigtype.md)     | Signature record                                             |
| [**MicrosoftDNS\_SOAType**](microsoftdns-soatype.md)     | Start of authority                                           |
| [**MicrosoftDNS\_SRVType**](microsoftdns-srvtype.md)     | Service record                                               |
| [**MicrosoftDNS\_TXTType**](microsoftdns-txttype.md)     | Text record                                                  |
| [**MicrosoftDNS\_WINSType**](microsoftdns-winstype.md)   | WINS server record                                           |
| [**MicrosoftDNS\_WINSRType**](microsoftdns-winsrtype.md) | WINS reverse-lookup record                                   |
| [**MicrosoftDNS\_WKSType**](microsoftdns-wkstype.md)     | Well-known services record                                   |
| [**MicrosoftDNS\_X25Type**](microsoftdns-x25type.md)     | X.121 Address-to-name mapping record                         |



 

## Administration Steps

The DNS WMI Provider enables the administration of RRs from the server itself, or from remote hosts. The general steps necessary to administer RRs using the DNS WMI Provider are:

-   Connecting to the DNS WMI Provider
-   Getting a resource record instance
-   Listing or modifying a resource record property or using a method

The following tasks are linked to their associated scripting samples.

-   [Listing Resource Types](dns-wmi-provider-samples-managing-dns-resource-records.md)
-   [Adding a Resource Record](dns-wmi-provider-samples-managing-dns-resource-records.md)
-   [Deleting a Resource Record](dns-wmi-provider-samples-managing-dns-resource-records.md)
-   [Modifying a Resource Record](dns-wmi-provider-samples-managing-dns-resource-records.md)

 

 




