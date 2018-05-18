---
title: DefaultColumnFile
description: DefaultColumnFile
ms.assetid: '96326766-d661-4d7f-aea6-23421b0f608e'
---

# DefaultColumnFile

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DefaultColumnFile** entry is the full physical path and name of the file to read for column definitions in .asp files and in .idq files.

### Summary



|          |             |
|----------|-------------|
| Type:    | **REG\_SZ** |
| Default: | ""          |



 

### Remarks

The DefaultColumnFile entry is found under the key

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\ContentIndexCommon**.

If the value of the **DefaultColumnFile** entry is the default, the columns (properties) available for queries are those given in the topic [Default Property Names for a Web Catalog](default-property-names-for-a-web-catalog.md).

If a value other than the default is specified, the specified column definitions file includes one line for each column (or property) that can be used in a query. The content and format of the columns definition file is identical to that given in the topic [Names Section of .Idq Files](names-section-of-idq-files.md).

The value of an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog cannot override the value of this entry.

## Related topics

<dl> <dt>

[Main Registry Entries](main-registry-entries.md)
</dt> </dl>

 

 




