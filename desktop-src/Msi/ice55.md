---
description: ICE55 validates that all LockPermission objects exist and have valid permission values.
ms.assetid: e23e43ce-942f-4f6b-b5fd-cf366f7a7fe5
title: ICE55
ms.topic: article
ms.date: 05/31/2018
---

# ICE55

ICE55 validates that all LockPermission objects exist and have valid permission values.

## Result

ICE55 post an error if a LockObject listed in the [LockPermissions table](lockpermissions-table.md) does not exist or if no privilege level is specified in the Permission column.

## Example

ICE55 would report the following errors for the example.

``` syntax
LockObject 'File1'.'File'.''.'guest' in the LockPermissions table 
    has a null Permission value. 
Could not find item 'File3' in table 'File' which is referenced 
    in the LockPermissions table.
```

[LockPermissions Table](lockpermissions-table.md) (partial)



| LockObject | Table | Domain | User  | Permission |
|------------|-------|--------|-------|------------|
| File1      | File  |        | guest |            |
| File3      | File  |        | guest | 1          |



 

[File Table](file-table.md) (partial)



| File  | Version | Language |
|-------|---------|----------|
| File1 | File2   |          |
| File2 | 1.0.0.0 | 1033     |



 

The object File1 has a null in the Permission column. Each row must have a value in the Permissions column. To fix this error specify a numeric value in this column. If no privileges are needed for this object then you should remove the row.

The object File3 described in the LockPermissions table is not listed in the File table. To fix this error refer to a valid object.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



