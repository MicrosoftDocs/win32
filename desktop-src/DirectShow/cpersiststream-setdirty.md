---
Description: Changes the dirty flag for the current stream.
ms.assetid: 65fa7fbe-4fa7-45a3-91a4-4a3547b035b9
title: CPersistStream.SetDirty method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPersistStream.SetDirty method

Changes the dirty flag for the current stream.

## Syntax


```C++
HRESULT SetDirty(
   BOOL fDirty
);
```



## Parameters

<dl> <dt>

*fDirty* 
</dt> <dd>

New dirty flag for this stream. **TRUE** means that the data has not been saved.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




