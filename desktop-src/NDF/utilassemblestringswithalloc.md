---
title: UtilAssembleStringsWithAlloc function
description: Allocates a string and formats it using strings provided by the string table. This function uses StringCchPrintf to create the formatted string.
ms.assetid: eedc2874-b949-4cc2-ba7c-ebf1924f1156
keywords:
- UtilAssembleStringsWithAlloc function NDF
topic_type:
- apiref
api_name:
- UtilAssembleStringsWithAlloc
api_location:
- ndattributils.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# UtilAssembleStringsWithAlloc function

The **UtilAssembleStringsWithAlloc** function allocates a string and formats it using strings provided by the string table. This function uses [**StringCchPrintf**](https://msdn.microsoft.com/library/windows/desktop/ms647541) to create the formatted string.

## Syntax


```C++
HRESULT UtilAssembleStringsWithAlloc(
  _Out_ LPWSTR  *Buffer,
  _In_  UINT    BufferMax,
  _In_  LPCWSTR InputFormat,
  _In_  LPCWSTR InputString,
  _In_  BOOLEAN AdditionalArgument,
  _In_  ULONG   AdditionalValue
);
```



## Parameters

<dl> <dt>

*Buffer* \[out\]
</dt> <dd>

Type: **LPWSTR\***

The location where the newly allocated string will be placed. When the string is no longer needed, it must be released with [**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722).

</dd> <dt>

*BufferMax* \[in\]
</dt> <dd>

Type: **UINT**

The maximum number of characters allowed in the string allocated by *Buffer*. If the resulting formatted string is longer than the number of characters specified, it is truncated and null-terminated.

> [!Note]  
> This parameter may not be set to zero.

 

</dd> <dt>

*InputFormat* \[in\]
</dt> <dd>

Type: **LPCWSTR**

String resource out of the string table representing a format parameter passed to [**StringCchPrintf**](https://msdn.microsoft.com/library/windows/desktop/ms647541). It is constructed using [**MAKEINTRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/ms648029).

The resource string format must specify either a format parameter taking a wide string, or a format parameter taking an unsigned long and a wide string.

</dd> <dt>

*InputString* \[in\]
</dt> <dd>

Type: **LPCWSTR**

String resource out of the string table representing an argument passed to [**StringCchPrintf**](https://msdn.microsoft.com/library/windows/desktop/ms647541) in place of the wide string in the format parameter. It is constructed using [**MAKEINTRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/ms648029).

</dd> <dt>

*AdditionalArgument* \[in\]
</dt> <dd>

Type: **BOOLEAN**

True if *AdditionalValue* should be passed in as the first formatting argument to [**StringCchPrintf**](https://msdn.microsoft.com/library/windows/desktop/ms647541); otherwise, false (and only the resource string identified by *InputString* will be passed).

</dd> <dt>

*AdditionalValue* \[in\]
</dt> <dd>

Type: **ULONG**

The value to pass as the first formatting argument to [**StringCchPrintf**](https://msdn.microsoft.com/library/windows/desktop/ms647541) if *AdditionalArgument* is true.

</dd> </dl>

## Return value

Type: **HRESULT**

Possible return values include, but are not limited to, the following.



| Return code                                                                                  | Description                                                        |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The operation succeeded.<br/>                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One or more parameters has not been provided correctly.<br/> |



 

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Ndattributils.h</dt> </dl> |



## See also

<dl> <dt>

[**UtilStringCopyWithAlloc**](utilstringcopywithalloc.md)
</dt> <dt>

[**UtilLoadStringWithAlloc**](utilloadstringwithalloc.md)
</dt> <dt>

[**StringCchPrintf**](https://msdn.microsoft.com/library/windows/desktop/ms647541)
</dt> <dt>

[**MAKEINTRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/ms648029)
</dt> <dt>

[**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722)
</dt> </dl>

 

 





