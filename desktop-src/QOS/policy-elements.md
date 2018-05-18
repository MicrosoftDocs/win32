---
title: Policy Elements
description: Policy element values are standardized by the Internet Engineering Task Force (IETF), and the allocation of vendor-specific policy elements is governed by the Internet Assigned Numbers Authority (IANA).
ms.assetid: '72eeb985-85e2-48c6-b79f-73f48295740a'
keywords: ["Quality of Service QOS , described, policy elements"]
---

# Policy Elements

Policy element values are standardized by the Internet Engineering Task Force (IETF), and the allocation of vendor-specific policy elements is governed by the Internet Assigned Numbers Authority (IANA). The range of values for policy element (PE) types provides for globally standardized numbers. These numbers are reserved, vendor-specific numbers, which can be obtained, and private use numbers, which do not require registration.

The following table identifies PE type values and their associated usage restriction. Developers should adhere to the following guidelines when assigning numeric values to user-defined policy elements.



| PE type value  | Usage description                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------------|
| Zero to 49151  | Standardized policy elements.                                                                                        |
| 49152 to 53247 | Vendor-specific values assigned by the IANA, with one element value per vendor, on a first-come, first-served basis. |
| 53248 to 65535 | Reserved for private use, such as user-defined policy elements used by private developers.                           |



 

> \[!Important\]  
> Assignment of PE type values are undergoing changes, and RFCs 2751 and 2752 are being reissued to reflect those changes. Consult the IETF web site at [www.ietf.org](Http://go.microsoft.com/fwlink/p/?linkid=84023) for the reissued RFCs and corresponding numbers.

 

Other values may be assigned in future RFCs. Check with the IETF at [www.ietf.org](Http://go.microsoft.com/fwlink/p/?linkid=84023) for the most recent assignment of policy element values.

The following standardized policy elements are defined as shown in the following table.



| PE type value  | Usage                                          |
|----------------|------------------------------------------------|
| 1              | Preemption priority                            |
| 2 (AUTH\_USER) | Authentication scheme to identify users        |
| 3 (AUTH\_APP)  | Authentication scheme to identify applications |



 

For more information about policy elements and the RFCs standardizing their usage, see the following RFCs at [www.ietf.org](Http://go.microsoft.com/fwlink/p/?linkid=84023):

RFC 2751 - Signaled Preemption Priority Policy Element

RFC 2752 - Identity Representation for RSVP

RFC 2753 - A Framework for Policy-based Admission Control

RFC 2872 - Application and Sub Application Identity Policy Element for Use with RSVP

There are also numerous internet drafts under consideration associated with policy elements and their numerical representations. For the most recent information, consult the IETF web site at [www.ietf.org](Http://go.microsoft.com/fwlink/p/?linkid=84023).

 

 




