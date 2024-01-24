---
title: IVMMouse SetButton method (VPCCOMInterfaces.h)
description: Sets the current state (up or down) of the specified mouse button.
ms.assetid: 52b24472-68d6-4a42-8ae5-b1434a6d67f3
keywords:
- SetButton method Virtual PC
- SetButton method Virtual PC , IVMMouse interface
- IVMMouse interface Virtual PC , SetButton method
topic_type:
- apiref
api_name:
- IVMMouse.SetButton
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMMouse::SetButton method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Sets the current state (up or down) of the specified mouse button.

## Syntax


```C++
HRESULT SetButton(
  [in] VMMouseButton buttonIndex,
  [in] VARIANT_BOOL  down
);
```



## Parameters

<dl> <dt>

*buttonIndex* \[in\]
</dt> <dd>

The button index. For a list of values, see [**VMMouseButton**](vmmousebutton.md).

</dd> <dt>

*down* \[in\]
</dt> <dd>

The new button state. Use **TRUE** if the button state is to be set to down, and **FALSE** if it is to be set to up.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                        | Description                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                              | The operation was successful.<br/>                                                                                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>             | The *buttonIndex* parameter is not valid.<br/>                                                                                              |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>   | The virtual machine to which this mouse device is attached is not currently running.<br/>                                                   |
| <dl> <dt>**VM\_E\_MOUSE\_NOT\_ACTIVE**</dt> <dt>0xA0040800</dt> </dl> | The operation could not be completed because the mouse device is not powered up, or it is not currently active in the virtual machine.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>        | An unexpected error has occurred.<br/>                                                                                                      |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMmouse is defined as ac903f6d-6346-4f29-8875-5d511a13895e<br/>                   |



## See also

<dl> <dt>

[**IVMMouse**](ivmmouse.md)
</dt> </dl>

 

