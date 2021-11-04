---
description: Using .NET Framework 4 with Applications Built on Earlier Versions
ms.assetid: 287E25AD-A560-40DA-A4E6-C46A3123914E
title: Using .NET Framework 4 with Applications Built on Earlier Versions
ms.topic: article
ms.date: 05/31/2018
---

# Using .NET Framework 4 with Applications Built on Earlier Versions

## Platform

 **Clients** - Windows XP, Windows Vista, Windows 7  
**Servers** - Windows Server 2003, Windows Server 2008, Windows Server 2008 R2  


## Feature Impact

 **Severity** - Low  
**Frequency** - High  






## Description

The .NET Framework 4 is highly compatible with applications that are built by using earlier .NET Framework versions. The primary changes in .NET Framework 4 are to improve security, standards compliance, correctness, reliability, and performance.

However, .NET Framework 4 does not automatically use its version of the common language runtime (CLR) to run applications that are built by using earlier versions of the .NET Framework.

## Manifestation

If you built an application by using an earlier .NET Framework and a user opens that application on a computer that has both .NET Framework 4 and the earlier version of the .NET Framework installed, the application uses the earlier CLR version.

However, if the .NET Framework 4 is the only runtime version that is installed on the computer, the application throws an exception and asks the user to install the runtime version that you built the application against.

## Solution

To run applications that are built with earlier .NET Framework versions with .NET Framework 4, you must compile your application to target the .NET Framework 4 version by specifying it in the properties for your project in Microsoft Visual Studio, or you can specify .NET Framework 4 in the [**&lt;supportedRuntime&gt; element**](/previous-versions/dotnet/netframework-1.1/w4atty68(v=vs.71)) in an application configuration file.

For more information about how to migrate to the .NET Framework 4, see [Migration Guide to the .NET Framework 4](/previous-versions/dotnet/netframework-4.0/ff657133(v=vs.100)) and [Version Compatibility in the .NET Framework](/previous-versions/dotnet/netframework-4.0/ff602939(v=vs.100)).

## Compatibility Tests

After you make the changes, test your application to make sure that it runs correctly. You can test compatibility as described in the [.NET Framework 4 Application Compatibility](/previous-versions/dd889541(v=msdn.10)) topic.

If your application or component does not work after .NET Framework 4 is installed, submit a bug through the [Microsoft Connect](https://connect.microsoft.com/visualstudio) website.

## Links to Other Resources

-   [**&lt;supportedRuntime&gt; element**](/previous-versions/dotnet/netframework-1.1/w4atty68(v=vs.71))
-   [Migration Guide to the .NET Framework 4](/previous-versions/dotnet/netframework-4.0/ff657133(v=vs.100))
-   [Version Compatibility in the .NET Framework](/previous-versions/dotnet/netframework-4.0/ff602939(v=vs.100))
-   **.NET Framework 4 RTM Application Compatibility Walkthrough:**<https://msdn.microsoft.com/library/dd889541.aspx>
-   [Microsoft Connect](https://connect.microsoft.com/)

 

 
