---
Description: This tutorial summarizes typical programming tasks required to incorporate the functionality of the Fax Service Client API in a Microsoft Visual Basic fax client application if you are using the Component Object Model (COM) implementation.
ms.assetid: 7d2f818a-c303-4939-8247-781e10f49275
title: Using the COM Implementation in a Visual Basic Program
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the COM Implementation in a Visual Basic Program

The following steps summarize typical programming tasks required to incorporate the functionality of the Fax Service Client API in a Microsoft Visual Basic fax client application if you are using the Component Object Model (COM) implementation.

## To code a fax client application

1.  Create an instance of a [**FaxServer**](-mfax-faxserver.md) object by calling the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function. Then connect to an active fax server by calling the [**Connect**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxserver-connect) method of the object. For more information, see [Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md).

2.  To create other objects you need, call one or more of the following methods of the [**FaxServer**](-mfax-faxserver.md) object.

    -   To create a [FaxJobs](-mfax-faxjobs.md) object, call the [**GetJobs**](/previous-versions/windows/desktop/api/faxcomex/) method. Use this object to create [FaxJob](-mfax-faxjob.md) objects and enumerate the fax jobs associated with the connected fax server.
    -   To create a [FaxPorts](-mfax-faxports.md) object, call the [**GetPorts**](/previous-versions/windows/desktop/api/faxcomex/) method. Use this object to create [FaxPort](-mfax-faxport.md) objects and enumerate fax port configuration information for the connected fax server.
    -   To create a [FaxDoc](-mfax-faxdoc.md) object, call the [**CreateDocument**](/previous-versions/windows/desktop/api/faxcomex/) method. Use this object to transmit a fax and to retrieve and set the properties of FaxDoc objects.

3.  After creating an instance of a [FaxPort](-mfax-faxport.md) object for a specific port, create a [FaxRoutingMethods](-mfax-faxroutingmethods.md) object by calling the [**GetRoutingMethods**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxport-getroutingmethods) method of the object.

4.  Create a [FaxRoutingMethod](-mfax-faxroutingmethod.md) object by calling the [**Item**](-mfax-faxinboundroutingmethods-item.md) method of the [FaxRoutingMethods](-mfax-faxroutingmethods.md) object. The FaxRoutingMethod object allows you to query and modify the fax routing information for a fax port. For more information, see [Managing Fax Routing Data](-mfax-managing-fax-routing-data.md).

5.  Create a [FaxStatus](-mfax-faxstatus.md) object by calling the [**GetStatus**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxport-getstatus) method of the [FaxPort](-mfax-faxport.md) object. The FaxStatus object allows you to provide real-time status information about a fax port.

6.  After creating an instance of a [FaxDoc](-mfax-faxdoc.md) object, transmit a fax document by calling the [**Send**](/previous-versions/windows/desktop/api/Faxcom/) method of the object. Note that the application must supply transmission information such as the fax number and the name of the file to transmit. The client can also supply other data that appears on the cover page by setting various properties of the FaxDoc object. For more information, see [Transmitting Faxes](-mfax-transmitting-faxes.md).

7.  Terminate the connection to the fax server by calling the [**IFaxServer::Disconnect**](/previous-versions/windows/desktop/api/FaxComex/) method of the [**FaxServer**](-mfax-faxserver.md) object. For more information, see [Disconnecting from a Fax Server](-mfax-disconnecting-from-a-fax-server.md).

In addition, the application may need to set other properties and call other methods to query device or server configuration data and to manage fax jobs. You may also need to create an instance of a [FaxTiff](-mfax-faxtiff.md) object to retrieve information about a file the fax service has sent or received.

For more information, see [Fax Server Configuration Management](-mfax-fax-server-configuration-management.md), [Fax Device Management](-mfax-fax-device-management.md), [Managing Fax Jobs](-mfax-managing-fax-jobs.md), and [General Fax Client Programming Tasks](-mfax-general-fax-client-programming-tasks.md).

For more information about creating and deallocating fax client objects, see the [Fax Service Client API Visual Basic Reference](-mfax-fax-service-client-api-visual-basic-reference.md) and the hierarchical diagram included in [The Fax Client Object Model](-mfax-the-fax-client-object-model.md).

 

 



