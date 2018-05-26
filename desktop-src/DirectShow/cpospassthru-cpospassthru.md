---
Description: Constructor method.
ms.assetid: b258401c-158b-4eb8-8736-1e1ad9a8403a
title: CPosPassThru.CPosPassThru constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPosPassThru.CPosPassThru constructor

Constructor method.

## Syntax


```C++
CPosPassThru(
   const TCHAR     *pName,
         LPUNKNOWN pUnk,
         HRESULT   *phr,
         IPin      *pPin,
                   
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to the name of the object, for debugging purposes. Allocate this parameter in static memory.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. Ignored.

</dd> <dt>

*pPin* 
</dt> <dd>

Pointer to the [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) interface of the filter's input pin.

</dd> <dt>

 
</dt> <dd></dd> </dl>

 

 



