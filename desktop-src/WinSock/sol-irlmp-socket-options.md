---
description: The following table describes SOL\_IRLMP socket options that apply to sockets created for the Infrared Data Association (IrDA) address family (AF\_IRDA) and the InfraRed Link Management Protocol (IRLMP).
ms.assetid: 0457159d-8509-435c-8f57-752530d5df65
title: SOL_IRLMP Socket Options (Af\_irda.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SOL\_IRLMP Socket Options

The following table describes **SOL\_IRLMP** socket options that apply to sockets created for the Infrared Data Association (IrDA) address family (AF\_IRDA) and the InfraRed Link Management Protocol (IRLMP). See the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) and [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function reference pages for more information on getting and setting socket options.

To enumerate protocols and discover supported properties for each installed protocol, use the [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa), [**WSCEnumProtocols**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols), or [**WSCEnumProtocols32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols32) function.

<dl> <dt><span id="SOL_IRLMP_Socket_Options"></span><span id="sol_irlmp_socket_options"></span><span id="SOL_IRLMP_SOCKET_OPTIONS"></span>**SOL\_IRLMP Socket Options**</dt> <dd> <dl> <dt> 

| Option                 | Get | Set | Optval type     | Description                                                            |
|------------------------|-----|-----|-----------------|------------------------------------------------------------------------|
| IRLMP\_DISCOVERY\_MODE |     |     |                 |                                                                        |
| IRLMP\_ENUMDEVICES     | yes |     | **DEVICELIST**  | Returns a list of IrDA device IDs for IR capable devices within range. |
| IRLMP\_EXCLUSIVE\_MODE |     |     | DWORD (boolean) | Sets socket to bypass TinyTP layer to directly communicate with IrLMP. |
| IRLMP\_IAS\_QUERY      | yes |     | **IAS\_QUERY**  | Queries IAS on a given service and class name for its attributes.      |
| IRLMP\_IAS\_SET        |     | yes | **IAS\_SET**    | Sets an attribute value for a given class name and attribute into IAS. |
| IRLMP\_IRLPT\_MODE     |     | yes | DWORD (boolean) | Enables communication with IR capable printers.                        |
| IRLMP\_PARAMETERS      |     |     |                 |                                                                        |
| IRLMP\_SEND\_PDU\_LEN  | yes |     | DWORD           | Retrieves the maximum PDU length required to use IRLMP\_9WIRE\_MODE.   |
| IRLMP\_SHARP\_MODE     |     | yes |                 |                                                                        |
| IRLMP\_TINYTP\_MODE    |     | yes |                 |                                                                        |
| IRLMP\_9WIRE\_MODE     | yes | yes | DWORD (boolean) | Puts the IrDA socket into IrCOMM mode.                                 |



 

</dt> </dl> </dd> <dt><span id="Windows_Support_for_SOL_IRLMP_options"></span><span id="windows_support_for_sol_irlmp_options"></span><span id="WINDOWS_SUPPORT_FOR_SOL_IRLMP_OPTIONS"></span>**Windows Support for SOL\_IRLMP options**</dt> <dd> <dl> <dt> 

| Option                            | Windows 7 | Windows Server 2008 | Windows Vista | Windows Server 2003 | Windows XP | Windows 2000 | Windows Me, Windows 98 | Windows NT 4.0 |
|-----------------------------------|-----------|---------------------|---------------|---------------------|------------|--------------|------------------------|----------------|
| IRLMP\_DISCOVERY\_MODE<br/> |           |                     |               |                     |            |              | x                      |                |
| IRLMP\_ENUMDEVICES<br/>     | x         | x                   | x             | x                   | x          | x            | x                      |                |
| IRLMP\_EXCLUSIVE\_MODE<br/> |           |                     |               |                     |            |              |                        |                |
| IRLMP\_IAS\_QUERY<br/>      | x         | x                   | x             | x                   | x          | x            | x                      |                |
| IRLMP\_IAS\_SET<br/>        | x         | x                   | x             | x                   | x          | x            | x                      |                |
| IRLMP\_IRLPT\_MODE<br/>     | x         | x                   | x             | x                   | x          | x            |                        |                |
| IRLMP\_PARAMETERS<br/>      |           |                     |               |                     |            |              | x                      |                |
| IRLMP\_SEND\_PDU\_LEN<br/>  | x         | x                   | x             | x                   | x          | x            |                        |                |
| IRLMP\_SHARP\_MODE<br/>     |           |                     |               |                     |            |              |                        |                |
| IRLMP\_TINYTP\_MODE<br/>    |           |                     |               |                     |            |              | x                      |                |
| IRLMP\_9WIRE\_MODE<br/>     | x         | x                   | x             | x                   | x          | x            |                        |                |



 


</dt> </dl> </dd> </dl>

## Remarks

The **SOL\_IRLMP** socket options and the structures used by these socket options are defined in the *Af\_irda.h* header file.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Af\_irda.h</dt> </dl> |



 

 




