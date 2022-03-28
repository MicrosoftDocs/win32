---
description: Introduction (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)
ms.assetid: 6BB5AABC-6281-4575-8189-477C57DF4F4F
title: Introduction (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)
ms.topic: article
ms.date: 05/31/2018
---

# Introduction (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)

Around the world, many companies are adopting Windows 7 because of its enterprise features and abilities. IT departments are also changing how they approach their long-term platform needs to support a modern desktop. The Windows 7 operating system helps lower the total cost of ownership by helping users stay productive anywhere, enhances security and control, and simplifies desktop management across the organization. Windows 7 also includes a standards-based modern browser, Windows Internet Explorer 8, which provides improved security and enhanced browsing capabilities. These two platforms increase IT efficiency and enhance an organization’s agility and security.

However, migrating to a new operating system creates unique challenges, primarily with the need to support legacy web applications. Companies may have applications that are built for previous versions of Windows Internet Explorer, such as Windows Internet Explorer 7 or Microsoft Internet Explorer 6. These web applications may encounter compatibility issues with Internet Explorer 8. Additionally Internet Explorer 6 does not natively run on Windows 7 and Windows does not support running two versions of Internet Explorer simultaneously. For more information, see the Microsoft Knowledge Base article, "Running Multiple Versions of Internet Explorer on Single Operating System is Unsupported."

Many companies still use Internet Explorer 6-based web applications that were built and customized over the past decade. Companies that plan to deploy Windows 7 need to have a comprehensive strategy and an execution plan in place to migrate legacy web applications to Internet Explorer 8. This document provides a detailed overview of Internet Explorer 8 compatibility issues, discusses how to migrate web applications, and introduces related tools and processes.

The Internet Explorer 8 release focused on three major themes:

-   Provide real-world interoperability with other browsers and compatibility for existing websites.
-   Make web development faster and easier by using the built-in developer tools.
-   Enable experiences that reach beyond the page, through new browser features that connect users to innovative web services.

In addition to significant advances in standards support, Internet Explorer 8 contains additional platform investments for developers. Internet Explorer 8 improves performance in many Internet Explorer subsystems, such as the HTML parser, cascading style sheet (CSS) rule processing, markup tree manipulation, the JavaScript parser, garbage collector runtime, and memory management. Additional developer investments include:

-   CSS 2.1: You can write your pages once and have them more easily render properly across different browsers, because Internet Explorer 8 fully supports the CSS 2.1 specification.
-   Document Object Model (DOM) and HTML 4.01 improvements: Internet Explorer 8 provides additional HTML 4.01 improvements and full CSS 2.1 compliance. Internet Explorer 8 also fixes many cross-browser inconsistencies. For example, get/set/remove attribute implementation is now interoperable with other browsers, and performance is improved in asynchronous JavaScript and XML (AJAX) design patterns.
-   Emerging standards: Internet Explorer 8 incorporates future standards, such as W3C’s HTML5 Draft DOM Storage standard, the Web Applications Working Group’s Selectors API, and ECMAScript 3.1 endorsed syntax.
-   New navigation features for AJAX applications: You can update the browser back and forward navigation stack and Address Bar from a AJAX applications so those browser features work correctly in your application.
-   Acid2: Internet Explorer 8 renders the Acid2 browser test correctly.
-   Compatibility: Internet Explorer 8 includes a more standards-compatible layout engine that allows you to build a standards-based site for multiple browsers. To migrate your sites more easily to the new standards-compliant layout engine, Internet Explorer 8 enables you to use the Internet Explorer 7 layout engine by inserting a simple **meta** element into your code or by adding a single HTTP header on your servers.
-   Developer Tools: Developer Tools in Internet Explorer (which you access by pressing the F12 key) enable you to quickly debug HTML, CSS, and JavaScript code in a visual environment. These tools are included directly in Internet Explorer 8 with expanded functionality, including ann option to choose which application to use when you are viewing the source of a webpage. You can quickly identify and resolve issues because of the deep insight that the tool provides into the DOM.
-   For more information about the new and enhanced features of Internet Explorer 8, see [What's New in Internet Explorer 8](https://msdn.microsoft.com/library/Gg598940(v=VS.85).aspx) in the MSDN Library.

## Related topics

<dl> <dt>

[Addressing Application Compatibility When Migrating to Internet Explorer 8](addressing-application-compatibility-when-migrating-to-internet-explorer-8.md)
</dt> </dl>

 

 



