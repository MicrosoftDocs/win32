---
title: Network Address Translation Traversal
description: Network Address Translation (NAT) is commonly implemented in residential gateways to share an Internet connection across a private home or small office network.
ms.assetid: '29dc9ad0-e419-4762-a8c5-aec243b52656'
keywords: ["Network Address Translation Traversal", "Network Address Translation Traversal ,start page", "NAT", "traversal ICS/ICF"]
---

# Network Address Translation Traversal

## Purpose

Network Address Translation (NAT) is commonly implemented in residential gateways to share an Internet connection across a private home or small office network. The NAT architecture is limited in that network applications behind the NAT cannot listen for incoming connections from the Internet unless port mappings are configured on the NAT device. Applications can use the NAT Traversal API to configure these port mappings on UPnP-enabled NAT devices.

## Where applicable

NAT Traversal works on networks where a UPnP-enabled NAT is deployed. UPnP NATs are commonly deployed on home and small office networks, but not Internet Service Provider or Enterprise environments.

## Developer audience

The NAT API is designed for use by programmers using C/C++, Microsoft Visual Basic development system, Visual Basic Scripting Edition, and JScript development software. Programmers should be familiar with networking concepts such as stateful packet filtering and network address translation (NAT).

## Run-time requirements

The NAT API is supported on Windows XP and later.

## In this section



| Topic                                                                       | Description                                                                                                         |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [Overview](network-address-translation-traversal.md)<br/>            | General information about Network Address Translation Traversal.<br/>                                         |
| [Reference](network-address-translation-traversal-reference.md)<br/> | Documentation for Network Address Translation Traversal interfaces, structures, and other code elements.<br/> |



 

 

 





