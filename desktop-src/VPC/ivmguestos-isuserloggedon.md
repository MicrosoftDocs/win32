---
title: IVMGuestOS IsUserLoggedOn method (VPCCOMInterfaces.h)
description: Determines whether the requested session is present.
ms.assetid: 28035e30-023a-4ec2-88ef-43fe22f6d14e
keywords:
- IsUserLoggedOn method Virtual PC
- IsUserLoggedOn method Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , IsUserLoggedOn method
topic_type:
- apiref
api_name:
- IVMGuestOS.IsUserLoggedOn
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::IsUserLoggedOn method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Determines whether the requested session is present.

## Syntax


```C++
HRESULT IsUserLoggedOn(
  [in]          long         inRailSession,
  [out, retval] VARIANT_BOOL *outSessionPresent
);
```



## Parameters

<dl> <dt>

*inRailSession* \[in\]
</dt> <dd>

Set to 0 for a Rail session or 1 for an RDP session.

</dd> <dt>

*outSessionPresent* \[out, retval\]
</dt> <dd>

Set to **VARIANT\_TRUE** if the session is present and **VARIANT\_FALSE** otherwise.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                       | Description                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                             | The operation was successful.<br/>                                   |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                               | The parameter is **NULL**.<br/>                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                            | The *outSessionPresent* parameter is not valid or is **NULL**.<br/>  |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                       | An unexpected error has occurred.<br/>                               |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_OUTOFMEMORY)**</dt> <dt>0x8007000e</dt> </dl> | There is not enough memory available to complete this request.<br/>  |
| <dl> <dt>**VM\_E\_TIMED\_OUT**</dt> <dt>0xA0040202</dt> </dl>                        | The operation did not complete in a timely manner.<br/>              |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>                  | The virtual machine (VM) must be running for this operation.<br/>    |
| <dl> <dt>**VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL**</dt> <dt>0xA0040505</dt> </dl>    | The integration components feature is not installed in this VM.<br/> |
| <dl> <dt>**VM\_E\_VM\_PAUSED**</dt> <dt>0xA00400507</dt> </dl>                       | The VM is paused.<br/>                                               |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMGuestOS is defined as 99fea0db-4880-499a-b6d8-73dff9bc91be<br/>                 |



## See also

<dl> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> </dl>

 

