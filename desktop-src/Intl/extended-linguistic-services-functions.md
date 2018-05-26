---
Description: ELS supports the functions defined in the following table.
ms.assetid: d62ab664-a75a-4d06-aefb-a3311ea7d4a7
title: Extended Linguistic Services Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Extended Linguistic Services Functions

ELS supports the functions defined in the following table.



| Function                                                 | Description                                                                                                                                    |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MappingCallbackProc**](/windows/win32/Elscore/nc-elscore-pfn_mappingcallbackproc?branch=master)       | An application-defined callback function that asynchronously processes data produced by the **MappingRecognizeText** function.                 |
| [**MappingDoAction**](/windows/win32/Elscore/nf-elscore-mappingdoaction?branch=master)               | Causes an ELS service to perform an action after text recognition has occurred.                                                                |
| [**MappingFreePropertyBag**](/windows/win32/Elscore/nf-elscore-mappingfreepropertybag?branch=master) | Frees memory and resources allocated during an ELS text recognition operation.                                                                 |
| [**MappingFreeServices**](/windows/win32/Elscore/nf-elscore-mappingfreeservices?branch=master)       | Frees memory and resources allocated for the application to interact with one or more ELS services.                                            |
| [**MappingGetServices**](/windows/win32/Elscore/nf-elscore-mappinggetservices?branch=master)         | Retrieves a list of available ELS platform-supported services, along with associated information, according to application-specified criteria. |
| [**MappingRecognizeText**](/windows/win32/Elscore/nf-elscore-mappingrecognizetext?branch=master)     | Calls upon an ELS service to recognize text.                                                                                                   |



 

 

 



