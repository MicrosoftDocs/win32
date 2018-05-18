---
Description: 'The StringFromResource function loads a string from a resource file with the given resource identifier.'
ms.assetid: '26b40905-db16-46d1-8621-9aa8cb8e7232'
title: StringFromResource function
---

# StringFromResource function

The `StringFromResource` function loads a string from a resource file with the given resource identifier.

## Syntax


```C++
TCHAR* WINAPI StringFromResource(
   TCHAR *pBuffer,
   int   iResourceID
);
```



## Parameters

<dl> <dt>

*pBuffer* 
</dt> <dd>

Pointer to the string corresponding to *iResourceID*.

</dd> <dt>

*iResourceID* 
</dt> <dd>

Resource identifier of the string to retrieve.

</dd> </dl>

## Return value

Returns the same string as *pBuffer*. If the function is not successful, returns a null string.

## Remarks

The *pBuffer* buffer must be at least STR\_MAX\_LENGTH bytes.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Property Page Helper Functions](property-page-helper-functions.md)
</dt> </dl>

 

 




