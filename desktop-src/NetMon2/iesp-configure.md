---
description: The Configure method submits configuration information for a capture.
ms.assetid: b8cbbae1-3c07-489f-8e8f-77c95ec03209
title: IESP::Configure method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IESP.Configure
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IESP::Configure method

The **Configure** method submits configuration information for a capture.

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

Handle to an error BLOB that contains additional error information. For information about the contents of an error BLOB, see the Remarks section in this topic.

</dd> </dl>

## Return value

If the method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                                         | Description                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NOT\_CONNECTED**</dt> </dl>                | The NPP is not connected to the network.<br/>                                                                                                                                                               |
| <dl> <dt>**NMERR\_NOT\_ESP**</dt> </dl>                      | The NPP is connected to the network but not with the [IESP::Connect](iesp-connect.md) method.<br/>                                                                                                         |
| <dl> <dt>**NMERR\_CAPTURING**</dt> </dl>                     | The NPP reports that the capture session has started.<br/>                                                                                                                                                  |
| <dl> <dt>**NMERR\_ILLEGAL\_TRIGGER**</dt> </dl>              | The trigger portion of the configuration BLOB is corrupt.<br/>                                                                                                                                              |
| <dl> <dt>**NMERR\_BLOB\_ENTRY\_DOES\_NOT\_EXIST**</dt> </dl> | The configuration BLOB specified by *hConfigurationBlob* is missing an entry needed to perform this operation. Look at the error BLOB returned by *hErrorBlob* to determine which entry was not found.<br/> |
| <dl> <dt>**NMERR\_BLOB\_CONVERSION\_ERROR**</dt> </dl>       | The BLOB is corrupt.<br/>                                                                                                                                                                                   |
| <dl> <dt>**NMERR\_BLOB\_NOT\_INITIALIZED**</dt> </dl>        | The **CreateBlob** method has not been called.<br/>                                                                                                                                                         |
| <dl> <dt>**NMERR\_INVALID\_BLOB**</dt> </dl>                 | The object that is pointed to is not a BLOB.<br/>                                                                                                                                                           |
| <dl> <dt>**NMERR\_BLOB\_STRING\_INVALID**</dt> </dl>         | The string is not null-terminated.<br/>                                                                                                                                                                     |
| <dl> <dt>**NMERR\_UPLEVEL\_BLOB**</dt> </dl>                 | The BLOB version number is incorrect.<br/>                                                                                                                                                                  |
| <dl> <dt>**NMERR\_OUT\_OF\_MEMORY**</dt> </dl>               | No memory was available. Shut down windows to free up resources.<br/>                                                                                                                                       |
| <dl> <dt>**NMERR\_TIMEOUT**</dt> </dl>                       | The request has timed out.<br/>                                                                                                                                                                             |



 

## Remarks

You must apply this method to restart an NPP that has been started and stopped, but not disconnected.

The error BLOB returned by the *hErrorBlob* parameter contains entries that Network Monitor could not understand or find in the configuration BLOB specified in *hConfigurationBlob*. The returned error BLOB contains error information that the application can use for troubleshooting. For example, if NMERR\_BLOB\_ENTRY\_DOES\_NOT\_EXIST is returned, the entry Network Monitor could not find is included in the returned error BLOB.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



 

 




