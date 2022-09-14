---
title: International text and font guidance
description: International text and font guidance
ms.assetid: 0540C9AD-8774-4F0F-B013-48C3EAE59BF2
ms.topic: article
ms.date: 05/31/2018
---

# International text and font guidance

## Affected Platforms

<dl> Clients - Windows 8 \| Windows 8.1  
Servers - Windows Server 2012 \| Windows Server 2012 R2  
</dl>

## Description

Since before Windows 2000, text-display support for new scripts has been added in each major release of Windows. You can find descriptions of the changes made in each major release in the [Script and Font Support for Windows](https://msdn.microsoft.com/goglobal/bb688099.aspx) article at the [Go Global Development Center](https://msdn.microsoft.com/goglobal/default).

Note that support for a script may require certain changes to text stack components as well as changes to fonts. The Windows operating system has many text stack components: DirectWrite, GDI, Uniscribe, GDI+, WPF, RichEdit, ComCtl32, and others. The information provided pertains primarily to GDI and DirectWrite. It is also generally applicable to UI frameworks such as RichEdit or the MSHTML rendering agent used for Windows 8 Store apps and for rendering web content, though those components may exhibit certain differences.

## Best Practices

**Typography guidance for developers**

Typography is at the heart of the Microsoft design language. Each of the Microsoft design principles reinforces the importance of typography. For the first time, app developers have a set of frameworks that support advanced typographic features. Go to [Displaying and editing text](/previous-versions/windows/apps/hh465442(v=win.10)) for information about how to use JavaScript and HTML to display and edit text in Windows Store apps.

**Font metrics**

Font metrics are an area of particular importance to application developers. Font files contain various values related to vertical and horizontal metrics. These values are documented in the [OpenType specification](https://www.microsoft.com/typography/otspec/) and these are exposed via a variety of APIs found at [DWRITE\_FONT\_METRICS structure](/windows/win32/api/dwrite/ns-dwrite-dwrite_font_metrics) and at [TEXTMETRIC Structure](/windows/win32/api/wingdi/ns-wingdi-textmetrica).

## Resources

-   [Script and Font Support for Windows](https://msdn.microsoft.com/goglobal/bb688099.aspx)
-   [Go Global Development Center](https://msdn.microsoft.com/goglobal/default)
-   [Displaying and editing text](/previous-versions/windows/apps/hh465442(v=win.10))
-   [OpenType specification](https://www.microsoft.com/typography/otspec/)
-   [DWRITE\_FONT\_METRICS structure](/windows/win32/api/dwrite/ns-dwrite-dwrite_font_metrics)
-   [TEXTMETRIC Structure](/windows/win32/api/wingdi/ns-wingdi-textmetrica)

 

 