---
title: LAN_policy schema elements
description: A wired (LAN) policy profile contains the following schema elements.
ms.topic: article
ms.date: 06/21/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.assetid: 361f76f1-a26f-46b3-a9ab-e56627c9b19f
---

# LAN_policy schema elements

A wired (LAN) policy profile contains the following schema elements. All of the named elements are in the namespace `https://www.microsoft.com/networking/LAN/policy/v1`.

The following list shows the defined elements in the order in which the elements appear in a profile. The ordering of elements is enforced. Not all elements are in every profile, as some elements are optional.

This list does not show all possible elements that can appear in a profile, as elements can be added in **xs:any** insertion points.

## Elements

* [**LANPolicy**](lan-policyschema-lanpolicy-element.md)
  * [**name (LANPolicy)**](lan-policyschema-name-lanpolicy-element.md)
  * [**description (LANPolicy)**](lan-policyschema-description-lanpolicy-element.md)
  * [**globalFlags (LANPolicy)**](lan-policyschema-globalflags-lanpolicy-element.md)
    * [**enableAutoConfig (globalFlags)**](lan-policyschema-enableautoconfig-globalflags-element.md)
  * [**profileList (LANPolicy)**](lan-policyschema-profilelist-lanpolicy-element.md)
