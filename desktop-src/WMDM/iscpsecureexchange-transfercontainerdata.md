---
title: ISCPSecureExchange TransferContainerData method
description: The TransferContainerData method transfers container file data to the secure content provider. The secure content provider breaks down the container internally and reports which parts of the content are available as they are extracted from the container.
ms.assetid: '97b55751-b45e-4204-87e2-1e653d55a718'
keywords: ["TransferContainerData method windows Media Device Manager", "TransferContainerData method windows Media Device Manager , ISCPSecureExchange interface", "ISCPSecureExchange interface windows Media Device Manager , TransferContainerData method"]
topic_type:
- apiref
api_name:
- ISCPSecureExchange.TransferContainerData
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureExchange::TransferContainerData method

The **TransferContainerData** method transfers container file data to the secure content provider. The secure content provider breaks down the container internally and reports which parts of the content are available as they are extracted from the container.

## Syntax


```C++
HRESULT TransferContainerData(
  [in]      BYTE  *pData,
  [in]      DWORD dwSize,
  [out]     UINT  *pfuReadyFlags,
  [in, out] BYTE  abMac
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to a buffer holding the current data being transferred from the container file. This parameter must be included in the input message authentication code and must be encrypted.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

**DWORD** that contains the number of bytes in the buffer. This parameter must be included in the input message authentication code.

</dd> <dt>

*pfuReadyFlags* \[out\]
</dt> <dd>

Flag indicating which parts of the container file are ready to be read. This parameter is included in the output message authentication code. The following flags indicate what is ready.



| Flag                            | Description                                                                                                                                                                                                                               |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMDM\_SCP\_TRANSFER\_OBJECTDATA | Data of the object is available by calling the [**ObjectData**](iscpsecureexchange-objectdata.md) method.                                                                                                                                |
| WMDM\_SCP\_NO\_MORE\_CHANGES    | Set when the secure content provider has determined that it requires no further processing and/or modification of the file being transferred. Windows Media Device Manager can directly transfer the remainder of the file to the device. |



 

</dd> <dt>

*abMac* \[in, out\]
</dt> <dd>

Array of eight bytes containing the message authentication code for the parameter data of this method. (WMDM\_MAC\_LENGTH is defined as 8.)

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.



| Return code                                                                                                | Description                                                                                 |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_NOT\_CERTIFIED**</dt> </dl>     | The caller is not authorized to use this interface.<br/>                              |
| <dl> <dt>**WMDM\_E\_NORIGHTS**</dt> </dl>           | The caller does not have the rights required to perform the requested operation.<br/> |
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl> | The message authentication code is not valid.<br/>                                    |
| <dl> <dt>**S\_FALSE**</dt> </dl>                    | The method failed. Terminate interaction with the secure content provider.<br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | A parameter is invalid or is a **NULL** pointer.<br/>                                 |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | An unspecified error occurred.<br/>                                                   |



 

## Remarks

Windows Media Device Manager calls this method repeatedly, transferring data from the container file to the secure content provider. Windows Media Device Manager eventually calls this method with *dwSize* set to zero to indicate that it has no more data to transfer. As the secure content provider collects the data and extracts the various objects from it, it reports back to Windows Media Device Manager which objects, if any, are available after each call. If no objects are available, the secure content provider returns S\_OK with the *pfuReadyFlags* parameter set to zero. When the secure content provider has determined that it requires no further processing and/or modification of the file being transferred, the flag WMDM\_SCP\_NO\_MORE\_CHANGES is returned. Windows Media Device Manager can then directly transfer the remainder of the file to the device.

Object data is transferred from the secure content provider by calling the **ObjectData** method. Windows Media Device Manager calls **ObjectData** repeatedly until it returns zero in the second parameter, *dwBytesWrite*.

The **TransferComplete** method is called by Windows Media Device Manager to signal the end of a secure transfer of data.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureExchange Interface**](iscpsecureexchange.md)
</dt> </dl>

 

 





