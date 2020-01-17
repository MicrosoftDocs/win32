---
title: About RAS Server and Port Administration
description: The RAS server administration functions get information about a specified RAS server and its ports. These functions are also used to terminate a connection on a specified RAS server port.
ms.assetid: eedac23e-d716-451e-b08b-594398656bb5
keywords:
- RAS Administration RRAS , server and port administration
ms.topic: article
ms.date: 05/31/2018
---

# About RAS Server and Port Administration

The RAS server administration functions get information about a specified RAS server and its ports. These functions are also used to terminate a connection on a specified RAS server port.

The [**MprAdminServerGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminservergetinfo) function returns a [**MPR\_SERVER\_0**](/windows/desktop/api/Mprapi/ns-mprapi-mpr_server_0) structure that contains information about the configuration of a RAS server. The returned information includes the number of ports currently available for connections, the number of ports currently in use, and the server version number.

The [**MprAdminPortEnum**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportenum) function retrieves an array of [**RAS\_PORT\_0**](/windows/desktop/api/Mprapi/ns-mprapi-ras_port_0) structures. Each structure contains information for one of the ports configured on a RAS server. The information for each port includes:

-   The name of the port
-   Information about the device attached to the port
-   Whether the RAS server associated with the port is a Windows NT/Windows 2000 Server
-   Whether the port is currently in use and, if it is, information about the connection

To obtain the ports in use by a specific connection, pass [**MprAdminPortEnum**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportenum) a handle to that connection in the *hConnection* parameter. To obtain a handle to a connection, use the [**MprAdminConnectionEnum**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionenum) function. Alternatively, if you have implemented a [RAS Administration DLL](ras-administration-dll.md), the [**MprAdminAcceptNewConnection**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection) and [**MprAdminAcceptNewConnection2**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection2) functions receive a handle to each new connection at the time the connection is established.

You can call the [**MprAdminPortGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportgetinfo) function to get additional information about a specified port on a RAS server. This function returns a [**RAS\_PORT\_1**](/windows/desktop/api/Mprapi/ns-mprapi-ras_port_1) structure that contains a [**RAS\_PORT\_0**](/windows/desktop/api/Mprapi/ns-mprapi-ras_port_0) structure and additional information about the current state of the port. The [**RasAdminPortGetInfo**](rasadminportgetinfo.md) function also returns an array of [**RAS\_PARAMETERS**](ras-parameters-str.md) structures that describe the values of any media-specific keys associated with the port. A **RAS\_PARAMETERS** structure uses a value from the [**RAS\_PARAMS\_FORMAT**](ras-params-format-str.md) enumeration to indicate the format of the value for each media-specific key.

The [**MprAdminPortGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportgetinfo) function also returns a [**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md) structure that contains various statistic counters for the current connection, if any, on the port. For a port that is part of a multilink connection, **MprAdminPortGetInfo** returns statistics for the individual port and cumulative statistics for all ports involved in the connection. You can use the [**MprAdminPortClearStats**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportclearstats) function to reset the statistic counters for the port. The [**MprAdminPortDisconnect**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportdisconnect) function disconnects a port that is in use.

Use the [**MprAdminBufferFree**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminbufferfree) function to free memory allocated by the [**MprAdminPortEnum**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportenum) and [**MprAdminPortGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportgetinfo) functions. Use the [**MprAdminGetErrorString**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingeterrorstring) function to get a string that describes a RAS error code returned by one of the RAS server administration (RasAdmin) functions.

 

 




