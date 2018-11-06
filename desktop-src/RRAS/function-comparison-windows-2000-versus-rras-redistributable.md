---
title: Function Comparison Windows 2000 vs. RRAS Redistributable
description: The RAS API is distributed as a feature of Windows 2000 and later operating systems and is available as a redistributable for Windows NT 4.0 with Service Pack 3 (SP3) and earlier.
ms.assetid: fd6c76b9-52e2-405e-b62e-055cfbdb5ad6
ms.topic: article
ms.date: 05/31/2018
---

# Function Comparison: Windows 2000 vs. RRAS Redistributable

The RAS API is distributed as a feature of Windows 2000 and later operating systems and is available as a redistributable for Windows NT 4.0 with Service Pack 3 (SP3) and earlier. RAS provides the same functionality in both of these forms but the naming convention that is used is different for the reference elements in each version of the RAS API.

The RAS functions for Windows NT 4.0 with SP3 and earlier typically begin with the "RasAdmin" prefix. The analogous functions for Routing and Remote Access Service (RRAS) begin with the "MprAdmin" prefix. For example, RAS provides a function called [**RasAdminPortGetInfo**](rasadminportgetinfo.md). The analogous function in RRAS is called [**MprAdminPortGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportgetinfo). As a similar example, RAS provides the callback function [**RasAdminGetIpAddressForUser**](rasadmingetipaddressforuser.md). RRAS provides a similar callback function called [**MprAdminGetIpAddressForUser**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingetipaddressforuser). Exceptions to this rule are [**RasAdminPortClearStatistics**](rasadminportclearstatistics.md), which under RRAS is [**MprAdminPortClearStats**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportclearstats), and [**RasAdminFreeBuffer**](rasadminfreebuffer.md), which under RRAS is [**MprAdminBufferFree**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminbufferfree).

The following table lists the Windows NT 4.0 SP3 RAS functions and the corresponding RRAS functions.



| Windows NT 4.0 RAS                                                                   | RRAS                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**RasAdminAcceptNewConnection**](rasadminacceptnewconnection.md)                   | [**MprAdminAcceptNewConnection**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection)                   |
| [**RasAdminConnectionHangupNotification**](rasadminconnectionhangupnotification.md) | [**MprAdminConnectionHangupNotification**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionhangupnotification) |
| [**RasAdminFreeBuffer**](rasadminfreebuffer.md)                                     | [**MprAdminBufferFree**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminbufferfree)                                     |
| [**RasAdminGetErrorString**](rasadmingeterrorstring.md)                             | [**MprAdminGetErrorString**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingeterrorstring)                             |
| [**RasAdminGetIpAddressForUser**](rasadmingetipaddressforuser.md)                   | [**MprAdminGetIpAddressForUser**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingetipaddressforuser)                   |
| [**RasAdminPortClearStatistics**](rasadminportclearstatistics.md)                   | [**MprAdminPortClearStats**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportclearstats)                             |
| [**RasAdminPortDisconnect**](rasadminportdisconnect.md)                             | [**MprAdminPortDisconnect**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportdisconnect)                             |
| [**RasAdminPortEnum**](rasadminportenum.md)                                         | [**MprAdminPortEnum**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportenum)                                         |
| [**RasAdminPortGetInfo**](rasadminportgetinfo.md)                                   | [**MprAdminPortGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportgetinfo)                                   |
| [**RasAdminReleaseIpAddress**](rasadminreleaseipaddress.md)                         | [**MprAdminReleaseIpAddress**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminreleaseipaddress)                         |
| [**RasAdminUserGetInfo**](rasadminusergetinfo.md)                                   | [**MprAdminUserGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminusergetinfo)                                   |
| [**RasAdminUserSetInfo**](rasadminusersetinfo.md)                                   | [**MprAdminUserSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminusersetinfo)                                   |



 

Although the RRAS functions are similar to their Windows NT 4.0 with SP3 and earlier RAS counterparts in functionality, RRAS functions often take a different set of parameters. See the reference page for a particular function for complete information on that function's parameter list.

The RRAS redistributable for Windows NT 4.0 with SP3 and earlier adds the following functions, which have no RAS counterparts:

[**MprAdminAcceptNewLink**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewlink)

[**MprAdminConnectionClearStats**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionclearstats)

[**MprAdminConnectionEnum**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionenum)

[**MprAdminConnectionGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectiongetinfo)

[**MprAdminGetPDCServer**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingetpdcserver)

[**MprAdminIsServiceRunning**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminisservicerunning)

[**MprAdminLinkHangupNotification**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminlinkhangupnotification)

[**MprAdminPortReset**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportreset)

[**MprAdminServerConnect**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminserverconnect)

[**MprAdminServerDisconnect**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminserverdisconnect)

In addition to the preceding functions, Windows 2000 and later operating systems add the following functions:

[**MprAdminSendUserMessage**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminsendusermessage)

[**MprAdminAcceptNewConnection2**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection2)

[**MprAdminConnectionHangupNotification2**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionhangupnotification2)

 

 




