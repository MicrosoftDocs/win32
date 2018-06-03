---
title: Remote Differential Compression
description: Applications to synchronize data between two computers in an efficient manner.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 128178a5-efaf-49cc-8f21-6e83bceb87f0
ms.prod: windows-server-dev
ms.technology: remote-differential-compression
ms.tgt_platform: multiple
keywords:
- Remote Differential Compression Files
- Remote Differential Compression Files , home page
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remote Differential Compression

## Purpose

Remote Differential Compression (RDC) allows applications to synchronize data between two computers in an efficient manner.

## Where applicable

An RDC application can synchronize data between any two or more computers across a network with a minimum amount of data transfer over the network.

## Developer audience

RDC is designed for C and C++ developers. Familiarity with COM and client/server architecture is required.

## Run-time requirements

For information about which operating system versions are required to use a particular programming element, see the Requirements section of the reference page for that element.

> [!Note]  
> End users should not [disable](http://go.microsoft.com/fwlink/p/?linkid=159021) RDC. RDC is a dynamic-link library (DLL) that does not consume any system resources, except when you run an application that uses RDC specifically. If you disable RDC, any application that uses it will either not be able to take advantage of RDC or will simply fail.

 

## In this section

<dl> <dt>

[About Remote Differential Compression](about-remote-differential-compression.md)
</dt> <dd>

Describes Remote Differential Compression concepts and terminology.

</dd> <dt>

[Using Remote Differential Compression](using-remote-differential-compression.md)
</dt> <dd>

Describes basic tasks and guidelines for implementing a Remote Differential Compression application.

</dd> <dt>

[Remote Differential Compression Reference](remote-differential-compression-reference.md)
</dt> <dd>

Describes Remote Differential Compression enumerations, interfaces, and structures.

</dd> </dl>

 

 




