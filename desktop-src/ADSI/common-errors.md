---
title: Common Errors (ADSI)
description: All ADSI-specific errors have a hexadecimal form of 80005xxx. The most common error codes encountered are outlined in the following table.
ms.assetid: fdee4f0a-b39e-4011-af4f-9fe408f6ca6c
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Common Errors (ADSI)

All ADSI-specific errors have a hexadecimal form of 80005xxx. The most common error codes encountered are outlined in the following table.



| ADSI hex error code | Description                                                                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 80005000<br/> | An invalid ADSI pathname was passed. This error results from passing a poorly formed ADsPath to **GetObject** when binding to an object.<br/> |
| 8000500D<br/> | The ADSI property cannot be found in the property cache.<br/>                                                                                 |
| 8000500E<br/> | The ADSI object exists. If you attempt to create an ADSI object with the same name as an existing ADSI object, this error will occur.<br/>    |



 

For a complete list of ADSI error codes, see [Generic ADSI Error Codes](generic-adsi-error-codes.md).

## COM Errors

Since ADSI is composed of COM objects, it will return standard COM error codes. The following table lists the COM error codes most commonly encountered in ADSI programming.



| COM hex error code  | Description                                                                                                                   |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| 80004005<br/> | Unspecified error. The cause of the COM object failure is indeterminate by ADSI. <br/>                                  |
| 800041E4<br/> | Object not found. This error predominantly occurs due to misspelling the ADsPath string when binding to an object.<br/> |



 

See [Generic COM Error Codes](generic-com-error-codes.md) for a few more examples of COM errors that may occur in ADSI programming.

## Win32 Errors

Any error code of the hexadecimal form 8007xxxx is a standard Win32 error code. If you convert the last four digits from hexadecimal to decimal, you can access the error from the Windows 2000 command line:

**net helpmsg &lt;number&gt;**

In the command line above, "&lt;number&gt;" is the decimal number obtained by converting the last four digits of the error code from hexadecimal. This command line will provide a more useful description of the Win32 error, which can be of great help in debugging your script.

 

 





