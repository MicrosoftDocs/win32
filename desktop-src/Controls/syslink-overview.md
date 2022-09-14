---
title: About SysLink Controls
description: A SysLink control is a window that renders marked-up text, and notifies the application when users click its embedded hyperlinks. This control provides a convenient alternative to using the Command link button. For more information, see Button Types.
ms.assetid: 38cfac3d-de60-4882-a434-4f498330b77d
ms.topic: article
ms.date: 05/31/2018
---

# About SysLink Controls

A SysLink control is a window that renders marked-up text, and notifies the application when users click its embedded hyperlinks. This control provides a convenient alternative to using the [**Command link button**](button-styles.md). For more information, see [Button Types](button-types-and-styles.md).

Each SysLink control can support multiple hyperlinks, and you can access each hyperlink through a zero-based index. The SysLink control is defined in the ComCtl32.dll version 6, and it requires a manifest or directive that specifies that version 6 of the DLL should be used if it is available. For more information, see [Enabling Visual Styles](cookbook-overview.md).

This article contains the following sections.

-   [SysLink Markup](#syslink-markup)
-   [Link Attributes](#link-attributes)
-   [Link States](#link-states)
-   [Limitations on Bidirectional Text Display](#limitations-on-bidirectional-text-display)

## SysLink Markup

The SysLink control supports the anchor tag(&lt;a&gt;) along with the attributes **HREF** and **ID**. An **HREF** can be any protocol, such as http, ftp, and mailto. An **ID** is an optional name, unique within a SysLink control, and it is associated with an individual link. Links are also assigned a zero-based index according to their position within the string. This index is used to access a link.

## Link Attributes

Each link's attributes can be set either within the anchor tag for each link or by sending the [**LM\_SETITEM**](lm-setitem.md) message. Setting an attribute by specifying it within the initialization string merely initializes the value. You can change the value of an attribute through subsequent use of the **LM\_SETITEM** message.

## Link States

Link items can be in any one of three states, represented by the flags in the following table.



| State flag   | Appearance and meaning                                            |
|--------------|-------------------------------------------------------------------|
| LIS\_FOCUSED | The link has the keyboard focus, and pressing Enter activates it. |
| LIS\_ENABLED | The link is enabled.                                              |
| LIS\_VISITED | The user has already visited the URL represented by the link.     |



 

## Limitations on Bidirectional Text Display

Some languages, such as Arabic or Hebrew, are written right-to-left (RTL); English is written left-to-right (LTR). Combining RTL with LTR is called bidirectional text. Mixing LTR and RTL Unicode or HTML directional markup constructs in resource strings, as bidirectional flow markers to control the flow of strings, may not produce the expected result when using a SysLink control. For instance, an LTR-marked sentence may not display correctly in RTL context.

> [!Note]  
> SysLink controls do not support bidirectional display under all scenarios. Use a SysLink control only if you know that a simple LTR or RTL layout is adequate. Otherwise, consider using a more advanced technology such as [MSHTML](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa753630(v=vs.85)).

 

 

 