---
title: WLAN_profile schema elements
description: The WLAN\_profile schema defines the following elements.
ms.assetid: 9eb0f446-1202-4770-b09e-250e83524119
ms.topic: article
ms.date: 04/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# WLAN_profile schema elements

The WLAN\_profile schema defines the following elements. Most elements are in the namespace `https://www.microsoft.com/networking/WLAN/profile/v1`, with some exceptions. For example, [**FIPSMode (authEncryption)**](wlan-profileschema-fipsmode-authencryption-element.md) is in the namespace `https://www.microsoft.com/networking/WLAN/profile/v2`.

The following list shows the defined elements in the order in which the elements appear in a profile. The ordering of elements is enforced. Not all elements are in every profile, as some elements are optional.

This list doesn't show all possible elements that can appear in a wireless profile, as elements can be added in **xs:any** insertion points.

-   [**WLANProfile**](wlan-profileschema-wlanprofile-element.md)
    -   [**name (WLANProfile)**](wlan-profileschema-name-wlanprofile-element.md)
    -   [**SSIDConfig (WLANProfile)**](wlan-profileschema-ssidconfig-wlanprofile-element.md)
        -   [**SSID (SSIDConfig)**](wlan-profileschema-ssid-ssidconfig-element.md)
            -   [**hex (SSID)**](wlan-profileschema-hex-ssid-element.md)
            -   [**name (SSID)**](wlan-profileschema-name-ssid-element.md)
        -   [**SSIDPrefix (SSIDConfig)**](wlan-profileschema-ssidprefix-ssidconfig-element.md)
            -   [**hex (SSIDPrefix)**](wlan-profileschema-hex-ssidprefix-element.md)
            -   [**name (SSIDPrefix)**](wlan-profileschema-name-ssidprefix-element.md)
        -   [**nonBroadcast (SSIDConfig)**](wlan-profileschema-nonbroadcast-ssidconfig-element.md)
    -   [**Hotspot2 (WLANProfile)**](wlan-profileschema-hotspot2-element.md)
        -   [**DomainName (Hotspot2)**](wlan-profileschema-hotspot2-domainname-element.md)
        -   [**NAIRealm (Hotspot2)**](wlan-profileschema-hotspot2-nairealm-element.md)
        -   [**Network3GPP (Hotspot2)**](wlan-profileschema-hotspot2-network3gpp-element.md)
        -   [**RoamingConsortium (Hotspot2)**](wlan-profileschema-hotspot2-roamingconsortium-element.md)
    -   [**connectionType (WLANProfile)**](wlan-profileschema-connectiontype-wlanprofile-element.md)
    -   [**connectionMode (WLANProfile)**](wlan-profileschema-connectionmode-wlanprofile-element.md)
    -   [**autoSwitch (WLANProfile)**](wlan-profileschema-autoswitch-wlanprofile-element.md)
    -   [**MSM (WLANProfile)**](wlan-profileschema-msm-wlanprofile-element.md)
        -   [**connectivity (MSM)**](wlan-profileschema-connectivity-msm-element.md)
            -   [**phyType (connectivity)**](wlan-profileschema-phytype-connectivity-element.md)
            -   [**QoSDSCPToUPMappingAllowed (connectivity)**](wlan-profileschema-qosdscptoupmappingallowed-connectivity-element.md)
        -   [**security (MSM)**](wlan-profileschema-security-msm-element.md)
            -   [**authEncryption (security)**](wlan-profileschema-authencryption-security-element.md)
                -   [**authentication (authEncryption)**](wlan-profileschema-authentication-authencryption-element.md)
                -   [**encryption (authEncryption)**](wlan-profileschema-encryption-authencryption-element.md)
                -   [**useOneX (authEncryption)**](wlan-profileschema-useonex-authencryption-element.md)
                -   [**FIPSMode (authEncryption)**](wlan-profileschema-fipsmode-authencryption-element.md)
                -   [**transitionMode (authEncryption)**](wlan-profileschema-transitionmode-authencryption-element.md)
            -   [**sharedKey (security)**](wlan-profileschema-sharedkey-security-element.md)
                -   [**keyType (sharedKey)**](wlan-profileschema-keytype-sharedkey-element.md)
                -   [**protected (sharedKey)**](wlan-profileschema-protected-sharedkey-element.md)
                -   [**keyMaterial (sharedKey)**](wlan-profileschema-keymaterial-sharedkey-element.md)
            -   [**keyIndex (security)**](wlan-profileschema-keyindex-security-element.md)
            -   [**PMKCacheMode (security)**](wlan-profileschema-pmkcachemode-security-element.md)
            -   [**PMKCacheTTL (security)**](wlan-profileschema-pmkcachettl-security-element.md)
            -   [**PMKCacheSize (security)**](wlan-profileschema-pmkcachesize-security-element.md)
            -   [**preAuthMode (security)**](wlan-profileschema-preauthmode-security-element.md)
            -   [**preAuthThrottle (security)**](wlan-profileschema-preauththrottle-security-element.md)
    -   [**IHV (WLANProfile)**](wlan-profileschema-ihv-wlanprofile-element.md)
        -   [**OUIHeader (IHV)**](wlan-profileschema-ouiheader-ihv-element.md)
            -   [**OUI (OUIHeader)**](wlan-profileschema-oui-ouiheader-element.md)
            -   [**type (OUIHeader)**](wlan-profileschema-type-ouiheader-element.md)
        -   [**connectivity (IHV)**](wlan-profileschema-connectivity-ihv-element.md)
        -   [**security (IHV)**](wlan-profileschema-security-ihv-element.md)
        -   [**useMSOneX (IHV)**](wlan-profileschema-usemsonex-ihv-element.md)
    -   [**MacRandomization (WLANProfile)**](wlan-profileschema-macrandomization-wlanprofile-element.md)
        -   [**enableRandomization (MacRandomization)**](wlan-profileschema-enablerandomization-macrandomization-element.md)
        -   [**randomizeEveryday (MacRandomization)**](wlan-profileschema-randomizeeveryday-macrandomization-element.md)
        -   [**randomizationSeed (MacRandomization)**](wlan-profileschema-randomizationseed-macrandomization-element.md)
