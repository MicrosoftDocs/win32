---
description: ELS supports the functions defined in the following table.
ms.assetid: d62ab664-a75a-4d06-aefb-a3311ea7d4a7
title: Extended Linguistic Services Functions
ms.topic: article
ms.date: 05/31/2018
---

# Extended Linguistic Services Functions

ELS supports the functions defined in the following table.



| Function                                                 | Description                                                                                                                                    |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MappingCallbackProc**](/windows/desktop/api/Elscore/nc-elscore-pfn_mappingcallbackproc)       | An application-defined callback function that asynchronously processes data produced by the **MappingRecognizeText** function.                 |
| [**MappingDoAction**](/windows/desktop/api/Elscore/nf-elscore-mappingdoaction)               | Causes an ELS service to perform an action after text recognition has occurred.                                                                |
| [**MappingFreePropertyBag**](/windows/desktop/api/Elscore/nf-elscore-mappingfreepropertybag) | Frees memory and resources allocated during an ELS text recognition operation.                                                                 |
| [**MappingFreeServices**](/windows/desktop/api/Elscore/nf-elscore-mappingfreeservices)       | Frees memory and resources allocated for the application to interact with one or more ELS services.                                            |
| [**MappingGetServices**](/windows/desktop/api/Elscore/nf-elscore-mappinggetservices)         | Retrieves a list of available ELS platform-supported services, along with associated information, according to application-specified criteria. |
| [**MappingRecognizeText**](/windows/desktop/api/Elscore/nf-elscore-mappingrecognizetext)     | Calls upon an ELS service to recognize text.                                                                                                   |



 

 

 



