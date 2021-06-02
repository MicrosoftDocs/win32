---
description: The Configure method submits configuration information used for a capture.
ms.assetid: 6418c465-c339-44b6-84eb-36c7b89231f8
title: IDelaydCConfigure method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDelaydC.Configure
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IDelaydC::Configure method

The **Configure** method submits configuration information used for a capture.

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

Handle to the BLOB that contains the configuration information.

</dd> <dt>

*hErrorBlob* \[out\]
</dt> <dd>

Handle to an error BLOB that contains additional error information. For information about the contents of an error BLOB, see the Remarks section in this topic .

</dd> </dl>

## Return value

If this method is successful, the return value is NMERR\_SUCCESS.

If the method is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                                      | Description                                                                               |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_CAPTURING**</dt> </dl>                  | The NPP reports that the capture session has started.<br/>                          |
| <dl> <dt>**NMERR\_DISK\_NOT\_LOCAL\_FIXED**</dt> </dl>    |                                                                                           |
| <dl> <dt>**NMERR\_COULD\_NOT\_CREATE\_MEMORY**</dt> </dl> |                                                                                           |
| <dl> <dt>**NMERR\_OUT\_OF\_MEMORY**</dt> </dl>            | No memory was available. Shut down windows to free up resources.<br/>               |
| <dl> <dt>**NMERR\_INVALID\_PARAMETER**</dt> </dl>         | The configuration BLOB specified by the hConfiguration parameter is not valid.<br/> |



 

## Remarks

You must apply this method to restart an NPP that has been started, stopped, but not disconnected.

The error BLOB returned by *hErrorBlob* contains entries that Network Monitor could not understand or find in the configuration BLOB specified in *hConfigurationBlob*. The returned error BLOB contains error information that the application can use for troubleshooting. For example, if NMERR\_BLOB\_ENTRY\_DOES\_NOT\_EXIST is returned, the entry Network Monitor could not find is included in the returned error BLOB.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



## See also

<dl> <dt>

[IDelaydC](idelaydc.md)
</dt> <dt>

[IDelaydC::Connect](idelaydc-connect.md)
</dt> <dt>

[IDelaydC::Start](idelaydc-start.md)
</dt> <dt>

[IDelaydC::Stop](idelaydc-stop.md)
</dt> </dl>

 

 




