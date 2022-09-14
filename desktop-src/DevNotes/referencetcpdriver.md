---
description: Obtains a reference to a TCP v4 driver object.
ms.assetid: 8f12fa58-1622-40d0-9a99-e7c8ede08b38
title: ReferenceTcpDriver function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ReferenceTcpDriver
api_type: 
- LibDef
api_location: 
- Drvref.lib
---

# ReferenceTcpDriver function

Obtains a reference to a TCP v4 driver object.

## Syntax


```C++
NTSTATUS WINAPI ReferenceTcpDriver(
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

[**ReferenceTcpDriverV6**](referencetcpdriverv6.md)
</dt> </dl>

 

 




