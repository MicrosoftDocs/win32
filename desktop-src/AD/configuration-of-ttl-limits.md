---
title: Configuration of TTL Limits
description: A client can request a TTL value for an entry ranging between 1 and 31557600 (that is, from 1 second to 1 year).
ms.assetid: 4009702c-7992-4e20-9d37-384f8137ba8f
ms.tgt_platform: multiple
keywords:
- Configuration of TTL Limits AD
ms.topic: article
ms.date: 05/31/2018
---

# Configuration of TTL Limits

A client can request a TTL value for an entry ranging between 1 and 31557600 (that is, from 1 second to 1 year). This attribute value range will be enforced by the **rangeLower** and **rangeUpper** attribute values in the **attributeSchema** definition for the **entryTTL** attribute. As per RFC 2589, directory servers are not required to accept this value and might return a different TTL value to the client. Clients must be able to use this server-dictated value as their client refresh period (CRP) which will govern how often the client will need to perform the refresh operation on the dynamic entry.

Active Directory Domain Services provide administrators with the ability to configure the default and minimum TTL values for a forest. The default TTL value is what will be assigned to a newly created dynamic entry if a TTL is not explicitly specified. The minimum TTL will override any client specified TTL value that is lower than the configured minimum. No configurable maximum TTL value needs to be provided because a maximum will be imposed by the **rangeUpper** attribute value in the **attributeSchema** object. Allowing administrators to configure these values will enable them to set TTL values which will enforce a low refresh traffic or, at the other extreme, provide a highly up-to-date directory.

The default values for the two configurable TTL parameters will be as follows:

-   Default TTL value = 86400 seconds (1 day)
-   Minimum TTL value = 900 seconds (15 minutes)

The configurable TTL parameters will be stored as AVA (attribute value assertion) entries of the form "&lt;value-name&gt;=&lt;value&gt;" in the attribute **ms-DS-Other-Settings** of the NTDS-Service object given by the following DN in the Configuration partition:


```C++
CN=Directory Service,CN=Windows NT,CN=Services,CN=Configuration,DC=...
```



The exact AVA syntax, for the two configurable TTL parameters, is as follows where NNNN is expressed in seconds:


```C++
DynamicObjectDefaultTTLSeconds=NNNN
```




```C++
DynamicObjectMinTTLSeconds=NNNN
```



These values can be set by an administrator through the command-line utility ntdsutil.

 

 




