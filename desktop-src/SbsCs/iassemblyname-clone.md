---
Description: 'The Clone method copies the current side-by-side assembly name to a new instance of IAssemblyName.'
ms.assetid: '5096b7de-e53d-49fa-bb43-16d768787b4e'
title: 'IAssemblyName::Clone method'
---

# IAssemblyName::Clone method

The **Clone** method copies the current side-by-side assembly name to a new instance of [**IAssemblyName**](iassemblyname.md).

## Syntax


```C++
HRESULT Clone(
  [out] IAssemblyName **pName
);
```



## Parameters

<dl> <dt>

*pName* \[out\]
</dt> <dd>

Pointer to the location that contains the pointer to the new instance of [**IAssemblyName**](iassemblyname.md).

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

 

 




