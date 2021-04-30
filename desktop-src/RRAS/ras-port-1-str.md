---
title: RAS_PORT_1 structure (Rassapi.h)
description: The RAS\_PORT\_1 structure contains information about a RAS port.
ms.assetid: f226ef16-feb4-41e0-ba60-ddb2f0acd305
keywords:
- RAS_PORT_1 structure RAS
- PRAS_PORT_1 structure pointer RAS
topic_type:
- apiref
api_name:
- RAS_PORT_1
api_location:
- Rassapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RAS\_PORT\_1 structure

\[This version of the **RAS\_PORT\_1** structure is not supported as of Windows Vista. Use the newer [**RAS\_PORT\_1**](/windows/desktop/api/Mprapi/ns-mprapi-ras_port_1) defined in mprapi.h instead.\]

The **RAS\_PORT\_1** structure contains information about a RAS port.

## Syntax


```C++
typedef struct _RAS_PORT_1 {
  RAS_PORT_0                rasport0;
  DWORD                     LineCondition;
  DWORD                     HardwareCondition;
  DWORD                     LineSpeed;
  WORD                      NumStatistics;
  WORD                      NumMediaParms;
  DWORD                     SizeMediaParms;
  RAS_PPP_PROJECTION_RESULT ProjResult;
} RAS_PORT_1, *PRAS_PORT_1;
```



## Members

<dl> <dt>

**rasport0**
</dt> <dd>

Specifies a [**RAS\_PORT\_0**](ras-port-0-str.md) structure that contains information about the port, such as the name of the port, the name of the remote user connected to the port, and so on.

</dd> <dt>

**LineCondition**
</dt> <dd>

Specifies the state of the port. This member can be one of the following values.



| Value                                                                                                                                                                                            | Meaning                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RAS_PORT_NON_OPERATIONAL"></span><span id="ras_port_non_operational"></span><dl> <dt>**RAS\_PORT\_NON\_OPERATIONAL**</dt> </dl> | The port is not operational. Check the event log for errors reported by the server.<br/>                                                                         |
| <span id="RAS_PORT_DISCONNECTED"></span><span id="ras_port_disconnected"></span><dl> <dt>**RAS\_PORT\_DISCONNECTED**</dt> </dl>           | The port is currently disconnected.<br/>                                                                                                                         |
| <span id="RAS_PORT_CALLING_BACK"></span><span id="ras_port_calling_back"></span><dl> <dt>**RAS\_PORT\_CALLING\_BACK**</dt> </dl>          | The RAS server is calling back the RAS client.<br/>                                                                                                              |
| <span id="RAS_PORT_LISTENING"></span><span id="ras_port_listening"></span><dl> <dt>**RAS\_PORT\_LISTENING**</dt> </dl>                    | The port is waiting for a client to call in.<br/>                                                                                                                |
| <span id="RAS_PORT_AUTHENTICATING"></span><span id="ras_port_authenticating"></span><dl> <dt>**RAS\_PORT\_AUTHENTICATING**</dt> </dl>     | The server is in the process of authenticating the remote client.<br/>                                                                                           |
| <span id="RAS_PORT_AUTHENTICATED"></span><span id="ras_port_authenticated"></span><dl> <dt>**RAS\_PORT\_AUTHENTICATED**</dt> </dl>        | The remote client is now authenticated.<br/>                                                                                                                     |
| <span id="RAS_PORT_INITIALIZING"></span><span id="ras_port_initializing"></span><dl> <dt>**RAS\_PORT\_INITIALIZING**</dt> </dl>           | The device attached to the port is being initialized. The state of the port will change to RAS\_PORT\_LISTENING when the initialization has been completed.<br/> |



 

</dd> <dt>

**HardwareCondition**
</dt> <dd>

Specifies one of the following values to indicate the state of the device attached to the port.



| Value                                                                                                                                                                                                  | Meaning                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <span id="RAS_MODEM_OPERATIONAL"></span><span id="ras_modem_operational"></span><dl> <dt>**RAS\_MODEM\_OPERATIONAL**</dt> </dl>                 | The modem attached to this port is operational and is ready to receive client calls.<br/> |
| <span id="RAS_MODEM_HARDWARE_FAILURE"></span><span id="ras_modem_hardware_failure"></span><dl> <dt>**RAS\_MODEM\_HARDWARE\_FAILURE**</dt> </dl> | The modem attached to this port has a hardware problem.<br/>                              |



 

</dd> <dt>

**LineSpeed**
</dt> <dd>

Specifies the speed, in bits per second, with which the computer can communicate with the port.

</dd> <dt>

**NumStatistics**
</dt> <dd>

This member is not used. The RAS administration functions, such as the [**RasAdminPortGetInfo**](rasadminportgetinfo.md) function, use the [**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md) structure to return port statistics.

</dd> <dt>

**NumMediaParms**
</dt> <dd>

Specifies the number of media-specific parameters for this port. For serial media this is typically the number of values that appear in the SERIAL.INI file.

</dd> <dt>

**SizeMediaParms**
</dt> <dd>

Specifies the size, in bytes, of the buffer required for all media-specific parameters. The [**RasAdminPortGetInfo**](rasadminportgetinfo.md) function returns a buffer that contains an array of [**RAS\_PARAMETERS**](ras-parameters-str.md) structures with the media parameters and values for the port.

</dd> <dt>

**ProjResult**
</dt> <dd>

A [**RAS\_PPP\_PROJECTION\_RESULT**](ras-ppp-projection-result-str.md) structure that specifies the PPP projection information for this port. This structure provides information for each protocol that is negotiated when a RAS client connects to a server.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP<br/>                                                                |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>Rassapi.h</dt> </dl> |



## See also

<dl> <dt>

[Remote Access Service (RAS) Overview](about-remote-access-service.md)
</dt> <dt>

[RAS Server Administration Structures](ras-server-administration-structures.md)
</dt> <dt>

[**RAS\_PARAMETERS**](ras-parameters-str.md)
</dt> <dt>

[**RAS\_PORT\_0**](ras-port-0-str.md)
</dt> <dt>

[**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md)
</dt> <dt>

[**RAS\_PPP\_PROJECTION\_RESULT**](ras-ppp-projection-result-str.md)
</dt> <dt>

[**RasAdminAcceptNewConnection**](rasadminacceptnewconnection.md)
</dt> <dt>

[**RasAdminConnectionHangupNotification**](rasadminconnectionhangupnotification.md)
</dt> <dt>

[**RasAdminPortGetInfo**](rasadminportgetinfo.md)
</dt> </dl>

 

 





