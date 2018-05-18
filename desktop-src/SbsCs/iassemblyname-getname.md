---
Description: 'The GetName method returns the name portion of the assembly name.'
ms.assetid: 'b27ebe4e-02b6-473f-a8cb-c68a3e65e493'
title: 'IAssemblyName::GetName method'
---

# IAssemblyName::GetName method

The **GetName** method returns the name portion of the assembly name.

## Syntax


```C++
HRESULT GetName(
  [in, out] LPDWORD lpcwBuffer,
  [out]     WCHAR   *pwzName
);
```



## Parameters

<dl> <dt>

*lpcwBuffer* \[in, out\]
</dt> <dd>

When calling this method, set this parameter to the size of the buffer specified by *pwzName*. The specify the size in characters and include the null terminator. When the method returns, the value of *lpcwBuffer* is the size of the name returned.

</dd> <dt>

*pwzName* \[out\]
</dt> <dd>

Pointer to the string value that receives the name.

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                        | Description                            |
|-------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>    | The method succeeded.<br/>       |
| <dl> <dt>S\_FALSE</dt> </dl> | The method did not succeed.<br/> |



 

## Remarks

This method is equivalent to using the [**GetProperty**](iassemblyname-getproperty.md) method with the *PropertyId* set to the **ASM\_NAME\_NAME** option of [**ASM\_NAME**](asm-name-.md). In case ASM\_NAME\_NAME is not set, the size of the buffer returned by *lpcwBuffer* is 0, and the content of *pwzName* is undefined.

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

 

 




