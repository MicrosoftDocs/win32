---
description: Submits configuration data for a data capture.
ms.assetid: fb8c8ac8-cef4-45e0-bb06-3cf09c8ad9ac
title: IRTC::Configure method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRTC.Configure
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IRTC::Configure method

The [**Configure**](configure.md) method submits configuration data for a data capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE Configure(
  [in]  HBLOB hConfigurationBlob,
  [out] HBLOB hErrorBlob
);
```



## Parameters

<dl> <dt>

*hConfigurationBlob* \[in\]
</dt> <dd>

A handle to the BLOB that is configured by the caller.

</dd> <dt>

*hErrorBlob* \[out\]
</dt> <dd>

A handle to an error BLOB that contains additional error data.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                                         | Description                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_BLOB\_NOT\_INITIALIZED**</dt> </dl>        | The **CreateBlob** method has not been called.<br/>                                                                                                                                                 |
| <dl> <dt>**NMERR\_INVALID\_BLOB**</dt> </dl>                 | The object pointed to is not a BLOB.<br/>                                                                                                                                                           |
| <dl> <dt>**NMERR\_UPLEVEL\_BLOB**</dt> </dl>                 | The BLOB version number is incorrect.<br/>                                                                                                                                                          |
| <dl> <dt>**NMERR\_BLOB\_ENTRY\_ALREADY\_EXISTS**</dt> </dl>  | Duplicate BLOB.<br/>                                                                                                                                                                                |
| <dl> <dt>**NMERR\_BLOB\_ENTRY\_DOES\_NOT\_EXIST**</dt> </dl> | The configuration BLOB specified by *hConfigurationBlob* lacks an entry needed to perform this operation. View the error BLOB returned by *hErrorBlob* to determine which entry was not found.<br/> |
| <dl> <dt>**NMERR\_AMBIGUOUS\_SPECIFIER**</dt> </dl>          | The BLOB Owner or Category data is missing.<br/>                                                                                                                                                    |
| <dl> <dt>**NMERR\_BLOB\_OWNER\_NOT\_FOUND**</dt> </dl>       | The BLOB Owner section was not found.<br/>                                                                                                                                                          |
| <dl> <dt>**NMERR\_BLOB\_CATEGORY\_NOT\_FOUND**</dt> </dl>    | The BLOB Category section was not found.<br/>                                                                                                                                                       |
| <dl> <dt>**NMERR\_UNKNOWN\_CATEGORY**</dt> </dl>             | The BLOB Category section was found, but not understood.<br/>                                                                                                                                       |
| <dl> <dt>**NMERR\_UNKNOWN\_TAG**</dt> </dl>                  | The BLOB Tag section was found, but not understood.<br/>                                                                                                                                            |
| <dl> <dt>**NMERR\_BLOB\_CONVERSION\_ERROR**</dt> </dl>       | The BLOB is corrupt.<br/>                                                                                                                                                                           |
| <dl> <dt>**NMERR\_ILLEGAL\_TRIGGER**</dt> </dl>              | The trigger portion of the BLOB is corrupt.<br/>                                                                                                                                                    |
| <dl> <dt>**NMERR\_BLOB\_STRING\_INVALID**</dt> </dl>         | The string is not null-terminated.<br/>                                                                                                                                                             |



 

## Remarks

You must apply this method to restart an NPP that has been started, stopped, but not disconnected.

The error BLOB returned by *hErrorBlob* contains entries that Network Monitor could not understand or find in the configuration BLOB specified in *hConfigurationBlob*. The returned error BLOB contains error data that the application can use for troubleshooting. For example, if NMERR\_BLOB\_ENTRY\_DOES\_NOT\_EXIST is returned, the entry Network Monitor cannot find is included in the returned error BLOB.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[IRTC](irtc.md)
</dt> <dt>

[IRTC::Connect](irtc-connect.md)
</dt> <dt>

[Network Monitor BLOBS](network-monitor-blobs.md)
</dt> </dl>

 

 




