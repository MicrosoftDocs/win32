---
Description: A fax routing method can call one or more callback functions to manage the files in the fax file list associated with a received fax document.
ms.assetid: fadb1b42-416f-4e26-8817-808b445ab305
title: Managing a Fax File List
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managing a Fax File List

A fax routing method can call one or more callback functions to manage the files in the fax file list associated with a received fax document.

Before the first fax routing method runs, the only file in the fax file list is the received Tagged Image File Format Class F (TIFF Class F) file. A fax routing method can use the received Tagged Image File Format (TIFF) file as a read-only resource to create and add one or more files to the document's fax file list.

For example, the method could convert the received TIFF file to an editable text file. Then the method could add the text file to the fax file list associated with the received fax. To add the file to the fax file list, the fax routing method must call the [**FaxRouteAddFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxrouteaddfile) callback function and provide a pointer to the path and name of the text file.

A fax routing method calls the [**FaxRouteDeleteFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutedeletefile) callback function to delete files that a fax routing extension's method has added to the fax file list. The fax routing method cannot modify the initial TIFF file or remove it from the fax file list.

To enumerate the files in the fax file list, a fax routing method calls the [**FaxRouteEnumFiles**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxrouteenumfiles) callback function. **FaxRouteEnumFiles** passes a pointer to the [**FaxRouteEnumFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxrouteenumfile) callback function. (The routing extension must define a **FaxRouteEnumFile** function.) The fax service calls **FaxRouteEnumFile** once for each file in the fax file list. This function returns the fully qualified path and name of each file in the list.

The fax routing method can also call the [**FaxRouteGetFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutegetfile) callback function using a file's index to retrieve a specific file name from the fax file list. The fax routing method must call the **FaxRouteGetFile** function twice. The first time the routing method calls **FaxRouteGetFile**, it must pass a **NULL** pointer in the *FileNameBuffer* parameter. The fax service sets the *RequiredSize* parameter to the size required for the *FileNameBuffer*. The fax routing method must allocate the memory required for the buffer from the heap specified by the [**FaxRouteInitialize**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxrouteinitialize) function, and call **FaxRouteGetFile** again. The second time the routing method calls **FaxRouteGetFile** it must pass a valid pointer in the *FileNameBuffer* parameter.

The fax service passes function pointers to the [**FaxRouteAddFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxrouteaddfile), [**FaxRouteDeleteFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutedeletefile), [**FaxRouteGetFile**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutegetfile), [**FaxRouteModifyRoutingData**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxroutemodifyroutingdata), and [**FaxRouteEnumFiles**](/previous-versions/windows/desktop/api/FaxRoute/nc-faxroute-pfaxrouteenumfiles) callback functions when the fax service calls the [**FaxRouteInitialize**](/previous-versions/windows/desktop/api/FaxRoute/nf-faxroute-faxrouteinitialize) function. The service passes the pointers in a [**FAX\_ROUTE\_CALLBACKROUTINES**](/previous-versions/windows/desktop/api/FaxRoute/ns-faxroute-_fax_route_callbackroutines) structure.

## Related topics

<dl> <dt>

[Fax File Lists](-mfax-fax-file-lists.md)
</dt> </dl>

 

 



