---
Description: This topic describes how to manage fax routing data for individual ports in a Microsoft Win32 environment.
ms.assetid: f440de0b-7a31-4df1-8086-d29f98aab47c
title: Managing Fax Routing Data for Individual Ports (Win32 Environment)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Fax Routing Data for Individual Ports (Win32 Environment)

A fax administration application can call the [**FaxEnumRoutingMethods**](/windows/previous-versions/Winfax/nf-winfax-faxenumroutingmethodsa?branch=master) function to display all of the fax routing methods associated with a particular device. Call the [**FaxGetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxgetroutinginfoa?branch=master) function to query an individual method associated with a device. Both functions return detailed information in [**FAX\_ROUTING\_METHOD**](/windows/previous-versions/Winfax/ns-winfax-_fax_routing_methoda?branch=master) structures, one method per structure. The data includes an indication of whether the fax routing method is enabled for the device, and the name of the DLL that exports the routing method. It also includes the GUID and function name that uniquely identify the routing method, and the method's user-friendly name.

A call to the [**FaxSetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxsetroutinginfoa?branch=master) function changes the routing data for a particular fax routing method.

Note that an application must first call the [**FaxOpenPort**](/windows/previous-versions/Winfax/nc-winfax-pfaxopenport?branch=master) function to obtain a fax port handle before calling the [**FaxEnumRoutingMethods**](/windows/previous-versions/Winfax/nf-winfax-faxenumroutingmethodsa?branch=master), [**FaxGetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxgetroutinginfoa?branch=master), and [**FaxSetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxsetroutinginfoa?branch=master) functions.

Because functions that begin with **FaxGet** and **FaxEnum** allocate the memory required for data buffers, the application must call the [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master) function to deallocate these resources.

 

 



