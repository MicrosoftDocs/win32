---
Description: 'Gets the capabilities information for the content.'
ms.assetid: '04d35ac6-af8c-4e95-865b-54bbc7e36059'
title: 'IPlayToControlWithCapabilities::GetCapabilities method'
---

# IPlayToControlWithCapabilities::GetCapabilities method

Gets the capabilities information for the content.

## Syntax


```C++
HRESULT GetCapabilities(
  [out] PLAYTO_SOURCE_CREATEFLAGS *pCapabilities
);
```



## Parameters

<dl> <dt>

*pCapabilities* \[out\]
</dt> <dd>

The capabilities information for the content.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Mfsharingengine.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mfsharingengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IPlayToControlWithCapabilities**](iplaytocontrolwithcapabilities.md)
</dt> <dt>

[**IPlayToSource**](iplaytosourceclassfactory.md)
</dt> </dl>

 

 




