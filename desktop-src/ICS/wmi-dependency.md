---
title: WMI Dependency
ms.assetid: 94f74d56-a3be-4122-9714-d9a764145d80
description: 
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WMI Dependency

If your component is dependent on WMI for functionality then you should add three rules with the following parameters to your firewall rule group:

dir="in" protocol="6" lport="135" binary="%systemroot%\\system32\\svchost.exe" svc="RPCSS"

dir="in" protocol="6" lport="RPC" binary="%systemroot%\\system32\\svchost.exe" svc="winmgmt"

dir="out" protocol="6" binary="%systemroot%\\system32\\svchost.exe" svc="winmgmt"

If you require Asynchronous WMI calls then you will need to add an additional rule:

active="true" dir="in" protocol="6" binary="%systemroot%\\system32\\unsecapp.exe"

 

 




