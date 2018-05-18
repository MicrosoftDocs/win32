---
Description: 'Notifies an application when the IME needs to change the RECONVERTSTRING structure. The application receives this command through the WM\_IME\_REQUEST message with parameter settings as shown below.'
ms.assetid: '035a7072-d292-4883-bc3e-d1e9ed64d9ec'
title: 'IMR\_CONFIRMRECONVERTSTRING notification code'
---

# IMR\_CONFIRMRECONVERTSTRING notification code

Notifies an application when the IME needs to change the [**RECONVERTSTRING**](reconvertstring.md) structure. The application receives this command through the [**WM\_IME\_REQUEST**](wm-ime-request.md) message with parameter settings as shown below.


```C++
LRESULT IMR_CONFIRMRECONVERTSTRING
```



## Parameters

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

Set to IMR\_CONFIRMRECONVERTSTRING.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

Pointer to a [**RECONVERTSTRING**](reconvertstring.md) structure from the IME. For more information, see the Remarks section.

</dd> </dl>

## Return Value

Returns a nonzero value if the application accepts the changed [**RECONVERTSTRING**](reconvertstring.md) structure. Otherwise, the command returns 0 and the IME uses the original **RECONVERTSTRING** structure.

## Remarks

The application fills in the [**RECONVERTSTRING**](reconvertstring.md) structure upon receiving the [IMR\_RECONVERTSTRING](imr-reconvertstring.md) command.

After the application has handled [IMR\_RECONVERTSTRING](imr-reconvertstring.md), the IME might or might not adjust the [**RECONVERTSTRING**](reconvertstring.md) structure. The IME sends WM\_IME\_REQUEST with **IMR\_CONFIRMRECONVERTSTRING** to confirm the changes to the **RECONVERTSTRING** structure. If the application returns **TRUE** for **IMR\_CONFIRMRECONVERTSTRING**, the IME generates a new composition string based on the **RECONVERTSTRING** structure for the **IMR\_CONFIRMRECONVERTSTRING** command. If the application returns **FALSE** for **IMR\_CONFIRMRECONVERTSTRING**, the IME generates a new composition string based on the original **RECONVERTSTRING** structure specified by the application in the IMR\_RECONVERTSTRING command.

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>Imm.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Input Method Manager](input-method-manager.md)
</dt> <dt>

[Input Method Manager Commands](input-method-manager-commands.md)
</dt> <dt>

[IMR\_RECONVERTSTRING](imr-reconvertstring.md)
</dt> <dt>

[**RECONVERTSTRING**](reconvertstring.md)
</dt> <dt>

[**WM\_IME\_REQUEST**](wm-ime-request.md)
</dt> </dl>

 

 




