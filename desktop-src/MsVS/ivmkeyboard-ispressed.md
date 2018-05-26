---
title: IVMKeyboard IsPressed method
description: The IsPressed method returns the current state (pressed or released) of the specified key within the virtual machine.
ms.assetid: 15cfccab-dabd-41e4-81f6-558a3453209f
keywords:
- IsPressed method Virtual Server
- IsPressed method Virtual Server , IVMKeyboard interface
- IVMKeyboard interface Virtual Server , IsPressed method
- IsPressed method Virtual Server , VMKeyboard interface
- VMKeyboard interface Virtual Server , IsPressed method
topic_type:
- apiref
api_name:
- IVMKeyboard.IsPressed
- VMKeyboard.IsPressed
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMKeyboard::IsPressed method

The **IsPressed** method returns the current state (pressed or released) of the specified key within the virtual machine.

## Syntax


```C++
HRESULT IsPressed(
  [in]  BSTR         key,
  [out] VARIANT_BOOL *pressed
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

The key code for the key whose state is being queried.

</dd> <dt>

*pressed* \[out\]
</dt> <dd>

**TRUE** if the key is currently pressed down, **FALSE** otherwise.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                         | Description                                                                 |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>                                    |
| <dl> <dt> **E\_POINTER**</dt> </dl>          | The *key* or *pressed* parameter is **NULL**.<br/>                    |
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

 

 





