---
Description: This topic describes how to query global routing method data in the Microsoft Win32 environment.
ms.assetid: 858b2326-7634-4021-8cff-128bbc167aba
title: Managing Global Fax Routing Data
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managing Global Fax Routing Data

This functionality is currently available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

A fax client application can call the [**FaxEnumGlobalRoutingInfo**](-mfax-faxenumglobalroutinginfo.md) function to query global routing method data. The function returns the data in a [**FAX\_GLOBAL\_ROUTING\_INFO**](-mfax-fax-global-routing-info-str.md) structure. The information includes the priority level of the fax routing method, and the name of the DLL that exports the routing method. It also includes the GUID and function name that identify the fax routing method, and the method's user-friendly name.

Because the [**FaxEnumGlobalRoutingInfo**](-mfax-faxenumglobalroutinginfo.md) function allocates the memory required for the [**FAX\_GLOBAL\_ROUTING\_INFO**](-mfax-fax-global-routing-info-str.md) structure, the application must call the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function to deallocate these resources.

Call the [**FaxSetGlobalRoutingInfo**](-mfax-faxsetglobalroutinginfo.md) function to modify global routing method data. (Currently the priority of the routing method is the only global value that an application can modify.)

Note that an application must first call the [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md) function to obtain a fax server handle before calling the [**FaxEnumGlobalRoutingInfo**](-mfax-faxenumglobalroutinginfo.md) function and the [**FaxSetGlobalRoutingInfo**](-mfax-faxsetglobalroutinginfo.md) function.

## Related topics

<dl> <dt>

[Fax Server Configuration Management](-mfax-fax-server-configuration-management.md)
</dt> </dl>

 

 



