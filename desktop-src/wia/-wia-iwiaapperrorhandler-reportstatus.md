---
description: Handles device status and error messages during image data transfers and displays the messages to the user.
ms.assetid: 8d3ba598-8649-4108-aebc-94f2bcb64ad8
title: IWiaAppErrorHandler::ReportStatus method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaAppErrorHandler.ReportStatus
api_type: 
- COM
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# IWiaAppErrorHandler::ReportStatus method

Handles device status and error messages during image data transfers and displays the messages to the user.

## Syntax


```C++
HRESULT ReportStatus(
  [in] LONG      lFlags,
  [in] IWiaItem2 *pWiaItem2,
  [in] HRESULT   hrStatus,
  [in] LONG      lPercentComplete
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Not used. Set to 0.

</dd> <dt>

*pWiaItem2* \[in\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\***

Pointer to the item being transferred.

</dd> <dt>

*hrStatus* \[in\]
</dt> <dd>

Type: **HRESULT**

Device status code.

</dd> <dt>

*lPercentComplete* \[in\]
</dt> <dd>

Type: **LONG**

Percentage completed of current operation.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns *hrStatus* if recovery from the error is not possible. Otherwise, it returns one of the following values.



| Return code                                                                                              | Description                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | If *hrStatus* is an error, the appropriate action was taken to correct the error, and the transfer can continue. If *hrStatus* is informational, the user was informed with a modeless dialog box and chose not to cancel the transfer.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl>                  | The user cancelled the transfer from the error handler modeless dialog box. This value can be returned at any point no matter what *hrStatus* is. <br/>                                                                                      |
| <dl> <dt>**WIA\_STATUS\_NOT\_HANDLED**</dt> </dl> | No action was taken; that is, no dialog box was presented to the user. The next error handler will be invoked. The order of error handlers is: application, driver, and system default.<br/>                                                 |



 

## Remarks

The *lPercentComplete* parameter enables an error handler window to show progress. For example, a driver might provide an estimate of how long "warming up" takes. The *lPercentComplete* parameter passed into **IWiaAppErrorHandler::ReportStatus** is the same value as the **lPercentComplete** that the driver sets into the [**WiaTransferParams**](-wia-wiatransferparams.md) structure.

An error handler can use the SUCCEEDED and FAILED macros to find out if *hrStatus* has SEVERITY\_ERROR or SEVERITY\_SUCCESS.

If *hrStatus* is SEVERITY\_SUCCESS, the user should be allowed to cancel the transfer.

If *hrStatus* is SEVERITY\_ERROR, the error handler should display a modal dialog box owned by the application parent window.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 




