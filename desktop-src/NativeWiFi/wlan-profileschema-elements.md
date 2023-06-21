---
title: WLAN_profile schema elements
description: The WLAN\_profile schema defines the following elements.
ms.topic: reference
ms.date: 05/25/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.assetid: 9eb0f446-1202-4770-b09e-250e83524119
---

# WLAN_profile schema elements

The WLAN\_profile schema defines the following elements. Most elements are in the namespace `https://www.microsoft.com/networking/WLAN/profile/v1`, with some exceptions. For example, [**FIPSMode (authEncryption)**](wlan-profileschema-authencryption-security-element.md#fipsmode) is in the namespace `https://www.microsoft.com/networking/WLAN/profile/v2`.

The following list shows the defined elements in the order in which the elements appear in a profile. The ordering of elements is enforced. Not all elements are in every profile, as some elements are optional.

This list doesn't show all possible elements that can appear in a wireless profile, since elements can be added in **xs:any** insertion points.

> [!NOTE]
> The **OneX** configuration parameters must be present immediately under `security` (MSM) if the `useOneX` (authEncryption) flag is set to "true".

## Elements

* [**WLANProfile**](wlan-profileschema-wlanprofile-element.md)
  * [**name (WLANProfile)**](wlan-profileschema-wlanprofile-element.md#name)
  * [**SSIDConfig (WLANProfile)**](wlan-profileschema-ssidconfig-wlanprofile-element.md)
    * [**SSID (SSIDConfig)**](wlan-profileschema-ssid-ssidconfig-element.md)
      * [**hex (SSID)**](wlan-profileschema-ssid-ssidconfig-element.md#hex)
      * [**name (SSID)**](wlan-profileschema-ssid-ssidconfig-element.md#name)
    * [**SSIDPrefix (SSIDConfig)**](wlan-profileschema-ssidprefix-ssidconfig-element.md)
      * [**hex (SSIDPrefix)**](wlan-profileschema-ssidprefix-ssidconfig-element.md#hex)
      * [**name (SSIDPrefix)**](wlan-profileschema-ssidprefix-ssidconfig-element.md#name)
    * [**nonBroadcast (SSIDConfig)**](wlan-profileschema-ssidconfig-wlanprofile-element.md#nonbroadcast)
  * [**Hotspot2 (WLANProfile)**](wlan-profileschema-hotspot2-element.md)
    * [**DomainName (Hotspot2)**](wlan-profileschema-hotspot2-element.md#domainname)
    * [**NAIRealm (Hotspot2)**](wlan-profileschema-hotspot2-nairealm-element.md)
    * [**Network3GPP (Hotspot2)**](wlan-profileschema-hotspot2-network3gpp-element.md)
    * [**RoamingConsortium (Hotspot2)**](wlan-profileschema-hotspot2-roamingconsortium-element.md)
  * [**connectionType (WLANProfile)**](wlan-profileschema-wlanprofile-element.md#connectiontype)
  * [**connectionMode (WLANProfile)**](wlan-profileschema-wlanprofile-element.md#connectionmode)
  * [**autoSwitch (WLANProfile)**](wlan-profileschema-wlanprofile-element.md#autoswitch)
  * [**MSM (WLANProfile)**](wlan-profileschema-msm-wlanprofile-element.md)
    * [**connectivity (MSM)**](wlan-profileschema-connectivity-msm-element.md)
      * [**phyType (connectivity)**](wlan-profileschema-connectivity-msm-element.md#phytype)
      * [**QoSDSCPToUPMappingAllowed (connectivity)**](wlan-profileschema-connectivity-msm-element.md#qosdscptoupmappingallowed)
    * [**security (MSM)**](wlan-profileschema-security-msm-element.md)
      * [**authEncryption (security)**](wlan-profileschema-authencryption-security-element.md)
        * [**authentication (authEncryption)**](wlan-profileschema-authencryption-security-element.md#authentication)
        * [**encryption (authEncryption)**](wlan-profileschema-authencryption-security-element.md#encryption)
        * [**useOneX (authEncryption)**](wlan-profileschema-authencryption-security-element.md#useonex)
        * [**FIPSMode (authEncryption)**](wlan-profileschema-authencryption-security-element.md#fipsmode)
        * [**transitionMode (authEncryption)**](wlan-profileschema-authencryption-security-element.md#transitionmode)
      * [**sharedKey (security)**](wlan-profileschema-sharedkey-security-element.md)
        * [**keyType (sharedKey)**](wlan-profileschema-sharedkey-security-element.md#keytype)
        * [**protected (sharedKey)**](wlan-profileschema-sharedkey-security-element.md#protected)
        * [**keyMaterial (sharedKey)**](wlan-profileschema-sharedkey-security-element.md#keymaterial)
      * [**keyIndex (security)**](wlan-profileschema-security-msm-element.md#keyindex)
      * [**PMKCacheMode (security)**](wlan-profileschema-security-msm-element.md#pmkcachemode)
      * [**PMKCacheTTL (security)**](wlan-profileschema-security-msm-element.md#pmkcachettl)
      * [**PMKCacheSize (security)**](wlan-profileschema-security-msm-element.md#pmkcachesize)
      * [**preAuthMode (security)**](wlan-profileschema-security-msm-element.md#preauthmode)
      * [**preAuthThrottle (security)**](wlan-profileschema-security-msm-element.md#preauththrottle)
      * [**OneX**](/windows/win32/nativewifi/onexschema-onex-element)
  * [**IHV (WLANProfile)**](wlan-profileschema-ihv-wlanprofile-element.md)
    * [**OUIHeader (IHV)**](wlan-profileschema-ouiheader-ihv-element.md)
      * [**OUI (OUIHeader)**](wlan-profileschema-ouiheader-ihv-element.md#oui)
      * [**type (OUIHeader)**](wlan-profileschema-ouiheader-ihv-element.md#type)
    * [**connectivity (IHV)**](wlan-profileschema-ihv-wlanprofile-element.md#connectivity)
    * [**security (IHV)**](wlan-profileschema-ihv-wlanprofile-element.md#security)
    * [**useMSOneX (IHV)**](wlan-profileschema-ihv-wlanprofile-element.md#usemsonex)
  * [**MacRandomization (WLANProfile)**](wlan-profileschema-macrandomization-wlanprofile-element.md)
    * [**enableRandomization (MacRandomization)**](wlan-profileschema-macrandomization-wlanprofile-element.md#enablerandomization)
    * [**randomizeEveryday (MacRandomization)**](wlan-profileschema-macrandomization-wlanprofile-element.md#randomizeeveryday)
    * [**randomizationSeed (MacRandomization)**](wlan-profileschema-macrandomization-wlanprofile-element.md#randomizationseed)
