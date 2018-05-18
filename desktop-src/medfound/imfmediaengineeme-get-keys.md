---
Description: 'Gets the media keys object associated with the media engine or null if there is not a media keys object.'
ms.assetid: 'e6556a02-445d-4436-80de-e4156d6a3d63'
title: 'IMFMediaEngineEME::get\_Keys method'
---

# IMFMediaEngineEME::get\_Keys method

Gets the media keys object associated with the media engine or **null** if there is not a media keys object.

## Syntax


```C++
HRESULT get_Keys(
   IMFMediaKeys **keys
);
```



## Parameters

<dl> <dt>

*keys* 
</dt> <dd>

The media keys object associated with the media engine or **null** if there is not a media keys object.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFMediaEngineEME**](imfmediaengineeme.md)
</dt> </dl>

 

 




