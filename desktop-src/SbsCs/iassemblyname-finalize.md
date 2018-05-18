---
Description: 'The Finalize method prevents a side-by-side assembly name from being changed. After Finalize is called, additional calls to the SetProperty returns E\_UNEXPECTED.'
ms.assetid: '9930826e-3082-4ad3-991e-13cf426983a4'
title: 'IAssemblyName::Finalize method'
---

# IAssemblyName::Finalize method

The **Finalize** method prevents a side-by-side assembly name from being changed. After **Finalize** is called, additional calls to the [**SetProperty**](iassemblyname-setproperty.md) returns **E\_UNEXPECTED**.

## Syntax


```C++
HRESULT Finalize();
```



## Parameters

This method has no parameters.

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

 

 




