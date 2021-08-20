---
title: ' include Directive'
description: Preprocessor directive that inserts the contents of the specified file into the source program at the point where the directive appears.
ms.assetid: 24796d89-5690-469b-950e-df56783aa05a
keywords:
- include Directive HLSL
topic_type:
- apiref
api_name:
- include Directive
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# \#include Directive

Preprocessor directive that inserts the contents of the specified file into the source program at the point where the directive appears.


| \#include "*filename*"       |
|------------------------------|
| \#include <*filename*> |

## Parameters

| Item | Description |
|------|-------------|
| *filename* | Filename of the file to include, optionally preceded by a directory specification. The filename must specify an existing file. |

## Remarks

The \#include directive causes replacement of the directive by the entire contents of the specified file. The preprocessor stops searching as soon as it finds a file with the specified name; if you specify a complete, unambiguous path specification for the file, the preprocessor searches only the specified path.

> [!NOTE]
> The [Effect-Compiler Tool](/windows/desktop/direct3dtools/fxc) has a built-in include handler using the /I switch. However, when executing the compiler from the API, you can provide a customized include handler by implementing the ID3DXInclude interface.

The difference between the two syntax forms is the order in which the preprocessor searches for header files when the path is incompletely specified, as shown in the following table.

<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Syntax form</th>
<th>Preprocessor search pattern</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>#include <b>&quot;</b><em>filename</em><b>&quot;</b></td>
<td>Searches for the include file:
<ol>
<li>in the same directory as the file that contains the #include directive.</li>
<li>in the directories of any files that contain a #include directive for the file that contains the #include directive.</li>
<li>in paths specified by the /I compiler option, in the order in which they are listed.</li>
<li><p>in paths specified by the INCLUDE environment variable, in the order in which they are listed.</p>
<blockquote>
[!NOTE]<br />
The INCLUDE environment variable is ignored in an development environment. Refer to your development environment's documentation for information about how to set the include paths for your project.
</blockquote>
<p><br/></p></li>
</ol></td>
</tr>
<tr class="even">
<td>#include <b><</b><em>filename</em><b>></b></td>
<td>Searches for the include file:
<ol>
<li>in paths specified by the /I compiler option, in the order in which they are listed.</li>
<li><p>in paths specified by the INCLUDE environment variable, in the order in which they are listed.</p>
<blockquote>
[!NOTE]<br />
The INCLUDE environment variable is ignored in an development environment. Refer to your development environment's documentation for information about how to set the include paths for your project.
</blockquote>
<p><br/></p></li>
</ol></td>
</tr>
</tbody>
</table>

## Examples

The following example causes the preprocessor to replace the \#include directive with the contents of stdio.h. Because the example uses the angle bracket format, the preprocessor will search for the file only in the directories listed by the /I compiler option and the INCLUDE environment variable.

```cpp
#include <stdio.h>
```

## See also

- [Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)

- [ID3D10Include Interface](/previous-versions/windows/desktop/legacy/bb173775(v=vs.85))

- [Effect-Compiler Tool](/windows/desktop/direct3dtools/fxc)
