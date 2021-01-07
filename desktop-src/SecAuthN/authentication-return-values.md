---
description: Lists the values returned by functions in authentication APIs.
ms.assetid: ea519e5c-98b0-4a01-b2cc-e5ff736a5396
title: Authentication Return Values
ms.topic: article
ms.date: 05/31/2018
---

# Authentication Return Values

## Network Provider Values

The [Network Provider API](network-provider-api.md) uses the following defined values.



| Value                                                                           | Description                                               |
|---------------------------------------------------------------------------------|-----------------------------------------------------------|
| [Network Security Return Values](network-security-return-values.md)<br/> | Return values that a network provider can set.<br/> |



 

## Smart Card Return Values

[Smart Card Functions](authentication-functions.md) return the following return values. These return values are defined in Scarderr.h.

> [!Note]  
> Some return values may have the same value as existing Windows return values that signify a similar condition. For information about error codes not listed here, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

 



| Value                                                               | Description                                                                                                                                                                                                 |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR\_BROKEN\_PIPE<br/> 0x00000109<br/>                | The client attempted a smart card operation in a remote session, such as a client session running on a terminal server, and the operating system in use does not support smart card redirection.<br/> |
| SCARD\_E\_BAD\_SEEK<br/> 0x80100029<br/>                | An error occurred in setting the smart card file object pointer.<br/>                                                                                                                                 |
| SCARD\_E\_CANCELLED<br/> 0x80100002<br/>                | The action was canceled by an [**SCardCancel**](/windows/desktop/api/Winscard/nf-winscard-scardcancel) request.<br/>                                                                                                                        |
| SCARD\_E\_CANT\_DISPOSE<br/> 0x8010000E<br/>            | The system could not dispose of the media in the requested manner.<br/>                                                                                                                               |
| SCARD\_E\_CARD\_UNSUPPORTED<br/> 0x8010001C<br/>        | The smart card does not meet minimal requirements for support.<br/>                                                                                                                                   |
| SCARD\_E\_CERTIFICATE\_UNAVAILABLE<br/> 0x8010002D<br/> | The requested certificate could not be obtained.<br/>                                                                                                                                                 |
| SCARD\_E\_COMM\_DATA\_LOST<br/> 0x8010002F<br/>         | A communications error with the smart card has been detected. <br/>                                                                                                                                   |
| SCARD\_E\_DIR\_NOT\_FOUND<br/> 0x80100023<br/>          | The specified directory does not exist in the smart card.<br/>                                                                                                                                        |
| SCARD\_E\_DUPLICATE\_READER<br/> 0x8010001B<br/>        | The [*reader*](/windows/desktop/SecGloss/r-gly) driver did not produce a unique reader name.<br/>                                                                            |
| SCARD\_E\_FILE\_NOT\_FOUND<br/> 0x80100024<br/>         | The specified file does not exist in the smart card.<br/>                                                                                                                                             |
| SCARD\_E\_ICC\_CREATEORDER<br/> 0x80100021<br/>         | The requested order of object creation is not supported.<br/>                                                                                                                                         |
| SCARD\_E\_ICC\_INSTALLATION<br/> 0x80100020<br/>        | No primary provider can be found for the smart card.<br/>                                                                                                                                             |
| SCARD\_E\_INSUFFICIENT\_BUFFER<br/> 0x80100008<br/>     | The data buffer for returned data is too small for the returned data.<br/>                                                                                                                            |
| SCARD\_E\_INVALID\_ATR<br/> 0x80100015<br/>             | An [*ATR string*](/windows/desktop/SecGloss/a-gly) obtained from the registry is not a valid ATR string.<br/>                                                        |
| SCARD\_E\_INVALID\_CHV<br/> 0x8010002A<br/>             | The supplied PIN is incorrect.<br/>                                                                                                                                                                   |
| SCARD\_E\_INVALID\_HANDLE<br/> 0x80100003<br/>          | The supplied handle was not valid.<br/>                                                                                                                                                               |
| SCARD\_E\_INVALID\_PARAMETER<br/> 0x80100004<br/>       | One or more of the supplied parameters could not be properly interpreted.<br/>                                                                                                                        |
| SCARD\_E\_INVALID\_TARGET<br/> 0x80100005<br/>          | Registry startup information is missing or not valid.<br/>                                                                                                                                            |
| SCARD\_E\_INVALID\_VALUE<br/> 0x80100011<br/>           | One or more of the supplied parameter values could not be properly interpreted.<br/>                                                                                                                  |
| SCARD\_E\_NO\_ACCESS<br/> 0x80100027<br/>               | Access is denied to the file.<br/>                                                                                                                                                                    |
| SCARD\_E\_NO\_DIR<br/> 0x80100025<br/>                  | The supplied path does not represent a smart card directory.<br/>                                                                                                                                     |
| SCARD\_E\_NO\_FILE<br/> 0x80100026<br/>                 | The supplied path does not represent a smart card file.<br/>                                                                                                                                          |
| SCARD\_E\_NO\_KEY\_CONTAINER<br/> 0x80100030<br/>       | The requested key container does not exist on the smart card.<br/>                                                                                                                                    |
| SCARD\_E\_NO\_MEMORY<br/> 0x80100006<br/>               | Not enough memory available to complete this command.<br/>                                                                                                                                            |
| SCARD\_E\_NO\_PIN\_CACHE<br/> 0x80100033<br/>           | The smart card PIN cannot be cached.<br/> **Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This error code is not available.<br/> <br/>                        |
| SCARD\_E\_NO\_READERS\_AVAILABLE<br/> 0x8010002E<br/>   | No smart card reader is available.<br/>                                                                                                                                                               |
| SCARD\_E\_NO\_SERVICE<br/> 0x8010001D<br/>              | The smart card [*resource manager*](/windows/desktop/SecGloss/r-gly) is not running.<br/>                                                                |
| SCARD\_E\_NO\_SMARTCARD<br/> 0x8010000C<br/>            | The operation requires a smart card, but no smart card is currently in the device.<br/>                                                                                                               |
| SCARD\_E\_NO\_SUCH\_CERTIFICATE<br/> 0x8010002C<br/>    | The requested certificate does not exist.<br/>                                                                                                                                                        |
| SCARD\_E\_NOT\_READY<br/> 0x80100010<br/>               | The reader or card is not ready to accept commands.<br/>                                                                                                                                              |
| SCARD\_E\_NOT\_TRANSACTED<br/> 0x80100016<br/>          | An attempt was made to end a nonexistent transaction.<br/>                                                                                                                                            |
| SCARD\_E\_PCI\_TOO\_SMALL<br/> 0x80100019<br/>          | The PCI receive buffer was too small.<br/>                                                                                                                                                            |
| SCARD\_E\_PIN\_CACHE\_EXPIRED<br/> 0x80100032<br/>      | The smart card PIN cache has expired.<br/> **Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This error code is not available.<br/> <br/>                       |
| SCARD\_E\_PROTO\_MISMATCH<br/> 0x8010000F<br/>          | The requested protocols are incompatible with the protocol currently in use with the card.<br/>                                                                                                       |
| SCARD\_E\_READ\_ONLY\_CARD<br/> 0x80100034<br/>         | The smart card is read-only and cannot be written to.<br/> **Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This error code is not available.<br/> <br/>       |
| SCARD\_E\_READER\_UNAVAILABLE<br/> 0x80100017<br/>      | The specified reader is not currently available for use.<br/>                                                                                                                                         |
| SCARD\_E\_READER\_UNSUPPORTED<br/> 0x8010001A<br/>      | The reader driver does not meet minimal requirements for support.<br/>                                                                                                                                |
| SCARD\_E\_SERVER\_TOO\_BUSY<br/> 0x80100031<br/>        | The smart card resource manager is too busy to complete this operation.<br/>                                                                                                                          |
| SCARD\_E\_SERVICE\_STOPPED<br/> 0x8010001E<br/>         | The smart card resource manager has shut down.<br/>                                                                                                                                                   |
| SCARD\_E\_SHARING\_VIOLATION<br/> 0x8010000B<br/>       | The smart card cannot be accessed because of other outstanding connections.<br/>                                                                                                                      |
| SCARD\_E\_SYSTEM\_CANCELLED<br/> 0x80100012<br/>        | The action was canceled by the system, presumably to log off or shut down.<br/>                                                                                                                       |
| SCARD\_E\_TIMEOUT<br/> 0x8010000A<br/>                  | The user-specified time-out value has expired.<br/>                                                                                                                                                   |
| SCARD\_E\_UNEXPECTED<br/> 0x8010001F<br/>               | An unexpected card error has occurred.<br/>                                                                                                                                                           |
| SCARD\_E\_UNKNOWN\_CARD<br/> 0x8010000D<br/>            | The specified smart card name is not recognized.<br/>                                                                                                                                                 |
| SCARD\_E\_UNKNOWN\_READER<br/> 0x80100009<br/>          | The specified reader name is not recognized.<br/>                                                                                                                                                     |
| SCARD\_E\_UNKNOWN\_RES\_MNG<br/> 0x8010002B<br/>        | An unrecognized error code was returned.<br/>                                                                                                                                                         |
| SCARD\_E\_UNSUPPORTED\_FEATURE<br/> 0x80100022<br/>     | This smart card does not support the requested feature.<br/>                                                                                                                                          |
| SCARD\_E\_WRITE\_TOO\_MANY<br/> 0x80100028<br/>         | An attempt was made to write more data than would fit in the target object.<br/>                                                                                                                      |
| SCARD\_F\_COMM\_ERROR<br/> 0x80100013<br/>              | An internal communications error has been detected.<br/>                                                                                                                                              |
| SCARD\_F\_INTERNAL\_ERROR<br/> 0x80100001<br/>          | An internal consistency check failed.<br/>                                                                                                                                                            |
| SCARD\_F\_UNKNOWN\_ERROR<br/> 0x80100014<br/>           | An internal error has been detected, but the source is unknown.<br/>                                                                                                                                  |
| SCARD\_F\_WAITED\_TOO\_LONG<br/> 0x80100007<br/>        | An internal consistency timer has expired.<br/>                                                                                                                                                       |
| SCARD\_P\_SHUTDOWN<br/> 0x80100018<br/>                 | The operation has been aborted to allow the server application to exit.<br/>                                                                                                                          |
| SCARD\_S\_SUCCESS<br/>                                        | No error was encountered.<br/>                                                                                                                                                                        |
| SCARD\_W\_CANCELLED\_BY\_USER<br/> 0x8010006E<br/>      | The action was canceled by the user.<br/>                                                                                                                                                             |
| SCARD\_W\_CACHE\_ITEM\_NOT\_FOUND<br/> 0x80100070<br/>  | The requested item could not be found in the cache.<br/>                                                                                                                                              |
| SCARD\_W\_CACHE\_ITEM\_STALE<br/> 0x80100071<br/>       | The requested cache item is too old and was deleted from the cache.<br/>                                                                                                                              |
| SCARD\_W\_CACHE\_ITEM\_TOO\_BIG<br/> 0x80100072<br/>    | The new cache item exceeds the maximum per-item size defined for the cache.<br/>                                                                                                                      |
| SCARD\_W\_CARD\_NOT\_AUTHENTICATED<br/> 0x8010006F<br/> | No PIN was presented to the smart card.<br/>                                                                                                                                                          |
| SCARD\_W\_CHV\_BLOCKED<br/> 0x8010006C<br/>             | The card cannot be accessed because the maximum number of PIN entry attempts has been reached.<br/>                                                                                                   |
| SCARD\_W\_EOF<br/> 0x8010006D<br/>                      | The end of the smart card file has been reached.<br/>                                                                                                                                                 |
| SCARD\_W\_REMOVED\_CARD<br/> 0x80100069<br/>            | The smart card has been removed, so further communication is not possible.<br/>                                                                                                                       |
| SCARD\_W\_RESET\_CARD<br/> 0x80100068<br/>              | The smart card was reset.<br/>                                                                                                                                                                        |
| SCARD\_W\_SECURITY\_VIOLATION<br/> 0x8010006A<br/>      | Access was denied because of a security violation.<br/>                                                                                                                                               |
| SCARD\_W\_UNPOWERED\_CARD<br/> 0x80100067<br/>          | Power has been removed from the smart card, so that further communication is not possible.<br/>                                                                                                       |
| SCARD\_W\_UNRESPONSIVE\_CARD<br/> 0x80100066<br/>       | The smart card is not responding to a reset.<br/>                                                                                                                                                     |
| SCARD\_W\_UNSUPPORTED\_CARD<br/> 0x80100065<br/>        | The reader cannot communicate with the card, due to ATR string configuration conflicts.<br/>                                                                                                          |
| SCARD\_W\_WRONG\_CHV<br/> 0x8010006B<br/>               | The card cannot be accessed because the wrong PIN was presented.<br/>                                                                                                                                 |



 

## Related topics

<dl> <dt>

[System Error Codes](/windows/desktop/Debug/system-error-codes)
</dt> </dl>

 

