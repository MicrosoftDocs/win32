---
description: The Configure method submits capture configuration information.
ms.assetid: 739ed1df-1a84-4c48-a1ac-2dba7a614cdd
title: IStats::Configure method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStats.Configure
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IStats::Configure method

The **Configure** method submits capture configuration information.

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

Handle to the BLOB that the caller configures.

</dd> <dt>

*hErrorBlob* \[out\]
</dt> <dd>

Handle to an error BLOB that contains additional error information.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                                         | Description                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_BLOB\_STRING\_INVALID**</dt> </dl>         | The string is not null-terminated.<br/>                                                                                                                                                                                            |
| <dl> <dt>**NMERR\_BLOB\_NOT\_INITIALIZED**</dt> </dl>        | The **CreateBlob** method has not been called.<br/>                                                                                                                                                                                |
| <dl> <dt>**NMERR\_INVALID\_BLOB**</dt> </dl>                 | The object that is pointed to is not a BLOB.<br/>                                                                                                                                                                                  |
| <dl> <dt>**NMERR\_UPLEVEL\_BLOB**</dt> </dl>                 | The BLOB version number is incorrect.<br/>                                                                                                                                                                                         |
| <dl> <dt>**NMERR\_BLOB\_ENTRY\_ALREADY\_EXISTS**</dt> </dl>  | A BLOB entry already exists.<br/>                                                                                                                                                                                                  |
| <dl> <dt>**NMERR\_BLOB\_ENTRY\_DOES\_NOT\_EXIST**</dt> </dl> | The configuration BLOB specified by the *hConfigurationBlob* parameter lacks an entry needed to perform this operation. Look at the error BLOB returned by the *hErrorBlob* parameter to determine which entry was not found.<br/> |
| <dl> <dt>**NMERR\_AMBIGUOUS\_SPECIFIER**</dt> </dl>          | The BLOB lacks owner or category information.<br/>                                                                                                                                                                                 |
| <dl> <dt>**NMERR\_BLOB\_OWNER\_NOT\_FOUND**</dt> </dl>       | The Owner section of the BLOB was not found.<br/>                                                                                                                                                                                  |
| <dl> <dt>**NMERR\_BLOB\_CATEGORY\_NOT\_FOUND**</dt> </dl>    | The Category section of the BLOB was not found.<br/>                                                                                                                                                                               |
| <dl> <dt>**NMERR\_UNKNOWN\_CATEGORY**</dt> </dl>             | Category information was found but not understood.<br/>                                                                                                                                                                            |
| <dl> <dt>**NMERR\_UNKNOWN\_TAG**</dt> </dl>                  | Tag information was found but not understood.<br/>                                                                                                                                                                                 |
| <dl> <dt>**NMERR\_BLOB\_CONVERSION\_ERROR**</dt> </dl>       | The BLOB is corrupt.<br/>                                                                                                                                                                                                          |
| <dl> <dt>**NMERR\_ILLEGAL\_TRIGGER**</dt> </dl>              | The trigger portion of the BLOB is corrupt.<br/>                                                                                                                                                                                   |



 

## Remarks

You must apply this method to restart an NPP that has been started, stopped but not disconnected.

The error BLOB returned by *hErrorBlob* contains entries that Network Monitor could not understand or find in the configuration BLOB specified in the *hConfigurationBlob* parameter. The returned error BLOB contains error information that the application can use for troubleshooting. For example, if NMERR\_BLOB\_ENTRY\_DOES\_NOT\_EXIST is returned, the entry Network Monitor could not find is included in the returned error BLOB.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[IStats](istats.md)
</dt> <dt>

[ISTATS::Connect](istats-connect.md)
</dt> <dt>

[Network Monitor BLOBS](network-monitor-blobs.md)
</dt> </dl>

 

 




