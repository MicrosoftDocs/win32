---
description: All view classes must have a string array qualifier called ViewSources.
ms.assetid: aefa8cda-962f-4f6c-92a0-a8825d48db60
ms.tgt_platform: multiple
title: ViewSources Qualifier
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ViewSources
api_type: 
- NA
api_location: 
---

# ViewSources Qualifier

All view classes must have a string array qualifier called **ViewSources**. The **ViewSources** qualifier contains the source queries that define the source instances used in the view class. The value of the **ViewSources** qualifier is a string array containing [*WMI Query Language (WQL)*](gloss-w.md) queries. You can define source classes and restrict the source instances your view class uses with the [Querying with WQL](querying-with-wql.md)[WHERE Clause](where-clause.md) to create a filtered view.

The [View Provider](view-provider.md) matches the source queries in the **ViewSources** qualifier to the namespaces listed in the [ViewSpaces qualifier](viewspaces-qualifier.md) in the order the queries and namespaces are listed. The number of source queries must match the number of namespaces listed in the ViewSpaces qualifier. The order in which you list the source queries determines the namespaces from which the source instances are drawn.

The following example selects only instances of the **LocalDisk** class where the value of the **FileSystem** property is "NTFS" and instances of the **RemoteDisk** class where the value of the **FreeSpace** property is greater than 45 megabytes:


```sql
ViewSources{
"SELECT __Namespace, 
   Description, 
   DeviceID, 
   FileSystem, 
   FreeSpace, 
   VolumeName FROM LocalDisk 
 WHERE FileSystem = \"NTFS\"", 
   "SELECT __Namespace, 
   Description,
   DeviceID, 
   FileSystem, 
   FreeSpace, 
   VolumeName FROM RemoteDisk 
 WHERE FreeSpace > 45000000"}
```



> [!Note]  
> The number of source queries you can define for join view classes depends on the number of instances these queries return and how many ways these instances can be joined. The number of possible combinations of source instances for view classes grows exponentially, so keep source queries for join view classes as simple as possible.

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**Qualifiers Specific to the View Provider**](qualifiers-specific-to-the-view-provider.md)
</dt> </dl>

 

 




