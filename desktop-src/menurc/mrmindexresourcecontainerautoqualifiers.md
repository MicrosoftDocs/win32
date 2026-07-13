---
title: MrmIndexResourceContainerAutoQualifiers function (MrmResourceIndexer.h)
description: Adds the string resources embedded in a resource container to a Resource Indexer, inferring the resource names and qualifiers from the file path.
ms.assetid: 7FCAA2B5-FF45-4961-84BA-B444B550C91D
keywords:
- MrmIndexResourceContainerAutoQualifiers function Menus and Other Resources
topic_type:
- apiref
api_name:
- MrmIndexResourceContainerAutoQualifiers
api_location:
- Mrmsupport.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MrmIndexResourceContainerAutoQualifiers function

Adds the string resources embedded in a resource container to a Resource Indexer, inferring
the resource names and qualifiers from the container path. A resource container is a file such as a
`resw` or `resjson` file that contains a list of resource name / value pairs. You can also add the
contents of an existing existing PRI file to the indexer with this function. Note that it is the 
resource names inside the container that are indexed, not the values.

## Syntax


```C++
HRESULT HRESULT MrmIndexResourceContainerAutoQualifiers(
  _In_ MrmResourceIndexerHandle indexer,
  _In_ PCWSTR                   containerPath
);
```



## Parameters

<dl> <dt>

*indexer* \[in\]
</dt> <dd>

Type: **[**MrmResourceIndexerHandle**](mrmresourceindexerhandle.md)**

A handle identifying the resource indexer to add the resources to. This handle is returned via a call to 
[**MrmCreateResourceIndexer**](mrmcreateresourceindexer.md) or one of the related **MrmCreateResourceIndexer...*** functions.


</dd> <dt>

*containerPath* \[in\]
</dt> <dd>

Type: **PCWSTR**

A path to a `resw`, `resjson`, or `.pri` file containing string resources that you want to add to the index. 
This path is relative to the project root specified when creating the indexer via one of the 
**MrmCreateResourceIndexer...** functions. The file must exist.

</dd> </dl>

## Return value

Type: **HRESULT**

S\_OK if the function succeeded, otherwise some other value. Use the **SUCCEEDED** or **FAILED** macros (defined in winerror.h) 
to determine success or failure.

## Remarks

This function infers the resource names and qualifiers from both *containerPath* and the resources inside the
container itself. The file identified by *containerPath* does not need to be included in your final app installation 
package.

The algorithm for computing resource names differs depending on the file type:

### For resw and resjson files:

Given a *containerPath* of the form `path1\path2\pathn\filename.ext`, the following basic algorithm is used:

1. Let `resourceName` be the string `ms-resource:///`.
1. Let `qualifiers` be an empty string.
1. For each `path` segment in *filePath*, check if it consists of a valid qualifier list string
(see [Qualifiers in MRM](mrmqualifiers.md) for more info). If so, append those qualifiers to `qualifiers`,
otherwise ignore it.
1. For `filename`, split it up into segments separated by dots (`.`). Note that `.ext` is ignored.
   * If there are exactly two segments, and the second segment is a valid qualifier list, 
   add it to `qualifiers` and append the first segment to`resourceName`.
   * Otherwise, append the entire `filename` (but not `.ext`) `resourceName`.
1. For each resource name inside `filename`, replaces any dots (`.`) with forward slashes (`/`) and append
it to `resourceName`, then add to the indexer with the specified value and `qualifiers`.
    * Note there is no attempt to infer qualifiers from the resource name inside the container; the
    name is just added verbatim to the `resourceName`

For example:

| filePath | resource name (inside file) | resourceName | qualifiers |
|-|-|-|-|
| resources.resw | my_string | ms-resource:///resources/my_string | \<N/A> |
| images.resw | logo.scale-200.png | ms-resource:///images/logo/scale-200/png | \<N/A> |
| **language-es**\\text.**homeregion-mx**.resjson | greeting | ms-resource:///text/greeting | language-es_homeregion-mx |
| content\\**language-jp**\\menu.scale-100.submenu.resjson | title.text | ms-resource:///menu.scale-100.submenu/title/text | language-jp |

The last line of the table illustrates three of the more subtle parts of the algorithm:

1. Directory names that aren't qualifiers are ignored (in this case, "content").
1. Embedded qualifiers in filenames are ignored if there are additional segments (in this case, ".submenu").
1. Dots inside resource names are turned into slashes (but dots inside file paths are retained).
    
In some cases, having embedded dots or slashes inside a resource name inside a container will lead to
an error **0x80073b39** when creating the resource file (not when adding it to the index). In general,
it is best to avoid embedded slashes or dots in names, and to avoid embedded qualifiers since they will
be ignored.

### For PRI files:

Because PRI files already contain resources with qualifier information, no qualifiers are inferred
from *filePath*; it is simply the name of the file to read. When indexing resources from within the PRI file,
for a given resource name `ms-resource:///rootPath/theRest...` the following algorithm is used:

1. If the type of resource is `String`, then replace `rootPath` with "strings" and use the result as the
resource name.
1. Otherwise (the type of the resource is `Path` or `EmbeddedData`), use the resource name as-is.

The value and qualifiers are added verbatim from the PRI file, with this new resource name.

## Requirements


| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1803 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>MrmResourceIndexer.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>Mrmsupport.lib</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Mrmsupport.dll</dt> </dl>       |



## See also
<dt><dt>

[**MrmIndexEmbeddedData**](mrmindexembeddeddata.md)
</dt></dl>

<dt><dt>

[**MrmIndexFile**](mrmindexfile.md)
</dt></dl>

<dt><dt>

[**MrmIndexFileAutoQualifiers**](mrmindexfileautoqualifiers.md)
</dt></dl>

<dt><dt>

[**MrmIndexString**](mrmindexstring.md)
</dt></dl>

<dt><dt>

[File resources in MRM](mrmfiles.md)
</dt></dl>

<dt><dt>

[Package resource indexing (PRI) APIs and custom build systems](/windows/uwp/app-resources/pri-apis-custom-build-systems)
</dt></dl>
