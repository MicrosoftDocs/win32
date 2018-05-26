---
Description: This topic describes how to query fax port data in the Microsoft Win32 environment.
ms.assetid: 03f68e2a-fceb-4186-aa75-a4bf5658aff5
title: Querying Fax Port Data (Win32 Environment)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Querying Fax Port Data (Win32 Environment)

The [**FaxEnumPorts**](/windows/previous-versions/Winfax/nf-winfax-faxenumportsa?branch=master) function permits a fax client application to display all the fax devices currently attached to the fax server. To query an individual fax device, call the [**FaxGetPort**](/windows/previous-versions/Winfax/nf-winfax-faxgetporta?branch=master) function. Both functions return detailed information for the devices in [**FAX\_PORT\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_port_infoa?branch=master) structures, one device per structure. The data includes the permanent line identifier, and the current status and capability of the port. Note that an application must call the [**FaxOpenPort**](/windows/previous-versions/Winfax/nc-winfax-pfaxopenport?branch=master) function and specify the PORT\_OPEN\_QUERY port access level before calling the **FaxGetPort** function.

To display the current status of one fax device associated with a fax server, call the [**FaxGetDeviceStatus**](/windows/previous-versions/Winfax/nf-winfax-faxgetdevicestatusa?branch=master) function. The function returns the data in a [**FAX\_DEVICE\_STATUS**](/windows/previous-versions/Winfax/ns-winfax-_fax_device_statusa?branch=master) structure. The structure includes the current device status flag, device and station identifiers, sender and recipient names, and fax routing information.

Note that an application must first call the [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master) function to obtain a fax server handle before calling the [**FaxEnumPorts**](/windows/previous-versions/Winfax/nf-winfax-faxenumportsa?branch=master) function. An application must call the [**FaxOpenPort**](/windows/previous-versions/Winfax/nc-winfax-pfaxopenport?branch=master) function, specifying the PORT\_OPEN\_QUERY port access level, to obtain a fax port handle before calling the [**FaxGetDeviceStatus**](/windows/previous-versions/Winfax/nf-winfax-faxgetdevicestatusa?branch=master) function and the [**FaxGetPort**](/windows/previous-versions/Winfax/nf-winfax-faxgetporta?branch=master) function.

Because functions that begin with **FaxGet** and **FaxEnum** allocate the memory required for data buffers, the application must call the [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master) function to deallocate these resources.

To modify a fax device's configuration settings, an application can call the [**FaxSetPort**](/windows/previous-versions/Winfax/nf-winfax-faxsetporta?branch=master) function.

 

 



