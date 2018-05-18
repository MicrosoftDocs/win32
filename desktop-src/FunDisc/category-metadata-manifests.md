---
Description: Category Metadata Manifests
ms.assetid: '66f107e9-3328-4d3d-9340-e7a55a60285b'
title: Category Metadata Manifests
---

# Category Metadata Manifests

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

Manifest entries appear in the registry for queries made to layered categories or subcategories. The following registry subkeys specify a manifest entry.

```
HKLM\SOFTWARE\Microsoft\Function Discovery\Categories\Layered
   categoryN
      subcategory1
      subcategoryX
```

Manifest entries should be REG\_SZ string values containing valid XML data of the following form:

``` syntax
<categoryMetaData name="All User files" RecurseSubcategory="FALSE" >
    <querydefinition>
        <category identity="File System"/>
        <queryconstraints>
            <queryconstraint name="SubCategory" value="\Users\all users"/>
            <queryconstraint name="&" value="&"/>
        </queryconstraints>
    </querydefinition>
</categoryMetaData>
```

Any additional information within the XML data will be ignored. When specifying query constraints, the grouping element **queryconstraints** is optional.

The **RecurseSubcategory** attribute controls how Function Discovery will handle the RecurseSubcategory query constraint. By default the attribute is set to True, which means that the category manager will recurse all the keys in the registry from the specified starting point and construct queries to return the results based on each of the registry keys.

Category definitions must not be cyclical. All categories must resolve to a provider category that will be used to locate the function instances in response to a query of the category. Metadata categories can be composed of other metadata categories. These category compositions can be at most nine levels deep.

> [!Note]  
> At run time, Function Discovery will return the error HRESULT\_FROM\_WIN32( ERROR\_SXS\_XML\_E\_INTERNALERROR ) if the above requirements are not met.

 

The category manager does not support multiple **categoryMetaData** or **querydefinition** elements in the same REG\_SZ value; however, multiple REG\_SZ values can be created in a single registry key and Function Discovery will create multiple queries and aggregate the results for the client.

> [!Note]  
> Property constraints are currently not supported as part of the manifest query definition.

 

## Related topics

<dl> <dt>

[Provider Manifest Entries](provider-manifest-entries.md)
</dt> </dl>

 

 



