---
description: The longevity of IPv4 resulted in hard coding many well-known IPv4 addresses, such as loopback addresses (127.x.x.x), integer constants such as INADDR\_LOOPBACK, among others.
ms.assetid: adb39f27-c219-43cd-9e86-b2d3b663c79c
title: Use of Hardcoded IPv4 Addresses
ms.topic: article
ms.date: 05/31/2018
---

# Use of Hardcoded IPv4 Addresses

The longevity of IPv4 resulted in hard coding many well-known IPv4 addresses, such as loopback addresses (127.x.x.x), integer constants such as INADDR\_LOOPBACK, among others. The practice of hard coding these addresses presents obvious problems when modifying and existing application to support IPv6 or creating new IP version-independent programs.

Best Practice

-   The best approach is to avoid hardcoding any addresses.

Code To Avoid

-   Avoid using hardcoded addresses in code.

**To modify your existing code base from IPv4 to IPv4- and IPv6-interoperability**

1.  Acquire the *Checkv4.exe* utility. The *Checkv4.exe* utility is installed as part of the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later. The Windows SDK is available through an MSDN subscription and can also be downloaded from the Microsoft website (https://msdn.microsoft.com).
2.  Run the *Checkv4.exe* utility against your code. Learn about how to run the *Checkv4.exe* utility against your files in the section on [Using the Checkv4.exe Utility](using-the-checkv4-exe-utility-2.md).
3.  The *Checkv4.exe* utility alerts you to the presence of common defines for IPv4 addresses, such as INADDR\_LOOPBACK. Modify any code that uses literal strings with code that is protocol-version agnostic.
4.  Search your code base for other potential literal strings, as appropriate.

The *Checkv4.exe* utility can help you find common literal strings, but there may be others that are specific to your application. You should perform thorough searching and testing to ensure your code base has eradicated potential problems associated with literal strings.

## Related topics

<dl> <dt>

[IPv6 Guide for Windows Sockets Applications](ipv6-guide-for-windows-sockets-applications-2.md)
</dt> <dt>

[Changing Data Structures for IPv6 Winsock Appications](changing-data-structures-2.md)
</dt> <dt>

[Dual-Stack Sockets for IPv6 Winsock Applications](dual-stack-sockets.md)
</dt> <dt>

[Function Calls for IPv6 Winsock Applications](function-calls-2.md)
</dt> <dt>

[User Interface Issues for IPv6 Winsock Applications](user-interface-issues-2.md)
</dt> <dt>

[Underlying Protocols for IPv6 Winsock Applications](underlying-protocols-2.md)
</dt> </dl>

 

 



