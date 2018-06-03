---
title: Access Point Initialization of EAP
description: Upon initialization, the Access Point (AP) queries the registry for installed authentication protocols.
ms.assetid: e230e01f-27df-4f61-8755-262ec11af660
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Access Point Initialization of EAP

Upon initialization, the Access Point (AP) queries the registry for installed authentication protocols. The AP then calls the exported function [**RasEapGetInfo**](/previous-versions/windows/desktop/api/Raseapif/nf-raseapif-raseapgetinfo) for each authentication protocol. The **RasEapGetInfo** function receives a single parameter of type [**PPP\_EAP\_INFO**](/previous-versions/windows/desktop/api/Raseapif/ns-raseapif-_ppp_eap_info). The AP uses the **dwEapTypeId** member of this structure to specify the authentication protocol. Note that a single DLL may support more than one protocol. If **RasEapGetInfo** returns any value other than **NO\_ERROR**, the AP assumes that the authentication protocol is unavailable.

On return from [**RasEapGetInfo**](/previous-versions/windows/desktop/api/Raseapif/nf-raseapif-raseapgetinfo) the [**PPP\_EAP\_INFO**](/previous-versions/windows/desktop/api/Raseapif/ns-raseapif-_ppp_eap_info) structure contains pointers to the functions [**RasEapInitialize**](https://www.bing.com/search?q=**RasEapInitialize**), [**RasEapBegin**](https://www.bing.com/search?q=**RasEapBegin**), [**RasEapMakeMessage**](https://www.bing.com/search?q=**RasEapMakeMessage**), and [**RasEapEnd**](https://www.bing.com/search?q=**RasEapEnd**) in the EAP DLL. The AP service uses these functions to interoperate with the authentication protocol. The AP immediately calls **RasEapInitialize** for each authentication protocol, to initialize it. When the service shuts down it calls **RasEapInitialize** again, this time with the *fInitialize* parameter set to **FALSE** to indicate that the authentication protocol should shut itself down.

 

 




