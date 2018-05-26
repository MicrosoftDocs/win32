---
title: SSDP/UPnP Dependency
ms.assetid: e239cdab-aab5-4a9f-883b-e77a3d54b53d
description: 
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SSDP/UPnP Dependency

Components may utilize SSDP or UPnP/SSDP in combination. The following are the rules required for SSDP:

dir="in" protocol="17" lport="1900" binary="%systemroot%\\system32\\svchost.exe" svc="ssdpsrv"

dir="out" protocol="17" rport="1900" binary="%systemroot%\\system32\\svchost.exe" svc="ssdpsrv"

If you require UPnP/SSDP then you will need three additional rules:

dir="in" protocol="6" lport="2869" binary="System"

dir="out" protocol="6" binary="System"

dir="out" protocol="6" binary="%systemroot%\\system32\\svchost.exe" svc="upnphost"

 

 




