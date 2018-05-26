---
Description: This topic describes how to query global routing method data in the Microsoft Win32 environment.
ms.assetid: 858b2326-7634-4021-8cff-128bbc167aba
title: Managing Global Fax Routing Data
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Global Fax Routing Data

This functionality is currently available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

A fax client application can call the [**FaxEnumGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxenumglobalroutinginfoa?branch=master) function to query global routing method data. The function returns the data in a [**FAX\_GLOBAL\_ROUTING\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_global_routing_infoa?branch=master) structure. The information includes the priority level of the fax routing method, and the name of the DLL that exports the routing method. It also includes the GUID and function name that identify the fax routing method, and the method's user-friendly name.

Because the [**FaxEnumGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxenumglobalroutinginfoa?branch=master) function allocates the memory required for the [**FAX\_GLOBAL\_ROUTING\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_global_routing_infoa?branch=master) structure, the application must call the [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master) function to deallocate these resources.

Call the [**FaxSetGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxsetglobalroutinginfoa?branch=master) function to modify global routing method data. (Currently the priority of the routing method is the only global value that an application can modify.)

Note that an application must first call the [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master) function to obtain a fax server handle before calling the [**FaxEnumGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxenumglobalroutinginfoa?branch=master) function and the [**FaxSetGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxsetglobalroutinginfoa?branch=master) function.

## Related topics

<dl> <dt>

[Fax Server Configuration Management](-mfax-fax-server-configuration-management.md)
</dt> </dl>

 

 



