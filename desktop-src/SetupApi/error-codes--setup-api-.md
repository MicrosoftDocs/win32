---
description: The following error codes are specific to the Setup API.
ms.assetid: C4EB130F-2A83-4A14-BBA8-DB10225D0C0A
title: Error Codes (Setup API)
ms.topic: article
ms.date: 05/31/2018
---

# Error Codes (Setup API)

The following error codes are specific to the Setup API.



| INF Parsing Errors              | Description                                                                                                         |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ERROR\_EXPECTED\_SECTION\_NAME  | A section name was expected and not found.                                                                          |
| ERROR\_BAD\_SECTION\_NAME\_LINE | The section name was not of the correct format. (For example, a name not terminated by a right-hand bracket ( \] ). |
| ERROR\_SECTION\_NAME\_TOO\_LONG | The section name exceeded the maximum length of MAX\_SECT\_NAME\_LEN.                                               |
| ERROR\_GENERAL\_SYNTAX          | The general syntax is incorrect.                                                                                    |



 



| INF Runtime Errors         | Description                                                                                                                                                                                                                                    |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR\_WRONG\_INF\_STYLE   | The INF file is not of the type specified in the function call. For example, this error may be returned by the [**SetupOpenAppendInfFile**](/windows/desktop/api/Setupapi/nf-setupapi-setupopenappendinffilea) function if the INF file was intended for an early version of Windows. |
| ERROR\_SECTION\_NOT\_FOUND | The section was not found in the INF file.                                                                                                                                                                                                     |
| ERROR\_LINE\_NOT\_FOUND    | The line was not found in the INF section.                                                                                                                                                                                                     |



 

 

 



