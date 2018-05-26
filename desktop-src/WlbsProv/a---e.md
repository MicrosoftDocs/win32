---
title: A - E
description: A \ 8211;E F \ 8211;M N \ 8211;Z
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f8d98c3b-fde3-4659-8c8f-6bd5980ef7ad
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# A - E

A–E [F–M](https://msdn.microsoft.com/library/aa369591) [N–Z](https://msdn.microsoft.com/library/aa371764)

<dl> <dt>

<span id="mscs.a___e_1_gly"></span><span id="MSCS.A___E_1_GLY"></span>**availability**
</dt> <dd>

A measure of a computer system's ability to maintain services despite hardware or software failures. A highly available system delivers services to clients a high percentage of the time.

</dd> <dt>

<span id="mscs.a___e_2_gly"></span><span id="MSCS.A___E_2_GLY"></span>**CIM**
</dt> <dd>

See *Common Information Model*.

</dd> <dt>

<span id="mscs.a___e_3_gly"></span><span id="MSCS.A___E_3_GLY"></span>**CIM class**
</dt> <dd>

See [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly).

</dd> <dt>

<span id="mscs.a___e_4_gly"></span><span id="MSCS.A___E_4_GLY"></span>**CIP**
</dt> <dd>

See *cluster IP address*.

</dd> <dt>

<span id="mscs.a___e_5_gly"></span><span id="MSCS.A___E_5_GLY"></span>**cluster**
</dt> <dd>

A group of independent computer systems, referred to as [*nodes*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly), working together as a unified computing resource.

</dd> <dt>

<span id="mscs.a___e_6_gly"></span><span id="MSCS.A___E_6_GLY"></span>**cluster IP address**
</dt> <dd>

The IP address serviced by a Network Load Balancing *cluster*. All network traffic directed to the cluster IP address is either handled by the current [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) settings or by the *default host*. The cluster IP address is sometimes referred to as the CIP or VIP.

</dd> <dt>

<span id="mscs.a___e_7_gly"></span><span id="MSCS.A___E_7_GLY"></span>**Common Information Model (CIM)**
</dt> <dd>

A programming paradigm that describes how to represent real-world managed objects. Used for [*WMI*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-21-gly) class specification.

</dd> <dt>

<span id="mscs.a___e_8_gly"></span><span id="MSCS.A___E_8_GLY"></span>**convergence**
</dt> <dd>

The process of redistributing the existing connection load to operational cluster [*nodes*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) according to the current [*load balancing*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-5-gly) rules.

</dd> <dt>

<span id="mscs.a___e_9_gly"></span><span id="MSCS.A___E_9_GLY"></span>**default host**
</dt> <dd>

The [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) with the lowest [*host priority*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-3-gly) is the default host, The default host handles all of the network traffic for TCP and UDP ports that are not otherwise covered by [*port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly).

</dd> <dt>

<span id="mscs.a___e_10_gly"></span><span id="MSCS.A___E_10_GLY"></span>**direct connection**
</dt> <dd>

A WMI connection in which the [*namespace*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-1-gly) resolves to the dedicated IP address of a cluster [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly), which becomes the [*provider node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-11-gly).

</dd> <dt>

<span id="mscs.a___e_11_gly"></span><span id="MSCS.A___E_11_GLY"></span>**drain**
</dt> <dd>

A state in which a [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) is no longer accepting incoming traffic is draining. No new connections are allowed, but existing connections are allowed to complete their jobs and terminate naturally. While draining, a node can participate in *convergence* and remains part of the *cluster*.

</dd> </dl>

 

 




