---
title: Function Comparison Windows 2000 vs. RRAS Redistributable
description: The RAS API is distributed as a feature of Windows 2000 and later operating systems and is available as a redistributable for Windows NT 4.0 with Service Pack 3 (SP3) and earlier.
ms.assetid: fd6c76b9-52e2-405e-b62e-055cfbdb5ad6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Function Comparison: Windows 2000 vs. RRAS Redistributable

The RAS API is distributed as a feature of Windows 2000 and later operating systems and is available as a redistributable for Windows NT 4.0 with Service Pack 3 (SP3) and earlier. RAS provides the same functionality in both of these forms but the naming convention that is used is different for the reference elements in each version of the RAS API.

The RAS functions for Windows NT 4.0 with SP3 and earlier typically begin with the "RasAdmin" prefix. The analogous functions for Routing and Remote Access Service (RRAS) begin with the "MprAdmin" prefix. For example, RAS provides a function called [**RasAdminPortGetInfo**](rasadminportgetinfo.md). The analogous function in RRAS is called [**MprAdminPortGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradminportgetinfo?branch=master). As a similar example, RAS provides the callback function [**RasAdminGetIpAddressForUser**](rasadmingetipaddressforuser.md). RRAS provides a similar callback function called [**MprAdminGetIpAddressForUser**](/windows/win32/Mprapi/nf-mprapi-mpradmingetipaddressforuser?branch=master). Exceptions to this rule are [**RasAdminPortClearStatistics**](rasadminportclearstatistics.md), which under RRAS is [**MprAdminPortClearStats**](/windows/win32/Mprapi/nf-mprapi-mpradminportclearstats?branch=master), and [**RasAdminFreeBuffer**](rasadminfreebuffer.md), which under RRAS is [**MprAdminBufferFree**](/windows/win32/Mprapi/nf-mprapi-mpradminbufferfree?branch=master).

The following table lists the Windows NT 4.0 SP3 RAS functions and the corresponding RRAS functions.



| Windows NT 4.0 RAS                                                                   | RRAS                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**RasAdminAcceptNewConnection**](rasadminacceptnewconnection.md)                   | [**MprAdminAcceptNewConnection**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptnewconnection?branch=master)                   |
| [**RasAdminConnectionHangupNotification**](rasadminconnectionhangupnotification.md) | [**MprAdminConnectionHangupNotification**](/windows/win32/Mprapi/nf-mprapi-mpradminconnectionhangupnotification?branch=master) |
| [**RasAdminFreeBuffer**](rasadminfreebuffer.md)                                     | [**MprAdminBufferFree**](/windows/win32/Mprapi/nf-mprapi-mpradminbufferfree?branch=master)                                     |
| [**RasAdminGetErrorString**](rasadmingeterrorstring.md)                             | [**MprAdminGetErrorString**](/windows/win32/Mprapi/nf-mprapi-mpradmingeterrorstring?branch=master)                             |
| [**RasAdminGetIpAddressForUser**](rasadmingetipaddressforuser.md)                   | [**MprAdminGetIpAddressForUser**](/windows/win32/Mprapi/nf-mprapi-mpradmingetipaddressforuser?branch=master)                   |
| [**RasAdminPortClearStatistics**](rasadminportclearstatistics.md)                   | [**MprAdminPortClearStats**](/windows/win32/Mprapi/nf-mprapi-mpradminportclearstats?branch=master)                             |
| [**RasAdminPortDisconnect**](rasadminportdisconnect.md)                             | [**MprAdminPortDisconnect**](/windows/win32/Mprapi/nf-mprapi-mpradminportdisconnect?branch=master)                             |
| [**RasAdminPortEnum**](rasadminportenum.md)                                         | [**MprAdminPortEnum**](/windows/win32/Mprapi/nf-mprapi-mpradminportenum?branch=master)                                         |
| [**RasAdminPortGetInfo**](rasadminportgetinfo.md)                                   | [**MprAdminPortGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradminportgetinfo?branch=master)                                   |
| [**RasAdminReleaseIpAddress**](rasadminreleaseipaddress.md)                         | [**MprAdminReleaseIpAddress**](/windows/win32/Mprapi/nf-mprapi-mpradminreleaseipaddress?branch=master)                         |
| [**RasAdminUserGetInfo**](rasadminusergetinfo.md)                                   | [**MprAdminUserGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradminusergetinfo?branch=master)                                   |
| [**RasAdminUserSetInfo**](rasadminusersetinfo.md)                                   | [**MprAdminUserSetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradminusersetinfo?branch=master)                                   |



 

Although the RRAS functions are similar to their Windows NT 4.0 with SP3 and earlier RAS counterparts in functionality, RRAS functions often take a different set of parameters. See the reference page for a particular function for complete information on that function's parameter list.

The RRAS redistributable for Windows NT 4.0 with SP3 and earlier adds the following functions, which have no RAS counterparts:

[**MprAdminAcceptNewLink**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptnewlink?branch=master)

[**MprAdminConnectionClearStats**](/windows/win32/Mprapi/nf-mprapi-mpradminconnectionclearstats?branch=master)

[**MprAdminConnectionEnum**](/windows/win32/Mprapi/nf-mprapi-mpradminconnectionenum?branch=master)

[**MprAdminConnectionGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradminconnectiongetinfo?branch=master)

[**MprAdminGetPDCServer**](/windows/win32/Mprapi/nf-mprapi-mpradmingetpdcserver?branch=master)

[**MprAdminIsServiceRunning**](/windows/win32/Mprapi/nf-mprapi-mpradminisservicerunning?branch=master)

[**MprAdminLinkHangupNotification**](/windows/win32/Mprapi/nf-mprapi-mpradminlinkhangupnotification?branch=master)

[**MprAdminPortReset**](/windows/win32/Mprapi/nf-mprapi-mpradminportreset?branch=master)

[**MprAdminServerConnect**](/windows/win32/Mprapi/nf-mprapi-mpradminserverconnect?branch=master)

[**MprAdminServerDisconnect**](/windows/win32/Mprapi/nf-mprapi-mpradminserverdisconnect?branch=master)

In addition to the preceding functions, Windows 2000 and later operating systems add the following functions:

[**MprAdminSendUserMessage**](/windows/win32/Mprapi/nf-mprapi-mpradminsendusermessage?branch=master)

[**MprAdminAcceptNewConnection2**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptnewconnection2?branch=master)

[**MprAdminConnectionHangupNotification2**](/windows/win32/Mprapi/nf-mprapi-mpradminconnectionhangupnotification2?branch=master)

 

 




