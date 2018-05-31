---
title: DBPROPSET\_MSIDXS\_ROWSETEXT
description: DBPROPSET\_MSIDXS\_ROWSETEXT
ms.assetid: dd8d22ab-fd63-43ff-ac96-6077bc0f37f6
keywords:
- DBPROPSET_MSIDXS_ROWSETEXT
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBPROPSET\_MSIDXS\_ROWSETEXT

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The DBPROPSET\_MSIDXS\_ROWSETEXT property set extends properties defined for the OLE DB [**Rowset**](3d41e965-292d-405d-a67c-9278f64f97aa) object.

``` syntax
#define DBPROPSET_MSIDXS_ROWSETEXT \
    { 0xaa6ee6b0, 0xe828, 0x11d0, \
        { 0xb2, 0x3e, 0x00, 0xaa, 0x00, 0x47, 0xfc, 0x01 } }
```

### Remarks

The DBPROPSET\_MSIDXS\_ROWSETEXT property set contains the following property constants:

<dl> <dt>

<span id="MSIDXSPROP_ROWSETQUERYSTATUS"></span><span id="msidxsprop_rowsetquerystatus"></span>MSIDXSPROP\_ROWSETQUERYSTATUS
</dt> <dd>

Property ID 2. Query status for the rowset. The [**STAT\_\***](stat-constants.md) constants indicate the execution and reliability status.

</dd> <dt>

<span id="MSIDXSPROP_COMMAND_LOCALE_STRING"></span><span id="msidxsprop_command_locale_string"></span>MSIDXSPROP\_COMMAND\_LOCALE\_STRING
</dt> <dd>

Property ID 3. Locale string that represents the language and locale setting to use for this rowset.

</dd> <dt>

<span id="MSIDXSPROP_QUERY_RESTRICTION"></span><span id="msidxsprop_query_restriction"></span>MSIDXSPROP\_QUERY\_RESTRICTION
</dt> <dd>

Property ID 4. The query string associated with this rowset.

</dd> </dl>

## Related topics

<dl> <dt>

[OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md)
</dt> <dt>

[**Rowset**](3d41e965-292d-405d-a67c-9278f64f97aa)
</dt> </dl>

 

 




