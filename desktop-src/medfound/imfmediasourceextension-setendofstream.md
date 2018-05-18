---
Description: 'Indicate that the end of the media stream has been reached.'
ms.assetid: '6d6bffcc-aa3c-4825-9268-00dcd2a347e6'
title: 'IMFMediaSourceExtension::SetEndOfStream method'
---

# IMFMediaSourceExtension::SetEndOfStream method

Indicate that the end of the media stream has been reached.

## Syntax


```C++
HRESULT SetEndOfStream(
  [in] MF_MSE_ERROR error
);
```



## Parameters

<dl> <dt>

*error* \[in\]
</dt> <dd>

Used to pass error information.

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

[**IMFMediaSourceExtension**](imfmediasourceextension.md)
</dt> <dt>

[**MF\_MSE\_ERROR**](mf-mse-error.md)
</dt> </dl>

 

 




