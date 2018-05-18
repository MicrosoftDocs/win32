---
title: Function Comparison Windows 2000 vs. RRAS Redistributable
description: The RAS API is distributed as a feature of Windows 2000 and later operating systems and is available as a redistributable for Windows NT 4.0 with Service Pack 3 (SP3) and earlier.
ms.assetid: 'fd6c76b9-52e2-405e-b62e-055cfbdb5ad6'
---

# Function Comparison: Windows 2000 vs. RRAS Redistributable

The RAS API is distributed as a feature of Windows 2000 and later operating systems and is available as a redistributable for Windows NT 4.0 with Service Pack 3 (SP3) and earlier. RAS provides the same functionality in both of these forms but the naming convention that is used is different for the reference elements in each version of the RAS API.

The RAS functions for Windows NT 4.0 with SP3 and earlier typically begin with the "RasAdmin" prefix. The analogous functions for Routing and Remote Access Service (RRAS) begin with the "MprAdmin" prefix. For example, RAS provides a function called [**RasAdminPortGetInfo**](rasadminportgetinfo.md). The analogous function in RRAS is called [**MprAdminPortGetInfo**](mpradminportgetinfo.md). As a similar example, RAS provides the callback function [**RasAdminGetIpAddressForUser**](rasadmingetipaddressforuser.md). RRAS provides a similar callback function called [**MprAdminGetIpAddressForUser**](mpradmingetipaddressforuser.md). Exceptions to this rule are [**RasAdminPortClearStatistics**](rasadminportclearstatistics.md), which under RRAS is [**MprAdminPortClearStats**](mpradminportclearstats.md), and [**RasAdminFreeBuffer**](rasadminfreebuffer.md), which under RRAS is [**MprAdminBufferFree**](mpradminbufferfree.md).

The following table lists the Windows NT 4.0 SP3 RAS functions and the corresponding RRAS functions.



| Windows NT 4.0 RAS                                                                   | RRAS                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**RasAdminAcceptNewConnection**](rasadminacceptnewconnection.md)                   | [**MprAdminAcceptNewConnection**](mpradminacceptnewconnection.md)                   |
| [**RasAdminConnectionHangupNotification**](rasadminconnectionhangupnotification.md) | [**MprAdminConnectionHangupNotification**](mpradminconnectionhangupnotification.md) |
| [**RasAdminFreeBuffer**](rasadminfreebuffer.md)                                     | [**MprAdminBufferFree**](mpradminbufferfree.md)                                     |
| [**RasAdminGetErrorString**](rasadmingeterrorstring.md)                             | [**MprAdminGetErrorString**](mpradmingeterrorstring.md)                             |
| [**RasAdminGetIpAddressForUser**](rasadmingetipaddressforuser.md)                   | [**MprAdminGetIpAddressForUser**](mpradmingetipaddressforuser.md)                   |
| [**RasAdminPortClearStatistics**](rasadminportclearstatistics.md)                   | [**MprAdminPortClearStats**](mpradminportclearstats.md)                             |
| [**RasAdminPortDisconnect**](rasadminportdisconnect.md)                             | [**MprAdminPortDisconnect**](mpradminportdisconnect.md)                             |
| [**RasAdminPortEnum**](rasadminportenum.md)                                         | [**MprAdminPortEnum**](mpradminportenum.md)                                         |
| [**RasAdminPortGetInfo**](rasadminportgetinfo.md)                                   | [**MprAdminPortGetInfo**](mpradminportgetinfo.md)                                   |
| [**RasAdminReleaseIpAddress**](rasadminreleaseipaddress.md)                         | [**MprAdminReleaseIpAddress**](mpradminreleaseipaddress.md)                         |
| [**RasAdminUserGetInfo**](rasadminusergetinfo.md)                                   | [**MprAdminUserGetInfo**](mpradminusergetinfo.md)                                   |
| [**RasAdminUserSetInfo**](rasadminusersetinfo.md)                                   | [**MprAdminUserSetInfo**](mpradminusersetinfo.md)                                   |



 

Although the RRAS functions are similar to their Windows NT 4.0 with SP3 and earlier RAS counterparts in functionality, RRAS functions often take a different set of parameters. See the reference page for a particular function for complete information on that function's parameter list.

The RRAS redistributable for Windows NT 4.0 with SP3 and earlier adds the following functions, which have no RAS counterparts:

[**MprAdminAcceptNewLink**](mpradminacceptnewlink.md)

[**MprAdminConnectionClearStats**](mpradminconnectionclearstats.md)

[**MprAdminConnectionEnum**](mpradminconnectionenum.md)

[**MprAdminConnectionGetInfo**](mpradminconnectiongetinfo.md)

[**MprAdminGetPDCServer**](mpradmingetpdcserver.md)

[**MprAdminIsServiceRunning**](mpradminisservicerunning.md)

[**MprAdminLinkHangupNotification**](mpradminlinkhangupnotification.md)

[**MprAdminPortReset**](mpradminportreset.md)

[**MprAdminServerConnect**](mpradminserverconnect.md)

[**MprAdminServerDisconnect**](mpradminserverdisconnect.md)

In addition to the preceding functions, Windows 2000 and later operating systems add the following functions:

[**MprAdminSendUserMessage**](mpradminsendusermessage.md)

[**MprAdminAcceptNewConnection2**](mpradminacceptnewconnection2.md)

[**MprAdminConnectionHangupNotification2**](mpradminconnectionhangupnotification2.md)

 

 




