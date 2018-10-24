---
Description: This topic provides information about security considerations related to GDI. This topic does not provide all you need to know about security issues. Instead, use it as a starting point and reference for this technology area.
ms.assetid: 374e3ac7-f635-47f1-a72a-14e1be85c795
title: 'Security Considerations: GDI'
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Security Considerations: GDI

This topic provides information about security considerations related to GDI. This topic does not provide all you need to know about security issues. Instead, use it as a starting point and reference for this technology area.

GDI generally has few security concerns because it deals with display rather than input. However, here are a few issues that you should consider.

Bitmaps, metafiles, and fonts are complex structures that could become corrupted. It is good practice to try to ensure that these items are uncorrupted and from a trustworthy source.

An application can specify the security descriptor for some of the printing and spooling APIs. You should take care when setting the security descriptor.

## Related topics

<dl> <dt>

[Microsoft Security Central](http://www.microsoft.com/security/)
</dt> <dt>

[Security Developer Center](http://msdn.microsoft.com/en-us/security/default.aspx)
</dt> <dt>

[Security TechCenter](http://technet.microsoft.com/en-us/security/default.aspx)
</dt> </dl>

 

 



