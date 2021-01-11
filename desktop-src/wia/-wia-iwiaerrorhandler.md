---
description: The IWiaErrorHandler interface provides methods to handle errors that may occur when an application requests image data, whether for preview or final bits.
ms.assetid: 33d8ccc5-6856-4a54-b1f0-d015933d63ab
title: IWiaErrorHandler interface (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaErrorHandler
api_type: 
- COM
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# IWiaErrorHandler interface

The **IWiaErrorHandler** interface provides methods to handle errors that may occur when an application requests image data, whether for preview or final bits.

## Members

The **IWiaErrorHandler** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IWiaErrorHandler** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaErrorHandler** interface has these methods.



| Method                                                                     | Description                                                                                             |
|:---------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**GetStatusDescription**](-wia-iwiaerrorhandler-getstatusdescription.md) | Returns a string that describes the status code.<br/>                                             |
| [**ReportStatus**](-wia-iwiaerrorhandler-reportstatus.md)                 | Handles status and error messages during image data transfers and displays them to the user.<br/> |



 

## Remarks

The application callback object can implement **IWiaErrorHandler**.

This interface is not designed to handle errors encountered outside of image data transfers, for example, errors in getting or setting device properties or unreturned callbacks into a driver.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 
