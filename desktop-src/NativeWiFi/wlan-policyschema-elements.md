---
title: WLAN_policy schema elements
description: A Native Wifi wireless LAN (WLAN) policy profile is composed of the following schema elements.
ms.topic: reference
ms.date: 06/24/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
api_type: 
- Schema
api_location: 
ms.assetid: e3f45b02-6aea-4df3-938e-c13e7c52ca04
---

# WLAN_policy schema elements

A Native Wifi wireless LAN (WLAN) policy profile is composed of the following schema elements. All of the named elements are in the namespace `https://www.microsoft.com/networking/WLAN/policy/v1`.

The following list shows the defined elements in the order in which the elements appear in a profile. The ordering of elements is enforced. Not all elements are in every profile, as some elements are optional.

This list does not show all possible elements that can appear in a profile, as elements can be added in **xs:any** insertion points.

## All elements

* [**WLANPolicy**](./wlan-policyschema-wlanpolicy-element.md)
  * [**name (WLANPolicy)**](./wlan-policyschema-wlanpolicy-element.md#name)
  * [**description (WLANPolicy)**](./wlan-policyschema-wlanpolicy-element.md#description)
  * [**globalFlags (WLANPolicy)**](./wlan-policyschema-globalflags-wlanpolicy-element.md)
    * [**enableAutoConfig (globalFlags)**](./wlan-policyschema-globalflags-wlanpolicy-element.md#enableautoconfig)
    * [**showDeniedNetwork (globalFlags)**](./wlan-policyschema-globalflags-wlanpolicy-element.md#showdeniednetwork)
    * [**allowEveryoneToCreateAllUserProfiles (globalFlags)**](./wlan-policyschema-globalflags-wlanpolicy-element.md#alloweveryonetocreatealluserprofiles)
    * [**onlyUseGPProfilesForAllowedNetworks (globalFlags)**](./wlan-policyschema-globalflags-wlanpolicy-element.md#onlyusegpprofilesforallowednetworks)
    * [**enbleSoftAP (globalFlags)**](./wlan-policyschema-globalflags-wlanpolicy-element.md#enblesoftap)
    * [**enableExplicitCreds (globalFlags)**](./wlan-policyschema-globalflags-wlanpolicy-element.md#enableexplicitcreds)
    * [**blockPeriod (globalFlags)**](./wlan-policyschema-globalflags-wlanpolicy-element.md#blockperiod)
    * [**enableWFD (globalFlags)**](./wlan-policyschema-globalflags-wlanpolicy-element.md#enablewfd)
  * [**networkFilter (WLANPolicy)**](./wlan-policyschema-networkfilter-wlanpolicy-element.md)
    * [**allowList (networkFilter)**](./wlan-policyschema-allowlist-networkfilter-element.md)
      * [**network (allowList)**](./wlan-policyschema-network-allowlist-element.md)
        * [**networkName (network)**](./wlan-policyschema-network-allowlist-element.md#networkname)
        * [**networkType (network)**](./wlan-policyschema-network-allowlist-element.md#networktype)
    * [**blockList (networkFilter)**](./wlan-policyschema-blocklist-networkfilter-element.md)
      * [**network (blockList)**](./wlan-policyschema-network-blocklist-element.md)
        * [**networkName (network)**](./wlan-policyschema-network-blocklist-element.md#networkname)
        * [**networkType (network)**](./wlan-policyschema-network-blocklist-element.md#networktype)
    * [**denyAllIBSS (networkFilter)**](./wlan-policyschema-networkfilter-wlanpolicy-element.md#denyallibss)
    * [**denyAllESS (networkFilter)**](./wlan-policyschema-networkfilter-wlanpolicy-element.md#denyalless)
  * [**profileList (WLANPolicy)**](./wlan-policyschema-wlanpolicy-element.md#profilelist)
