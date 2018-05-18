---
title: Properties
description: Properties
ms.assetid: 'ab959ef3-db10-4028-be40-1ebe57376d50'
---

# Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **Properties** entry is a subkey containing a list of entries that are combinations of property set IDs and property names or IDs, each specifying information for a property to cache.

### Summary



|       |             |
|-------|-------------|
| Type: | **REG\_SZ** |



 

### Remarks

Each entry under the **Properties** subkey names a cached property using one of the following forms: *PropertySetID* *PropertyName*, or *PropertySetID* *PropertyID*, where a space character separates the *PropertySetID* and the *PropertyName* or *PropertyID* parts of the name.

Each entry also specifies a value of: *PropertyVarType*,*SizeInBytes*,*StorageLevel*,*Modifiability*, where a comma separates the parts of the value.

The following table gives the meaning of the parts of the name and value of an entry.



| Value             | Meaning                                                                                                                                                                                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *PropertySetID*   | GUID of the property set of the cached property.                                                                                                                                                                                                                |
| *PropertyName*    | Property name of the cached property.                                                                                                                                                                                                                           |
| *PropertyID*      | Property ID of the cached property.                                                                                                                                                                                                                             |
| *PropertyVarType* | Data type of the cached property. For a list of the correspondence between numeric and symbolic variant types, see the [**PROPVARIANT structure.**](_stg_propvariant)                                                                                           |
| *SizeInBytes*     | Size in bytes allocated for the cached property. A value of 0 signifies that the property should be deleted from the property cache.                                                                                                                            |
| *StorageLevel*    | Storage level in the property cache. A value of 0 signifies the Primary Cache, and a value of 1 signifies the Secondary Cache.                                                                                                                                  |
| *Modifiability*   | Modifiability of the cached property. A value of 0 signifies that the property entry can't be modified once cached, and a value of 1 signifies that the other parts of the cached property (such as *SizeInBytes*) can be modified once the property is cached. |



 

An example **Property** entry is the following.

<dl> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

D5CDD502-2E9C-101B-9397-08002B2CF9AE 2

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

30,10,1,1

</dd> </dl>

This entry is for the **Category** property of the DocumentSummaryInformation property set. The data type of the property is VT\_LSTR, 10 bytes of storage are allocated for the property in the Secondary Cache, and the property entry is modifiable.

**Property** entries usually don't occur in the registry until you enter them using the Microsoft Management Console (MMC). If a property is not previously cached, its name and value are added to the registry. If a property is already cached, the value is changed to the newly specified value. Newly cached properties are not available until Indexing Service is restarted.

## Related topics

<dl> <dt>

[Caching Value-Type Properties](caching-value-type-properties.md)
</dt> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> </dl>

 

 




