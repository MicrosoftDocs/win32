---
title: LAN_policy schema elements
description: A wired (LAN) policy profile contains the following schema elements.
ms.topic: reference
ms.date: 06/24/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
api_type: 
- Schema
api_location: 
ms.assetid: 361f76f1-a26f-46b3-a9ab-e56627c9b19f
---

# LAN_policy schema elements

A wired (LAN) policy profile contains the following schema elements. All of the named elements are in the namespace `https://www.microsoft.com/networking/LAN/policy/v1`.

The following list shows the defined elements in the order in which the elements appear in a profile. The ordering of elements is enforced. Not all elements are in every profile, as some elements are optional.

This list does not show all possible elements that can appear in a profile, as elements can be added in **xs:any** insertion points.

## All elements

* [**LANPolicy**](./lan-policyschema-lanpolicy-element.md)
  * [**name (LANPolicy)**](./lan-policyschema-lanpolicy-element.md#name)
  * [**description (LANPolicy)**](./lan-policyschema-lanpolicy-element.md#description)
  * [**globalFlags (LANPolicy)**](./lan-policyschema-globalflags-lanpolicy-element.md)
    * [**enableAutoConfig (globalFlags)**](./lan-policyschema-globalflags-lanpolicy-element.md#enableautoconfig)
    * [**enableExplicitCreds (globalFlags)**](./lan-policyschema-globalflags-lanpolicy-element.md#enableexplicitcreds)
    * [**blockPeriod (globalFlags)**](./lan-policyschema-globalflags-lanpolicy-element.md#blockperiod)
  * [**profileList (LANPolicy)**](./lan-policyschema-lanpolicy-element.md#profilelist)
