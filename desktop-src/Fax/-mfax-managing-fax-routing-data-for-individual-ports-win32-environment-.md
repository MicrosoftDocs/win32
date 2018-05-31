---
Description: This topic describes how to manage fax routing data for individual ports in a Microsoft Win32 environment.
ms.assetid: f440de0b-7a31-4df1-8086-d29f98aab47c
title: Managing Fax Routing Data for Individual Ports (Win32 Environment)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managing Fax Routing Data for Individual Ports (Win32 Environment)

A fax administration application can call the [**FaxEnumRoutingMethods**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumroutingmethodsa) function to display all of the fax routing methods associated with a particular device. Call the [**FaxGetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetroutinginfoa) function to query an individual method associated with a device. Both functions return detailed information in [**FAX\_ROUTING\_METHOD**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_routing_methoda) structures, one method per structure. The data includes an indication of whether the fax routing method is enabled for the device, and the name of the DLL that exports the routing method. It also includes the GUID and function name that uniquely identify the routing method, and the method's user-friendly name.

A call to the [**FaxSetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetroutinginfoa) function changes the routing data for a particular fax routing method.

Note that an application must first call the [**FaxOpenPort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxopenport) function to obtain a fax port handle before calling the [**FaxEnumRoutingMethods**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumroutingmethodsa), [**FaxGetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetroutinginfoa), and [**FaxSetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetroutinginfoa) functions.

Because functions that begin with **FaxGet** and **FaxEnum** allocate the memory required for data buffers, the application must call the [**FaxFreeBuffer**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxfreebuffer) function to deallocate these resources.

 

 



