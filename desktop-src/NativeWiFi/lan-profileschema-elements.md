---
title: LAN_profile schema elements
description: A wired network profile contains the following schema elements.
ms.assetid: 3f316725-0cb9-414c-a267-875b3ad67765
ms.topic: article
ms.date: 06/13/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# LAN_profile schema elements

A wired network profile contains the schema elements shown below. All of the named elements are in the namespace `https://www.microsoft.com/networking/LAN/profile/v1`.

The following list shows the defined elements in the order in which the elements appear in a profile. The ordering of elements is enforced. This list doesn't show all possible elements that can appear in a profile, since you can add elements in **xs:any** insertion points.

> [!NOTE]
> The **OneX** configuration parameters must be present if either the `OneXEnforced` or `OneXEnabled` flag is set to "true".

-   [**LANProfile**](lan-profileschema-lanprofile-element.md)
    -   [**MSM (LANProfile)**](lan-profileschema-msm-lanprofile-element.md)
        -   [**security (MSM)**](lan-profileschema-security-msm-element.md)
            -   [**OneXEnforced (security)**](lan-profileschema-onexenforced-security-element.md)
            -   [**OneXEnabled (security)**](lan-profileschema-onexenabled-security-element.md)
            -   [**OneX**](/windows/win32/nativewifi/onexschema-onex-element)
