---
description: Windows Sockets (Winsock) Service Provider Interface (SPI).
ms.assetid: '59ac7ce6-10e7-40ac-bdce-dc01251b0bc5'
title: Winsock SPI
ms.topic: article
ms.date: 05/31/2018
---

# Winsock SPI

The Winsock Service Provider Interface, or Winsock SPI, is a specialized discipline of Winsock used to create providers; transport providers such as TCP/IP or IPX/SPX protocol stacks use the Winsock SPI, as do namespace providers such as the Internet's Domain Naming System (DNS).

Traditional network programming, such as enabling applications to communicate over the network, does not require use of Winsock SPI interfaces; use standard [Winsock](winsock-reference.md) interfaces instead.

 

The Winsock SPI uses the following function prefix naming convention.



| Prefix | Meaning                          | Description                                       |
|--------|----------------------------------|---------------------------------------------------|
| WSP    | Windows Sockets Service Provider | Transport service provider entry points           |
| WPU    | Windows Sockets Provider Upcall  | Ws2\_32.dll entry points for service providers    |
| WSC    | Windows Sockets Configuration    | WS2\_32.dll entry points for installation applets |
| NSP    | Namespace Provider               | Namespace provider entry points                   |



 

 

 



