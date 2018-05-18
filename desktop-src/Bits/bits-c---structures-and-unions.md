---
title: BITS Structures and Unions
description: The Background Intelligent Transfer Service (BITS) interfaces use the following structures.
ms.assetid: 'a1b8b4a1-77d6-46ac-96d5-6a0c99cfc643'
---

# BITS Structures and Unions

The Background Intelligent Transfer Service (BITS) [interfaces](bits-interfaces.md) use the following structures.

## In this section



| Topic                                                                        | Description                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BG\_AUTH\_CREDENTIALS**](bg-auth-credentials.md)<br/>              | The [**BG\_AUTH\_CREDENTIALS**](bg-auth-credentials.md) structure identifies the target (proxy or server), authentication scheme, and the user's credentials to use for user authentication requests. The structure is passed to the [**IBackgroundCopyJob2::SetCredentials**](ibackgroundcopyjob2-setcredentials.md) method.<br/>                  |
| [**BG\_AUTH\_CREDENTIALS\_UNION**](bg-auth-credentials-union.md)<br/> | The [**BG\_AUTH\_CREDENTIALS\_UNION**](bg-auth-credentials-union.md) union identifies the credentials to use for the authentication scheme specified in the [**BG\_AUTH\_CREDENTIALS**](bg-auth-credentials.md) structure.<br/>                                                                                                                     |
| [**BG\_BASIC\_CREDENTIALS**](bg-basic-credentials.md)<br/>            | The [**BG\_BASIC\_CREDENTIALS**](bg-basic-credentials.md) structure identifies the user name and password to authenticate.<br/>                                                                                                                                                                                                                      |
| [**BG\_FILE\_INFO**](bg-file-info.md)<br/>                            | The [**BG\_FILE\_INFO**](bg-file-info.md) structure provides the local and remote names of the file to transfer.<br/>                                                                                                                                                                                                                                |
| [**BG\_FILE\_PROGRESS**](bg-file-progress.md)<br/>                    | The [**BG\_FILE\_PROGRESS**](bg-file-progress.md) structure provides file-related progress information, such as the number of bytes transferred.<br/>                                                                                                                                                                                                |
| [**BG\_FILE\_RANGE**](bg-file-range.md)<br/>                          | The [**BG\_FILE\_RANGE**](bg-file-range.md) structure identifies a range of bytes to download from a file.<br/>                                                                                                                                                                                                                                      |
| [**BG\_JOB\_PROGRESS**](bg-job-progress.md)<br/>                      | The [**BG\_JOB\_PROGRESS**](bg-job-progress.md) structure provides job-related progress information, such as the number of bytes and files transferred. For upload jobs, the progress applies to the upload file, not the reply file. To view reply file progress, see the [**BG\_JOB\_REPLY\_PROGRESS**](bg-job-reply-progress.md) structure.<br/> |
| [**BG\_JOB\_REPLY\_PROGRESS**](bg-job-reply-progress.md)<br/>         | The [**BG\_JOB\_REPLY\_PROGRESS**](bg-job-reply-progress.md) structure provides progress information related to the reply portion of an upload-reply job.<br/>                                                                                                                                                                                       |
| [**BG\_JOB\_TIMES**](bg-job-times.md)<br/>                            | The [**BG\_JOB\_TIMES**](bg-job-times.md) structure provides job-related time stamps.<br/>                                                                                                                                                                                                                                                           |
| [**BITS\_FILE\_PROPERTY\_VALUE**](bits-file-property-value.md)<br/>   | Provides the property value of a BITS file.<br/>                                                                                                                                                                                                                                                                                                      |
| [**BITS\_JOB\_PROPERTY\_VALUE**](bits-job-property-value.md)<br/>     | Provides the property value of the BITS job based on the value of the [**BITS\_JOB\_PROPERTY\_ID**](bits-job-property-id.md) enumeration.<br/>                                                                                                                                                                                                       |



 

 

 





