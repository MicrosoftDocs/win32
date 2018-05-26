---
title: Routing Protocol Interface Functions
description: Implement the following functions for a routing protocol DLL
ms.assetid: fd780458-ef23-4ef2-8fe8-29b32100917f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Routing Protocol Interface Functions

Implement the following functions for a routing protocol DLL:

[**AddInterface**](/windows/win32/Routprot/nc-routprot-padd_interface?branch=master)

[**ConnectClient**](/windows/win32/Routprot/nc-routprot-pconnect_client?branch=master)

[**DeleteInterface**](/windows/win32/Routprot/nc-routprot-pdelete_interface?branch=master)

[**DisconnectClient**](/windows/win32/Routprot/nc-routprot-pdisconnect_client?branch=master)

[**DoUpdateRoutes**](/windows/win32/Routprot/nc-routprot-pdo_update_routes?branch=master)

[*DoUpdateServices*](https://msdn.microsoft.com/library/windows/desktop/aa374005)

[**GetEventMessage**](/windows/win32/Routprot/nc-routprot-pget_event_message?branch=master)

[**GetGlobalInfo**](/windows/win32/Routprot/nc-routprot-pget_global_info?branch=master)

[**GetInterfaceInfo**](/windows/win32/Routprot/nc-routprot-pget_interface_info?branch=master)

[**GetMfeStatus**](/windows/win32/Routprot/nc-routprot-pget_mfe_status?branch=master)

[**GetNeighbors**](/windows/win32/Routprot/nc-routprot-pget_neighbors?branch=master)

[**InterfaceStatus**](/windows/win32/Routprot/nc-routprot-pinterface_status?branch=master)

[**MibCreate**](/windows/win32/Routprot/nc-routprot-pmib_create?branch=master)

[**MibDelete**](/windows/win32/Routprot/nc-routprot-pmib_delete?branch=master)

[**MibGet**](/windows/win32/Routprot/nc-routprot-pmib_get?branch=master)

[**MibGetFirst**](/windows/win32/Routprot/nc-routprot-pmib_get_first?branch=master)

[**MibGetNext**](/windows/win32/Routprot/nc-routprot-pmib_get_next?branch=master)

[*MibGetTrapInfo*](/windows/win32/Routprot/nc-routprot-pmib_get_trap_info?branch=master)

[**MibSet**](/windows/win32/Routprot/nc-routprot-pmib_set?branch=master)

[**MibSetTrapInfo**](/windows/win32/Routprot/nc-routprot-pmib_set_trap_info?branch=master)

[**QueryPower**](/windows/win32/Routprot/nc-routprot-pquery_power?branch=master)

[**RegisterProtocol**](/windows/win32/Routprot/nc-routprot-pregister_protocol?branch=master)

[**SetGlobalInfo**](/windows/win32/Routprot/nc-routprot-pset_global_info?branch=master)

[**SetInterfaceInfo**](/windows/win32/Routprot/nc-routprot-pset_interface_info?branch=master)

[**SetPower**](/windows/win32/Routprot/nc-routprot-pset_power?branch=master)

[**StartComplete**](/windows/win32/Routprot/nc-routprot-pstart_complete?branch=master)

[**StartProtocol**](/windows/win32/Routprot/nc-routprot-pstart_protocol?branch=master)

[**StopProtocol**](/windows/win32/Routprot/nc-routprot-pstop_protocol?branch=master)

[**UnbindInterface**](https://msdn.microsoft.com/library/windows/desktop/aa382296)

If the routing protocol supports service handling, implement the following function in addition to those listed preceding:

[**DoUpdateServices**](https://msdn.microsoft.com/library/windows/desktop/aa374005)

 

 




