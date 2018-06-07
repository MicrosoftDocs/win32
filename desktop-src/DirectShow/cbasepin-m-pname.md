---
Description: Pin name.
ms.assetid: 324cb8cc-7e57-43d0-9358-2683efc4fb1e
title: CBasePin::m\_pName member
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBasePin::m\_pName member

Pin name.

## Syntax


```C++
WCHAR *m_pName;
```



## Remarks

The [**CBasePin::QueryPinInfo**](cbasepin-querypininfo.md) method returns this string as the pin name, and the [**CBasePin::QueryId**](cbasepin-queryid.md) method returns it as the pin identifier. In general, however, the pin name and the pin identifier are not required to be the same. The pin identifier is used for graph persistence. For more information, see [**IBaseFilter::FindPin**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-findpin).

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




