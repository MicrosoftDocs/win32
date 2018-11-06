---
title: ProxyStubClsid
description: Maps an IID to a CLSID in 16-bit proxy DLLs.
ms.assetid: 07e1e9de-e529-496c-b9f7-e7f799089f02
keywords:
- ProxyStubClsid registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# ProxyStubClsid

Maps an IID to a CLSID in 16-bit proxy DLLs.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Interface
   {IID}
      ProxyStubClsid = {CLSID}
```

## Remarks

This is a **REG\_SZ** value that specifies the CLSID for the IID.

If you add interfaces, you must use this entry to register them (16-bit systems) so that OLE can find the appropriate remoting code to establish interprocess communication.

## Related topics

<dl> <dt>

[**Interface**](interface-key.md)
</dt> <dt>

[**ProxyStubClsid32**](proxystubclsid32.md)
</dt> </dl>

 

 




