---
description: Handles status and error messages during image data transfers and displays them to the user.
ms.assetid: 23e85c63-80b9-4510-854d-289c8d23be2d
title: IWiaErrorHandler::ReportStatus method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaErrorHandler.ReportStatus
api_type: 
- COM
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# IWiaErrorHandler::ReportStatus method

Handles status and error messages during image data transfers and displays them to the user.

## Syntax


```C++
HRESULT ReportStatus(
  [in] HWND     hwndParent,
  [in] IUnknown *punkItem,
  [in] HRESULT  hrStatus,
  [in] LONG     cbResLength,
  [in] BYTE     *pbData
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **HWND**

**HWND** that is the parent window for the message window.

</dd> <dt>

*punkItem* \[in\]
</dt> <dd>

Type: **[IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown)\***

Pointer to the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface of the item being transferred. This object minimally implements [**IWiaItem2**](-wia-iwiaitem2.md) and [**IWiaDataTransfer**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadatatransfer).

</dd> <dt>

*hrStatus* \[in\]
</dt> <dd>

Type: **HRESULT**

**HRESULT** that is the status code received by [**BandedDataCallback**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadatacallback-bandeddatacallback).

</dd> <dt>

*cbResLength* \[in\]
</dt> <dd>

Type: **LONG**

**LONG** that is the size of the data referred to by *pbData*.

</dd> <dt>

*pbData* \[in\]
</dt> <dd>

Type: **BYTE\***

Pointer to the data buffer as received by [**BandedDataCallback**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadatacallback-bandeddatacallback).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns *hrStatus* if the error cannot be recovered from. Otherwise, it returns one of the following values.



| Return code                                                                             | Description                                                                                      |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | The appropriate action was taken to correct the error and the transfer can continue. <br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | No action was taken to handle the error or report status to the user. <br/>                |
| <dl> <dt>**E\_ABORT**</dt> </dl> | The user chose to abort the transfer in response to the displayed dialog box. <br/>        |



 

## Remarks

Windows Image Acquisition (WIA) 2.0 calls **IWiaErrorHandler::ReportStatus** when the driver sends an **IT\_MSG\_DEVICE\_STATUS** message to [**BandedDataCallback**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadatacallback-bandeddatacallback). This method handles the message and displays information to the user about the status or error. If the message is about an error, the method lets the user choose, if possible, whether to try to recover from the error and continue the transfer or to abort.

*hrStatus* is set to WIA\_STATUS\_TRANSFER\_BEGIN to inform the handler a transfer has started. It is set to WIA\_STATUS\_TRANSFER\_END when the transfer is complete.

If *hrStatus* is SEVERITY\_SUCCESS, the user should be allowed to cancel the transfer.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 
