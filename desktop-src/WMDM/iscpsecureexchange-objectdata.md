---
title: ISCPSecureExchange ObjectData method
description: The ObjectData method transfers a block of object data back to Windows Media Device Manager.
ms.assetid: '825539e4-9162-40b7-bae0-336e728fb34e'
keywords: ["ObjectData method windows Media Device Manager", "ObjectData method windows Media Device Manager , ISCPSecureExchange interface", "ISCPSecureExchange interface windows Media Device Manager , ObjectData method"]
topic_type:
- apiref
api_name:
- ISCPSecureExchange.ObjectData
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureExchange::ObjectData method

The **ObjectData** method transfers a block of object data back to Windows Media Device Manager.

## Syntax


```C++
HRESULT ObjectData(
  [out]     BYTE  *pData,
  [in, out] DWORD *pdwSize,
  [in, out] BYTE  abMac
);
```



## Parameters

<dl> <dt>

*pData* \[out\]
</dt> <dd>

Pointer to a buffer to receive data. This parameter is included in the output message authentication code and is encrypted.

</dd> <dt>

*pdwSize* \[in, out\]
</dt> <dd>

Pointer to a **DWORD** containing the transfer size. This parameter must be included in both the input and output message authentication codes.

</dd> <dt>

*abMac* \[in, out\]
</dt> <dd>

Array of eight bytes containing the message authentication code for the parameter data of this method. (WMDM\_MAC\_LENGTH is defined as 8.)

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.



| Return code                                                                                                | Description                                                                                 |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl> | The message authentication code is not valid.<br/>                                    |
| <dl> <dt>**WMDM\_E\_NORIGHTS**</dt> </dl>           | The caller does not have the rights required to perform the requested operation.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl>                    | The method failed. Terminate interaction with the secure content provider.<br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | A parameter is an invalid or **NULL** pointer.<br/>                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | An unspecified error occurred.<br/>                                                   |



 

## Remarks

To transfer data, Windows Media Device Manager calls the [**TransferContainerData**](iscpsecureexchange-transfercontainerdata.md) method to obtain the container data. **ObjectData** is then called to transfer blocks of object data from the secure content provider to Windows Media Device Manager. If S\_OK is returned with *pdwSize* set to zero, Windows Media Device Manager will request no further data.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureExchange Interface**](iscpsecureexchange.md)
</dt> </dl>

 

 





