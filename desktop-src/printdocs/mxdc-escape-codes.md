---
Description: This section describes the structures that are used with the MXDC\_ESCAPE function and the Microsoft XPS Document Converter (MXDC).
ms.assetid: 102dc056-7f65-47d4-8bcd-3b11608bdb9c
title: MXDC Escape Code Structures
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MXDC Escape Code Structures

This section describes the structures that are used with the [**MXDC\_ESCAPE**](mxdc-escape.md) function and the Microsoft XPS Document Converter (MXDC).

## In this section



| Structure                                                                              | Description                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MXDC\_ESCAPE\_HEADER\_T**](mxdcescapeheader.md)<br/>                         | The [**MXDC\_ESCAPE\_HEADER\_T**](https://msdn.microsoft.com/library/windows/desktop/dd162730) structure holds the operation code for a call to [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) with [**MXDC\_ESCAPE**](mxdc-escape.md) as the *nEscape* parameter. It also provides the sizes of the input and output buffers.<br/>  |
| [**MXDC\_GET\_FILENAME\_DATA\_T**](mxdcgetfilenamedata.md)<br/>                 | The [**MXDC\_GET\_FILENAME\_DATA\_T**](https://msdn.microsoft.com/library/windows/desktop/dd162731) structure holds the full path and file name of a Microsoft XPS Document Converter (MXDC) output file.<br/>                                                                                                     |
| [**MXDC\_PRINTTICKET\_ESCAPE\_T**](mxdcprintticketescape.md)<br/>               | The [**MXDC\_PRINTTICKET\_ESCAPE\_T**](mxdcprintticketescape.md) structure is a [**MXDC\_ESCAPE\_HEADER\_T**](mxdcescapeheader.md) structure concatenated with a [**MXDC\_PRINTTICKET\_DATA\_T**](mxdcprintticketpassthrough.md) structure.<br/>                            |
| [**MXDC\_PRINTTICKET\_DATA\_T**](mxdcprintticketpassthrough.md)<br/>            | The [**MXDC\_PRINTTICKET\_DATA\_T**](https://msdn.microsoft.com/library/windows/desktop/dd162733) structure holds an XPS document print ticket, which contains printer and print job settings, to pass to the Microsoft XPS Document Converter (MXDC) output file without any processing.<br/>              |
| [**MXDC\_S0PAGE\_DATA\_T**](mxdcs0pagedata.md)<br/>                             | The [**MXDC\_S0PAGE\_DATA\_T**](https://msdn.microsoft.com/library/windows/desktop/dd162734) structure holds an XPS document page to be passed to the Microsoft XPS Document Converter (MXDC) output file without any processing.<br/>                                                                                  |
| [**MXDC\_S0PAGE\_PASSTHROUGH\_ESCAPE\_T**](mxdcs0pagepassthroughescape.md)<br/> | The [**MXDC\_S0PAGE\_PASSTHROUGH\_ESCAPE\_T**](https://msdn.microsoft.com/library/windows/desktop/dd162736) structure is an [**MXDC\_ESCAPE\_HEADER\_T**](mxdcescapeheader.md) structure concatenated with an [**MXDC\_S0PAGE\_DATA\_T**](mxdcs0pagedata.md) structure.<br/>                             |
| [**MXDC\_S0PAGE\_RESOURCE\_ESCAPE\_T**](mxdcs0pageresourceescape.md)<br/>       | The [**MXDC\_S0PAGE\_RESOURCE\_ESCAPE\_T**](https://msdn.microsoft.com/library/windows/desktop/dd162737) structure is an [**MXDC\_ESCAPE\_HEADER\_T**](mxdcescapeheader.md) structure concatenated with an [**MXDC\_XPS\_S0PAGE\_RESOURCE\_T**](mxdcxpss0pageresource.md) structure.<br/>                   |
| [**MXDC\_XPS\_S0PAGE\_RESOURCE\_T**](mxdcxpss0pageresource.md)<br/>             | The [**MXDC\_XPS\_S0PAGE\_RESOURCE\_T**](https://msdn.microsoft.com/library/windows/desktop/dd162738) structure holds information about a resource, such as an image or font, that is associated with an XPS document page, and is to be passed to the Microsoft XPS Document Converter (MXDC) output file.<br/> |



 

## Related topics

<dl> <dt>

[**MXDC\_ESCAPE**](mxdc-escape.md)
</dt> </dl>

 

 




