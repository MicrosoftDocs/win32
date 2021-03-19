---
description: Constructor method.
ms.assetid: 9b69632b-7932-4a9b-bd68-69b06dd8a5ec
title: CBaseVideoRenderer.CBaseVideoRenderer constructor (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.CBaseVideoRenderer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.CBaseVideoRenderer constructor

Constructor method.

## Syntax


```C++
CBaseVideoRenderer(
   REFCLSID  RenderClass,
   TCHAR     *pName,
   LPUNKNOWN pUnk,
   HRESULT   *phr
);
```



## Parameters

<dl> <dt>

*RenderClass* 
</dt> <dd>

Class identifier for this renderer.

</dd> <dt>

*pName* 
</dt> <dd>

Pointer to a description used for debugging purposes.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the aggregated owner object.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




