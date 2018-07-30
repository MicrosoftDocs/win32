---
Description: .
ms.assetid: 1cb0456d-501a-4272-b89d-35e79d29d13a
title: Internet Explorer 8 - User Agent String
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Internet Explorer 8 - User Agent String

## Affected Platforms

<dl> **Clients** - Windows XP \| Windows Vista \| Windows 7  
**Servers** - Windows Server 2003 \| Windows Server 2008 \| Windows Server 2008 R2  
</dl>

## Feature Impact

<dl> **Severity** - Medium  
**Frequency** - High  
</dl>

## Description

The User Agent String is the Internet Explorer identifier that provides data about its version and other attributes to web servers. Many web applications rely on, and piggyback on, the IE User Agent String. Those that do so and depend on an earlier version number will be impacted. The User Agent string now includes the string 'Trident/4.0' in order to allow differentiation between the Internet Explorer 7 User Agent String and the Internet Explorer 8 User Agent string when running in Internet Explorer 7 Compatibility View. See Understanding User Agent Strings for details.

## Manifestation of Impact

There are two impacted areas:

-   Webpages that explicitly check the User Agent String and do not support the Internet Explorer 8 User Agent String may not run properly. In the majority of cases, this means the pages will be block users from the content they are attempting to access or display incorrect or malformed content.
-   Applications that host Trident (see Hosting and Reuse) will default to Internet Explorer 7 using the Web Optional Component, but will not have access to Internet Explorer 8 features.

## Solution

Ensure that your applications properly handle the new 'MSIE 8.0' version in the User Agent String. You may also opt in to the Internet Explorer 7 Compatibility View for those applications based on Internet Explorer 7. This can be done with meta tags. See the discussion in Understanding User Agent Strings for details.

## Compatibility, Performance, Reliability, and Usability Testing

-   Run your applications and webpages in an Internet Explorer 8 environment on Windows Vista or Windows XP to ensure that they behave in the desired manner.
-   Alternatively, you can run the Internet Explorer Compatibility Test Tool (IECTT) provided with the Application Compatibility Toolkit (ACT) to locate any potential issues due to security feature updates.

## Links to Other Resources

-   [Understanding User Agent Strings](https://msdn.microsoft.com/library/ms537503(v=VS.85).aspx)
-   [Internet Explorer 8 User-Agent String](http://go.microsoft.com/fwlink/p/?linkid=205081)
-   [User-Agent String and Version Vector](http://go.microsoft.com/fwlink/p/?linkid=203822)
-   [Hosting and Reuse](https://msdn.microsoft.com/library/Aa752038(v=VS.85).aspx)
-   [Application Compatibility Toolkit Download](http://go.microsoft.com/fwlink/p/?linkid=205020)
-   [Known Internet Explorer Security Feature Issues](http://go.microsoft.com/fwlink/p/?linkid=205080)

 

 



