---
description: What Is Compatibility View?
ms.assetid: 1EAC5799-7943-40AB-A67E-F6D6888C4B7D
title: What Is Compatibility View?
ms.topic: article
ms.date: 05/31/2018
---

# What Is Compatibility View?

*Compatibility View* is a feature of Windows Internet Explorer 8 that enables the browser to render a webpage nearly identically to the way that Windows Internet Explorer 7 would render it.

In Internet Explorer 8, Compatibility View changes how the browser interprets code that is written in CSS, HTML, and the Document Object Model (DOM) to try to match Internet Explorer 7. A site that a user views in Internet Explorer 8 Compatibility View is almost identical to a site that the user views in Internet Explorer 7. However, Compatibility View does not change how the browser interprets all code. For example, the changes in Internet Explorer 8 for how the browser handles ActiveX, the parser, AJAX, JavaScript, networking, and security might still cause compatibility issues. Compatibility View does not change these behaviors.

In an enterprise environment, some areas have lower risk for compatibility issues. For example, Intranet Zone websites use Compatibility View by default. Client web applications that render by using the Web Browser Control, or the WebOC (Internet Explorer rendering engine), also have a low risk for compatibility issues because Internet Explorer 8 defaults to a compatibility mode for the WebOC. However, the default configuration settings for Compatibility View might not ensure complete compatibility. To determine if a website or web application is compatible with Internet Explorer 8, you should test the website or web application.

For more information about the differences between Internet Explorer 8 Compatibility View and Internet Explorer 7, see the [Site Compatibility and Internet Explorer 8 blog](/archive/blogs/ie/site-compatibility-and-ie8). For a list of what to check when you upgrade to Internet Explorer 8, see the [Internet Explorer 8 Readiness Toolkit](https://www.microsoft.com/windows/internet-explorer/readiness/developers.aspx).

For more information about Compatibility View, see the [Internet Explorer Team Blog](/archive/blogs/ie/).

## Related topics

<dl> <dt>

[Fixing Compatibility Issues in Web Applications by Using Compatibility View](remediating-web-applications-and-add-ons.md)
</dt> </dl>

 

 
