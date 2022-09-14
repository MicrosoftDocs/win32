---
title: VMEndpointType enumeration (VPCCOMInterfaces.h)
description: Specifies the endpoint type.
ms.assetid: b48bd860-50dc-4c8c-b65b-69c407d4612a
keywords:
- VMEndpointType enumeration Virtual PC
topic_type:
- apiref
api_name:
- VMEndpointType
api_location:
- VPCCOMInterfaces.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# VMEndpointType enumeration

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Specifies the endpoint type.

## Syntax


```C++
typedef enum  { 
  vmEndpoint_NamedPipe  = 0,
  vmEndpoint_TCPIP      = 1
} VMEndpointType;
```



## Constants

<dl> <dt>

<span id="vmEndpoint_NamedPipe"></span><span id="vmendpoint_namedpipe"></span><span id="VMENDPOINT_NAMEDPIPE"></span>**vmEndpoint\_NamedPipe**
</dt> <dd>

The host side.

</dd> <dt>

<span id="vmEndpoint_TCPIP"></span><span id="vmendpoint_tcpip"></span><span id="VMENDPOINT_TCPIP"></span>**vmEndpoint\_TCPIP**
</dt> <dd>

The guest side.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |



## See also

<dl> <dt>

[**IVMVirtualMachine::StartCommunicationChannel**](ivmvirtualmachine-startcommunicationchannel.md)
</dt> </dl>

 

