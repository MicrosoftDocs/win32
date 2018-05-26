---
title: DO Structures and Unions
description: The Delivery Optimization (DO) interfaces use the following structures.
ms.assetid: 58A5361E-871A-4911-85BD-83F18CB9A2F5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DO Structures and Unions

The Delivery Optimization (DO) [interfaces](do-interfaces.md) use the following structures.

## In this section



| Topic                                                                      | Description                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DOSwarmStats**](doswarmstats.md)<br/>                            | Contains fields for download and upload statistics for a file.<br/>                                                                                                                                                   |
| [**BG\_FILE\_PROGRESS**](bg-file-progress.md)<br/>                  | The **BG\_FILE\_PROGRESS** structure provides file-related progress information, such as the number of bytes transferred.<br/>                                                                                        |
| [**BG\_FILE\_RANGE**](bg-file-range.md)<br/>                        | The **BG\_FILE\_RANGE** structure identifies a range of bytes to download from a file.<br/>                                                                                                                           |
| [**BG\_JOB\_PROGRESS**](bg-job-progress.md)<br/>                    | The **BG\_JOB\_PROGRESS** structure provides job-related progress information, such as the number of bytes and files transferred. For upload jobs, the progress applies to the upload file, not the reply file. <br/> |
| [**BG\_JOB\_TIMES**](bg-job-times.md)<br/>                          | The **BG\_JOB\_TIMES** structure provides job-related time stamps.<br/>                                                                                                                                               |
| [**BITS\_FILE\_PROPERTY\_VALUE**](bits-file-property-value.md)<br/> | The **BITS\_FILE\_PROPERTY\_VALUE** union provides the property value of the DO file based on a value from the [**BITS\_FILE\_PROPERTY\_ID**](bits-file-property-id-.md) enumeration.<br/>                           |
| [**BITS\_JOB\_PROPERTY\_VALUE**](bits-job-property-value-.md)<br/>  | The **BITS\_JOB\_PROPERTY\_VALUE** union provides the property value of the DO job based on the value of the [**BITS\_JOB\_PROPERTY\_ID**](bits-job-property-id.md) enumeration.<br/>                                |



 

 

 





