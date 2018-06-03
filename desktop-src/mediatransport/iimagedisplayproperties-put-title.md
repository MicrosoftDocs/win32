---
title: IImageDisplayProperties put\_Title method
description: Sets the title of the image.
ms.assetid: A9C46D9E-FB19-4148-B49E-A058A141B103
keywords:
- put_Title method
- put_Title method, IImageDisplayProperties interface
- IImageDisplayProperties interface, put_Title method
topic_type:
- apiref
api_name:
- IImageDisplayProperties.put_Title
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

# IImageDisplayProperties::put\_Title method

Sets the title of the image.

## Syntax


```C++
HRESULT put_Title(
   HSTRING value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **[**HSTRING**](https://msdn.microsoft.com/library/windows/desktop/br205775)**

The title of the image.

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

 

 





