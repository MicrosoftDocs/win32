---
title: TreatAs
description: Specifies the CLSID of a class that can emulate the current class.
ms.assetid: '1d7a1677-738a-4258-9afc-e77bd0dcf40f'
keywords:
- TreatAs registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# TreatAs

Specifies the CLSID of a class that can emulate the current class.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      TreatAs = {CLSID_TreatAs}
```

## Remarks

This is a **REG\_SZ** value.

Emulation is the ability of one application to open and edit an object of a different class, while retaining the original format of the object. Resolution occurs on the local computer, so in remote activation case, resolution occurs on the client computer using the CLSID specified by **TreatAs**.

DCOM looks at the local registry for **TreatAs**, even if you call the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) function and specify a remote server. This means that if you have a **TreatAs** entry for Class1 to be treated as Class2 on your local computer, but you call **CoCreateInstance** to create an instance of Class1 and you specify a remote server, DCOM will try to create an instance of Class2 on the remote server, even if Class2 is not registered on the remote server, which will cause the call to **CoCreateInstance** to fail.

## Related topics

<dl> <dt>

[**AutoTreatAs**](autotreatas.md)
</dt> <dt>

[**CoGetTreatAsClass**](/windows/desktop/api/combaseapi/nf-combaseapi-cogettreatasclass)
</dt> <dt>

[**CoTreatAsClass**](/windows/desktop/api/Objbase/nf-objbase-cotreatasclass)
</dt> </dl>

 

 




