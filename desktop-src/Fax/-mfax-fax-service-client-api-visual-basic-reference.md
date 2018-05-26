---
Description: The Fax Service Client API includes the following Component Object Model (COM) objects that are available through Microsoft Visual Basic.
ms.assetid: 3464d7b3-f2d4-4cfe-bc25-988bf04e3082
title: Fax Service Client API Visual Basic Reference
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Service Client API Visual Basic Reference

The Fax Service Client API includes the following Component Object Model (COM) objects that are available through Microsoft Visual Basic.

-   [**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md)
-   [**FaxJob**](-mfax-faxjob-object-visual-basic-.md)
-   [**FaxJobs**](-mfax-faxjobs-object-visual-basic-.md)
-   [**FaxPort**](-mfax-faxport-object-visual-basic-.md)
-   [**FaxPorts**](-mfax-faxports-object-visual-basic-.md)
-   [**FaxRoutingMethod**](-mfax-faxroutingmethod-object-visual-basic-.md)
-   [**FaxRoutingMethods**](-mfax-faxroutingmethods-object-visual-basic-.md)
-   [**FaxServer**](-mfax-faxserver-object-visual-basic-.md)
-   [**FaxStatus**](-mfax-faxstatus-object-visual-basic-.md)
-   [**FaxTiff**](-mfax-faxtiff-object-visual-basic-.md)

You must connect to an active fax server before accessing most objects that begin with **Fax**. (A fax server connection is not required to access a [**FaxTiff**](-mfax-faxtiff-object-visual-basic-.md) object.) To connect to and disconnect from a fax server, use the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object. Call the [**Connect**](-mfax-ifaxserver-connect-client-vb.md) method of the **FaxServer** object to initiate the connection. After you obtain the connection, you can call other methods to create other objects you need.

When you have finished using an object, and before disconnecting from the server, you must destroy each object you have created. To do this, set the variable to `Nothing` as illustrated in the following example.


```
Set objFaxPort = Nothing
Set objFaxPorts = Nothing
```



To disconnect from the server, call the [**Disconnect**](-mfax-ifaxserver-disconnect-client-vb.md) method of the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object.

## Related topics

<dl> <dt>

[The Fax Client Object Model](-mfax-the-fax-client-object-model.md)
</dt> <dt>

[Using the Fax Client COM Implementation with Visual Basic](-mfax-using-the-fax-client-com-implementation-with-visual-basic.md)
</dt> </dl>

 

 



