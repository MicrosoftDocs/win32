---
title: International text and font guidance
description: International text and font guidance
ms.assetid: 0540C9AD-8774-4F0F-B013-48C3EAE59BF2
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# International text and font guidance

## Affected Platforms

<dl> Clients - Windows 8 \| Windows 8.1  
Servers - Windows Server 2012 \| Windows Server 2012 R2  
</dl>

## Description

Since before Windows 2000, text-display support for new scripts has been added in each major release of Windows. You can find descriptions of the changes made in each major release in the [Script and Font Support for Windows](http://go.microsoft.com/fwlink/p/?LinkId=325315) article at the [Go Global Development Center](http://go.microsoft.com/fwlink/p/?LinkId=325339).

Note that support for a script may require certain changes to text stack components as well as changes to fonts. The Windows operating system has many text stack components: DirectWrite, GDI, Uniscribe, GDI+, WPF, RichEdit, ComCtl32, and others. The information provided pertains primarily to GDI and DirectWrite. It is also generally applicable to UI frameworks such as RichEdit or the MSHTML rendering agent used for Windows 8 Store apps and for rendering web content, though those components may exhibit certain differences.

## Best Practices

**Typography guidance for developers**

Typography is at the heart of the Microsoft design language. Each of the Microsoft design principles reinforces the importance of typography. For the first time, app developers have a set of frameworks that support advanced typographic features. Go to [Displaying and editing text](http://go.microsoft.com/fwlink/p/?LinkId=325341) for information about how to use JavaScript and HTML to display and edit text in Windows Store apps.

**Font metrics**

Font metrics are an area of particular importance to application developers. Font files contain various values related to vertical and horizontal metrics. These values are documented in the [OpenType specification](http://go.microsoft.com/fwlink/p/?LinkId=325342) and these are exposed via a variety of APIs found at [DWRITE\_FONT\_METRICS structure](http://go.microsoft.com/fwlink/p/?LinkId=325343) and at [TEXTMETRIC Structure](http://go.microsoft.com/fwlink/p/?LinkId=325344).

## Resources

-   [Script and Font Support for Windows](http://go.microsoft.com/fwlink/p/?LinkId=325315)
-   [Go Global Development Center](http://go.microsoft.com/fwlink/p/?LinkId=325339)
-   [Displaying and editing text](http://go.microsoft.com/fwlink/p/?LinkId=325341)
-   [OpenType specification](http://go.microsoft.com/fwlink/p/?LinkId=325342)
-   [DWRITE\_FONT\_METRICS structure](http://go.microsoft.com/fwlink/p/?LinkId=325343)
-   [TEXTMETRIC Structure](http://go.microsoft.com/fwlink/p/?LinkId=325344)

 

 




