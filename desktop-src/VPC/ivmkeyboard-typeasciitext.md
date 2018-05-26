---
title: IVMKeyboard TypeAsciiText method
description: Simulates a series of ASCII keys being typed into the guest.
ms.assetid: 6c7fbfed-d495-4f11-a7d1-dc08bd075870
keywords:
- TypeAsciiText method Virtual PC
- TypeAsciiText method Virtual PC , IVMKeyboard interface
- IVMKeyboard interface Virtual PC , TypeAsciiText method
topic_type:
- apiref
api_name:
- IVMKeyboard.TypeAsciiText
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMKeyboard::TypeAsciiText method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](https://msdn.microsoft.com/library/windows/desktop/hh850319).\]

Simulates a series of ASCII keys being typed into the guest.

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



| Return code/value                                                                                                                                                 | Description                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>      | The specified string is empty.<br/>    |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMKeyboard is defined as 00695f2e-c5ad-4d6e-b1ab-336ed121f8c4<br/>                |



## See also

<dl> <dt>

[**IVMKeyboard**](ivmkeyboard.md)
</dt> </dl>

 

 





