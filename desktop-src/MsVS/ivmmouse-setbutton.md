---
title: IVMMouse SetButton method
description: The SetButton method sets the current state (up or down) of the specified mouse button.
ms.assetid: 02c2527e-51b4-43ad-a51b-d1c3a20e6d08
keywords:
- SetButton method Virtual Server
- SetButton method Virtual Server , IVMMouse interface
- IVMMouse interface Virtual Server , SetButton method
- SetButton method Virtual Server , VMMouse interface
- VMMouse interface Virtual Server , SetButton method
topic_type:
- apiref
api_name:
- IVMMouse.SetButton
- VMMouse.SetButton
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMMouse::SetButton method

The **SetButton** method sets the current state (up or down) of the specified mouse button.

## Syntax


```C++
HRESULT SetButton(
  [in] VMMouseButton buttonIndex,
  [in] VARIANT_BOOL  down
);
```



## Parameters

<dl> <dt>

*buttonIndex* \[in\]
</dt> <dd>

The enumerated index of the button whose state is being set.

</dd> <dt>

*down* \[in\]
</dt> <dd>

The state of the button. **TRUE** sets the button state to down, and **FALSE** sets its state to up.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                               | Description                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                     | The operation was successful.<br/>                                                                                                          |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>             | The *buttonIndex* parameter is not valid.<br/>                                                                                              |
| <dl> <dt> **VM\_E\_MOUSE\_NOT\_ACTIVE**</dt> </dl> | The operation could not be completed because the mouse device is not powered up, or it is not currently active in the virtual machine.<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>        | An unexpected error occurred.<br/>                                                                                                          |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMMouse**](ivmmouse.md)
</dt> <dt>

[**VMMouseButton**](vmmousebutton.md)
</dt> </dl>

 

 





