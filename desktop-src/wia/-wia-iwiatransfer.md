---
description: The IWiaTransfer interface provides stream-based transfer of data.
ms.assetid: 7bc6d3b8-9bf0-4b77-aa2b-b7c64c5730c0
title: IWiaTransfer interface (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaTransfer
api_type: 
- COM
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# IWiaTransfer interface

The **IWiaTransfer** interface provides stream-based transfer of data.

## Members

The **IWiaTransfer** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IWiaTransfer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaTransfer** interface has these methods.



| Method                                                                 | Description                                                                                 |
|:-----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**Cancel**](-wia-iwiatransfer-cancel.md)                             | Cancels the current transfer operation. <br/>                                         |
| [**Download**](-wia-iwiatransfer-download.md)                         | Initiates a data download to the caller. <br/>                                        |
| [**EnumWIA\_FORMAT\_INFO**](-wia-iwiatransfer-enumwia-format-info.md) | Creates an enumerator for the transfer formats that the WIA 2.0 device supports.<br/> |
| [**Upload**](-wia-iwiatransfer-upload.md)                             | Initiates a data upload of a single item from the caller. <br/>                       |



 

## Remarks

The **IWiaTransfer** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface methods.



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref)                 | Increments reference count.               |
| [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release)               | Decrements reference count.               |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 
