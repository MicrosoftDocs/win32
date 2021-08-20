---
title: warning pragma Directive
description: Pragma directive that modifies the behavior of compiler warning messages.
ms.assetid: 69488014-36e3-4c87-8b65-6123b5e87bcb
keywords:
- warning pragma Directive HLSL
topic_type:
- apiref
api_name:
- warning pragma Directive
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# warning pragma Directive

Pragma directive that modifies the behavior of compiler warning messages.



| \#pragma warning( *warning-specifier* : *warning-number-list* \[; *warning-specifier* : *warning-number-list*...\] ) |
|----------------------------------------------------------------------------------------------------------------------|



 

## Parameters



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="warning-specifier"></span><span id="WARNING-SPECIFIER"></span><em>warning-specifier</em><br/></td>
<td>Behavior to set for the specified warnings. This parameter can take one of the values listed in the following table. <br/> 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>once</td>
<td>Display the message of the warnings with the specified numbers only once.</td>
</tr>
<tr class="even">
<td>default</td>
<td>Reset the behavior of the warnings with the specified numbers to their default value. This also has the effect of turning a warning on that is off by default. The warning will be generated at its default level.</td>
</tr>
<tr class="odd">
<td>1, 2, 3, 4</td>
<td>Apply the specified level to the warnings with the specified numbers. This also has the effect of turning a warning on that is off by default.</td>
</tr>
<tr class="even">
<td>disable</td>
<td>Do not issue the warnings with the specified numbers.</td>
</tr>
<tr class="odd">
<td>error</td>
<td>Report the warnings with the specified numbers as errors.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td><p><span id="warning-number-list"></span><span id="WARNING-NUMBER-LIST"></span><em>warning-number-list</em></p></td>
<td><p>White space-delimited list of the numbers of the warnings to modify the behavior of.</p></td>
</tr>
</tbody>
</table>



 

## Remarks

You can specify any number of distinct warning behavior changes within the same warning pragma by separating the changes with semicolons.

The compiler will add 4000 to any warning number that is between 0 and 999. For warning numbers greater than 4699, (those associated with code generation) the warning pragma has effect only when placed outside function definitions. The pragma is ignored if it specifies a number greater than 4699 and is used inside a function.

The HLSL warning pragma does not support the **push** and **pop** functionality of the warning pragma included in the C++ compiler.

## Examples

The following example disables warnings 4507 and 4034, displays warning 4385 once once, and reports warning 4164 as an error.


```
#pragma warning( disable : 4507 34; once : 4385; error : 164 )
```



The preceding example is functionally equivalent to the following:


```
#pragma warning( disable : 4507 34 )
#pragma warning( once : 4385 )
#pragma warning( error : 164 )
```



## See also

<dl> <dt>

[Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)
</dt> <dt>

[\#pragma Directive (DirectX HLSL)](dx-graphics-hlsl-appendix-pre-pragma.md)
</dt> </dl>

 

 





