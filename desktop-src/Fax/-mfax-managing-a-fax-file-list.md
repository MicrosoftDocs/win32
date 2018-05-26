---
Description: A fax routing method can call one or more callback functions to manage the files in the fax file list associated with a received fax document.
ms.assetid: fadb1b42-416f-4e26-8817-808b445ab305
title: Managing a Fax File List
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing a Fax File List

A fax routing method can call one or more callback functions to manage the files in the fax file list associated with a received fax document.

Before the first fax routing method runs, the only file in the fax file list is the received Tagged Image File Format Class F (TIFF Class F) file. A fax routing method can use the received Tagged Image File Format (TIFF) file as a read-only resource to create and add one or more files to the document's fax file list.

For example, the method could convert the received TIFF file to an editable text file. Then the method could add the text file to the fax file list associated with the received fax. To add the file to the fax file list, the fax routing method must call the [**FaxRouteAddFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxrouteaddfile?branch=master) callback function and provide a pointer to the path and name of the text file.

A fax routing method calls the [**FaxRouteDeleteFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutedeletefile?branch=master) callback function to delete files that a fax routing extension's method has added to the fax file list. The fax routing method cannot modify the initial TIFF file or remove it from the fax file list.

To enumerate the files in the fax file list, a fax routing method calls the [**FaxRouteEnumFiles**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxrouteenumfiles?branch=master) callback function. **FaxRouteEnumFiles** passes a pointer to the [**FaxRouteEnumFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxrouteenumfile?branch=master) callback function. (The routing extension must define a **FaxRouteEnumFile** function.) The fax service calls **FaxRouteEnumFile** once for each file in the fax file list. This function returns the fully qualified path and name of each file in the list.

The fax routing method can also call the [**FaxRouteGetFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutegetfile?branch=master) callback function using a file's index to retrieve a specific file name from the fax file list. The fax routing method must call the **FaxRouteGetFile** function twice. The first time the routing method calls **FaxRouteGetFile**, it must pass a **NULL** pointer in the *FileNameBuffer* parameter. The fax service sets the *RequiredSize* parameter to the size required for the *FileNameBuffer*. The fax routing method must allocate the memory required for the buffer from the heap specified by the [**FaxRouteInitialize**](/windows/previous-versions/FaxRoute/nf-faxroute-faxrouteinitialize?branch=master) function, and call **FaxRouteGetFile** again. The second time the routing method calls **FaxRouteGetFile** it must pass a valid pointer in the *FileNameBuffer* parameter.

The fax service passes function pointers to the [**FaxRouteAddFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxrouteaddfile?branch=master), [**FaxRouteDeleteFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutedeletefile?branch=master), [**FaxRouteGetFile**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutegetfile?branch=master), [**FaxRouteModifyRoutingData**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxroutemodifyroutingdata?branch=master), and [**FaxRouteEnumFiles**](/windows/previous-versions/FaxRoute/nc-faxroute-pfaxrouteenumfiles?branch=master) callback functions when the fax service calls the [**FaxRouteInitialize**](/windows/previous-versions/FaxRoute/nf-faxroute-faxrouteinitialize?branch=master) function. The service passes the pointers in a [**FAX\_ROUTE\_CALLBACKROUTINES**](/windows/previous-versions/FaxRoute/ns-faxroute-_fax_route_callbackroutines?branch=master) structure.

## Related topics

<dl> <dt>

[Fax File Lists](-mfax-fax-file-lists.md)
</dt> </dl>

 

 



