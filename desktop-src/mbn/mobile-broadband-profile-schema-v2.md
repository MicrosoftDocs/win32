---
description: Mobile Broadband Profile Schema v2.
ms.assetid: 0E140DCC-373C-44B3-8A91-F38AE7A5797C
title: Mobile Broadband Profile Schema v2
ms.topic: reference
ms.date: 05/31/2018
---

# Mobile Broadband Profile Schema v2

The Windows 8Mobile Broadband Profile Schema v2 is available in the namespace `https://www.microsoft.com/networking/WWAN/profile/v2`.

-   [Mobile Broadband Profile Schema v2 Elements](mobile-broadband-profile-schema-v2-elements.md)

``` syntax
<xs:schema targetNamespace="https://www.microsoft.com/networking/WWAN/profile/v2"
    xmlns="https://www.microsoft.com/networking/WWAN/profile/v2" 
    xmlns:xs="https://www.w3.org/2001/XMLSchema"
    xmlns:WWAN_profile_v1="https://www.microsoft.com/networking/WWAN/profile/v1" 
    elementFormDefault="qualified">

    <xs:import namespace="https://www.microsoft.com/networking/WWAN/profile/v1" schemaLocation="WWAN_profile_v1.xsd"/>

    <!-- Flag to indicate whether this is a purchase profile, default is "false" -->
    <xs:element name="IsPurchaseProfile" type="xs:boolean"/>

    <!-- Display Provider Name -->
    <xs:element name="DisplayProviderName" type="WWAN_profile_v1:providerNameType"/>

</xs:schema>
```

 

 



