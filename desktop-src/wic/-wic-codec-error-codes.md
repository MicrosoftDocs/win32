---
description: This document contains a list of the Windows Imaging Component (WIC) defined error codes.
ms.assetid: 1ded909c-311b-49e3-ba23-b22cd7a77bc6
title: Codec Error Codes
ms.topic: article
ms.date: 05/31/2018
---

# Codec Error Codes

This document contains a list of the Windows Imaging Component (WIC) defined error codes.

-   [WIC Errors by Code](#wic-errors-by-code)
-   [WIC Errors by Value](#wic-errors-by-value)

## WIC Errors by Code

The following table is a list of the error codes used by the WICAPIs sorted in alphabetical order. 

| Error Code                                      | Error Value                      |
|-------------------------------------------------|----------------------------------|
| WINCODEC\_ERR\_ABORTED                          | 0x80004004 (E\_ABORT)            |
| WINCODEC\_ERR\_ACCESSDENIED                     | 0x80070005 (E\_ACCESSDENIED)     |
| WINCODEC\_ERR\_ALREADYLOCKED                    | 0x88982f0D                       |
| WINCODEC\_ERR\_BADHEADER                        | 0x88982f61                       |
| WINCODEC\_ERR\_BADIMAGE                         | 0x88982f60                       |
| WINCODEC\_ERR\_BADMETADATAHEADER                | 0x88982f63                       |
| WINCODEC\_ERR\_BADSTREAMDATA                    | 0x88982f70                       |
| WINCODEC\_ERR\_CODECNOTHUMBNAIL                 | 0x88982f44                       |
| WINCODEC\_ERR\_CODECPRESENT                     | 0x88982f43                       |
| WINCODEC\_ERR\_CODECTOOMANYSCANLINES            | 0x88982f46                       |
| WINCODEC\_ERR\_COMPONENTINITIALIZEFAILURE       | 0x88982f8B                       |
| WINCODEC\_ERR\_COMPONENTNOTFOUND                | 0x88982f50                       |
| WINCODEC\_ERR\_DUPLICATEMETADATAPRESENT         | 0x88982f8D                       |
| WINCODEC\_ERR\_FRAMEMISSING                     | 0x88982f62                       |
| WINCODEC\_ERR\_GENERIC\_ERROR                   | 0x80004005 (E\_FAIL)             |
| WINCODEC\_ERR\_IMAGESIZEOUTOFRANGE              | 0x88982f51                       |
| WINCODEC\_ERR\_INSUFFICIENTBUFFER               | 0x88982f8C                       |
| WINCODEC\_ERR\_INTERNALERROR                    | 0x88982f48                       |
| WINCODEC\_ERR\_INVALIDPARAMETER                 | 0x80070057 (E\_INVALIDARG)       |
| WINCODEC\_ERR\_INVALIDQUERYCHARACTER            | 0x88982f93                       |
| WINCODEC\_ERR\_INVALIDQUERYREQUEST              | 0x88982f90                       |
| WINCODEC\_ERR\_INVALIDREGISTRATION              | 0x88982f8A                       |
| WINCODEC\_ERR\_NOTIMPLEMENTED                   | 0x80004001 (E\_NOTIMPL)          |
| WINCODEC\_ERR\_NOTINITIALIZED                   | 0x88982f0C                       |
| WINCODEC\_ERR\_OUTOFMEMORY                      | 0x8007000E (E\_OUTOFMEMORY)      |
| WINCODEC\_ERR\_PALETTEUNAVAILABLE               | 0x88982f45                       |
| WINCODEC\_ERR\_PROPERTYNOTFOUND                 | 0x88982f40                       |
| WINCODEC\_ERR\_PROPERTYNOTSUPPORTED             | 0x88982f41                       |
| WINCODEC\_ERR\_PROPERTYSIZE                     | 0x88982f42                       |
| WINCODEC\_ERR\_PROPERTYUNEXPECTEDTYPE           | 0x88982f8E                       |
| WINCODEC\_ERR\_REQUESTONLYVALIDATMETADATAROOT   | 0x88982f92                       |
| WINCODEC\_ERR\_SOURCERECTDOESNOTMATCHDIMENSIONS | 0x88982f49                       |
| WINCODEC\_ERR\_STREAMWRITE                      | 0x88982f71                       |
| WINCODEC\_ERR\_STREAMREAD                       | 0x88982f72                       |
| WINCODEC\_ERR\_STREAMNOTAVAILABLE               | 0x88982f73                       |
| WINCODEC\_ERR\_TOOMUCHMETADATA                  | 0x88982f52                       |
| WINCODEC\_ERR\_UNKNOWNIMAGEFORMAT               | 0x88982f07                       |
| WINCODEC\_ERR\_UNEXPECTEDMETADATATYPE           | 0x88982f91                       |
| WINCODEC\_ERR\_UNEXPECTEDSIZE                   | 0x88982f8F                       |
| WINCODEC\_ERR\_UNSUPPORTEDOPERATION             | 0x88982f81                       |
| WINCODEC\_ERR\_UNSUPPORTEDPIXELFORMAT           | 0x88982f80                       |
| WINCODEC\_ERR\_UNSUPPORTEDVERSION               | 0x88982f0B                       |
| WINCODEC\_ERR\_VALUEOUTOFRANGE                  | 0x88982f05                       |
| WINCODEC\_ERR\_VALUEOVERFLOW                    | INTSAFE\_E\_ARITHMETIC\_OVERFLOW |
| WINCODEC\_ERR\_WRONGSTATE                       | 0x88982f04                       |



 

## WIC Errors by Value

The following table is a list of the error codes used by the WICAPIs sorted in numerical order. 

| Error Code                       | Error Value                                     |
|----------------------------------|-------------------------------------------------|
| 0x80004005 (E\_FAIL)             | WINCODEC\_ERR\_GENERIC\_ERROR                   |
| 0x80070057 (E\_INVALIDARG)       | WINCODEC\_ERR\_INVALIDPARAMETER                 |
| 0x8007000E (E\_OUTOFMEMORY)      | WINCODEC\_ERR\_OUTOFMEMORY                      |
| 0x80004001 (E\_NOTIMPL)          | WINCODEC\_ERR\_NOTIMPLEMENTED                   |
| 0x80004004 (E\_ABORT)            | WINCODEC\_ERR\_ABORTED                          |
| 0x80070005 (E\_ACCESSDENIED)     | WINCODEC\_ERR\_ACCESSDENIED                     |
| INTSAFE\_E\_ARITHMETIC\_OVERFLOW | WINCODEC\_ERR\_VALUEOVERFLOW                    |
| 0x88982f04                       | WINCODEC\_ERR\_WRONGSTATE                       |
| 0x88982f05                       | WINCODEC\_ERR\_VALUEOUTOFRANGE                  |
| 0x88982f07                       | WINCODEC\_ERR\_UNKNOWNIMAGEFORMAT               |
| 0x88982f0B                       | WINCODEC\_ERR\_UNSUPPORTEDVERSION               |
| 0x88982f0C                       | WINCODEC\_ERR\_NOTINITIALIZED                   |
| 0x88982f0D                       | WINCODEC\_ERR\_ALREADYLOCKED                    |
| 0x88982f40                       | WINCODEC\_ERR\_PROPERTYNOTFOUND                 |
| 0x88982f41                       | WINCODEC\_ERR\_PROPERTYNOTSUPPORTED             |
| 0x88982f42                       | WINCODEC\_ERR\_PROPERTYSIZE                     |
| 0x88982f43                       | WINCODEC\_ERR\_CODECPRESENT                     |
| 0x88982f44                       | WINCODEC\_ERR\_CODECNOTHUMBNAIL                 |
| 0x88982f45                       | WINCODEC\_ERR\_PALETTEUNAVAILABLE               |
| 0x88982f46                       | WINCODEC\_ERR\_CODECTOOMANYSCANLINES            |
| 0x88982f48                       | WINCODEC\_ERR\_INTERNALERROR                    |
| 0x88982f49                       | WINCODEC\_ERR\_SOURCERECTDOESNOTMATCHDIMENSIONS |
| 0x88982f50                       | WINCODEC\_ERR\_COMPONENTNOTFOUND                |
| 0x88982f51                       | WINCODEC\_ERR\_IMAGESIZEOUTOFRANGE              |
| 0x88982f52                       | WINCODEC\_ERR\_TOOMUCHMETADATA                  |
| 0x88982f60                       | WINCODEC\_ERR\_BADIMAGE                         |
| 0x88982f61                       | WINCODEC\_ERR\_BADHEADER                        |
| 0x88982f62                       | WINCODEC\_ERR\_FRAMEMISSING                     |
| 0x88982f63                       | WINCODEC\_ERR\_BADMETADATAHEADER                |
| 0x88982f70                       | WINCODEC\_ERR\_BADSTREAMDATA                    |
| 0x88982f71                       | WINCODEC\_ERR\_STREAMWRITE                      |
| 0x88982f72                       | WINCODEC\_ERR\_STREAMREAD                       |
| 0x88982f73                       | WINCODEC\_ERR\_STREAMNOTAVAILABLE               |
| 0x88982f80                       | WINCODEC\_ERR\_UNSUPPORTEDPIXELFORMAT           |
| 0x88982f81                       | WINCODEC\_ERR\_UNSUPPORTEDOPERATION             |
| 0x88982f8A                       | WINCODEC\_ERR\_INVALIDREGISTRATION              |
| 0x88982f8B                       | WINCODEC\_ERR\_COMPONENTINITIALIZEFAILURE       |
| 0x88982f8C                       | WINCODEC\_ERR\_INSUFFICIENTBUFFER               |
| 0x88982f8D                       | WINCODEC\_ERR\_DUPLICATEMETADATAPRESENT         |
| 0x88982f8E                       | WINCODEC\_ERR\_PROPERTYUNEXPECTEDTYPE           |
| 0x88982f8F                       | WINCODEC\_ERR\_UNEXPECTEDSIZE                   |
| 0x88982f90                       | WINCODEC\_ERR\_INVALIDQUERYREQUEST              |
| 0x88982f91                       | WINCODEC\_ERR\_UNEXPECTEDMETADATATYPE           |
| 0x88982f92                       | WINCODEC\_ERR\_REQUESTONLYVALIDATMETADATAROOT   |
| 0x88982f93                       | WINCODEC\_ERR\_INVALIDQUERYCHARACTER            |



 

 

 



