---
title: IVMGuestOS GetParameter method (VPCCOMInterfaces.h)
description: Retrieves a named parameter within the guest operating system.
ms.assetid: d4d5acbd-fa19-4eb2-af75-2c94e5f6f7f0
keywords:
- GetParameter method Virtual PC
- GetParameter method Virtual PC , IVMGuestOS interface
- IVMGuestOS interface Virtual PC , GetParameter method
topic_type:
- apiref
api_name:
- IVMGuestOS.GetParameter
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMGuestOS::GetParameter method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves a named parameter within the guest operating system.

## Syntax


```C++
HRESULT GetParameter(
  [in]          BSTR inParameterName,
  [out, retval] BSTR *outParameterValue
);
```



## Parameters

<dl> <dt>

*inParameterName* \[in\]
</dt> <dd>

The parameter name. It must be between 1 and 255 characters in length and cannot contain a backslash (\\) character.

</dd> <dt>

*outParameterValue* \[out, retval\]
</dt> <dd>

The parameter value.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                    | Description                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                          | The operation was successful.<br/>                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                         | A parameter is not valid or not specified.<br/>                        |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                            | The parameter is **NULL**.<br/>                                        |
| <dl> <dt>**VM\_E\_TIMED\_OUT**</dt> <dt>0xA0040202</dt> </dl>                     | The operation did not complete in a timely manner.<br/>                |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>               | The virtual machine is not running.<br/>                               |
| <dl> <dt>**VM\_E\_VM\_PAUSED**</dt> <dt>0xA00400507</dt> </dl>                    | The virtual machine is paused.<br/>                                    |
| <dl> <dt>**VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL**</dt> <dt>0xA0040505</dt> </dl> | Integration components are not installed in this virtual machine.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                    | An unexpected error has occurred.<br/>                                 |



 

## Remarks

The virtual machine must be running and integration components must be installed when this method is invoked. This method is only supported for Windows-based guest operating systems.

With integration components installed, the following key is automatically added to the guest operating system's registry:

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Virtual Machine\\Guest\\Parameters**

When the guest operating system starts, the following registry string values are populated in the **Parameters** key:

-   **HostName**
-   **PhysicalHostName**
-   **PhysicalHostNameFullyQualified**
-   **VirtualMachineName**

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

 

