---
title: IVMKeyboard PressKey method
description: The PressKey method simulates the given key being pressed down inside the virtual machine.
ms.assetid: 12ace4bc-e17f-4522-a22c-a676e5bf6c59
keywords:
- PressKey method Virtual Server
- PressKey method Virtual Server , IVMKeyboard interface
- IVMKeyboard interface Virtual Server , PressKey method
- PressKey method Virtual Server , VMKeyboard interface
- VMKeyboard interface Virtual Server , PressKey method
topic_type:
- apiref
api_name:
- IVMKeyboard.PressKey
- VMKeyboard.PressKey
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

# IVMKeyboard::PressKey method

The **PressKey** method simulates the given key being pressed down inside the virtual machine.

## Syntax


```C++
HRESULT PressKey(
  [in] BSTR key
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

The key code for the key to be pressed inside the virtual machine.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                         | Description                                                                 |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>                                    |
| <dl> <dt> **E\_POINTER**</dt> </dl>          | The *key* parameter is **NULL**.<br/>                                 |
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

 

 





