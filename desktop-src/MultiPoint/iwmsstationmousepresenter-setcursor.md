---
title: IWmsStationMousePresenter SetCursor method
description: Updates the shape of the mouse cursor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 54d90eab-0609-49aa-802b-ae3c2f2525fb
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- SetCursor method
- SetCursor method, IWmsStationMousePresenter interface
- IWmsStationMousePresenter interface, SetCursor method
topic_type:
- apiref
api_name:
- IWmsStationMousePresenter.SetCursor
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsStationMousePresenter::SetCursor method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Updates the shape of the mouse cursor.

## Syntax


```C++
HRESULT SetCursor(
  [in] HCURSOR hCursor
);
```



## Parameters

<dl> <dt>

*hCursor* \[in\]
</dt> <dd>

A handle to the cursor. If this parameter is **NULL**, the cursor is removed from the screen.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsStationMousePresenter is defined as a391f331-00f0-4204-9d09-f926917233b0<br/>       |



## See also

<dl> <dt>

[**IWmsStationMousePresenter**](iwmsstationmousepresenter.md)
</dt> </dl>

 

 





