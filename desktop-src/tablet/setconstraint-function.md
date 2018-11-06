---
Description: Sets a constraint on the prefix of all recognition results.
ms.assetid: 0e804b11-eca0-40c7-bfdf-289ac3aa1e1f
title: SetConstraint function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetConstraint
api_type: 
- NA
api_location: 
---

# SetConstraint function

Sets a constraint on the prefix of all recognition results.

## Syntax


```C++
HRESULT WINAPI SetConstraint Function(
  _In_ HRECOCONTEXT hrc,
  _In_ int          cwcConstraint,
  _In_ WCHAR        *pwcConstraint
);
```



## Parameters

<dl> <dt>

*hrc* \[in\]
</dt> <dd>

The handle to the recognizer context.

</dd> <dt>

*cwcConstraint* \[in\]
</dt> <dd>

The number of characters in *pwcConstraint*.

</dd> <dt>

*pwcConstraint* \[in\]
</dt> <dd>

Unicode (wide) characters representing a prefix. The *pwcConstraint* parameter cannot contain spaces or control characters. The string is not **NULL** terminated.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                                 | Description                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Success.<br/>                                                                                                                           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>                   | The recognizer does not support this function.<br/>                                                                                     |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | An unspecified error occurred. The *pwcConstraint* parameter must not contain spaces or control characters.<br/>                        |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Unable to allocate memory to complete the operation.<br/>                                                                               |
| <dl> <dt>**E\_POINTER**</dt> </dl>                   | The recognizer context is invalid.<br/>                                                                                                 |
| <dl> <dt>**TPC\_E\_OUT\_OF\_ORDER\_CALL**</dt> </dl> | You must call the [**SetConstraint**](setconstraint-function.md) function before calling the [**Process**](/windows/desktop/api/recapis/nf-recapis-process) function.<br/> |



 

## Remarks

This function is optional.

To clear a prefix constraint, set it to an empty string (a zero-length string).

The constraint works with any factoid setting and also applies to any result that is not in the recognizer dictionary. When using a constraint, process context (strings that appear before and after the text to be recognized) as you normally would. Setting or resetting this constraint does not alter a factoid that is already set.

The constraint does not function unless the recognizer is running in word mode (the [**SetFlags**](/windows/desktop/api/recapis/nf-recapis-setflags) function is called to set the **RECOFLAG\_WORDMODE** flag); however, the recognizer context maintains any factoid constraint if you set it to other RECOFLAG modes.

The recognizer flag **RECOFLAG\_PREFIXOK** does not pertain to a constraint. For instance, if you set the constraint, *qui*, along with the **RECOFLAG\_PREFIXOK** flag, the recognizer does not consider the string, *qu*, a valid word. However, *qui* or *quie* are considered valid words, because they are prefixes for *quiet* that satisfy the constraint.

## See also

<dl> <dt>

[**SetFactoid**](/windows/desktop/api/recapis/nf-recapis-setfactoid)
</dt> <dt>

[**SetFlags**](/windows/desktop/api/recapis/nf-recapis-setflags)
</dt> <dt>

[**SetTextContext**](https://msdn.microsoft.com/en-us/library/ms704873(v=VS.85).aspx)
</dt> </dl>

 

 




