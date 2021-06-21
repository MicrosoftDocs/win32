---
title: Measured Boot
description: Measured Boot
ms.assetid: D7ED02FA-6D0F-4753-AC07-BD7DCE55B3FD
ms.topic: article
ms.date: 05/31/2018
---

# Measured Boot

## Platforms

 **Clients** - Windows 8  
**Servers** - Windows Server 2012  



## Description

As antimalware (AM) software has become better and better at detecting runtime malware, attackers are also becoming better at creating rootkits that can hide from detection. Detecting malware that starts early in the boot cycle is a challenge that most AM vendors address diligently. Typically, they create system hacks that are not supported by the host operating system and can actually result in placing the computer in an unstable state. Up to this point, Windows has not provided a good way for AM to detect and resolve these early boot threats. Windows 8 introduces a new feature called Measured Boot, which measures each component, from firmware up through the boot start drivers, stores those measurements in the Trusted Platform Module (TPM) on the machine, and then makes available a log that can be tested remotely to verify the boot state of the client.

## Manifestation

The Measured Boot feature provides AM software with a trusted (resistant to spoofing and tampering) log of all boot components that started before AM software. AM software can use the log to determine whether components that ran before it are trustworthy or if they are infected with malware. The AM software on the local machine can send the log to a remote server for evaluation. The remote server may initiate remediation actions either by interacting with software on the client or through out-of-band mechanisms, as appropriate.

## Mitigation

In enterprise scenarios, the system administrator has control of how Measured Boot info is used. In end-user scenarios for example, online banking), the consumer must opt in to use Measured Boot for the specific service.

## Solution

A white paper is being prepared that details the APIs and function calls that must be made for various Measured Boot scenarios.

 

 




