---
title: IImageDisplayProperties put\_Subtitle method
description: Sets the subtitle of the image.
ms.assetid: 7A10CFE2-D89B-4435-83F7-0FF5C7595E08
keywords:
- put_Subtitle method
- put_Subtitle method, IImageDisplayProperties interface
- IImageDisplayProperties interface, put_Subtitle method
topic_type:
- apiref
api_name:
- IImageDisplayProperties.put_Subtitle
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IImageDisplayProperties::put\_Subtitle method

Sets the subtitle of the image.

## Syntax


```C++
HRESULT put_Subtitle(
   HSTRING value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **[**HSTRING**](https://msdn.microsoft.com/library/windows/desktop/br205775)**

The subtitle of the image.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Windows.Media.SystemMediaTransportControls.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.Media.SystemMediaTransportControls.idl</dt> </dl> |



## See also

<dl> <dt>

[**IImageDisplayProperties**](iimagedisplayproperties.md)
</dt> </dl>

 

 





