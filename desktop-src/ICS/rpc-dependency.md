---
title: RPC Dependency
description: Which Firewall rules are necessary with RPC depends on how you are using RPC.
ms.assetid: 12f5f5c6-5138-4697-9493-b5a32b71f09b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RPC Dependency

Which Firewall rules are necessary with RPC depends on how you are using RPC.

## RPC/TCP

If your component is dependent on RPC/TCP functionality then you should add two rules with the following parameters to your firewall rule group:

dir="in" protocol="6" lport="RPC-EPMAP" binary="%systemroot%\\system32\\svchost.exe" svc="RPCSS"

dir="in" protocol="6" lport="RPC" binary="&lt;*YOUR BINARY THAT RECEIVES RPC/TCP*&gt;" svc="&lt;*YOUR SERVICE THAT IS HOSTED BY THE BINARY*&gt;"

## RPC/NP (Named Pipes)

If your component is dependent on RPC/NP functionality then a single rule is necessary:

dir="in" protocol="6" lport="445" binary="System"

## DCOM

If your component is dependent on DCOM functionality then a single rule is necessary:

dir="in" protocol="6" lport="RPC" binary="&lt;*YOUR BINARY THAT RECEIVES DCOM*&gt;" svc="&lt;*YOUR SERVICE THAT IS HOSTED BY THE BINARY*&gt;"

If you require DCOM Activation calls then you will need to add an additional rule:

dir="in" protocol="6" lport="135" binary="%systemroot%\\system32\\svchost.exe" svc="RPCSS"

 

 




