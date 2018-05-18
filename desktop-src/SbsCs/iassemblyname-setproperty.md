---
Description: 'The SetProperty method adds a name-value pair to the side-by-side assembly name. This method can change or delete the value of an existing name-value pair.'
ms.assetid: '057bc5b3-008b-495b-b96c-2c0dcc43f1a4'
title: 'IAssemblyName::SetProperty method'
---

# IAssemblyName::SetProperty method

The **SetProperty** method adds a name-value pair to the side-by-side assembly name. This method can change or delete the value of an existing name-value pair.

## Syntax


```C++
HRESULT SetProperty(
  [in]           DWORD  PropertyId,
  [in]           LPVOID pvProperty,
  [in, optional] DWORD  cbProperty
);
```



## Parameters

<dl> <dt>

*PropertyId* \[in\]
</dt> <dd>

A property ID that represents the name-value pair. Valid property IDs are [**ASM\_NAME**](asm-name-.md) enumeration values.

</dd> <dt>

*pvProperty* \[in\]
</dt> <dd>

A pointer to a buffer that contains the value of the name-value pair.

</dd> <dt>

*cbProperty* \[in, optional\]
</dt> <dd>

The size in bytes of the buffer specified by *pvProperty*. Set the value of this parameter to zero to remove the name-value pair from the assembly name.

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                             | Description                                                                                                                                                                |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The method succeeded.<br/>                                                                                                                                           |
| <dl> <dt>S\_FALSE</dt> </dl>      | The method did not succeed.<br/>                                                                                                                                     |
| <dl> <dt>E\_UNEXPECTED</dt> </dl> | The method did not succeed. The [**SetProperty**](iassemblyname-setproperty.md) method was called after the [**Finalize**](iassemblyname-finalize.md) method.<br/> |



 

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

 

 




