---
description: ICE49 checks for default registry entries that are not a REG\_SZ type.
ms.assetid: 53d976fe-07d2-4b68-ae21-1dbd00d76942
title: ICE49
ms.topic: article
ms.date: 05/31/2018
---

# ICE49

ICE49 checks for default registry entries that are not a **REG\_SZ** type.

## Result

ICE49 posts an warning if there is a default registry entry that is not a **REG\_SZ** type.

## Example

ICE49 reports the following warning for the example shown.

``` syntax
Reg Entry 'Reg1' is not of type REG_SZ. Default types must be REG_SZ 
    on Win95 Systems. Make sure the component is conditionalized 
    to never be installed on Win95 machines.
```

The value '\#123' is a **DWORD** registry value.

[Registry Table](registry-table.md) (partial)



| Registry | Name | Value |
|----------|------|-------|
| Reg1     |      | \#123 |



 

To fix this warning, change the value to type **REG\_SZ**.

Components with non-**REG\_SZ** are valid.

## Related topics

<dl> <dt>

[Conditional Statement Syntax](conditional-statement-syntax.md)
</dt> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



