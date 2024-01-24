---
description: Return values that a network provider can set.
ms.assetid: f8e6692f-4824-40fe-a5b3-9843689ea02e
title: Network Security Return Values
ms.topic: article
ms.date: 05/31/2018
---

# Network Security Return Values

The return values that a network provider can set include the following error codes.



| Error Codes         | Description                                                                                                                                                                                                                                                                                                                             |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WN\_SUCCESS         | The function succeeded.                                                                                                                                                                                                                                                                                                                 |
| WN\_NOT\_SUPPORTED  | The function is not supported on this network provider.                                                                                                                                                                                                                                                                                 |
| WN\_NET\_ERROR      | A unknown network error occurred.                                                                                                                                                                                                                                                                                                       |
| WN\_MORE\_DATA      | The data buffer passed in is insufficient to contain all of the available data.                                                                                                                                                                                                                                                         |
| WN\_BAD\_POINTER    | A pointer that is not valid was specified during the function call.                                                                                                                                                                                                                                                                     |
| WN\_BAD\_VALUE      | A numeric value that is not valid was specified during the function call.                                                                                                                                                                                                                                                               |
| WN\_BAD\_PASSWORD   | An incorrect password was specified.                                                                                                                                                                                                                                                                                                    |
| WN\_ACCESS\_DENIED  | The caller does not have sufficient permissions to complete the operation.                                                                                                                                                                                                                                                              |
| WN\_FUNCTION\_BUSY  | This function cannot be reentered and is currently being used, or the provider is still initializing and is not ready to be called yet. The provider should return this error code only if it is going to be available. This return code is passed by the MPR back to its caller and is likely to cause the caller to retry.<br/> |
| WN\_WINDOWS\_ERROR  | A required function failed.                                                                                                                                                                                                                                                                                                             |
| WN\_BAD\_USER       | A user name that is not valid was specified.                                                                                                                                                                                                                                                                                            |
| WN\_OUT\_OF\_MEMORY | There is insufficient memory to complete the operation.                                                                                                                                                                                                                                                                                 |
| WN\_NOT\_CONNECTED  | The device is not redirected.                                                                                                                                                                                                                                                                                                           |
| WN\_OPEN\_FILES     | The connection could not be canceled because files are still open.                                                                                                                                                                                                                                                                      |
| WN\_BAD\_NETNAME    | The network name is not valid.                                                                                                                                                                                                                                                                                                          |



 

 

 




