---
title: DO Structures and Unions
description: The Delivery Optimization (DO) interfaces use the following structures.
ms.assetid: 58A5361E-871A-4911-85BD-83F18CB9A2F5
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DO Structures and Unions

The Delivery Optimization (DO) [interfaces](do-interfaces.md) use the following structures.

## In this section



| Topic                                                                      | Description                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DOSwarmStats**](doswarmstats.md)<br/>                            | Contains fields for download and upload statistics for a file.<br/>                                                                                                                                                   |
| [**BG_FILE_PROGRESS**](bg-file-progress.md)<br/>                  | The **BG_FILE_PROGRESS** structure provides file-related progress information, such as the number of bytes transferred.<br/>                                                                                        |
| [**BG_FILE_RANGE**](bg-file-range.md)<br/>                        | The **BG_FILE_RANGE** structure identifies a range of bytes to download from a file.<br/>                                                                                                                           |
| [**BG_JOB_PROGRESS**](bg-job-progress.md)<br/>                    | The **BG_JOB_PROGRESS** structure provides job-related progress information, such as the number of bytes and files transferred. For upload jobs, the progress applies to the upload file, not the reply file. <br/> |
| [**BG_JOB_TIMES**](bg-job-times.md)<br/>                          | The **BG_JOB_TIMES** structure provides job-related time stamps.<br/>                                                                                                                                               |
| [**BITS_FILE_PROPERTY_VALUE**](bits-file-property-value.md)<br/> | The **BITS_FILE_PROPERTY_VALUE** union provides the property value of the DO file based on a value from the [**BITS_FILE_PROPERTY_ID**](bits-file-property-id-.md) enumeration.<br/>                           |
| [**BITS_JOB_PROPERTY_VALUE**](bits-job-property-value-.md)<br/>  | The **BITS_JOB_PROPERTY_VALUE** union provides the property value of the DO job based on the value of the [**BITS_JOB_PROPERTY_ID**](bits-job-property-id.md) enumeration.<br/>                                |



 

 

 





