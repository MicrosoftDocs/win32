---
title: IWmsStationMousePresenter SetCursorPos method
description: Updates the position of the mouse cursor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 41a848bd-9226-4b43-bc48-a5a30f5f4490
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- SetCursorPos method
- SetCursorPos method, IWmsStationMousePresenter interface
- IWmsStationMousePresenter interface, SetCursorPos method
topic_type:
- apiref
api_name:
- IWmsStationMousePresenter.SetCursorPos
api_location:
- winuser.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IWmsStationMousePresenter::SetCursorPos method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Updates the position of the mouse cursor.

## Syntax


```C++
HRESULT SetCursorPos(
  [in] int X,
  [in] int Y
);
```



## Parameters

<dl> <dt>

*X* \[in\]
</dt> <dd>

The new x-coordinate of the mouse cursor, in screen coordinates.

</dd> <dt>

*Y* \[in\]
</dt> <dd>

The new y-coordinate of the mouse cursor, in screen coordinates.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl>               |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsStationMousePresenter is defined as a391f331-00f0-4204-9d09-f926917233b0<br/>       |



## See also

<dl> <dt>

[**IWmsStationMousePresenter**](iwmsstationmousepresenter.md)
</dt> </dl>

 

 





