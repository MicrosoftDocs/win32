---
title: ISAPIHTXErrorFile
description: ISAPIHTXErrorFile
ms.assetid: 1e1e80a9-18e3-4eed-854a-4d6eee51a563
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISAPIHTXErrorFile

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ISAPIHTXErrorFile** entry specifies the full virtual path to the HTML error template returned in response to errors in the .htx file.

### Summary



|          |             |
|----------|-------------|
| Type:    | **REG\_SZ** |
| Default: | ""          |



 

### Remarks

If a value for the **ISAPIHTXErrorFile** entry is not specified, the error page specified by the value of the [ISAPIDefaultErrorFile](isapidefaulterrorfile.md) entry is used.

The variables [CiRestriction](variables-in-forms-and-in-idq-files.md#-idxs-cirestriction-var), [CiErrorMessage](read-only-variables-available-in-htx-files.md#-idxs-cierrormessage-var), and [CiErrorNumber](read-only-variables-available-in-htx-files.md#-idxs-cierrornumber-var) can all be referenced.

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[ISAPIDefaultErrorFile](isapidefaulterrorfile.md)
</dt> <dt>

[Language-Specific Registry Entries](language-specific-registry-entries.md)
</dt> </dl>

 

 




