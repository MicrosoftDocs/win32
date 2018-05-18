---
title: IImageDisplayProperties get\_Subtitle method
description: Gets the subtitle of the image.
ms.assetid: 'FB5CA178-AF22-40CE-A203-2B4DA361C620'
keywords: ["get_Subtitle method", "get_Subtitle method, IImageDisplayProperties interface", "IImageDisplayProperties interface, get_Subtitle method"]
topic_type:
- apiref
api_name:
- IImageDisplayProperties.get_Subtitle
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# IImageDisplayProperties::get\_Subtitle method

Gets the subtitle of the image.

## Syntax


```C++
HRESULT get_Subtitle(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**HSTRING**](https://msdn.microsoft.com/library/windows/desktop/br205775)\***

The subtitle of the image.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Windows.Media.SystemMediaTransportControls.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.Media.SystemMediaTransportControls.idl</dt> </dl> |



## See also

<dl> <dt>

[**IImageDisplayProperties**](iimagedisplayproperties.md)
</dt> </dl>

 

 





