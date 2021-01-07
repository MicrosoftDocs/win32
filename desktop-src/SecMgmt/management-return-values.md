---
description: Lists the values returned by security management functions.
ms.assetid: ee55364e-8ffe-4a78-a49a-250756561770
title: Security Management Return Values
ms.topic: article
ms.date: 05/31/2018
---

# Security Management Return Values

The security management return values include the following:

-   [Attachment Return Values](#attachment-return-values)
-   [LSA Policy Function Return Values](#lsa-policy-function-return-values)

## Attachment Return Values

The Security Configuration tool set supports the following **SCESTATUS** return codes. These values are returned by the attachment support functions and those functions implemented when writing an attachment engine or snap-in.



| Value                            | Description                                                                                      |
|----------------------------------|--------------------------------------------------------------------------------------------------|
| SCESTATUS\_SUCCESS               | The function succeeded.                                                                          |
| SCESTATUS\_INVALID\_PARAMETER    | One of the parameters passed to the function was not valid.                                      |
| SCESTATUS\_RECORD\_NOT\_FOUND    | The specified record was not found in the security database.                                     |
| SCESTATUS\_INVALID\_DATA         | The function failed because some data was not valid.                                             |
| SCESTATUS\_OBJECT\_EXISTS        | The object already exists.                                                                       |
| SCESTATUS\_BUFFER\_TOO\_SMALL    | The buffer passed into the function to receive data is not large enough to receive all the data. |
| SCESTATUS\_PROFILE\_NOT\_FOUND   | The specified profile was not found.                                                             |
| SCESTATUS\_BAD\_FORMAT           | The format is not valid.                                                                         |
| SCESTATUS\_NOT\_ENOUGH\_RESOURCE | There is insufficient memory.                                                                    |
| SCESTATUS\_ACCESS\_DENIED        | The caller does not have sufficient privileges to complete this action.                          |
| SCESTATUS\_CANT\_DELETE          | The function cannot delete the specified item.                                                   |
| SCESTATUS\_PREFIX\_OVERFLOW      | A prefix overflow occurred.                                                                      |
| SCESTATUS\_OTHER\_ERROR          | An unspecified error has occurred.                                                               |
| SCESTATUS\_ALREADY\_RUNNING      | The service is already running.                                                                  |
| SCESTATUS\_SERVICE\_NOT\_SUPPORT | The specified service is not supported.                                                          |
| SCESTATUS\_MOD\_NOT\_FOUND       | An attachment engine DLL listed in the registry either cannot be found or cannot be loaded.      |
| SCESTATUS\_EXCEPTION\_IN\_SERVER | An exception occurred in the server.                                                             |



 

## LSA Policy Function Return Values

Most [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) Policy functions return an NTSTATUS value to indicate success or failure. The various NTSTATUS values are defined in Ntstatus.h, which is distributed with the Microsoft Windows Driver Development Kit (DDK).

To convert an NTSTATUS return value to a Windows error code, use the [**LsaNtStatusToWinError**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsantstatustowinerror) function.

The following table lists the NTSTATUS values that might be returned by any LSA function. (The return value sections for some of the LSA functions list additional error codes that the function might return.) This table also lists the Windows error code that corresponds to each NTSTATUS value.



| NTSTATUS code (Windows error code)                                        | Meaning                                                                                                                                 |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| STATUS\_SUCCESS (ERROR\_SUCCESS)<br/>                               | The function was successful.                                                                                                            |
| STATUS\_ACCESS\_DENIED (ERROR\_ACCESS\_DENIED)<br/>                 | Caller does not have the appropriate access to complete the operation.                                                                  |
| STATUS\_INSUFFICIENT\_RESOURCES (ERROR\_NO\_SYSTEM\_RESOURCES)<br/> | There are not enough system resources (such as memory to allocate buffers) to complete the call.                                        |
| STATUS\_INTERNAL\_DB\_ERROR (ERROR\_INTERNAL\_DB\_ERROR)<br/>       | The LSA database contains an internal inconsistency.                                                                                    |
| STATUS\_INVALID\_HANDLE (ERROR\_INVALID\_HANDLE)<br/>               | Indicates an object or RPC handle is not valid in the [*context*](/windows/desktop/SecGloss/c-gly) used.     |
| STATUS\_INVALID\_SERVER\_STATE (ERROR\_INVALID\_SERVER\_STATE)<br/> | Indicates the LSA server is currently disabled.                                                                                         |
| STATUS\_INVALID\_PARAMETER (ERROR\_INVALID\_PARAMETER)<br/>         | One of the parameters is not valid.                                                                                                     |
| STATUS\_NO\_SUCH\_PRIVILEGE (ERROR\_NO\_SUCH\_PRIVILEGE)<br/>       | Indicates a specified privilege does not exist.                                                                                         |
| STATUS\_OBJECT\_NAME\_NOT\_FOUND (ERROR\_FILE\_NOT\_FOUND)<br/>     | An object in the LSA policy database was not found. The object may have been specified either by SID or by name, depending on its type. |
| STATUS\_UNSUCCESSFUL (ERROR\_GEN\_FAILURE)<br/>                     | Generic failure, such as RPC connection failure.                                                                                        |



 

 

