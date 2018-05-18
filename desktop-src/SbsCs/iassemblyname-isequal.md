---
Description: 'The IsEqual method compares the current assembly name to another assembly name.'
ms.assetid: '798102ce-b696-4940-941d-c3fd3054c584'
title: 'IAssemblyName::IsEqual method'
---

# IAssemblyName::IsEqual method

The **IsEqual** method compares the current assembly name to another assembly name.

## Syntax


```C++
HRESULT IsEqual(
  [in] IAssemblyName *pName,
  [in] DWORD         dwCmpFlags
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to another [**IAssemblyName**](iassemblyname.md) instance, which is to be compared to the current assembly.

</dd> <dt>

*dwCmpFlags* \[in\]
</dt> <dd>

Indicates which portion of the assembly names are to be compared. The value can be one of the options of the [**ASM\_CMP\_FLAGS**](asm-cmp-flags-.md) enumeration.

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                        | Description                                                  |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>    | The specified portions of the names match.<br/>        |
| <dl> <dt>S\_FALSE</dt> </dl> | The specified portions of the names do not match.<br/> |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| DLL<br/>                      | <dl> <dt>Sxs.dll</dt> </dl> |



## See also

<dl> <dt>

[**IAssemblyName**](iassemblyname.md)
</dt> </dl>

 

 




