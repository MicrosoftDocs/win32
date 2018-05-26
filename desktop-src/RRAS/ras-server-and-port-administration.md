---
title: RAS Server and Port Administration
description: The RAS server administration functions get information about a specified RAS server and its ports. These functions are also used to terminate a connection on a specified RAS server port.
ms.assetid: eedac23e-d716-451e-b08b-594398656bb5
keywords:
- RAS Administration RRAS , server and port administration
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RAS Server and Port Administration

The RAS server administration functions get information about a specified RAS server and its ports. These functions are also used to terminate a connection on a specified RAS server port.

The [**MprAdminServerGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradminservergetinfo?branch=master) function returns a [**MPR\_SERVER\_0**](/windows/win32/Mprapi/ns-mprapi-_mpr_server_0?branch=master) structure that contains information about the configuration of a RAS server. The returned information includes the number of ports currently available for connections, the number of ports currently in use, and the server version number.

The [**MprAdminPortEnum**](/windows/win32/Mprapi/nf-mprapi-mpradminportenum?branch=master) function retrieves an array of [**RAS\_PORT\_0**](/windows/win32/Mprapi/ns-mprapi-_ras_port_0?branch=master) structures. Each structure contains information for one of the ports configured on a RAS server. The information for each port includes:

-   The name of the port
-   Information about the device attached to the port
-   Whether the RAS server associated with the port is a Windows NT/Windows 2000 Server
-   Whether the port is currently in use and, if it is, information about the connection

To obtain the ports in use by a specific connection, pass [**MprAdminPortEnum**](/windows/win32/Mprapi/nf-mprapi-mpradminportenum?branch=master) a handle to that connection in the *hConnection* parameter. To obtain a handle to a connection, use the [**MprAdminConnectionEnum**](/windows/win32/Mprapi/nf-mprapi-mpradminconnectionenum?branch=master) function. Alternatively, if you have implemented a [RAS Administration DLL](ras-administration-dll.md), the [**MprAdminAcceptNewConnection**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptnewconnection?branch=master) and [**MprAdminAcceptNewConnection2**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptnewconnection2?branch=master) functions receive a handle to each new connection at the time the connection is established.

You can call the [**MprAdminPortGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradminportgetinfo?branch=master) function to get additional information about a specified port on a RAS server. This function returns a [**RAS\_PORT\_1**](/windows/win32/Mprapi/ns-mprapi-_ras_port_1?branch=master) structure that contains a [**RAS\_PORT\_0**](/windows/win32/Mprapi/ns-mprapi-_ras_port_0?branch=master) structure and additional information about the current state of the port. The [**RasAdminPortGetInfo**](rasadminportgetinfo.md) function also returns an array of [**RAS\_PARAMETERS**](ras-parameters-str.md) structures that describe the values of any media-specific keys associated with the port. A **RAS\_PARAMETERS** structure uses a value from the [**RAS\_PARAMS\_FORMAT**](ras-params-format-str.md) enumeration to indicate the format of the value for each media-specific key.

The [**MprAdminPortGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradminportgetinfo?branch=master) function also returns a [**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md) structure that contains various statistic counters for the current connection, if any, on the port. For a port that is part of a multilink connection, **MprAdminPortGetInfo** returns statistics for the individual port and cumulative statistics for all ports involved in the connection. You can use the [**MprAdminPortClearStats**](/windows/win32/Mprapi/nf-mprapi-mpradminportclearstats?branch=master) function to reset the statistic counters for the port. The [**MprAdminPortDisconnect**](/windows/win32/Mprapi/nf-mprapi-mpradminportdisconnect?branch=master) function disconnects a port that is in use.

Use the [**MprAdminBufferFree**](/windows/win32/Mprapi/nf-mprapi-mpradminbufferfree?branch=master) function to free memory allocated by the [**MprAdminPortEnum**](/windows/win32/Mprapi/nf-mprapi-mpradminportenum?branch=master) and [**MprAdminPortGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradminportgetinfo?branch=master) functions. Use the [**MprAdminGetErrorString**](/windows/win32/Mprapi/nf-mprapi-mpradmingeterrorstring?branch=master) function to get a string that describes a RAS error code returned by one of the RAS server administration (RasAdmin) functions.

 

 




