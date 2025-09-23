---
description: Defines 802.1X configuration elements.
ms.assetid: 4755356e-cb4b-4eed-a494-ca0d17f5184f
title: OneX Schema
ms.topic: reference
ms.date: 05/14/2025
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# OneX Schema

The OneX Schema defines 802.1X configuration elements. All OneX schema elements apply to both wired and wireless profiles. For a list of defined elements, see [OneX Schema Elements](onexschema-elements.md).

The root element of an 802.1X profile is the [**OneX**](onexschema-onex-element.md) element. Each profile will have exactly one root element. The **OneX** element is in the `https://www.microsoft.com/networking/OneX/v1` namespace.

To view sample profiles for wireless networks that include 802.1X configuration elements, see the following profile samples:

* [WPA3-Enterprise with TEAP profile sample](wpa3-enterprise-with-teap-profile-sample.md)
* [WPA3-Enterprise 192-bit mode with EAP-TLS profile sample](wpa3-enterprise-192bit-with-tls-profile-sample.md)
* [WPA2-Enterprise with PEAP-MSCHAPv2 profile sample](wpa2-enterprise-with-peap-mschapv2-profile-sample.md)
* [WPA2-Enterprise with TLS profile sample](wpa2-enterprise-with-tls-profile-sample.md)
* [Bootstrap profile sample](bootstrap-profile-sample.md)
* [FIPS profile sample](fips-profile-sample.md)
* [Single Sign-On profile sample](single-sign-on-profile-sample.md)

To view sample profiles for wired networks that include 802.1X configuration elements, see the following profile samples:

* [Machine Certificate profile sample](machine-certificate-profile-sample.md)
* [PEAP profile sample](peap-profile-sample.md)
* [Smart Card Certificate profile sample](smart-card-certificate-profile-sample.md)

## Related topics

* [Wireless profile samples](wireless-profile-samples.md)
* [Wired Profile Samples](wired-profile-samples.md)
* [WLAN_profile schema](wlan-profileschema-schema.md)
* [LAN_profile schema](lan-profileschema-schema.md)
* [Wireless Access Deployment](/windows-server/networking/core-network-guide/cncg/wireless/e-wireless-access-deployment)
* [Extensible Authentication Protocol (EAP) for network access](/windows-server/networking/technologies/extensible-authentication-protocol/network-access)
* [Configure EAP profiles and settings in Windows](/windows-server/networking/technologies/extensible-authentication-protocol/configure-eap-profiles)
