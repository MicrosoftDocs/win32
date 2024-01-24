---
title: IVMVirtualMachine StartCommunicationChannel method (VPCCOMInterfaces.h)
description: Sets up a communication channel between host and guest operating system.
ms.assetid: e4b04aa8-8400-4aa4-ad54-71ef57dec82a
keywords:
- StartCommunicationChannel method Virtual PC
- StartCommunicationChannel method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , StartCommunicationChannel method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.StartCommunicationChannel
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::StartCommunicationChannel method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Sets up a communication channel between host and guest operating system.

## Syntax


```C++
HRESULT StartCommunicationChannel(
  [in] VMEndpointType inHostEndpointType,
  [in] BSTR           inHostEndPointName,
  [in] VMEndpointType inGuestEndpointType,
  [in] BSTR           inGuestEndpointName
);
```



## Parameters

<dl> <dt>

*inHostEndpointType* \[in\]
</dt> <dd>

This parameter must be **vmEndpoint\_NamedPipe** (0).

</dd> <dt>

*inHostEndPointName* \[in\]
</dt> <dd>

The unique pipe name. This string must have the following form: "\\\\.\\pipe\\*pipename*". The *pipename* part of the name can include any character other than a backslash, including numbers and special characters. The entire pipe name string can be up to 256 characters long. Pipe names are not case sensitive.

</dd> <dt>

*inGuestEndpointType* \[in\]
</dt> <dd>

This parameter must be **vmEndpoint\_TCPIP** (1).

</dd> <dt>

*inGuestEndpointName* \[in\]
</dt> <dd>

The port number on which the TCP server in the guest is listening.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                                  | Description                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                        | The operation was successful.<br/>                                                                                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                                       | The *inHostEndpointType* parameter is not **vmEndpoint\_NamedPipe** (0) or the *inGuestEndpointType* parameter is not **vmEndpoint\_TCPIP** (1).<br/> |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                          | The *inHostEndPointName* or *inGuestEndpointName* parameter is **NULL** or not a valid value.<br/>                                                    |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                                  | An unexpected error has occurred.<br/>                                                                                                                |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_HANDLE)**</dt> <dt>0x80070006</dt> </dl>        | A handle is not valid.<br/>                                                                                                                           |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_OUTOFMEMORY)**</dt> <dt>0x8007000e</dt> </dl>            | There is not enough memory available to complete this request.<br/>                                                                                   |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_NOT\_READY)**</dt> <dt>0x80070015</dt> </dl>             | The underlying system it uses to provide network services is currently being initialized.<br/>                                                        |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ALREADY\_EXISTS)**</dt> <dt>0x800700b7</dt> </dl>        | The pipe name is already in use.<br/>                                                                                                                 |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_PIPE\_BUSY)**</dt> <dt>0x800700e7</dt> </dl>             | One or more channels are running down and may become available shortly.<br/>                                                                          |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_MAX\_SESSIONS\_REACHED)**</dt> <dt>0x80070161</dt> </dl> | The maximum numbers of communication channels available are in-use. Another channel cannot be started at this time.<br/>                              |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_REVISION\_MISMATCH)**</dt> <dt>0x8007051a</dt> </dl>     | There is a mismatch between the version of the host and guest subsystems. See the Windows Event Log for more detail.<br/>                             |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>                             | The VM is not running.<br/>                                                                                                                           |



 

## Remarks

The current implementation supports only named pipe interface on the host and TCP/IP interface on the guest operating system.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualMachine is defined as f7092aa1-33ed-4f78-a59f-c00adfc2edd7<br/>          |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> <dt>

[**VMEndpointType**](vmendpointtype.md)
</dt> </dl>

 

