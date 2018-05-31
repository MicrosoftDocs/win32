---
title: IVMKeyboard TypeAsciiText method
description: The TypeAsciiText method simulates the given series of ASCII keys being typed (pressed and then released) in the virtual machine.
ms.assetid: 0d411f2c-bc22-41f2-b5e0-3fb086106bf7
keywords:
- TypeAsciiText method Virtual Server
- TypeAsciiText method Virtual Server , IVMKeyboard interface
- IVMKeyboard interface Virtual Server , TypeAsciiText method
- TypeAsciiText method Virtual Server , VMKeyboard interface
- VMKeyboard interface Virtual Server , TypeAsciiText method
topic_type:
- apiref
api_name:
- IVMKeyboard.TypeAsciiText
- VMKeyboard.TypeAsciiText
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

# IVMKeyboard::TypeAsciiText method

The **TypeAsciiText** method simulates the given series of ASCII keys being typed (pressed and then released) in the virtual machine.

## Syntax


```C++
HRESULT TypeAsciiText(
  [in] BSTR text
);
```



## Parameters

<dl> <dt>

*text* \[in\]
</dt> <dd>

The ASCII text string to be typed inside the virtual machine.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                         | Description                                                                 |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>                                    |
| <dl> <dt> **E\_POINTER**</dt> </dl>          | The *text* parameter is **NULL**.<br/>                                |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>       | The given text string is empty, or contains an invalid key code.<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl> | An unexpected error occurred.<br/>                                    |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMKeyboard**](ivmkeyboard.md)
</dt> </dl>

 

 





