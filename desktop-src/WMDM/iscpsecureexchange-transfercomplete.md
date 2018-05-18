---
title: ISCPSecureExchange TransferComplete method
description: The TransferComplete method is called by Windows Media Device Manager to signal the end of a secure transfer of data. In this method, the secure content provider can perform any additional processing required to enable the content on the target device.
ms.assetid: '8a7a6de0-ab37-4764-8feb-82676e1e62ab'
keywords: ["TransferComplete method windows Media Device Manager", "TransferComplete method windows Media Device Manager , ISCPSecureExchange interface", "ISCPSecureExchange interface windows Media Device Manager , TransferComplete method"]
topic_type:
- apiref
api_name:
- ISCPSecureExchange.TransferComplete
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureExchange::TransferComplete method

The **TransferComplete** method is called by Windows Media Device Manager to signal the end of a secure transfer of data. In this method, the secure content provider can perform any additional processing required to enable the content on the target device.

## Syntax


```C++
HRESULT TransferComplete();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.



| Return code                                                                                                | Description                                                                                 |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_NOT\_CERTIFIED**</dt> </dl>     | The caller is not authorized to use this interface.<br/>                              |
| <dl> <dt>**WMDM\_E\_NORIGHTS**</dt> </dl>           | The caller does not have the rights required to perform the requested operation.<br/> |
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl> | The message authentication code is not valid.<br/>                                    |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | An unspecified error occurred.<br/>                                                   |



 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureExchange Interface**](iscpsecureexchange.md)
</dt> </dl>

 

 





