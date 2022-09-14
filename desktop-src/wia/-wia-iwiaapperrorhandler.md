---
description: The IWiaAppErrorHandler interface enables applications to display error windows (during data transfers) from which the user can choose whether to continue, cancel, or abort the transfer.
ms.assetid: ac2597e6-2857-4694-bea7-1ea65d63b365
title: IWiaAppErrorHandler interface (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaAppErrorHandler
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaAppErrorHandler interface

The **IWiaAppErrorHandler** interface enables applications to display error windows (during data transfers) from which the user can choose whether to continue, cancel, or abort the transfer.

## Members

The **IWiaAppErrorHandler** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IWiaAppErrorHandler** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaAppErrorHandler** interface has these methods.



| Method                                                        | Description                                                                                                                                             |
|:--------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetWindow**](-wia-iwiaapperrorhandler-getwindow.md)       | Gets a handle to the dialog box that displays error messages and provides one or more buttons to continue, cancel, or abort the application.<br/> |
| [**ReportStatus**](-wia-iwiaapperrorhandler-reportstatus.md) | Handles device status and error messages during image data transfers and displays the messages to the user.<br/>                                  |



 

## Remarks

The error handling, or callback, object that implements this interface is passed into [**IWiaTransfer::Download**](-wia-iwiatransfer-download.md) and [**IWiaTransfer::Upload**](-wia-iwiatransfer-upload.md).

This interface is not designed to handle errors encountered outside of image data transfers, for example, errors in getting or setting device properties or unreturned callbacks into a driver.

A driver error handler should implement [**IWiaErrorHandler**](-wia-iwiaerrorhandler.md), instead of **IWiaAppErrorHandler**.

The object that implements this interface should also implement [**IWiaTransferCallback**](-wia-iwiatransfercallback.md).

If you want a driver error handler and default error handler to display error message windows, but you do not want to create a complete error handler for the application, implement this interface and also implement the [**IWiaAppErrorHandler::ReportStatus**](-wia-iwiaapperrorhandler-reportstatus.md) method to return WIA\_STATUS\_NOT\_HANDLED.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
