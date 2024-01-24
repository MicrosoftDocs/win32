---
title: Appendix (VML)
description: This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9.
ms.assetid: e18e9388-d8b6-4eee-b4f1-3948830f7986
keywords:
- Web workshop,namespaces
- Web workshop,behavior styles
- designing Web pages,namespaces
- designing Web pages,behavior styles
- Vector Markup Language (VML),namespaces
- VML (Vector Markup Language),namespaces
- vector graphics,namespaces
- Vector Markup Language (VML),behavior styles
- VML (Vector Markup Language),behavior styles
- vector graphics,behavior styles
- VGX.DLL
ms.topic: article
ms.date: 05/31/2018
---

# Appendix (VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

To let the browsers know how to hand off data to a VML-specific processor, you need to type some information such as namespaces and behavior styles. You can then use VML to type graphics in the `<BODY>` region.

In this topic:

-   [Namespaces](#namespaces)
-   [Behavior Styles](#behavior-styles)

## Namespaces

An XML mechanism indicates the namespace that an element comes from. If you switch from parsing in HTML to parsing in XML, this mechanism indicates the switch within HTML.

Ask the vender of your VML processor what information is required for the XML namespace.

If you use Microsoft Internet Explorer to render VML, always type the following line in the `<HTML>` tag:


```HTML
<html xmlns:v="urn:schemas-microsoft-com:vml">
```



This information tells Internet Explorer to switch to namespace "urn:schemas-microsoft-com:vml" when parsing an XML tag with a prefix `v:`, and to hand off the resulting data to the VML processor.

[![back to top](images/top.gif) Back to top](#top)

## Behavior Styles

VML is defined in Microsoft Internet Explorer as a default behavior.

To render VML, always type the following lines in the `<HEAD>` region:


```HTML
<style>
v\:* { behavior: url(#default#VML); display:inline-block}
</style>
```



VML is implemented in Internet Explorer through VGX.DLL. If your initial installation of the browser did not include VML behavior, you may need to add it as an option. You do not need to add an `<object>` tag.

 

 
