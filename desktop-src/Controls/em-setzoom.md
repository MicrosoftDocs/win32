---
title: EM\_SETZOOM message
description: Sets the zoom ratio of a rich edit control. The ratio must be a value between 1/64 and 64.
ms.assetid: 6cdec5b8-4ce7-4fd5-8083-4daa63d17f63
keywords:
- EM_SETZOOM message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETZOOM
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EM\_SETZOOM message

Sets the zoom ratio of a rich edit control. The ratio must be a value between 1/64 and 64.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Numerator of the zoom ratio.

</dd> <dt>

*lParam* 
</dt> <dd>

Denominator of the zoom ratio. These parameters can have the following values.



| Value                                                                                                                                                                                                                                                              | Meaning                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Both_0"></span><span id="both_0"></span><span id="BOTH_0"></span><dl> <dt>**Both 0**</dt> </dl>                                                                                                   | Turns off zooming by using the **EM\_SETZOOM** message (zooming may still occur using [**TxGetExtent**](/windows/desktop/api/Textserv/nf-textserv-itexthost-txgetextent)).<br/> |
| <span id="1_64____wParam___lParam____64"></span><span id="1_64____wparam___lparam____64"></span><span id="1_64____WPARAM___LPARAM____64"></span><dl> <dt>**1/64 < (wParam / lParam) < 64**</dt> </dl> | Zooms display by the zoom ratio numerator/denominator<br/>                                                                                |



 

</dd> </dl>

## Return value

If the new zoom setting is accepted, the return value is **TRUE**.

If the new zoom setting is not accepted, the return value is **FALSE**.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Rich Edit 3.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETZOOM**](em-getzoom.md)
</dt> </dl>

 

 





