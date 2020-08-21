---
title: ProxyStubClsid32
description: Maps an IID to a CLSID in 32-bit proxy DLLs.
ms.assetid: 8d63d2b1-c8ba-4fe8-8025-e7ceee422ee7
keywords:
- ProxyStubClsid32 registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# ProxyStubClsid32

Maps an IID to a CLSID in 32-bit proxy DLLs.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Interface
   {IID}
      ProxyStubClsid32 = {CLSID}
```

## Remarks

This is a **REG\_SZ** value that specifies the CLSID for the IID.

This is a required entry since the IID-to-CLSID mapping may be different for 16-bit and 32-bit interfaces. The IID-to-CLSID mapping depends on the way the interface proxies are packaged into a set of proxy DLLs.

If you add interfaces, you must use this entry to register them (32-bit systems) so that OLE can find the appropriate remoting code to establish interprocess communication.

## Related topics

<dl> <dt>

[**IMarshal**](/windows/win32/api/objidlbase/nn-objidlbase-imarshal)
</dt> <dt>

[**Interface**](interface-key.md)
</dt> <dt>

[**ProxyStubClsid**](proxystubclsid.md)
</dt> </dl>

 

 