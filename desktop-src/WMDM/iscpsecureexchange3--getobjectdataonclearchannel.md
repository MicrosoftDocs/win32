---
title: GetObjectDataOnClearChannel method
description: The GetObjectDataOnClearChannel method transfers a block of object data on a clear channel back to Windows Media Device Manager.
ms.assetid: 62122415-b45b-436e-8c5f-28be759ba8c0
keywords:
- GetObjectDataOnClearChannel method windows Media Device Manager
topic_type:
- apiref
api_name:
- GetObjectDataOnClearChannel
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetObjectDataOnClearChannel method

The **GetObjectDataOnClearChannel** method transfers a block of object data on a clear channel back to Windows Media Device Manager.

This method is identical to [**ISCPSecureExchange::ObjectData**](/windows/desktop/api/mswmdm/nf-mswmdm-iscpsecureexchange-objectdata) except that the data returned by this method is not encrypted. Consequently this method is more efficient.

## Syntax


```C++
HRESULT GetObjectDataOnClearChannel(
   IMDSPDevice *pDevice,
   BYTE        *pData,
   DWORD       *pdwSize
);
```



## Parameters

<dl> <dt>

*pDevice* 
</dt> <dd>

Pointer to the device object.

</dd> <dt>

*pData* 
</dt> <dd>

Pointer to a buffer to receive data.

</dd> <dt>

*pdwSize* 
</dt> <dd>

Pointer to a **DWORD** containing the transfer size.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If the method fails, it returns an **HRESULT** error code.



| Return code                                                                                                | Description                                                                                 |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl> | The message authentication code is not valid.<br/>                                    |
| <dl> <dt>**WMDM\_E\_NORIGHTS**</dt> </dl>           | The caller does not have the rights required to perform the requested operation.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl>                    | The method failed. Terminate interaction with the content provider.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | A parameter is an invalid or **NULL** pointer.<br/>                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | An unspecified error occurred.<br/>                                                   |



 

## Remarks

To transfer data, Windows Media Device Manager calls the [TransferContainerDataOnClearChannel](/windows/desktop/api/mswmdm/nf-mswmdm-iscpsecureexchange3-transfercontainerdataonclearchannel) method to obtain the container data. **GetObjectDataOnClearChannel** is then called to transfer blocks of object data from the content provider to Windows Media Device Manager. If S\_OK is returned with *pdwSize* set to zero, Windows Media Device Manager will request no further data.

This method is identical to [**ISCPSecureExchange::ObjectData**](/windows/desktop/api/mswmdm/nf-mswmdm-iscpsecureexchange-objectdata) except that the data returned by this method is not encrypted. Consequently this method is more efficient.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureExchange::ObjectData**](/windows/desktop/api/mswmdm/nf-mswmdm-iscpsecureexchange-objectdata)
</dt> <dt>

[**ISCPSecureExchange3 Interface**](/windows/desktop/api/mswmdm/nn-mswmdm-iscpsecureexchange3)
</dt> </dl>

 

 





