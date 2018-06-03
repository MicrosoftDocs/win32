---
title: IWmsStationMousePresenter ShowCursor method
description: Displays or hides the mouse cursor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4500fa0d-bd74-4b80-84dc-eb652e4df6bb
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- ShowCursor method
- ShowCursor method, IWmsStationMousePresenter interface
- IWmsStationMousePresenter interface, ShowCursor method
topic_type:
- apiref
api_name:
- IWmsStationMousePresenter.ShowCursor
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsStationMousePresenter::ShowCursor method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Displays or hides the mouse cursor.

## Syntax


```C++
HRESULT ShowCursor(
  [in] BOOL fShow
);
```



## Parameters

<dl> <dt>

*fShow* \[in\]
</dt> <dd>

**TRUE** to display the mouse cursor; otherwise, **FALSE**.

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

 

 





