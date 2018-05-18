---
Description: 'Gets the IMFDXGIDeviceManager from the Microsoft Media Foundation video rendering sink.'
ms.assetid: '809e89e4-3ed5-4dba-82dc-4ec217b8ef38'
title: 'IMFDXGIDeviceManagerSource::GetManager method'
---

# IMFDXGIDeviceManagerSource::GetManager method

Gets the [**IMFDXGIDeviceManager**](imfdxgidevicemanager.md) from the Microsoft Media Foundation video rendering sink.

## Syntax


```C++
HRESULT GetManager(
  [out] IMFDXGIDeviceManager **ppManager
);
```



## Parameters

<dl> <dt>

*ppManager* \[out\]
</dt> <dd>

The [**IMFDXGIDeviceManager**](imfdxgidevicemanager.md) object.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                       |
| IDL<br/>                      | <dl> <dt>Mfidl.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFDXGIDeviceManagerSource**](imfdxgidevicemanagersource.md)
</dt> </dl>

 

 




