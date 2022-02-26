---
title: Top Tools and Techniques for Making More Robust Windows Games
description: This articles describes tools and techniques that you can use to help reduce the number of support calls you receive.
ms.assetid: ad3d100c-4f87-f1e4-3242-8b2052ba171d
ms.topic: article
ms.date: 05/31/2018
---

# Top Tools and Techniques for Making More Robust Windows Games

One of the more undesirable costs facing game production is support calls. Each time that a user contacts customer support, profit from the game is reduced. While some calls to customer support are not preventable, others can be eliminated or reduced by employing good development practices. This articles describes tools and techniques that you can use to help reduce the number of support calls you receive.

All of the tools described here are free, and the techniques are simple enough to add to most development methods.

Tools and techniques:

-   [PREfast](#prefast)
-   [AppVerifier](#appverifier)
-   [Microsoft Application Compatibility Toolkit](#microsoft-application-compatibility-toolkit)
-   [User Account Protection Testing](#user-account-protection-testing)
-   [PIX for Windows](#pix-for-windows)
-   [Configuration Detection](#configuration-detection)
-   [Enable Full Compiler Warnings](#enable-full-compiler-warnings)
-   [Microsoft Symbol Server](#microsoft-symbol-server)
-   [Windows Error Reporting](#windows-error-reporting)
-   [Performance Tuning Tools](#performance-tuning-tools)
-   [Summary](#summary)

## PREfast

PREfast for Drivers is a tool offered by Microsoft that analyzes execution paths in compiled C or C++ to help find run-time bugs. PREfast operates by working through all execution paths in all functions and assessing each path for problems. While this tool is normally used to develop drivers and other kernel code, it can help game developers save time by eliminating some bugs that are hard to find or that are ignored by the compiler. Use of PREfast is an excellent way of reducing your post-release workload and support costs.

PREfast comes with Visual Studio Team System and as part of the [Windows Driver Kit](https://www.microsoft.com/whdc/devtools/WDK/). For more information about PREfast, see [PREfast for Drivers](https://www.microsoft.com/whdc/devtools/tools/PREfast.mspx).

## AppVerifier

The Microsoft Application Verifier, or AppVerifier, is a tool that can help testers by providing multiple functions in one tool. AppVerifier was developed to make it easier to test for common programming errors. AppVerifier can check the parameters that are passed in API calls, inject erroneous input to check error-handling ability, and log changes to the registry and file system. AppVerifier can also detect buffer overruns in the heap, check that an access control list (ACL) has been properly defined, and enforce the safe use of sockets APIs.

While not exhaustive, AppVerifier can be one more component of a tester's toolbox to help a development studio release a quality product and reduce potential post-release costs.

For more information about Application Verifier, see [Application Verifier](/previous-versions/ms220948(v=vs.80)) and [Using Application Verifier Within Your Software Development Lifecycle](/previous-versions/aa480483(v=msdn.10)) on MSDN. 

A similar tool for drivers, Driver Verifier, is also available. For more information, see [Using Driver Verifier to Identify Issues with Windows Drivers for Advanced Users](https://support.microsoft.com/Default.aspx?kbid=244617) on Microsoft Help and Support.

## Microsoft Application Compatibility Toolkit

The Microsoft Application Compatibility Toolkit is a set of free tools to help developers quickly check to see how their releases will perform on newly released service packs for Microsoft Windows. By being ready for new service packs, developers can prevent or be ready for any issues.

The Application Compatibility Toolkit, and more information, can be found at [Windows Application Compatibility](https://www.microsoft.com/technet/prodtechnol/windows/appcompatibility/default.mspx).

## User Account Protection Testing

Windows Vista and Windows 7 have two primary types of user accounts: Standard User and Administrator. Standard User accounts are the preferred type for all users, since they reduce the risk of damage to the system by malicious applications. Because Standard User has access restrictions — such as not being able to write to the Program Files folder or to HKEY\_LOCAL\_MACHINE (HKLM) in the registry — it is important that games be designed and tested to work with a Standard User account.

More information about this topic can be found in the articles [Patching Game Software in Windows XP, Windows Vista, and Windows 7](./patching-methods-in-windows-xp-and-vista.md) and [User Account Control for Game Developers](./user-account-control-for-game-developers.md).

## PIX for Windows

PIX is a tool for collecting and analyzing performance information from a running application. PIX can gather statistical data on why some frames render more slowly than others and can identify poor API usage. PIX can also be automated to test the daily build and flag sudden changes in application performance. By using PIX across a variety of hardware configurations, testers and developers can help minimize support calls related to game performance.

## Configuration Detection

Device capabilities that are exposed by drivers are not always correct. One solution is to use a database-driven system for configuration of applications, like the system demonstrated in the sample ConfigSystem, which is included with the DirectX SDK. A detection model that is similar to the system in the sample can help identify device capabilities that are hampering game performance, and thus, reduce the number of support calls about performance.

## Enable Full Compiler Warnings

It is a good practice to restore any compiler warnings that were disabled by **\#pragma warning** once a project has become stable. Developers should try to eliminate all warnings before releasing a product. Even if a warning doesn't cause a crash or error on a developer's system, it might still cause a problem on a user's system. If a warning can't be eliminated, the test team needs to ascertain whether the warning will cause few or no errors on a user's system.

## Microsoft Symbol Server

Microsoft provides an Internet-accessible server that provides symbol files for the Microsoft Windows operating systems, as well as other Microsoft products. Symbols are also available from the server for current betas and release candidates of Windows products, as well as hot fixes and service packs. You can configure the debugger to download symbols as needed during a debugging session, rather than downloading symbol files separately before a debugging session. The symbols are downloaded to a directory location that you specify, and the debugger loads them from there.

For more information about the Microsoft Symbol Server, see [Debugging Tools and Symbols: Getting Started](https://www.microsoft.com/whdc/devtools/debugging/debugstart.mspx).

## Windows Error Reporting

Windows Error Reporting (WER) is a service provided by Microsoft to help developers collect error information from applications in a unified and organized manner. While it is completely voluntary, developers should take advantage of this service to help determine which bugs occur most often. Use of WER can help with the debugging of commonly reported problems, which will help eliminate support calls for the most commons bugs.

For more information about WER, see [Crash Dump Analysis](./crash-dump-analysis.md).

## Performance Tuning Tools

Developers can use performance analyzers to tune performance of their game. In addition to PIX, there are a number of popular performance analyzers for Windows, such as the Intel VTune Performance Analyzer and the [AMD CodeAnalyst Performance Analyzer](https://developer.amd.com/cpu/CodeAnalyst/). These tools help with identifying bottlenecks and with deciding how to improve the overall performance of an application. Improving performance bottlenecks prior to release will help bring down post-release costs.

## Summary

Everyone involved in the design, development, and testing needs to consider how his or her work will impact the post-release cost of a product. By using the aforementioned tools and methods in the production process, the volume of support calls can be reduced. This will, in turn, increase profits by reducing the post-release costs of game development.

 

 
