---
description: Applications must allocate memory for this data; TAPI and the service provider provide the data. If the operation is asynchronous, the data is not available until the asynchronous reply message indicates success.
ms.assetid: 61313fe3-74a1-4195-b5af-37463dad02c1
title: Memory Allocation
ms.topic: article
ms.date: 05/31/2018
---

# Memory Allocation

Applications must allocate memory for this data; TAPI and the service provider provide the data. If the operation is asynchronous, the data is not available until the asynchronous reply message indicates success.

All data structures used to pass data between the application and the TAPI are *flattened*. That is, data structures do not contain pointers to substructures that contain variably sized data components. Instead, data structures used to pass variable amounts of data back to the application must have the following metastructure:

``` syntax
  DWORD  dwTotalSize;
  DWORD  dwNeededSize;
  DWORD  dwUsedSize; 
    <fixed size fields> 
  DWORD  dw<VarSizeField1>Size;
  DWORD  dw<VarSizeField1>Offset; 
    <fixed size fields> 
  DWORD  dw<VarSizeField2>Size;
  DWORD  dw<VarSizeField2>Offset; 
    <common extensions> 
    <var sized field1> 
    <var sized field2>
```

The **dwTotalSize** member is the size, in bytes, allocated to this data structure. It marks the end of the data structure and is set by the application before it invokes the function that uses this data structure. The function does not read or write beyond this size. An application must set the **dwTotalSize** member to indicate the total number of bytes allocated for TAPI to return the contents of the structure.

TAPI fills in the **dwNeededSize** member. It indicates how many bytes are required to return all the requested data. The existence of variably sized fields often makes it impossible for the application to estimate the data structure size required to allocate. This field returns the number of bytes actually required for the data. This number could be smaller than, equal to, or larger than **dwTotalSize**, and it includes space for the **dwTotalSize** member itself. If larger, the returned structure is only partially filled. If the fields the application requires are available in the partial structure, nothing else must be done. Otherwise, the application should allocate a structure at least the size of **dwNeededSize** and invoke the function again. Usually, enough space is available this time to return all the information, although it is possible the size could have increased again.

TAPI fills the **dwUsedSize** member if it returns data to the application to indicate the actual size, in bytes, of the portion of the data structure that contains useful data. If, for example, a structure that was allocated was too small and the truncated field is a variably sized field, **dwNeededSize** is larger than **dwTotalSize**, and the truncated field is left empty. The **dwUsedSize** member could therefore be smaller than **dwTotalSize**. Partial field values are not returned.

Following this header is the fixed part of the data structure. It contains regular fields and size/offset pairs that describe the actual variably sized fields. The offset field contains the offset in bytes of the variably sized field from the beginning of the record. The size field contains the size in bytes of the variably sized field. If a variably sized field is empty, then the size field is zero and the offset is set to zero. Variably sized fields that would be truncated if the total structure size is insufficient are left empty. That is, their size field is set to zero and the offset is set to zero. The variably sized fields follow the fixed fields.

If the service provider must fill a variable member, TAPI initializes the corresponding size and offset members to zero. If the service provider fills in the variable member, it must set the corresponding size and offset members to appropriate values, including **dwUsedSize** and **dwNeededSize** if it sets variable members. The service provider must not truncate a variable member to make it fit into the available space.

The service provider must start variable members immediately after the fixed members of the structure, and leave any extra space at the end of the allocated memory so that TAPI can use it for the variable-length members. It can place the variable members in any order, but the members must be contiguous.

 

 



