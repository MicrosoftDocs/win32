---
title: update command
description: The update command repaints the current frame into the specified device context (DC). Digital-video devices recognize this command.
ms.assetid: '51a83262-91d5-4852-ad17-bd62c14417b1'
keywords:
- update command Windows Multimedia
topic_type:
- apiref
api_name:
- update
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# update command

The update command repaints the current frame into the specified device context (DC). Digital-video devices recognize this command.

To send this command, call the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function with the *lpszCommand* parameter set as follows.

``` syntax
_stprintf_s(
  lpszCommand, 
  TEXT("update %s %s %s"), 
  lpszDeviceID, 
  lpszHDC, 
  lpszFlags
); 
```

## Parameters

<dl> <dt>

<span id="lpszDeviceID"></span><span id="lpszdeviceid"></span><span id="LPSZDEVICEID"></span>*lpszDeviceID*
</dt> <dd>

Identifier of an MCI device. This identifier or alias is assigned when the device is opened.

</dd> <dt>

<span id="lpszHDC"></span><span id="lpszhdc"></span><span id="LPSZHDC"></span>*lpszHDC*
</dt> <dd>

Handle of a DC. The following table lists device types that recognize the **update** command and the flags used by each type.



| Value        | Meaning                       | Meaning         |
|--------------|-------------------------------|-----------------|
| digitalvideo | hdc *hdc* hdc *hdc* at *rect* | paint hdc *hdc* |



 

The following table lists the flags that can be specified in the **lpszHDC** parameter and their meanings.



| Value               | Meaning                                                                                                |
|---------------------|--------------------------------------------------------------------------------------------------------|
| hdc *hdc*           | Specifies the handle of the DC to paint.                                                               |
| hdc *hdc* at *rect* | Specifies the clipping rectangle relative to the client rectangle.                                     |
| paint hdc *hdc*     | Paints the DC when the application receives a [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message intended for a DC. |



 

To specify the handle of the DC, use the string "hdc" followed by an ASCII representation of the handle. The rectangle is specified as**X1 Y1 X2 Y2**. The coordinates**X1 Y1**specify the upper left corner of the rectangle, and the coordinates**X2 Y2**specify the width and height.

</dd> <dt>

<span id="lpszFlags"></span><span id="lpszflags"></span><span id="LPSZFLAGS"></span>*lpszFlags*
</dt> <dd>

Can be "wait", "notify", or both. For digital-video devices, "test" can also be specified. For more information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Examples

The following command updates the entire display window used by the "movie" device. The number 203 is a handle to a DC obtained from the [**BeginPaint**](/windows/desktop/api/winuser/nf-winuser-beginpaint) function.

``` syntax
update movie hdc 203
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Command Strings](mci-command-strings.md)
</dt> </dl>

 

