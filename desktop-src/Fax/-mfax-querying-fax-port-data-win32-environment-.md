---
Description: This topic describes how to query fax port data in the Microsoft Win32 environment.
ms.assetid: 03f68e2a-fceb-4186-aa75-a4bf5658aff5
title: Querying Fax Port Data (Win32 Environment)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying Fax Port Data (Win32 Environment)

The [**FaxEnumPorts**](-mfax-faxenumports.md) function permits a fax client application to display all the fax devices currently attached to the fax server. To query an individual fax device, call the [**FaxGetPort**](-mfax-faxgetport.md) function. Both functions return detailed information for the devices in [**FAX\_PORT\_INFO**](-mfax-fax-port-info-str.md) structures, one device per structure. The data includes the permanent line identifier, and the current status and capability of the port. Note that an application must call the [**FaxOpenPort**](-mfax-faxopenport.md) function and specify the PORT\_OPEN\_QUERY port access level before calling the **FaxGetPort** function.

To display the current status of one fax device associated with a fax server, call the [**FaxGetDeviceStatus**](-mfax-faxgetdevicestatus.md) function. The function returns the data in a [**FAX\_DEVICE\_STATUS**](-mfax-fax-device-status-str.md) structure. The structure includes the current device status flag, device and station identifiers, sender and recipient names, and fax routing information.

Note that an application must first call the [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md) function to obtain a fax server handle before calling the [**FaxEnumPorts**](-mfax-faxenumports.md) function. An application must call the [**FaxOpenPort**](-mfax-faxopenport.md) function, specifying the PORT\_OPEN\_QUERY port access level, to obtain a fax port handle before calling the [**FaxGetDeviceStatus**](-mfax-faxgetdevicestatus.md) function and the [**FaxGetPort**](-mfax-faxgetport.md) function.

Because functions that begin with **FaxGet** and **FaxEnum** allocate the memory required for data buffers, the application must call the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function to deallocate these resources.

To modify a fax device's configuration settings, an application can call the [**FaxSetPort**](-mfax-faxsetport.md) function.

 

 



