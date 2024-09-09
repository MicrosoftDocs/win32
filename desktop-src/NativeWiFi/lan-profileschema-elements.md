---
title: LAN_profile schema elements
description: A wired network profile contains the following schema elements.
ms.topic: reference
ms.date: 06/23/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
api_type: 
- Schema
api_location: 
ms.assetid: 3f316725-0cb9-414c-a267-875b3ad67765
---

# LAN_profile schema elements

A wired network profile contains the schema elements shown below. All of the named elements are in the namespace `https://www.microsoft.com/networking/LAN/profile/v1`.

The following list shows the defined elements in the order in which the elements appear in a profile. The ordering of elements is enforced. This list doesn't show all possible elements that can appear in a profile, since you can add elements in **xs:any** insertion points.

> [!NOTE]
> The **OneX** configuration parameters must be present if either the `OneXEnforced` or `OneXEnabled` flag is set to "true".

## All elements

* [**LANProfile**](./lan-profileschema-lanprofile-element.md)
  * [**MSM (LANProfile)**](./lan-profileschema-msm-lanprofile-element.md)
    * [**security (MSM)**](./lan-profileschema-security-msm-element.md)
      * [**OneXEnforced (security)**](./lan-profileschema-security-msm-element.md#onexenforced)
      * [**OneXEnabled (security)**](./lan-profileschema-security-msm-element.md#onexenabled)
      * [**OneX**](/windows/win32/nativewifi/onexschema-onex-element)
