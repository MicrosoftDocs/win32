---
title: IsapiDateTimeFormatting
description: IsapiDateTimeFormatting
ms.assetid: bce4b128-07e2-4213-8f53-8e435df9292d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IsapiDateTimeFormatting

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IsapiDateTimeFormatting** entry specifies which form of date and time formatting is applied for ISAPI queries.

### Summary



|          |                |
|----------|----------------|
| Type:    | **REG\_DWORD** |
| Default: | 1              |
| Range:   | 0 - 2          |



 

### Remarks

The value of the **IsapiDateTimeFormatting** entry can be one of the following values.



| Value | Formatting                                                                                               |
|-------|----------------------------------------------------------------------------------------------------------|
| 0     | Use the locale of the user issuing the query. This is the default behavior for Index Server 1.x and 2.0. |
| 1     | Use the default locale of the Indexing Service system.                                                   |
| 2     | Use a hard-coded, non-configurable format of the form 1999/12/31 23:59:59.                               |



 

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[IsapiDateTimeLocal](isapidatetimelocal.md)
</dt> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




