---
title: Private Online Stores
description: Private Online Stores
ms.assetid: c1e241f5-6d29-4b53-8be0-264597e03de7
keywords:
- Windows Media Player online stores,private
- online stores,private
- type 1 online stores,private
- type 2 online stores,private
- private online stores
- registry,private online stores
ms.topic: article
ms.date: 05/31/2018
---

# Private Online Stores

Windows Media Player 10 or later supports private online stores; that is, stores that are visible only to certain users. For a private online store to be visible to the current user, there must be an entry that represents the private online store under the following registry key.

HKEY\_CURRENT\_USER\\Software\\Microsoft\\MediaPlayer\\PrivateServices

The required registry entry must have the following format.



| Name                                                         | Type           | Value                                                                     |
|--------------------------------------------------------------|----------------|---------------------------------------------------------------------------|
| Any name chosen by the person who creates the registry entry | **REG\_DWORD** | A number, provided by Microsoft, that identifies the private online store |



 

The Windows Media Player 10 ActiveX control supports private online stores only if the control is running in remote mode. The Windows Media Player 11 ActiveX control supports private online stores regardless of whether the control is running in remote mode.

## Related topics

<dl> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> </dl>

 

 




