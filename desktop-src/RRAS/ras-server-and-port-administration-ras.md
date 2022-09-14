---
title: RAS Server and Port Administration
description: The RAS server administration functions enable you to get information about a specified RAS server and its ports. These functions also enable you to terminate a connection on a specified RAS server port.
ms.assetid: 783b0ded-7c0e-49eb-8040-563d5dd675f0
ms.topic: article
ms.date: 05/31/2018
---

# RAS Server and Port Administration

The RAS server administration functions enable you to get information about a specified RAS server and its ports. These functions also enable you to terminate a connection on a specified RAS server port.

The [**RasAdminServerGetInfo**](rasadminservergetinfo.md) function returns a [**RAS\_SERVER\_0**](ras-server-0-str.md) structure that contains information about the configuration of a RAS server. The returned information includes the number of ports currently available for connection, the number of ports currently in use, and the server version number.

The [**RasAdminPortEnum**](rasadminportenum.md) function retrieves an array of [**RAS\_PORT\_0**](ras-port-0-str.md) structures that contains information for each of the ports configured on a RAS server. The information for each port includes:

-   The name of the port
-   Information about the device attached to the port
-   Whether the RAS server associated with the port is a Windows NT/Windows 2000 Server
-   Whether the port is currently in use, and if it is, information about the connection

You can call the [**RasAdminPortGetInfo**](rasadminportgetinfo.md) function to get additional information about a specified port on a RAS server. This function returns a [**RAS\_PORT\_1**](ras-port-1-str.md) structure that contains a [**RAS\_PORT\_0**](/windows/desktop/api/Mprapi/ns-mprapi-ras_port_0) structure and additional information about the current state of the port. The **RasAdminPortGetInfo** function also returns an array of [**RAS\_PARAMETERS**](ras-parameters-str.md) structures that describe the values of any media-specific keys associated with the port. A **RAS\_PARAMETERS** structure uses a value from the [**RAS\_PARAMS\_FORMAT**](ras-params-format-str.md) enumeration to indicate the format of the value for each media-specific key.

The [**RasAdminPortGetInfo**](rasadminportgetinfo.md) function also returns a [**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md) structure that contains various statistic counters for the current connection, if any, on the port. For a port that is part of a multilink connection, **RasAdminPortGetInfo** returns statistics for the individual port and cumulative statistics for all ports involved in the connection. You can use the [**RasAdminPortClearStatistics**](rasadminportclearstatistics.md) function to reset the statistic counters for the port. The [**RasAdminPortDisconnect**](rasadminportdisconnect.md) function disconnects a port that is in use.

Use the [**RasAdminFreeBuffer**](rasadminfreebuffer.md) function to free memory allocated by the [**RasAdminPortEnum**](rasadminportenum.md) and [**RasAdminPortGetInfo**](rasadminportgetinfo.md) functions. Use the [**RasAdminGetErrorString**](rasadmingeterrorstring.md) function to get a string that describes a RAS error code returned by one of the RAS server administration (RasAdmin) functions.

 

 




