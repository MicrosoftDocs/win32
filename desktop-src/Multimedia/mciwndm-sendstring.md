---
title: MCIWNDM\_SENDSTRING message
description: The MCIWNDM\_SENDSTRING message sends an MCI command in string form to the device associated with the MCIWnd window. You can send this message explicitly or by using the MCIWndSendString macro.
ms.assetid: '0e999a0e-588d-4f06-a1bc-fd3f245d8980'
keywords: ["MCIWNDM_SENDSTRING message Windows Multimedia"]
topic_type:
- apiref
api_name:
- MCIWNDM_SENDSTRING
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# MCIWNDM\_SENDSTRING message

The **MCIWNDM\_SENDSTRING** message sends an MCI command in string form to the device associated with the MCIWnd window. You can send this message explicitly or by using the [**MCIWndSendString**](mciwndsendstring.md) macro.


```C++
MCIWNDM_SENDSTRING 
wParam = 0; 
lParam = (LPARAM) (LPSTR) sz; 
```



## Parameters

<dl> <dt>

<span id="sz"></span><span id="SZ"></span>*sz*
</dt> <dd>

String command to send to the MCI device.

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The message handler for **MCIWNDM\_SENDSTRING** appends a device alias to the MCI command you send to the device. Therefore, you should not use any alias in an MCI command that you issue with **MCIWNDM\_SENDSTRING**.

To get the return string, which contains the result of the command, send the [**MCIWNDM\_RETURNSTRING**](mciwndm-returnstring.md) message.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndSendString**](mciwndsendstring.md)
</dt> <dt>

[Multimedia Command Strings](multimedia-command-strings.md)
</dt> </dl>

 

 





