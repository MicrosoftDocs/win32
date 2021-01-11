---
description: Mobile Broadband Profile Schema v3.
ms.assetid: f7a3598f-57dd-4178-896f-31b4d2f65e56
title: Mobile Broadband Profile Schema v3
ms.topic: reference
ms.date: 05/31/2018
---

# Mobile Broadband Profile Schema v3

The Windows 8Mobile Broadband Profile Schema v3 is available in the namespace `https://www.microsoft.com/networking/WWAN/profile/v3`.

-   [Mobile Broadband Profile Schema v3 Elements](mobile-broadband-profile-schema-v3-elements.md)

``` syntax
<xs:schema targetNamespace="https://www.microsoft.com/networking/WWAN/profile/v3" 
    xmlns="https://www.microsoft.com/networking/WWAN/profile/v3"  
    xmlns:xs="https://www.w3.org/2001/XMLSchema" 
    xmlns:WWAN_profile_v2="https://www.microsoft.com/networking/WWAN/profile/v2"  
    elementFormDefault="qualified"> 

    <xs:import namespace="https://www.microsoft.com/networking/WWAN/profile/v2" schemaLocation="WWAN_profile_v2.xsd"/> 

    <!-- Flag to indicate whether this is an additional PDP context profile, default is "false" --> 
    <xs:element name="IsAdditionalPdpContextProfile" type="xs:boolean"/> 
</xs:schema> 
```

 

 



