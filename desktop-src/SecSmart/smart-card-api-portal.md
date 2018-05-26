---
title: Smart Card API
description: Use the Smart Card API to write smart card programming software for Windows.
ms.assetid: 695dc300-77a2-4c22-bff9-72480378f9da
keywords:
- Smart Card API Smart Card
- Smart Card API Smart Card , home page
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Smart Card API

## Purpose

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

Smart cards interface to the Microsoft Smart Card Base Cryptographic Service Provider (CSP) or to the Crypto Next Generation (CNG) Key Storage Provider (KSP) through a minidriver.

Smart card vendors can write smart card minidrivers to present a consistent interface for their smart card type to the CSP or the CNG KSP and to the Smart Card Management Interface. These card minidrivers plug in to the Windows operating system code. The scope of functionality in a card minidriver is narrowly and carefully defined so that the card-dependent code is simple to implement and easy to verify functionally.

## Developer audience

The Smart Card API is intended for smart card vendors who develop interchangeable plug-in components in which smart card specific implementation details are handled entirely within vendor-supplied smart card minidrivers, and the appropriately abstracted interface is presented to the CSP or KSP.

## Run-time requirements

For information about run-time requirements for a particular programming element, see the Requirements section of the reference page for that element.

## In this section



| Topic                                                               | Description                                                                      |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [About the Smart Card API](about-the-smart-card-api.md)<br/> | Key smart card minidriver concepts and architecture elements.<br/>         |
| [Using the Smart Card API](using-the-smart-card-api.md)<br/> | Smart card usage scenario and example.<br/>                                |
| [Smart Card API Reference](smart-card-api-reference.md)<br/> | Detailed descriptions of the Smart Card API functions and structures.<br/> |



 

 

 





