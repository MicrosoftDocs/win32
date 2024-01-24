---
description: You can filter the instances of a join view class by assigning a WQL query to the PostJoinFilter qualifier.
ms.assetid: 926a7262-ea6b-4a5a-8aa7-6ec0ae389031
ms.tgt_platform: multiple
title: PostJoinFilter Qualifier
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PostJoinFilter
api_type: 
- NA
api_location: 
---

# PostJoinFilter Qualifier

You can filter the instances of a join view class by assigning a WQL query to the **PostJoinFilter** qualifier. The value of the WQL query is applied to the instances of the join view class. You can use this qualifier to restrict the instances of your view class to those that meet specific conditions. The following WQL query filters instances of a join class called based on instances of [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk).


```C++
PostJoinFilter("SELECT * FROM JoinDrive" +
    " WHERE FreeSpace > 1000000" +
    " and Description = \"3 1/2 Inch Floppy Drive\"")
```



There are several restrictions to the use of this qualifier:

-   **PostJoinFilter** is only available to join view classes.
-   The class name and property names specified in the query refer to the properties of the view class, not the source class.
-   No exclusion of properties is permitted; only `SELECT *` type queries are allowed.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**Qualifiers Specific to the View Provider**](qualifiers-specific-to-the-view-provider.md)
</dt> </dl>

 

