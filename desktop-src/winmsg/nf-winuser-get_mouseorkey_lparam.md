---
UID: NF:winuser.GET_MOUSEORKEY_LPARAM
title: GET_MOUSEORKEY_LPARAM macro (winuser.h)
description: Retrieves the input device type from the specified LPARAM value.
helpviewer_keywords: ["GET_MOUSEORKEY_LPARAM","GET_MOUSEORKEY_LPARAM macro [Keyboard and Mouse Input]","_win32_GET_MOUSEORKEY_LPARAM","_win32_get_mouseorkey_lparam_cpp","inputdev.get_mouseorkey_lparam","winui._win32_get_mouseorkey_lparam","winuser/GET_MOUSEORKEY_LPARAM"]
tech.root: inputdev
ms.date: 06/23/2023
ms.keywords: GET_MOUSEORKEY_LPARAM, GET_MOUSEORKEY_LPARAM macro [Keyboard and Mouse Input], _win32_GET_MOUSEORKEY_LPARAM, _win32_get_mouseorkey_lparam_cpp, inputdev.get_mouseorkey_lparam, winui._win32_get_mouseorkey_lparam, winuser/GET_MOUSEORKEY_LPARAM
req.header: winuser.h
req.include-header: Windows.h
req.target-type: Windows
req.target-min-winverclnt: Windows 2000 Professional [desktop apps only]
req.target-min-winversvr: Windows 2000 Server [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
ms.custom: 19H1
f1_keywords:
 - GET_MOUSEORKEY_LPARAM
 - winuser/GET_MOUSEORKEY_LPARAM
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - HeaderDef
api_location:
 - Winuser.h
api_name:
 - GET_MOUSEORKEY_LPARAM
---

# GET_MOUSEORKEY_LPARAM macro

Retrieves the input device type from the specified **LPARAM** value.

## Syntax

``` c++
WORD GET_MOUSEORKEY_LPARAM(
   LPARAM lParam
);
```

### -param lParam

The value to be converted.

## Return value

The return value is the bit of the high-order word representing the input device type. It can be one of the following values.

<table>
<colgroup>
<col />
<col />
</colgroup>
<thead>
<tr class="header">
<th>Return code/value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>FAPPCOMMAND_KEY</strong>
0</td>
<td><p>User pressed a key.</p></td>
</tr>
<tr class="even">
<td><strong>FAPPCOMMAND_MOUSE</strong>
0x8000</td>
<td><p>User clicked a mouse button.</p></td>
</tr>
<tr class="odd">
<td><strong>FAPPCOMMAND_OEM</strong>
0x1000</td>
<td><p>An unidentified hardware source generated the event. It could be a mouse or a keyboard event.</p></td>
</tr>
</tbody>
</table>

## Remarks

This macro is identical to the [GET_DEVICE_LPARAM macro](nf-winuser-get_device_lparam.md) macro.

## See also

[GET_DEVICE_LPARAM macro](nf-winuser-get_device_lparam.md), [Mouse Input](/windows/win32/inputdev/mouse-input)
