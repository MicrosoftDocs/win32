---
title: Attaching to an SDO-Enabled Computer
description: Attaching to an SDO-Enabled Computer
ms.assetid: 434e2e0c-075e-48a9-9617-bbe75716380d
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Attaching to an SDO-Enabled Computer

The following code attaches to the local computer as an SDO computer.


```C++
   HRESULT  hr;
   CComPtr<ISdoMachine> pSdoMachine;
   CLSID    clsid;

   hr = CLSIDFromProgID(TEXT("IAS.SdoMachine"), &clsid);
   if (FAILED(hr))
   {
      return hr;
   }

   hr = CoCreateInstance(
      clsid,
      NULL,
      CLSCTX_INPROC_SERVER,
      __uuidof(ISdoMachine),
      (void**)&pSdoMachine
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Pass NULL to specify local computer.
   //
   hr = pSdoMachine->Attach(NULL); 
   if (FAILED(hr))
   {
      return hr;
   }

```



Attaching to a computer as an SDO computer is the first step in administering the computer through SDO.

For more information, see [**ISdoMachine**](/windows/desktop/api/sdoias/nn-sdoias-isdomachine), [**ISdoMachine::Attach**](/windows/desktop/api/sdoias/nf-sdoias-isdomachine-attach).

 

 