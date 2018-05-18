---
title: ISCPSecureExchange3 TransferContainerDataOnClearChannel method
description: The TransferContainerDataOnClearChannel method transfers container file data to the content provider through the clear channel.
ms.assetid: 'aac0fc79-4615-442f-8c08-06addf40c799'
keywords: ["TransferContainerDataOnClearChannel method windows Media Device Manager", "TransferContainerDataOnClearChannel method windows Media Device Manager , ISCPSecureExchange3 interface", "ISCPSecureExchange3 interface windows Media Device Manager , TransferContainerDataOnClearChannel method"]
topic_type:
- apiref
api_name:
- ISCPSecureExchange3.TransferContainerDataOnClearChannel
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureExchange3::TransferContainerDataOnClearChannel method

The **TransferContainerDataOnClearChannel** method transfers container file data to the content provider through the clear channel. The content provider breaks down the container internally and reports which parts of the content are available as they are extracted from the container.

This method is identical to [**ISCPSecureExchange::TransferContainerData**](iscpsecureexchange-transfercontainerdata.md) except that the parameters passed to this method are not encrypted. Consequently this method is more efficient.

## Syntax


```C++
HRESULT TransferContainerDataOnClearChannel(
   IMDSPDevice             *pDevice,
   BYTE                    *pData,
   DWORD                   dwSize,
   IWMDMProgress3 volatile *pProgressCallback,
   UINT                    *pfuReadyFlags
);
```



## Parameters

<dl> <dt>

*pDevice* 
</dt> <dd>

Pointer to a device object.

</dd> <dt>

*pData* 
</dt> <dd>

Pointer to a buffer holding the current data being transferred from the container file.

</dd> <dt>

*dwSize* 
</dt> <dd>

Contains the number of bytes in the buffer.

</dd> <dt>

*pProgressCallback* 
</dt> <dd>

Progress callback on which the content provider can report progress of any steps that it might need to carry out. The step will be identified by the *EventId* parameter of [**IWMDMProgress3**](iwmdmprogress3.md) methods.

</dd> <dt>

*pfuReadyFlags* 
</dt> <dd>

Flag indicating which parts of the container file are ready to be read. This parameter is included in the output message authentication code. The following flags indicate what is ready.



| Value                                                                                                                                                                                                        | Meaning                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WMDM_SCP_TRANSFER_OBJECTDATA"></span><span id="wmdm_scp_transfer_objectdata"></span><dl> <dt>**WMDM\_SCP\_TRANSFER\_OBJECTDATA**</dt> </dl> | Data of the object is available by calling the [GetObjectDataOnClearChannel](iscpsecureexchange3--getobjectdataonclearchannel.md) method.<br/>                                                                                |
| <span id="WMDM_SCP_NO_MORE_CHANGES"></span><span id="wmdm_scp_no_more_changes"></span><dl> <dt>**WMDM\_SCP\_NO\_MORE\_CHANGES**</dt> </dl>            | The content provider has determined that it requires no further processing and/or modification of the file being transferred. Windows Media Device Manager can directly transfer the remainder of the file to the device.<br/> |



 

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If the method fails, it returns an **HRESULT** error code.



| Return code                                                                                                | Description                                                                                 |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_NOT\_CERTIFIED**</dt> </dl>     | The caller is not authorized to use this interface.<br/>                              |
| <dl> <dt>**WMDM\_E\_NORIGHTS**</dt> </dl>           | The caller does not have the rights required to perform the requested operation.<br/> |
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl> | The message authentication code is not valid.<br/>                                    |
| <dl> <dt>**S\_FALSE**</dt> </dl>                    | The method failed. Terminate interaction with the content provider.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | A parameter is invalid or is a **NULL** pointer.<br/>                                 |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | An unspecified error occurred.<br/>                                                   |



 

## Remarks

Windows Media Device Manager calls this method repeatedly, transferring data from the container file to the content provider. Windows Media Device Manager eventually calls this method with *dwSize* set to zero to indicate that it has no more data to transfer. As the content provider collects the data and extracts the various objects from it, it reports back to Windows Media Device Manager which objects, if any, are available after each call. If no objects are available, the content provider returns S\_OK with the *pfuReadyFlags* parameter set to zero. When the content provider has determined that it requires no further processing and/or modification of the file being transferred, the flag WMDM\_SCP\_NO\_MORE\_CHANGES is returned. Windows Media Device Manager can then directly transfer the remainder of the file to the device.

Object data is transferred from the content provider by calling the **GetObjectDataOnClearChannel** method. Windows Media Device Manager calls **GetObjectDataOnClearChannel** repeatedly until it returns zero in the third parameter, *pdwsize*.

The [**ISCPSecureExchange::TransferComplete**](iscpsecureexchange-transfercomplete.md) (or [TransferCompleteForDevice](iscpsecureexchange3--transfercompletefordevice.md) if a session is active) method is called by Windows Media Device Manager to signal the end of a data transfer.

Windows Media Device Manager passes the application-provided progress callback to the content provider in the *pProgressCallback* parameter. The content provider can use this parameter to provide progress notification for any steps that it needs to carry out. The step itself is identified by *EventId*, which is the first parameter of the methods of **IWMDMProgress3**. A specific content provider implementation will define *EventId* values for applications to use.

This method is identical to [**ISCPSecureExchange::TransferContainerData**](iscpsecureexchange-transfercontainerdata.md) except that the parameters passed to this method are not encrypted. Consequently this method is more efficient.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureExchange::TransferContainerData**](iscpsecureexchange-transfercontainerdata.md)
</dt> <dt>

[**ISCPSecureExchange3 Interface**](iscpsecureexchange3.md)
</dt> </dl>

 

 





