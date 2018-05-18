---
Description: 'The GetProperty method gets the value of a name-value pair in the assembly name.'
ms.assetid: '0526fac9-1a3f-403b-b886-a7f833913e18'
title: 'IAssemblyName::GetProperty method'
---

# IAssemblyName::GetProperty method

The **GetProperty** method gets the value of a name-value pair in the assembly name.

## Syntax


```C++
HRESULT GetProperty(
  [in]      DWORD   PropertyId,
  [out]     LPVOID  pvProperty,
  [in, out] LPDWORD pcbProperty
);
```



## Parameters

<dl> <dt>

*PropertyId* \[in\]
</dt> <dd>

A property ID that represents the name-value pair. Valid property IDs are [**ASM\_NAME**](asm-name-.md) enumeration values.

</dd> <dt>

*pvProperty* \[out\]
</dt> <dd>

A pointer to a buffer that receives the value of the name-value pair.

</dd> <dt>

*pcbProperty* \[in, out\]
</dt> <dd>

The size in bytes of the buffer specified by *pvProperty*. The value is zero if this property is not set.

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                        | Description                            |
|-------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>    | The method succeeded.<br/>       |
| <dl> <dt>S\_FALSE</dt> </dl> | The method did not succeed.<br/> |



 

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

 

 




