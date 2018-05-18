---
Description: 'Retrieves the software version for this stream.'
ms.assetid: 'f54153df-5593-4784-acc5-3e0dcef424b5'
title: 'CPersistStream.GetSoftwareVersion method'
---

# CPersistStream.GetSoftwareVersion method

Retrieves the software version for this stream.

## Syntax


```C++
virtual DWORD GetSoftwareVersion();
```



## Parameters

This method has no parameters.

## Return value

Returns a **DWORD** containing the version number. Each time the format of the stream is changed, this function should be altered to return a larger number than before.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




