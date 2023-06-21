---
title: WLAN_policy schema elements
description: A Native Wifi wireless LAN (WLAN) policy profile is composed of the following schema elements.
ms.topic: article
ms.date: 06/21/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.assetid: e3f45b02-6aea-4df3-938e-c13e7c52ca04
---

# WLAN_policy schema elements

A Native Wifi wireless LAN (WLAN) policy profile is composed of the following schema elements. All of the named elements are in the namespace `https://www.microsoft.com/networking/WLAN/policy/v1`.

The following list shows the defined elements in the order in which the elements appear in a profile. The ordering of elements is enforced. Not all elements are in every profile, as some elements are optional.

This list does not show all possible elements that can appear in a profile, as elements can be added in **xs:any** insertion points.

## Elements

* [**WLANPolicy**](wlan-policyschema-wlanpolicy-element.md)
  * [**name (WLANPolicy)**](wlan-policyschema-name-wlanpolicy-element.md)
  * [**description (WLANPolicy)**](wlan-policyschema-description-wlanpolicy-element.md)
  * [**globalFlags (WLANPolicy)**](wlan-policyschema-globalflags-wlanpolicy-element.md)
    * [**enableAutoConfig (globalFlags)**](wlan-policyschema-enableautoconfig-globalflags-element.md)
    * [**showDeniedNetwork (globalFlags)**](wlan-policyschema-showdeniednetwork-globalflags-element.md)
    * [**allowEveryoneToCreateAllUserProfiles (globalFlags)**](wlan-policyschema-alloweveryonetocreatealluserprofiles-globalflags-element.md)
  * [**networkFilter (WLANPolicy)**](wlan-policyschema-networkfilter-wlanpolicy-element.md)
    * [**allowList (networkFilter)**](wlan-policyschema-allowlist-networkfilter-element.md)
      * [**network (allowList)**](wlan-policyschema-network-allowlist-element.md)
        * [**networkName (networkItemType)**](wlan-policyschema-networkname-networkitemtype-element.md)
        * [**networkType (networkItemType)**](wlan-policyschema-networktype-networkitemtype-element.md)
    * [**blockList (networkFilter)**](wlan-policyschema-blocklist-networkfilter-element.md)
      * [**network (blockList)**](wlan-policyschema-network-blocklist-element.md)
        * [**networkName (networkItemType)**](wlan-policyschema-networkname-networkitemtype-element.md)
        * [**networkType (networkItemType)**](wlan-policyschema-networktype-networkitemtype-element.md)
    * [**denyAllIBSS (networkFilter)**](wlan-policyschema-denyallibss-networkfilter-element.md)
    * [**denyAllESS (networkFilter)**](wlan-policyschema-denyalless-networkfilter-element.md)
  * [**profileList (WLANPolicy)**](wlan-policyschema-profilelist-wlanpolicy-element.md)
