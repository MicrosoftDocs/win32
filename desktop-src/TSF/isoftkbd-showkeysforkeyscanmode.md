---
title: ISoftKbd ShowKeysForKeyScanMode method (Softkbdc.h)
description: The ISoftKbd ShowKeysForKeyScanMode method displays the keys used for the key scan mode for a soft keyboard.
ms.assetid: bfa76e5b-6f6e-470a-ba3a-7ecff9f67f7b
keywords:
- ShowKeysForKeyScanMode method Text Services Framework
- ShowKeysForKeyScanMode method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , ShowKeysForKeyScanMode method
topic_type:
- apiref
api_name:
- ISoftKbd.ShowKeysForKeyScanMode
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::ShowKeysForKeyScanMode method

The **ISoftKbd::ShowKeysForKeyScanMode** method displays the keys used for the key scan mode for a soft keyboard.

## Syntax


```C++
HRESULT ShowKeysForKeyScanMode(
  [in] KEYID *lpKeyID,
  [in] INT   iKeyNum,
  [in] BOOL  fHighL
);
```



## Parameters

<dl> <dt>

*lpKeyID* \[in\]
</dt> <dd>

Pointer to an array of KEYID elements indicating the identifiers of keys to display.

</dd> <dt>

*iKeyNum* \[in\]
</dt> <dd>

The number of keys to display.

</dd> <dt>

*fHighL* \[in\]
</dt> <dd>

TRUE if the method is to highlight the keys, and **FALSE** otherwise.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                  |
|----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One of the parameters is invalid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Softkbd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ISoftKbd**](isoftkbd.md)
</dt> </dl>

 

 





