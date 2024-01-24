---
description: The IsValidDevmode function verifies that the contents of a DEVMODE structure are valid.
ms.assetid: 8b4e32cc-5eeb-4a0d-a1b7-f6edb99ed8d8
title: IsValidDevmode function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IsValidDevmode
- IsValidDevmodeA
- IsValidDevmodeW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# IsValidDevmode function

The **IsValidDevmode** function verifies that the contents of a DEVMODE structure are valid.

## Syntax


```C++
BOOL IsValidDevmode(
  _In_ PDEVMODE pDevmode,
       size_t   DevmodeSize
);
```



## Parameters

<dl> <dt>

*pDevmode* \[in\]
</dt> <dd>

A pointer to the [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) to validate.

</dd> <dt>

*DevmodeSize* 
</dt> <dd>

The size in bytes of the input byte buffer.

</dd> </dl>

## Return value

**TRUE**, if the [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) is structurally valid. If minor errors are found the function will fix them and return **TRUE**.

**FALSE**, if the [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) has one or more significant structural problems. For example, its **dmSize** member is misaligned or specifies a buffer that is too small. Also, **FALSE** if **pDevmode** is **NULL**.

## Remarks

No private printer driver fields of the [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) are checked, only the public fields.

Callers should use **dmSize**+**dmDriverExtra** for **DevmodeSize** only if they can guarantee that the input buffer size is at least that big. Since the [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) is generally untrusted data, the values that are in the input buffer at the **dmSize** and **dmDriverExtra** offsets are also untrusted.

This function is executable in Least-Privileged User Account (LUA) context.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Winspool.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl> |
| Unicode and ANSI names<br/>   | **IsValidDevmodeW** (Unicode) and **IsValidDevmodeA** (ANSI)<br/>                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea)
</dt> </dl>

 

 




