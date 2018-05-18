---
title: IWmsPresentationDevice GetDimensions method
description: Retrieves the dimensions of a monitor screen, in pixels.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '63e5d40a-1421-460a-a23a-2149d98988b9'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["GetDimensions method", "GetDimensions method, IWmsPresentationDevice interface", "IWmsPresentationDevice interface, GetDimensions method"]
topic_type:
- apiref
api_name:
- IWmsPresentationDevice.GetDimensions
api_location:
- WmsStationPresenter.idl
api_type:
- COM
---

# IWmsPresentationDevice::GetDimensions method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves the dimensions of a monitor screen, in pixels.

## Syntax


```C++
HRESULT GetDimensions(
  [out] UINT *pcx,
  [out] UINT *pcy
);
```



## Parameters

<dl> <dt>

*pcx* \[out\]
</dt> <dd>

On successful return, receives the width of the screen, in pixels.

</dd> <dt>

*pcy* \[out\]
</dt> <dd>

On successful return, receives the height of the screen, in pixels.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsPresentationDevice is defined as 3fa4b1eb-eb6c-455e-a7ae-0861a26c8fc4<br/>          |



## See also

<dl> <dt>

[**IWmsPresentationDevice**](iwmspresentationdevice.md)
</dt> </dl>

 

 





