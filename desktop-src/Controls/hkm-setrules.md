---
title: HKM_SETRULES message (Commctrl.h)
description: Defines the invalid combinations and the default modifier combination for a hot key control.
ms.assetid: de3dd463-a534-4c7c-ae04-da80a3bff2ab
keywords:
- HKM_SETRULES message Windows Controls
topic_type:
- apiref
api_name:
- HKM_SETRULES
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HKM\_SETRULES message

Defines the invalid combinations and the default modifier combination for a hot key control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

An array of flags that specify invalid key combinations. This parameter can be a combination of the following values:



| Value                                                                                                                                                   | Meaning                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| <span id="HKCOMB_A"></span><span id="hkcomb_a"></span><dl> <dt>**HKCOMB\_A**</dt> </dl>          | ALT<br/>             |
| <span id="HKCOMB_C"></span><span id="hkcomb_c"></span><dl> <dt>**HKCOMB\_C**</dt> </dl>          | CTRL<br/>            |
| <span id="HKCOMB_CA"></span><span id="hkcomb_ca"></span><dl> <dt>**HKCOMB\_CA**</dt> </dl>       | CTRL+ALT<br/>        |
| <span id="HKCOMB_NONE"></span><span id="hkcomb_none"></span><dl> <dt>**HKCOMB\_NONE**</dt> </dl> | Unmodified keys<br/> |
| <span id="HKCOMB_S"></span><span id="hkcomb_s"></span><dl> <dt>**HKCOMB\_S**</dt> </dl>          | SHIFT<br/>           |
| <span id="HKCOMB_SA"></span><span id="hkcomb_sa"></span><dl> <dt>**HKCOMB\_SA**</dt> </dl>       | SHIFT+ALT<br/>       |
| <span id="HKCOMB_SC"></span><span id="hkcomb_sc"></span><dl> <dt>**HKCOMB\_SC**</dt> </dl>       | SHIFT+CTRL<br/>      |
| <span id="HKCOMB_SCA"></span><span id="hkcomb_sca"></span><dl> <dt>**HKCOMB\_SCA**</dt> </dl>    | SHIFT+CTRL+ALT<br/>  |



 

</dd> <dt>

*lParam* 
</dt> <dd>

An array of flags that specify the key combination to use when the user enters an invalid combination. For a list of modifier flag values, see the description of the [**HKM\_GETHOTKEY**](hkm-gethotkey.md) message.

</dd> </dl>

## Return value

No return value.

## Remarks

When a user enters an invalid key combination, as defined by flags specified in *wParam*, the system uses the bitwise-OR operator to combine the keys entered by the user with the flags specified in *lParam*. The resulting key combination is converted into a string and then displayed in the hot key control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





