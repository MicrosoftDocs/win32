---
Description: 'The GetDisplayName method gets a string representation of the side-by-side assembly name.'
ms.assetid: 'd2d74d67-a893-4f2f-8161-80bf3d5cbedb'
title: 'IAssemblyName::GetDisplayName method'
---

# IAssemblyName::GetDisplayName method

The **GetDisplayName** method gets a string representation of the side-by-side assembly name.

## Syntax


```C++
HRESULT GetDisplayName(
  [out]     LPOLESTR szDisplayName,
  [in, out] LPDWORD  pccDisplayName,
  [in]      DWORD    dwDisplayFlags
);
```



## Parameters

<dl> <dt>

*szDisplayName* \[out\]
</dt> <dd>

A pointer to a buffer that receives the string value that contains the assembly name.

</dd> <dt>

*pccDisplayName* \[in, out\]
</dt> <dd>

When calling this method, set this parameter to the size of the buffer specified by **szDisplayName**. Specify the size in characters and include the null terminator. When the method returns, the value of *pccDisplayName* is the size of the name returned.

</dd> <dt>

*dwDisplayFlags* \[in\]
</dt> <dd>

One or more of the options of the [**ASM\_DISPLAY\_FLAGS**](asm-display-flags-.md) enumeration to specify which portions of the assembly's name to include in the string representation of the assembly name. The default for *dwDisplayFlags* is 0, which returns all portions of the assembly's display name.

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

 

 




