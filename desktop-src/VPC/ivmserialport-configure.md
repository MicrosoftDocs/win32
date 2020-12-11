---
title: IVMSerialPort Configure method (VPCCOMInterfaces.h)
description: Configures the serial port.
ms.assetid: fee2e373-8e7c-4f1d-84d0-f0f187a41e9f
keywords:
- Configure method Virtual PC
- Configure method Virtual PC , IVMSerialPort interface
- IVMSerialPort interface Virtual PC , Configure method
topic_type:
- apiref
api_name:
- IVMSerialPort.Configure
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMSerialPort::Configure method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Configures the serial port.

## Syntax


```C++
HRESULT Configure(
  [in] VMSerialPortType portType,
  [in] BSTR             portName,
  [in] VARIANT_BOOL     vmConnectImmediately
);
```



## Parameters

<dl> <dt>

*portType* \[in\]
</dt> <dd>

The type of serial port. For a list of values, see [**VMSerialPortType**](vmserialporttype.md).

</dd> <dt>

*portName* \[in\]
</dt> <dd>

The name of the serial port. For example, "COM1" for **vmSerialPort\_HostPort**, "C:\\SerialPort.txt" for **vmSerialPort\_TextFile**, or "\\\\*servername*\\pipe\\*pipename*" for **vmSerialPort\_NamedPipe**.

</dd> <dt>

*vmConnectImmediately* \[in\]
</dt> <dd>

**TRUE** if the host serial port should be opened immediately when the virtual machine is started and **FALSE** otherwise. Ignored if *portType* is not **vmSerialPort\_HostPort**.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                            | Description                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                                 | The *portType* parameter is not valid.<br/>                                                                                 |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                      |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                    | The *portName* parameter is **NULL**.<br/>                                                                                  |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_OUTOFMEMORY)**</dt> <dt>0x8007000e</dt> </dl>      | There is not enough memory available to complete this request.<br/>                                                         |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)**</dt> <dt>0x8007006f</dt> </dl> | The path specified by the *portName* parameter is too long. The path must be less than **MAX\_PATH** (260) characters.<br/> |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)**</dt> <dt>0x8007007b</dt> </dl>    | The *portName* parameter contains an invalid character (one of "\*?<>/\|":").<br/>                                    |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)**</dt> <dt>0x800700a1</dt> </dl>    | The *portName* parameter specifies an empty or relative path. An absolute path is required.<br/>                            |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>                            | The configuration for this virtual machine is not valid.<br/>                                                               |
| <dl> <dt>**VM\_E\_PREF\_ILLEGAL\_VALUE**</dt> <dt>0xA0040301</dt> </dl>                   | The specified port is already in use.<br/>                                                                                  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMSerialPort is defined as 2ce4460d-1d3f-4458-bf8b-44084b816815<br/>              |



## See also

<dl> <dt>

[**IVMSerialPort**](ivmserialport.md)
</dt> </dl>

 

