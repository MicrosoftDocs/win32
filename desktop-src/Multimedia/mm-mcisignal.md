---
title: MM_MCISIGNAL message (Mmsystem.h)
description: The MM\_MCISIGNAL message is sent to a window to notify an application that an MCI device has reached a position defined in a previous signal ( MCI\_SIGNAL) command.
ms.assetid: 12512d23-9a89-4e38-9ec5-88845766f4f6
keywords:
- MM_MCISIGNAL message Windows Multimedia
topic_type:
- apiref
api_name:
- MM_MCISIGNAL
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MM\_MCISIGNAL message

The **MM\_MCISIGNAL** message is sent to a window to notify an application that an MCI device has reached a position defined in a previous [**signal**](signal.md) ( [**MCI\_SIGNAL**](mci-signal.md)) command.


```C++
MM_MCISIGNAL 
wParam = (WPARAM) wID      
lParam = (LONG) lUserParm  
```



## Parameters

<dl> <dt>

<span id="wID"></span><span id="wid"></span><span id="WID"></span>*wID*
</dt> <dd>

Identifier of the device initiating the signal message.

</dd> <dt>

<span id="lUserParm"></span><span id="luserparm"></span><span id="LUSERPARM"></span>*lUserParm*
</dt> <dd>

Value passed in the **dwUserParm** member of the **MCI\_DGV\_SIGNAL\_PARAMS** structure when the **signal** command has defined this callback function. Alternatively, it might contain the position value.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Messages](mci-messages.md)
</dt> <dt>

[**signal**](signal.md)
</dt> </dl>

 

 





