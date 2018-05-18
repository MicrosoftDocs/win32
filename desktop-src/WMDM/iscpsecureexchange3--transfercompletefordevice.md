---
title: ISCPSecureExchange3 TransferCompleteForDevice method
description: The TransferCompleteForDevice method is called by Windows Media Device Manager to signal the end of a data transfer for a specific device.
ms.assetid: '5144d290-444d-4a8c-ad3d-292bb8168e99'
keywords: ["TransferCompleteForDevice method windows Media Device Manager", "TransferCompleteForDevice method windows Media Device Manager , ISCPSecureExchange3 interface", "ISCPSecureExchange3 interface windows Media Device Manager , TransferCompleteForDevice method"]
topic_type:
- apiref
api_name:
- ISCPSecureExchange3.TransferCompleteForDevice
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureExchange3::TransferCompleteForDevice method

The **TransferCompleteForDevice** method is called by Windows Media Device Manager to signal the end of a data transfer for a specific device.

## Syntax


```C++
HRESULT TransferCompleteForDevice(
   IMDSPDevice *pDevice
);
```



## Parameters

<dl> <dt>

*pDevice* 
</dt> <dd>

Pointer to a device object.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If the method fails, it returns an **HRESULT** error code.



| Return code                                                                                                | Description                                                                                 |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_NOT\_CERTIFIED**</dt> </dl>     | The caller is not authorized to use this interface.<br/>                              |
| <dl> <dt>**WMDM\_E\_NORIGHTS**</dt> </dl>           | The caller does not have the rights required to perform the requested operation.<br/> |
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl> | The message authentication code is not valid.<br/>                                    |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | An unspecified error occurred.<br/>                                                   |



 

## Remarks

This method is identical to [**ISCPSecureExchange::TransferComplete**](iscpsecureexchange-transfercomplete.md) except that this method is called when transfer is completed within a transfer session.

In that case, the secure content provider needs to know which device the transfer was completed for, so this method accepts a *pDevice* parameter.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureExchange::TransferComplete**](iscpsecureexchange-transfercomplete.md)
</dt> <dt>

[**ISCPSecureExchange3 Interface**](iscpsecureexchange3.md)
</dt> </dl>

 

 





