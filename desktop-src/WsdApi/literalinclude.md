---
description: Places a C or IDL include statement in the generated code.
ms.assetid: 7a7ffd54-09e9-412d-a637-5dc27597b46e
title: literalInclude element
ms.topic: reference
ms.date: 05/31/2018
---

# literalInclude element

Places a C or IDL include statement in the generated code.

## Usage

``` syntax
<literalInclude
  Language = "language string"
  Local = "Boolean"/>
```

## Attributes



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Language</strong><br/></td>
<td>language string<br/></td>
<td>No<br/></td>
<td>The type of header file to be included. <br/> <br/>
<dt><strong>C</strong></dt> <dd> Include a C header file.<br/> </dd> <dt><strong>IDL</strong></dt> <dd> Include an IDL file.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>Local</strong><br/></td>
<td>Boolean<br/></td>
<td>No<br/></td>
<td>This attribute is only used when <strong>Language</strong> is set to &quot;C&quot;.<br/> <br/>
<dt><strong>True</strong></dt> <dd> Searches the current directory for the named header before searching the system directories.<br/> </dd> <dt><strong>False</strong></dt> <dd> Only search system directories for the named header.<br/> </dd> </dl></td>
</tr>
</tbody>
</table>



## Child elements

There are no child elements.

## Parent elements



| Element                         | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| [**file**](file.md)<br/> | Outputs a file from the code generator.<br/> <br/> |



## Remarks

The following examples show the code generated from different **literalInclude** elements.

### Example 1 - Generating a C include statement

Input XML:

``` syntax
<literalInclude Language="C" Local="False">wsdapi.h</literalInclude>
```

Output code:

``` syntax
#include <wsdapi.h>
```

### Example 2 - Generating a C include statement

Input XML:

``` syntax
<literalInclude Language="C" Local="True">wsdapi.h</literalInclude>
```

Output code:

``` syntax
#include "wsdapi.h"
```

### Example 3 - Generating an IDL import statement

Input XML:

``` syntax
<literalInclude Language="IDL">wsdclient.idl</literalInclude>
```

Output code:

``` syntax
import wsdclient.idl;
```

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




