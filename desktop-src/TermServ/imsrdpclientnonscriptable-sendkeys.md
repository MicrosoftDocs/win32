---
title: IMsRdpClientNonScriptable SendKeys method
description: Sends a series of keystrokes to the control. The keystrokes are in scan code form, which is the keyboard data from the actual physical keys.
ms.assetid: 1f07a9cc-4795-43cb-ac99-4bb70b8b544a
ms.tgt_platform: multiple
keywords:
- SendKeys method Remote Desktop Services
- SendKeys method Remote Desktop Services , IMsRdpClientNonScriptable interface
- IMsRdpClientNonScriptable interface Remote Desktop Services , SendKeys method
- SendKeys method Remote Desktop Services , IMsRdpClientNonScriptable2 interface
- IMsRdpClientNonScriptable2 interface Remote Desktop Services , SendKeys method
- SendKeys method Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , SendKeys method
- SendKeys method Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , SendKeys method
- SendKeys method Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , SendKeys method
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable.SendKeys
- IMsRdpClientNonScriptable2.SendKeys
- IMsRdpClientNonScriptable3.SendKeys
- IMsRdpClientNonScriptable4.SendKeys
- IMsRdpClientNonScriptable5.SendKeys
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable::SendKeys method

Sends a series of keystrokes to the control. The keystrokes are in scan code form, which is the keyboard data from the actual physical keys.

## Syntax


```C++
HRESULT SendKeys(
  [in] LONG         numKeys,
  [in] VARIANT_BOOL *pbArrayKeyUp,
  [in] LONG         *plKeyData
);
```



## Parameters

<dl> <dt>

*numKeys* \[in\]
</dt> <dd>

The number of keystrokes to send. The maximum number of keys that can be sent in one operation is 20. The method returns **E\_INVALIDARG** if this parameter is greater than 20. For more information, see the following Remarks section.

</dd> <dt>

*pbArrayKeyUp* \[in\]
</dt> <dd>

An array whose size is equal to *numKeys*. An element is **TRUE** if the corresponding key is UP and **FALSE** if the corresponding key is DOWN.

</dd> <dt>

*plKeyData* \[in\]
</dt> <dd>

An array whose size is equal to *numKeys*. The array contains keystroke data and corresponds to the value of the *lParam* parameter of the [WM\_KEYDOWN](../inputdev/wm-keydown.md) message. The data specifies the repeat count, scan code, extended-key flag, context code, previous key-state flag, and transition-state flag. For a description of the bits in this array, see [WM\_KEYDOWN](../inputdev/wm-keydown.md).

The corresponding element in *pbArrayKeyUp* indicates if the key is UP or DOWN.

</dd> </dl>

## Return value

Return **S\_OK** if successful.

## Remarks

The **SendKeys** method does not mix keystrokes made by the local user with keystrokes that the method is sending. All keystrokes passed to the method are sent to the remote session in a single atomic sequence.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                               |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>       |
| IID<br/>                      | IID\_IMsRdpClientNonScriptable is defined as 2f079c4c-87b2-4afd-97ab-20cdb43038ae<br/> |



## See also

- [**IMsRdpClientNonScriptable2**](imsrdpclientnonscriptable2.md)
- [**IMsRdpClientNonScriptable3**](imsrdpclientnonscriptable3.md)
- [**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
- [**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
- [**IMsRdpClientNonScriptable**](imsrdpclientnonscriptable-interface.md)
- [WM\_KEYDOWN](../inputdev/wm-keydown.md)
- [Keyboard Input (Keyboard and Mouse Input)](../inputdev/keyboard-input.md)
- [About Keyboard Input](../inputdev/about-keyboard-input.md)
