---
description: Obtains a reference to a TCP v6 driver object.
ms.assetid: 9f57ea0b-0ab4-4ef9-9bf1-1f41f72dfbe9
title: ReferenceTcpDriverV6 function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ReferenceTcpDriverV6
api_type: 
- LibDef
api_location: 
- Drvref.lib
---

# ReferenceTcpDriverV6 function

Obtains a reference to a TCP v6 driver object.

## Syntax


```C++
NTSTATUS WINAPI ReferenceTcpDriverV6(
  _Out_ PDRIVER_OBJECT *ppDriverObject
);
```



## Parameters

<dl> <dt>

*ppDriverObject* \[out\]
</dt> <dd>

A pointer to a **DRIVER\_OBJECT** structure. For more information, see the documentation for the WDK.

</dd> </dl>

## Return value

If the function succeeds, it returns **STATUS\_SUCCESS**. If it fails, it will return the appropriate status code.

## Remarks

This function can be called only from kernel mode. The caller must decrement the reference count by calling the **ObDereferenceObject** function when it has finished with the object.

This function is implemented in Drvref.lib, which is available for download. See [Windows Network Driver Reference API Library](https://www.microsoft.com/downloads/details.aspx?FamilyID=85037e05-f8f8-46b4-a013-3aa6248396c0).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>Drvref.lib</dt> </dl> |



## See also

<dl> <dt>

[**ReferenceTcpDriver**](referencetcpdriver.md)
</dt> </dl>

 

 




