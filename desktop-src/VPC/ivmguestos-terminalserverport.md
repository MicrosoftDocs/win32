---
title: IVMGuestOS TerminalServerPort property
description: Port used by Remote Desktop Services in the guest operating system.
ms.assetid: 25a9114a-0992-4a9d-997a-37138d389970
keywords:
- TerminalServerPort property Virtual PC
- TerminalServerPort property Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , TerminalServerPort property
topic_type:
- apiref
api_name:
- IVMGuestOS.TerminalServerPort
- IVMGuestOS.get_TerminalServerPort
api_location:
- IVMGuestOS.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::TerminalServerPort property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Port used by Remote Desktop Services (formerly known as Terminal Services) in the guest operating system.

This property is read-only.

## Syntax


```C++
HRESULT get_TerminalServerPort(
  [out, retval] long *tsPort = 3389
);
```



## Property value

Returns the port used by Remote Desktop Services in the guest operating system.



| Value                                                                              | Meaning                                       |
|------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>3389</dt> </dl>    | Default value<br/>                      |
| <dl> <dt>1 65535</dt> </dl> | Valid range<br/>                        |
| <dl> <dt>0</dt> </dl>       | Valid port value is not available.<br/> |



 

## Error codes



| Name/value                                                                                                                                                                       | Meaning                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                          | The operation was successful.<br/>                                                 |
| <dl> <dt>S\_FALSE</dt> <dt>1</dt> </dl>                                       | Remote Desktop Services is not yet initialized in the guest operating system.<br/> |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                            | The *tsPort* parameter is **NULL**.<br/>                                           |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl>               | The virtual machine is not running.<br/>                                           |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL</dt> <dt>0xA0040505</dt> </dl> | Integration components are not installed in this virtual machine.<br/>             |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                    | An unexpected error has occurred.<br/>                                             |



## Remarks

The value of this property is not valid unless the [**TerminalServicesInitialized**](ivmguestos-terminalservicesinitialized.md) property is **VARIANT\_TRUE**.

If the [**TerminalServicesInitialized**](ivmguestos-terminalservicesinitialized.md) property is **VARIANT\_FALSE** due to a connection error on the port, then the value returned by the **TerminalServerPort** property contains the error value.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | None supported<br/>                                                                 |
| End of client support<br/>    | Windows 7<br/>                                                                      |
| IDL<br/>                      | <dl> <dt>IVMGuestOS.idl</dt> </dl> |
| IID<br/>                      | IID\_IVMGuestOS is defined as 99fea0db-4880-499a-b6d8-73dff9bc91be<br/>             |



## See also

<dl> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> </dl>

 

