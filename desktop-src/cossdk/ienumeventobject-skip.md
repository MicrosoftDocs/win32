---
Description: 'Skips over the specified number of items in the enumeration sequence.'
ms.assetid: '7c830d29-8e66-4139-9445-d83dc7f7004f'
title: 'IEnumEventObject::Skip method'
---

# IEnumEventObject::Skip method

Skips over the specified number of items in the enumeration sequence.

## Syntax


```C++
HRESULT Skip(
  [in] ULONG cSkipElem
);
```



## Parameters

<dl> <dt>

*cSkipElem* \[in\]
</dt> <dd>

The number of elements to be skipped.

</dd> </dl>

## Return value

This method can return the following values.



| Return code                                                                             | Description                                                                         |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | The requested number of elements was skipped.<br/>                            |
| <dl> <dt>**S\_FALSE**</dt> </dl> | The number of elements skipped was not the same as the number requested.<br/> |



 

## Remarks

**Skip** may return S\_FALSE if *cSkipElem* is greater than the remaining number of elements. In this case, **Skip** moves to the last element in the enumeration sequence.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| IDL<br/>                      | <dl> <dt>Eventsys.idl</dt> </dl> |



## See also

<dl> <dt>

[**IEnumEventObject**](ienumeventobject.md)
</dt> </dl>

 

 




