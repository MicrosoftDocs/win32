---
title: IVMMouse GetButton method (VPCCOMInterfaces.h)
description: Retrieves the current state of the specified mouse button.
ms.assetid: eb534f88-387d-42fb-bfc3-bca17685021e
keywords:
- GetButton method Virtual PC
- GetButton method Virtual PC , IVMMouse interface
- IVMMouse interface Virtual PC , GetButton method
topic_type:
- apiref
api_name:
- IVMMouse.GetButton
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMMouse::GetButton method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the current state (up or down) of the specified mouse button.

## Syntax


```C++
HRESULT GetButton(
  [in]          VMMouseButton buttonIndex,
  [out, retval] VARIANT_BOOL  *isDown
);
```



## Parameters

<dl> <dt>

*buttonIndex* \[in\]
</dt> <dd>

The index of the button whose state is being requested. For a list of values, see [**VMMouseButton**](vmmousebutton.md).

</dd> <dt>

*isDown* \[out, retval\]
</dt> <dd>

The state of the indicated button. **TRUE** if the button is currently down in the virtual machine, **FALSE** otherwise.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                        | Description                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                              | The operation was successful.<br/>                                                        |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                | The *isDown* parameter is **NULL**.<br/>                                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>             | The *buttonIndex* parameter is not valid.<br/>                                            |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>   | The virtual machine to which this mouse device is attached is not currently running.<br/> |
| <dl> <dt>**VM\_E\_MOUSE\_NOT\_ACTIVE**</dt> <dt>0xA0040800</dt> </dl> | The mouse device has not been powered up.<br/>                                            |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>        | An unexpected error has occurred.<br/>                                                    |



 

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

 

