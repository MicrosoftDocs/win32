---
title: WebhitsDisplayScript
description: WebhitsDisplayScript
ms.assetid: 2416b593-94f8-47dc-bd7c-912cf641ca84
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WebhitsDisplayScript

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **WebhitsDisplayScript** entry determines whether scripting code is returned in hit-highlighting results when a query searches a virtual directory that has read access and contains script files.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Default: | 1              |
| Range:   | 0, 1, 2        |



 

### Remarks

Setting the value of the **WebhitsDisplayScript** entry to zero directs the system not to return hit highlights. Setting the value of this entry to one specifies the display only of those files written in scripts with recognized filters. For example, the HTML filter allows hit highlights to be displayed for .asp files. No content is displayed for script files written in Perl.

Setting the value of this entry to two specifies the return of hit highlights for all scripts searched. Only the HTML portion of a script file is returned, and the raw code remains unavailable to hit-highlighting.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




