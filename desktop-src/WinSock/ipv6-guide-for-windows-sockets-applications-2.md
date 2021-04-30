---
description: This guide provides the information you need to enable your Microsoft Windows application to use the next generation of Internet Protocol, version 6 (IPv6).
ms.assetid: 8e862eb0-2ba9-40b0-ac73-fcb0e625965e
title: IPv6 Guide for Windows Sockets Applications
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 Guide for Windows Sockets Applications

This guide provides the information you need to enable your Microsoft Windows application to use the next generation of Internet Protocol, version 6 (IPv6). Adding IPv6 capability to your application is not necessarily a porting process. To port an application suggests modifying code to work on a different platform, which implies leaving the previous platform behind. This guide is specifically structured to help add IPv6 capability to an application while retaining IPv4 functionality.

This guide discusses the issues associated with adding IPv6 functionality, then targets the areas of development most affected by the transition. Each area receives a thorough explanation of the pitfalls to watch out for, the strategies suggested to avoid them, and tips on how to make the best use of new [Windows Sockets 2](what-s-new-for-windows-sockets-2.md) programmatic elements (functions and structures). For additional information on IPv6, see [IPv6 Support](ipv6-support-2.md).

This guide also provides code examples to give you hands-on experience and visual representations of the issues you could encounter when modifying your applications. The examples come from complete, working examples of a simple Windows Sockets application that has been modified to support both IPv4 and IPv6. Source code for these working examples is included in its entirety in two appendixes at the end of this document: [Appendix A: IPv4-only Source Code](appendix-a-ipv4-only-source-code-2.md) includes the source code for an application before it is modified to support IPv6; [Appendix B: IP-version Agnostic Source Code](appendix-b-ip-version-agnostic-source-code-2.md) provides the source code after the application has been IPv6-enabled.

Microsoft provides a utility called Checkv4.exe that helps you find potentially porting-sensitive code in your application code, and also makes recommendations for fixes. The Checkv4.exe utility is demonstrated in this document, using the sample application included in the appendixes, along with screen shots displaying the output that the Checkv4.exe utility produces. For more information, see [Using the Checkv4.exe Utility](using-the-checkv4-exe-utility-2.md).

The programming areas addressed by this guide are:

-   [Changing Data Structures for IPv6 Winsock Appications](changing-data-structures-2.md)
-   [Function Calls for IPv6 Winsock Applications](function-calls-2.md)
-   [Use of Hardcoded IPv4 Addresses](use-of-hardcoded-ipv4-addresses-2.md)
-   [User Interface Issues for IPv6 Winsock Applications](user-interface-issues-2.md)
-   [Underlying Protocols for IPv6 Winsock Applications](underlying-protocols-2.md)
-   [Dual-Stack Sockets for IPv6 Winsock Applications](dual-stack-sockets.md)

Because there is no uniform sequence of events, the sections that address IPv6-enabling issues are not arranged in a sequentially significant manner, so you can reference any section at any time. It is strongly recommended that you review each section while adding IPv6 capability to your application. It is also advisable to read about the Checkv4.exe utility, as it includes tips on the order in which to address IPv6-enabling issues.

To look at the Checkv4.exe utility, and to review the order in which you should approach the porting process in your applications, see [Using the Checkv4.exe Utility](using-the-checkv4-exe-utility-2.md). This section includes information on a compile-time flag that strictly checks for programming elements incompatible with IPv6.

To go straight to the sample application, see [Appendix A: IPv4-only Source Code](appendix-a-ipv4-only-source-code-2.md) and [Appendix B: IP-version Agnostic Source Code](appendix-b-ip-version-agnostic-source-code-2.md).

## Related topics

<dl> <dt>

[Internet Protocol Version 6 (IPv6)](internet-protocol-version-6-ipv6-2.md)
</dt> <dt>

[IPv6 Support](ipv6-support-2.md)
</dt> <dt>

[IPv6 Technology Preview for Windows 2000](https://www.microsoft.com/downloads/details.aspx?FamilyID=27b1e6a6-bbdd-43c9-af57-dae19795a088)
</dt> <dt>

[Using the Checkv4.exe Utility](using-the-checkv4-exe-utility-2.md)
</dt> <dt>

[Appendix A: IPv4-only Source Code](appendix-a-ipv4-only-source-code-2.md)
</dt> <dt>

[Appendix B: IP-version Agnostic Source Code](appendix-b-ip-version-agnostic-source-code-2.md)
</dt> </dl>

 

 



