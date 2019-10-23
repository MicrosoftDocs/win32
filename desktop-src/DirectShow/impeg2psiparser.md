---
Description: The implementation of this interface is provided as sample code with the DirectShow SDK.
ms.assetid: a18fc6b6-f37e-4c87-9150-0504333d33c2
title: IMpeg2PsiParser interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMpeg2PsiParser
api_type: 
- COM
api_location: 
---

# IMpeg2PsiParser interface

The implementation of this interface is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.

The `IMpeg2PsiParser` interface retrieves Program Specific Information (PSI) from the PSI Parser filter, which is provided in the DirectShow SDK as a sample filter. An application can use this filter to map program IDs (PIDs) on the MPEG-2 Demultiplexer filter.

## Members

The **IMpeg2PsiParser** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface. **IMpeg2PsiParser** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMpeg2PsiParser** interface has these methods.



| Method                                                                             | Description                                                                               |
|:-----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**FindRecordProgramMapPid**](https://msdn.microsoft.com/en-us/library/Dd407137(v=VS.85).aspx)         | Finds the Program Map Table (PMT) PID for a program, given the program number.<br/> |
| [**GetCountOfElementaryStreams**](impeg2psiparser-getcountofelementarystreams.md) | Retrieves the number of elementary streams in a specified program.<br/>             |
| [**GetCountOfPrograms**](impeg2psiparser-getcountofprograms.md)                   | Retrieves the number of programs in the transport stream.<br/>                      |
| [**GetPatVersionNumber**](impeg2psiparser-getpatversionnumber.md)                 | Retrieves the version\_number field from the Program Association Table (PAT).<br/>  |
| [**GetPmtVersionNumber**](impeg2psiparser-getpmtversionnumber.md)                 | Retrieves the version\_number field from a specified PMT.<br/>                      |
| [**GetRecordElementaryPid**](https://msdn.microsoft.com/en-us/library/Dd376623(v=VS.85).aspx)           | Retrieves the PID assignment for a specified elementary stream in a program.<br/>   |
| [**GetRecordProgramMapPid**](https://msdn.microsoft.com/en-us/library/Dd376624(v=VS.85).aspx)           | Retrieves the PID assignment for a specified PMT.<br/>                              |
| [**GetRecordProgramNumber**](impeg2psiparser-getrecordprogramnumber.md)           | Retrieves the program number for a specified program.<br/>                          |
| [**GetRecordStreamType**](https://msdn.microsoft.com/en-us/library/Dd376626(v=VS.85).aspx)                 | Retrieves the stream type for a specified elementary stream in a program.<br/>      |
| [**GetTransportStreamId**](impeg2psiparser-gettransportstreamid.md)               | Retrieves the transport\_stream\_id field from the PAT.<br/>                        |



 

## See also

<dl> <dt>

[PSI Parser Filter Sample](psi-parser-filter-sample.md)
</dt> </dl>

 

 




