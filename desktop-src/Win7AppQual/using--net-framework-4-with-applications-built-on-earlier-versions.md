---
Description: Using .NET Framework 4 with Applications Built on Earlier Versions
ms.assetid: 287E25AD-A560-40DA-A4E6-C46A3123914E
title: Using .NET Framework 4 with Applications Built on Earlier Versions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using .NET Framework 4 with Applications Built on Earlier Versions

## Platform

<dl> **Clients** - Windows XP \| Windows Vista \| Windows 7  
**Servers** - Windows Server 2003 \| Windows Server 2008 \| Windows Server 2008 R2  
</dl>

## Feature Impact

<dl> **Severity** - Low  
**Frequency** - High  
</dl>

## Description

The .NET Framework 4 is highly compatible with applications that are built by using earlier .NET Framework versions. The primary changes in .NET Framework 4 are to improve security, standards compliance, correctness, reliability, and performance.

However, .NET Framework 4 does not automatically use its version of the common language runtime (CLR) to run applications that are built by using earlier versions of the .NET Framework.

## Manifestation

If you built an application by using an earlier .NET Framework and a user opens that application on a computer that has both .NET Framework 4 and the earlier version of the .NET Framework installed, the application uses the earlier CLR version.

However, if the .NET Framework 4 is the only runtime version that is installed on the computer, the application throws an exception and asks the user to install the runtime version that you built the application against.

## Solution

To run applications that are built with earlier .NET Framework versions with .NET Framework 4, you must compile your application to target the .NET Framework 4 version by specifying it in the properties for your project in Microsoft Visual Studio, or you can specify .NET Framework 4 in the [**<supportedRuntime> element**](https://msdn.microsoft.com/en-us/library/w4atty68(v=VS.71).aspx) in an application configuration file.

For more information about how to migrate to the .NET Framework 4, see [Migration Guide to the .NET Framework 4](https://msdn.microsoft.com/en-us/library/Ff657133(v=VS.100).aspx) and [Version Compatibility in the .NET Framework](https://msdn.microsoft.com/en-us/library/Ff602939(v=VS.100).aspx).

## Compatibility Tests

After you make the changes, test your application to make sure that it runs correctly. You can test compatibility as described in the [.NET Framework 4 Application Compatibility](http://go.microsoft.com/fwlink/p/?linkid=154814) topic.

If your application or component does not work after .NET Framework 4 is installed, submit a bug through the [Microsoft Connect](http://connect.microsoft.com/visualstudio) website.

## Links to Other Resources

-   [**<supportedRuntime> Element**](https://msdn.microsoft.com/en-us/library/w4atty68(v=VS.71).aspx)
-   [Migration Guide to the .NET Framework 4](https://msdn.microsoft.com/en-us/library/Ff657133(v=VS.100).aspx)
-   [Version Compatibility in the .NET Framework](https://msdn.microsoft.com/en-us/library/Ff602939(v=VS.100).aspx)
-   **.NET Framework 4 RTM Application Compatibility Walkthrough:**<http://msdn.microsoft.com/en-us/library/dd889541.aspx>
-   [Microsoft Connect](http://go.microsoft.com/fwlink/p/?linkid=101629)

 

 



