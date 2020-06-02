---
Description: The following table describes changes between Microsoft Internet Explorer 6 and Windows Internet Explorer 8.
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

Check for code that incorrectly special cases around Internet Explorer 6, Windows Internet Explorer 7, or Internet Explorer 8 through [user-agent string sniffing, versions vectors, or conditional comments](https://msdn.microsoft.com/library/ms537503(v=VS.85).aspx).

-   When a long User Agent (UA) String encounters a server that accepts only shorter UA Strings, users see [an error page](https://www.enhanceie.com/ua.aspx).

<!-- -->

-   The Compatibility View in Internet Explorer 8, which is turned on by default for intranet sites, sends a Internet Explorer 7 user agent string. To differentiate between Internet Explorer 7 and Compatibility View, look for the new [Trident token](https://blogs.msdn.com/ie/archive/2009/01/09/the-internet-explorer-8-user-agent-string-updated-edition.aspx).

${ROWSPAN3}$ Standards compliance updates

-   Applies to [specified document modes](https://msdn.microsoft.com/library/Cc288325(v=VS.85).aspx).
-   [Internet Explorer 8 Compatibility View mode](https://blogs.msdn.com/ie/archive/2008/08/27/introducing-compatibility-view.aspx), which is on by default for intranet sites, typically [reverts standards updates from Internet Explorer 7 to Internet Explorer 8](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx).
-   Use the [EmulateIE7 X-UA-Compatible](https://msdn.microsoft.com/library/Cc843977(v=VS.85).aspx) HTTP header or **meta** element to enable Compatibility View on websites or specific webpages.

${REMOVE}$  

Quirks mode exception: You do not need to make standards compliance changes for webpages that specify the quirks mode DOCTYPE (by setting the “standards-compliance” DOCTYPE switch to “off”).

Applies to Internet Explorer 7 Standards or “Strict” mode and above:

-   [XML prologs](https://msdn.microsoft.com/library/Bb250496(v=VS.85).aspx) in the first line of the source code no longer cause DOCTYPE declarations to fail.
-   [Box model](https://msdn.microsoft.com/library/Bb250496(v=VS.85).aspx) overflow content intersects box and no longer automatically -grows the box div to fit the content.
-   [Certain CSS filters](https://msdn.microsoft.com/library/Bb250496(v=VS.85).aspx) (for example, \*HTML, \_underscore, and /\*\*/ comment) are not supported.
-   [Only the outermost OBJECT element in nested objects](https://msdn.microsoft.com/library/ms649487(v=VS.85).aspx) is instantiated .
-   [Applications that rely on the SELECT element](https://msdn.microsoft.com/library/ms649487(v=VS.85).aspx) to get an HWND to use with Microsoft Win32 APIs might break because the [SELECT element](https://blogs.msdn.com/ie/archive/2006/01/17/514076.aspx) is now a windowless control.
-   [Channel Definition Format (CDF)](https://msdn.microsoft.com/ie/aa740486.aspx) is not supported, in favor of RSS feeds.
-   [XBM](https://msdn.microsoft.com/ie/aa740486.aspx), an imaging format that is designed for X-based systems, is not supported.
-   [BASE tags](https://msdn.microsoft.com/ie/aa740486.aspx) outside of the HEAD document are not allowed.

Applies to Internet Explorer 8 Standards mode and above:

-   [Unclosed P elements](https://msdn.microsoft.com/library/Cc843977(v=VS.85).aspx) are automatically closed when they are followed by [**TABLE**](https://msdn.microsoft.com/library/ms535901(v=VS.85).aspx), [**FORM**](https://msdn.microsoft.com/library/ms535249(v=VS.85).aspx), [**NOFRAMES**](https://msdn.microsoft.com/library/ms535857(v=VS.85).aspx), or [**NOSCRIPT**](https://msdn.microsoft.com/library/ms535858(v=VS.85).aspx) elements.
-   [Malformed HTML](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx) is not supported, in favor of well-formed, valid markup.
-   The ["className" attribute](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx) syntax is not supported, in favor of “class” syntax.
-   [The attributes collection](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx) does not contain all possible attributes that Windows Internet Explorer recognizes.
-   [Attribute ordering has changed](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx), affecting attributes collection, innerHTML, and outerHTML.
-   [GetElementById](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx) is case-sensitive and does not search name attributes.
-   [Generic CSS prefix selectors](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx) (that is, v\\:\* syntax) are not supported, in favor of explicit tag names.
-   [CSS expressions](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx) are not supported, in favor of improved CSS support or DHTML logic.
-   Code that is intended for custom JSON object methods might conflict with the [new native JSON object](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx) in Internet Explorer 8.
-   [Unset initial properties](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx) on the currentStyle object return their initial value.
-   [Unspecified properties values](https://blogs.msdn.com/b/ie/archive/2009/03/12/site-compatibility-and-ie8.aspx) on the currentStyle object style object return an empty string (for example, see the [ASP.NET Menu and IE8 rendering white issue](https://blogs.msdn.com/giorgio/archive/2009/02/01/asp-net-menu-and-ie8-rendering-white-issue.aspx) blog post).

<!-- -->

-   For sites and applications where accessibility is a concern, update [ARIA syntax across all Internet Explorer rendering modes](https://blogs.msdn.com/ie/archive/2009/01/16/accessibility-improved-aria-support-in-the-IE8-RC.aspx).
-   Check the [complete list of CSS updates from Internet Explorer 6 to Internet Explorer 8](https://msdn.microsoft.com/library/Cc843977(v=VS.85).aspx).

Security improvements

-   Apply regardless of document mode.
-   You can turn off security features by using [Group Policy](https://www.microsoft.com/p/group-policy/9wzdncrfjtm4?activetab=pivot:overviewtab).

<!-- -->

-   The [window.opener](https://msdn.microsoft.com/ie/aa740486.aspx) bypass to the window.close prompt is not allowed.
-   [Object caching protection](https://msdn.microsoft.com/library/ms649488(v=VS.85).aspx) is enabled by default, which blocks access to references of objects when users browse to a new domain (applies to Internet Explorer 6 and later versions on Windows XP with Service Pack 2 (SP2) and later versions).
-   [DHTML scriptlets](https://msdn.microsoft.com/library/ms649488(v=VS.85).aspx) are disabled by default.
-   [Scripts that write to the status bar](https://msdn.microsoft.com/library/ms649488(v=VS.85).aspx) are blocked.
-   [URL creation might fail](https://msdn.microsoft.com/library/Bb250493(v=VS.85).aspx) if URLs do not meet RFC guidelines.
-   [HTTPS pages display an error page](https://msdn.microsoft.com/library/Bb250503(v=VS.85).aspx) if the site is configured to SSLv2 only, or if the site security certificate is outdated or invalid, has errors, or has weak ciphers.
-   Only ["Punycode" encoded internationalized domain names](https://msdn.microsoft.com/library/Bb250505(v=VS.85).aspx) are supported. Other formats like ANSI and UTF-8 are blocked.
-   [Cross-domain script URLs](https://msdn.microsoft.com/library/Bb250493(v=VS.85).aspx), redirected navigation in DOM objects, and frame navigations are blocked.
-   [Modal or modeless dialog boxes](https://msdn.microsoft.com/ie/aa740486.aspx) that are created from script might seem [slightly bigger](https://blogs.msdn.com/ie/archive/2006/08/25/719355.aspx).
-   [Unsecure protocols](https://msdn.microsoft.com/ie/aa740486.aspx) view-source, Gopher (at the WinINET level), and Telnet do not work.

<!-- -->

-   [XSS filter](https://blogs.msdn.com/ie/archive/2008/07/02/ie8-security-part-iv-the-xss-filter.aspx) is on by default, which blocks script patterns that most frequently resemble Type-1 XSS attacks, unless you disable them through a X-XSS-Protection HTTP header.
-   Cross-domain, cross-document communication hacks like [SCRIPT SRC](https://blogs.msdn.com/jscript/archive/2007/11/29/ecmascript-mashups-and-security.aspx) are not supported, in favor of safer [XDM and XDR AJAX features](https://blogs.msdn.com/ie/archive/2008/07/02/ie8-security-part-v-comprehensive-protection.aspx).
-   AJAX-enabled sites that [manually manipulate the hash of the URL](https://msdn.microsoft.com/library/Cc891506(v=VS.85).aspx) might be broken by the new window.location.hash navigation property.
-   [New AJAX features](https://msdn.microsoft.com/library/Gg598940(v=VS.85).aspx) like [XDM](https://blogs.msdn.com/ie/archive/2008/07/02/ie8-security-part-v-comprehensive-protection.aspx) have [**native properties**](https://msdn.microsoft.com/library/Cc288548(v=VS.85).aspx) that might conflict with existing custom properties.
-   [File upload control](https://blogs.msdn.com/ie/archive/2008/07/02/ie8-security-part-v-comprehensive-protection.aspx) submits only the file path, not the full path, to the server.
-   HTML code or script that is delivered with an ["image/\*" MIME type](https://blogs.msdn.com/ie/archive/2008/07/02/ie8-security-part-v-comprehensive-protection.aspx) is blocked from executing.
-   [Navigating a top-level frame](https://msdn.microsoft.com/library/Dd565638(v=VS.85).aspx) to a site in a different security context opens a new window or tab instead of navigating within the existing frame.
-   [UTF-7 encoded script](https://msdn.microsoft.com/library/Dd565635(v=VS.85).aspx) is forced into Windows-1252 encoding, which might cause plain text rendering.
-   [HTTP/HTTPS "mixed mode" pages](https://blogs.msdn.com/b/askie/archive/2009/05/14/mixed-content-and-internet-explorer-8-0.aspx) display a dialog box that defaults to displaying secure items only (versus the previous nonsecure default). Users might mistakenly [choose to block HTTP elements](https://blogs.msdn.com/b/askie/archive/2009/05/14/mixed-content-and-internet-explorer-8-0.aspx), like key images.
-   [DEP/NX is on by default](https://www.microsoft.com/windows/internet-explorer/readiness/developers-existing.aspx#depnx), which blocks certain add-ons (that is, ActiveX controls and COM objects) that are built by using older versions of ATL from running code that is marked "non-executable" in memory.
-   [Content that is returned by a web proxy](https://msdn.microsoft.com/library/Dd565641(v=VS.85).aspx) is blocked if an SSL tunnel is not established in response to a CONNECT request to the original server.

Architectural changes

-   Apply regardless of document or compatibility mode.

<!-- -->

-   [Protected Mode](https://msdn.microsoft.com/library/bb250462(VS.85).aspx) is enabled by default for [Internet, Intranet, and Restricted Sites zones](https://msdn.microsoft.com/library/ms537187(v=VS.85).aspx). This mode [blocks browser extensions that could pose a security risk](https://msdn.microsoft.com/library/Dd565645(v=VS.85).aspx) from running and [lower privilege applications from accessing higher privilege processes](https://msdn.microsoft.com/library/Dd565646(v=VS.85).aspx), like the Start menu, Control Panel, and the Microsoft Windows registry (applies to Internet Explorer 7 and later versions on Windows Vista and later versions).

<!-- -->

-   [Protected Mode Update](https://msdn.microsoft.com/library/Dd565648(v=VS.85).aspx): Intranet runs in medium (instead of low) integrity level by default.
-   [Loosely Coupled Internet Explorer](https://www.microsoft.com/windows/internet-explorer/readiness/developers-existing.aspx#lcie) might block add-ons (that is, ActiveX controls and COM objects) that do one of the following:
    -   Use windows hierarchy techniques to locate UI frame and tab windows (which now run in separate processes at different integrity levels).
    -   Create a subclass of the UI frame (now at medium integrity level) from a low-integrity tab process.
    -   Use unsupported messaging techniques between UI frame and tabs.



 

## Related topics

<dl> <dt>

[Addressing Application Compatibility When Migrating to Internet Explorer 8](addressing-application-compatibility-when-migrating-to-internet-explorer-8.md)
</dt> </dl>

 

 
