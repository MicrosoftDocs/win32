---
description: New Low-Level Binaries
ms.assetid: 8c883462-29d8-46c4-b1c6-3ae8b8d3b397
title: New Low-Level Binaries
ms.topic: article
ms.date: 05/31/2018
---

# New Low-Level Binaries

## Affected Platforms

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

**Severity** - Medium  
**Frequency** - High  











## Description

To improve internal engineering efficiencies and improve foundations for future work, we have relocated some functionality to new low-level binaries. This refactoring will make it possible for future installs of Windows to provide subsets of functionality to reduce surface area (disk and memory requirements, servicing, and attack surface).

## Manifestation of Impact

As an example of functionality that we moved to low-level binaries, kernelbase.dll gets functionality from kernel32.dll and advapi32.dll. This means that the existing binary now forwards calls down to the new binary rather than handling them directly; the forwarding can be static (the export table shows the redirection), or runtime (the dll has a stub routine that calls down to the new binary). This will impact low-level applications such as security and backup applications that are dependent upon internal APIs and offsets.

## Solution

The only impact is to code that makes assumptions when attempting to look at the kernel32.dll or the advapi32.dll export table in memory, such as an anti-virus application might do. Use published APIs and not the details of their implementation. This is just one example of implementing around a detail of implementation for an API.

 

 



