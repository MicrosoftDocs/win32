---
Description: Fax service methods return an HRESULT value indicating success or failure. If the method succeeds, it returns S\_OK. Otherwise, it returns a Component Object Model (COM)-defined error code.
ms.assetid: b5d59fec-2802-40bd-8ce4-748137f30fb2
title: Fax Error Codes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Error Codes

Fax service methods return an **HRESULT** value indicating success or failure. If the method succeeds, it returns S\_OK. Otherwise, it returns a Component Object Model (COM)-defined error code.

You should not check directly for success or failure. Use the COM [SUCCEEDED](http://msdn.microsoft.com/en-us/library/ms687197.aspx) and [FAILED](http://msdn.microsoft.com/en-us/library/ms693474.aspx) macros instead.

The fax service extended COM API supports the [IErrorInfo](http://msdn.microsoft.com/en-us/library/ms221233.aspx) interface when reporting errors.

Methods that include remote procedure call (RPC) calls as part of their implementation can return any type of RPC error (Microsoft Win32 error) disguised as an **HRESULT**.

In addition, there are error codes that are specific to the fax service, as shown in the following table.



| Error ID                              | Value      | Remarks                                                                                                                                 |
|---------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| FAX\_E\_SRV\_OUTOFMEMORY              | 0x80041b59 | The fax server failed to allocate memory.                                                                                               |
| FAX\_E\_GROUP\_NOT\_FOUND             | 0x80041b5a | The fax server failed to locate an outbound routing group by name.                                                                      |
| FAX\_E\_BAD\_GROUP\_CONFIGURATION     | 0x80041b5b | The fax server encountered an outbound routing group with bad configuration.                                                            |
| FAX\_E\_GROUP\_IN\_USE                | 0x80041b5c | The fax server cannot remove an outbound routing group because it is in use by one or more outbound routing rules.                      |
| FAX\_E\_RULE\_NOT\_FOUND              | 0x80041b5d | The fax server failed to locate an outbound routing rule by country/region code and area code.                                          |
| FAX\_E\_NOT\_NTFS                     | 0x80041b5e | The fax server cannot set an archive folder to a non-NTFS partition.                                                                    |
| FAX\_E\_DIRECTORY\_IN\_USE            | 0x80041b5f | The fax server cannot use the same folder for both the inbox and the sent-items archives.                                               |
| FAX\_E\_FILE\_ACCESS\_DENIED          | 0x80041b60 | The fax server cannot access the specified file or folder.                                                                              |
| FAX\_E\_MESSAGE\_NOT\_FOUND           | 0x80041b61 | The fax server cannot find the job or message by its ID.                                                                                |
| FAX\_E\_DEVICE\_NUM\_LIMIT\_EXCEEDED  | 0x80041b62 | The fax server cannot complete the operation because the number of active fax devices allowed for this version of Windows was exceeded. |
| FAX\_E\_NOT\_SUPPORTED\_ON\_THIS\_SKU | 0x80041b63 | The fax server cannot complete the operation because it is not supported for this version of Windows.                                   |
| FAX\_E\_VERSION\_MISMATCH             | 0x80041b64 | The fax server API version does not support the requested operation.                                                                    |
| FAX\_E\_RECIPIENTS\_LIMIT             | 0x80041b65 | The limit for the number of recipients of a single fax broadcast was reached.                                                           |



 

 

 



