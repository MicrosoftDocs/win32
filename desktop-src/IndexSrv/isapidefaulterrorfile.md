---
title: ISAPIDefaultErrorFile
description: ISAPIDefaultErrorFile
ms.assetid: a540d7d2-a238-4bbd-b0f7-d56c902a2db1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISAPIDefaultErrorFile

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ISAPIDefaultErrorFile** entry specifies the full virtual path to the generic error template.

### Summary



|          |             |
|----------|-------------|
| Type:    | **REG\_SZ** |
| Default: | ""          |



 

### Remarks

The value of the **ISAPIDefaultErrorFile** is the .htx template to process when none of the specific HTML error pages ([ISAPIHTXErrorfile](isapihtxerrorfile.md), [ISAPIIDQErrorFile](isapiidqerrorfile.md), [ISAPIRestrictionErrorFile](isapirestrictionerrorfile.md)) apply.

If a value for this entry is not specified, a generic error page is used.

The variables [CiRestriction](https://www.bing.com/search?q=CiRestriction), [CiErrorMessage](https://www.bing.com/search?q=CiErrorMessage), and [CiErrorNumber](https://www.bing.com/search?q=CiErrorNumber) can all be referenced.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[ISAPIHTXErrorfile](isapihtxerrorfile.md)
</dt> <dt>

[ISAPIIDQErrorFile](isapiidqerrorfile.md)
</dt> <dt>

[ISAPIRestrictionErrorFile](isapirestrictionerrorfile.md)
</dt> <dt>

[Language-Specific Registry Entries](language-specific-registry-entries.md)
</dt> </dl>

 

 




