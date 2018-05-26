---
Description: When creating a security support provider (SSP) security package, you should not allow the domain joined client to authenticate to a domain controller by using a two part service provider name (SPN) of the following form.
ms.assetid: 6CD3BC5E-F9B2-4E8E-9DEE-064AE8837DFB
title: Using Three Part Principal Names
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Three Part Principal Names

When creating a security support provider (SSP) security package, you should not allow the domain joined client to authenticate to a domain controller by using a two part service provider name (SPN) of the following form.

-   &lt;*protocol*&gt;/&lt;*host name*&gt;

A client should always authenticate by specifying the domain.

-   &lt;*protocol*&gt;/&lt;*host name*&gt;/&lt;*domain name*&gt;

A domain joined client that logs on with a two part SPN may be able to impersonate the domain controller. If you allow two part SPNs, you should create a log entry that contains enough information to enable the administrator to identify the caller.

 

 



