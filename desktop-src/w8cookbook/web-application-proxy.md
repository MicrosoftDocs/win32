---
title: Web Application Proxy
description: Web Application Proxy
ms.assetid: DE47843C-D58B-4C71-99C2-D54073CBA531
ms.topic: article
ms.date: 05/31/2018
---

# Web Application Proxy

## Platform

**Servers -** Windows Server 2012 R2  






## Description

In Windows Server 2012 R2, we added a new service called the Web Application Proxy under the Remote Access role that allows administrators to publish applications for external access. This service acts as a reverse proxy and as an Active Directory Federation Services (AD FS) proxy. In fact, this service replaces the AD FS proxy service as it was known in Windows Server 2012.

With the Web Application Proxy, an organization can make on-premises web resources available for external access while at the same time managing the risk of this access by controlling authentication and authorization policies on the AD FS.

## Manifestation

The AD FS proxy service is no longer under the Active Directory Federation Services role (AD FS), but has been replaced by the Web Application Proxy under the Remote Access role. This represents an expansion of the AD FS proxy service by including reverse proxy functionality for application publishing.

## Solution

To access the Web Application Proxy, administrators can go to Server Manager and add a new role/role service. The administrator will find the Web Application Proxy under the Remote Access role.

## Resources

-   [Solution guide](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn280942(v=ws.11))

 

 