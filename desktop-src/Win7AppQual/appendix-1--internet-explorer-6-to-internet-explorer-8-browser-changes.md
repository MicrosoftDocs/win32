---
description: The following table describes changes between Microsoft Internet Explorer 6 and Windows Internet Explorer 8.
ms.assetid: 5A7DDFC4-69A4-4B5A-9C0A-6172E2142494
title: IE 8 browser changes
ms.topic: article
ms.date: 05/31/2018
---

# Appendix 1: Internet Explorer 6 to Internet Explorer 8 browser changes

The following table describes changes between Microsoft Internet Explorer 6 and Windows Internet Explorer 8.



Design changes from Internet Explorer 6 to Internet Explorer 7

Design changes from Internet Explorer 7 to Internet Explorer 8

${ROWSPAN2}$Internet Explorer versioning${REMOVE}$  

Check for code that incorrectly special cases around Internet Explorer 6, Windows Internet Explorer 7, or Internet Explorer 8 through [user-agent string sniffing, versions vectors, or conditional comments](/previous-versions/windows/internet-explorer/ie-developer/compatibility/ms537503(v=vs.85)).

-   When a long User Agent (UA) String encounters a server that accepts only shorter UA Strings, users see [an error page](https://www.enhanceie.com/ua.aspx).

<!-- -->

-   The Compatibility View in Internet Explorer 8, which is turned on by default for intranet sites, sends a Internet Explorer 7 user agent string. To differentiate between Internet Explorer 7 and Compatibility View, look for the new [Trident token](/archive/blogs/ie/).

${ROWSPAN3}$ Standards compliance updates

-   Applies to [specified document modes](/previous-versions/windows/internet-explorer/ie-developer/compatibility/cc288325(v=vs.85)).
-   [Internet Explorer 8 Compatibility View mode](/archive/blogs/ie/), which is on by default for intranet sites, typically [reverts standards updates from Internet Explorer 7 to Internet Explorer 8](/archive/blogs/ie/site-compatibility-and-ie8).
-   Use the [EmulateIE7 X-UA-Compatible](https://msdn.microsoft.com/library/Cc843977(v=VS.85).aspx) HTTP header or **meta** element to enable Compatibility View on websites or specific webpages.

${REMOVE}$  

Quirks mode exception: You do not need to make standards compliance changes for webpages that specify the quirks mode DOCTYPE (by setting the “standards-compliance” DOCTYPE switch to “off”).

Applies to Internet Explorer 7 Standards or “Strict” mode and above:

-   [XML prologs](/previous-versions/windows/internet-explorer/ie-developer/) in the first line of the source code no longer cause DOCTYPE declarations to fail.
-   [Box model](/previous-versions/windows/internet-explorer/ie-developer/) overflow content intersects box and no longer automatically -grows the box div to fit the content.
-   [Certain CSS filters](/previous-versions/windows/internet-explorer/ie-developer/) (for example, \*HTML, \_underscore, and /\*\*/ comment) are not supported.
-   [Only the outermost OBJECT element in nested objects](/previous-versions/windows/internet-explorer/ie-developer/) is instantiated .
-   [Applications that rely on the SELECT element](/previous-versions/windows/internet-explorer/ie-developer/) to get an HWND to use with Microsoft Win32 APIs might break because the [SELECT element](/archive/blogs/ie/) is now a windowless control.
-   [Channel Definition Format (CDF)](/previous-versions/aa740486(v=msdn.10)) is not supported, in favor of RSS feeds.
-   [XBM](/previous-versions/aa740486(v=msdn.10)), an imaging format that is designed for X-based systems, is not supported.
-   [BASE tags](/previous-versions/aa740486(v=msdn.10)) outside of the HEAD document are not allowed.

Applies to Internet Explorer 8 Standards mode and above:

-   [Unclosed P elements](https://msdn.microsoft.com/library/Cc843977(v=VS.85).aspx) are automatically closed when they are followed by [**TABLE**](https://msdn.microsoft.com/library/ms535901(v=VS.85).aspx), [**FORM**](https://msdn.microsoft.com/library/ms535249(v=VS.85).aspx), [**NOFRAMES**](https://msdn.microsoft.com/library/ms535857(v=VS.85).aspx), or [**NOSCRIPT**](https://msdn.microsoft.com/library/ms535858(v=VS.85).aspx) elements.
-   [Malformed HTML](/archive/blogs/ie/site-compatibility-and-ie8) is not supported, in favor of well-formed, valid markup.
-   The ["className" attribute](/archive/blogs/ie/site-compatibility-and-ie8) syntax is not supported, in favor of “class” syntax.
-   [The attributes collection](/archive/blogs/ie/site-compatibility-and-ie8) does not contain all possible attributes that Windows Internet Explorer recognizes.
-   [Attribute ordering has changed](/archive/blogs/ie/site-compatibility-and-ie8), affecting attributes collection, innerHTML, and outerHTML.
-   [GetElementById](/archive/blogs/ie/site-compatibility-and-ie8) is case-sensitive and does not search name attributes.
-   [Generic CSS prefix selectors](/archive/blogs/ie/site-compatibility-and-ie8) (that is, v\\:\* syntax) are not supported, in favor of explicit tag names.
-   [CSS expressions](/archive/blogs/ie/site-compatibility-and-ie8) are not supported, in favor of improved CSS support or DHTML logic.
-   Code that is intended for custom JSON object methods might conflict with the [new native JSON object](/archive/blogs/ie/site-compatibility-and-ie8) in Internet Explorer 8.
-   [Unset initial properties](/archive/blogs/ie/site-compatibility-and-ie8) on the currentStyle object return their initial value.
-   [Unspecified properties values](/archive/blogs/ie/site-compatibility-and-ie8) on the currentStyle object style object return an empty string (for example, see the [ASP.NET Menu and IE8 rendering white issue](/archive/blogs/giorgio/) blog post).

<!-- -->

-   For sites and applications where accessibility is a concern, update [ARIA syntax across all Internet Explorer rendering modes](/archive/blogs/ie/).
-   Check the [complete list of CSS updates from Internet Explorer 6 to Internet Explorer 8](https://msdn.microsoft.com/library/Cc843977(v=VS.85).aspx).

Security improvements

-   Apply regardless of document mode.
-   You can turn off security features by using [Group Policy](https://www.microsoft.com/p/group-policy/9wzdncrfjtm4?activetab=pivot:overviewtab).

<!-- -->

-   The [window.opener](/previous-versions/aa740486(v=msdn.10)) bypass to the window.close prompt is not allowed.
-   [Object caching protection](/previous-versions/windows/internet-explorer/ie-developer/) is enabled by default, which blocks access to references of objects when users browse to a new domain (applies to Internet Explorer 6 and later versions on Windows XP with Service Pack 2 (SP2) and later versions).
-   [DHTML scriptlets](/previous-versions/windows/internet-explorer/ie-developer/) are disabled by default.
-   [Scripts that write to the status bar](/previous-versions/windows/internet-explorer/ie-developer/) are blocked.
-   [URL creation might fail](/previous-versions/windows/internet-explorer/ie-developer/) if URLs do not meet RFC guidelines.
-   [HTTPS pages display an error page](/previous-versions/windows/internet-explorer/ie-developer/) if the site is configured to SSLv2 only, or if the site security certificate is outdated or invalid, has errors, or has weak ciphers.
-   Only ["Punycode" encoded internationalized domain names](/previous-versions/windows/internet-explorer/ie-developer/) are supported. Other formats like ANSI and UTF-8 are blocked.
-   [Cross-domain script URLs](/previous-versions/windows/internet-explorer/ie-developer/), redirected navigation in DOM objects, and frame navigations are blocked.
-   [Modal or modeless dialog boxes](/previous-versions/aa740486(v=msdn.10)) that are created from script might seem [slightly bigger](/archive/blogs/ie/).
-   [Unsecure protocols](/previous-versions/aa740486(v=msdn.10)) view-source, Gopher (at the WinINET level), and Telnet do not work.

<!-- -->

-   [XSS filter](/archive/blogs/ie/) is on by default, which blocks script patterns that most frequently resemble Type-1 XSS attacks, unless you disable them through a X-XSS-Protection HTTP header.
-   Cross-domain, cross-document communication hacks like [SCRIPT SRC](/archive/blogs/jscript/) are not supported, in favor of safer [XDM and XDR AJAX features](/archive/blogs/ie/).
-   AJAX-enabled sites that [manually manipulate the hash of the URL](/previous-versions//cc891506(v=vs.85)) might be broken by the new window.location.hash navigation property.
-   [New AJAX features](https://msdn.microsoft.com/library/Gg598940(v=VS.85).aspx) like [XDM](/archive/blogs/ie/) have [**native properties**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/cc288548(v=vs.85)) that might conflict with existing custom properties.
-   [File upload control](/archive/blogs/ie/) submits only the file path, not the full path, to the server.
-   HTML code or script that is delivered with an ["image/\*" MIME type](/archive/blogs/ie/) is blocked from executing.
-   [Navigating a top-level frame](/previous-versions/windows/internet-explorer/ie-developer/compatibility/dd565638(v=vs.85)) to a site in a different security context opens a new window or tab instead of navigating within the existing frame.
-   [UTF-7 encoded script](/previous-versions/windows/internet-explorer/ie-developer/compatibility/dd565635(v=vs.85)) is forced into Windows-1252 encoding, which might cause plain text rendering.
-   [HTTP/HTTPS "mixed mode" pages](/archive/blogs/askie/mixed-content-and-internet-explorer-8-0) display a dialog box that defaults to displaying secure items only (versus the previous nonsecure default). Users might mistakenly [choose to block HTTP elements](/archive/blogs/askie/mixed-content-and-internet-explorer-8-0), like key images.
-   [DEP/NX is on by default](https://www.microsoft.com/windows/internet-explorer/readiness/developers-existing.aspx#depnx), which blocks certain add-ons (that is, ActiveX controls and COM objects) that are built by using older versions of ATL from running code that is marked "non-executable" in memory.
-   [Content that is returned by a web proxy](/previous-versions/windows/internet-explorer/ie-developer/compatibility/dd565641(v=vs.85)) is blocked if an SSL tunnel is not established in response to a CONNECT request to the original server.

Architectural changes

-   Apply regardless of document or compatibility mode.

<!-- -->

-   [Protected Mode](/previous-versions/windows/internet-explorer/ie-developer/) is enabled by default for [Internet, Intranet, and Restricted Sites zones](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537187(v=vs.85)). This mode [blocks browser extensions that could pose a security risk](/previous-versions/windows/internet-explorer/ie-developer/compatibility/dd565645(v=vs.85)) from running and [lower privilege applications from accessing higher privilege processes](/previous-versions/windows/internet-explorer/ie-developer/compatibility/dd565646(v=vs.85)), like the Start menu, Control Panel, and the Microsoft Windows registry (applies to Internet Explorer 7 and later versions on Windows Vista and later versions).

<!-- -->

-   [Protected Mode Update](/previous-versions/windows/internet-explorer/ie-developer/compatibility/dd565648(v=vs.85)): Intranet runs in medium (instead of low) integrity level by default.
-   [Loosely Coupled Internet Explorer](https://www.microsoft.com/windows/internet-explorer/readiness/developers-existing.aspx#lcie) might block add-ons (that is, ActiveX controls and COM objects) that do one of the following:
    -   Use windows hierarchy techniques to locate UI frame and tab windows (which now run in separate processes at different integrity levels).
    -   Create a subclass of the UI frame (now at medium integrity level) from a low-integrity tab process.
    -   Use unsupported messaging techniques between UI frame and tabs.



 

## Related topics

<dl> <dt>

[Addressing Application Compatibility When Migrating to Internet Explorer 8](addressing-application-compatibility-when-migrating-to-internet-explorer-8.md)
</dt> </dl>

 

 
