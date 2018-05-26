---
title: DBPROPSET\_CIFRMWRKCORE\_EXT
description: DBPROPSET\_CIFRMWRKCORE\_EXT
ms.assetid: b5c0f263-bd76-4659-8159-978639b4666f
keywords:
- DBPROPSET_CIFRMWRKCORE_EXT
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBPROPSET\_CIFRMWRKCORE\_EXT

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The DBPROPSET\_CIFRMWRKCORE\_EXT property set contains system properties that define the machine name and client CLSID.

``` syntax
#define DBPROPSET_CIFRMWRKCORE_EXT \
    { 0xafafaca5, 0xb5d1, 0x11d0, \
        { 0x8c, 0x62, 0x00, 0xc0, 0x4f, 0xc2, 0xdb, 0x8d } }
```

### Remarks

The DBPROPSET\_CIFRMWRKCORE\_EXT property set contains the following property constants.

<dl> <dt>

<span id="DBPROP_MACHINE"></span><span id="dbprop_machine"></span>DBPROP\_MACHINE
</dt> <dd>

Property ID 2. The computer name running Indexing Service.

</dd> <dt>

<span id="DBPROP_CLIENT_CLSID"></span><span id="dbprop_client_clsid"></span>DBPROP\_CLIENT\_CLSID
</dt> <dd>

Property ID 3. The CLSID of the client querying Indexing Service.

</dd> </dl>

## Related topics

<dl> <dt>

[OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md)
</dt> </dl>

 

 




