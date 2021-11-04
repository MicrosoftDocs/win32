---
title: /n switch
description: The /n switch specifies the composition depth for composing metadata files.
ms.assetid: 7A1F8A9E-B3CC-4BB2-BF50-5662D4560280
keywords:
- /n switch MIDL
topic_type:
- apiref
api_name:
- /n
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /n switch

The **/n** switch specifies the composition depth for composing metadata files.

``` syntax
mdmerge /n namespace_depth
```

## Switch Options

<dl> <dt>

*namespace\_depth* 
</dt> <dd>

Specifies the namespace depth to compose into a single metadata file.

</dd> </dl>

## Remarks

Here are the possible value formats that you can specify with the **/n** switch.



| Value format                   | Description                                                                     |
|--------------------------------|---------------------------------------------------------------------------------|
| Int32 > 0                   | Compose all types at the namespace depth specified in the switch.               |
| -1                             | Compose all types into one IDL file per namespace.                              |
| &lt;namespace&gt;:Int32 > 0 | Compose all types with matching namespace at the depth specified in the switch. |
| &lt;namespace&gt;:-1           | Compose all types with matching namespace into one file per namespace.          |



 

The following table shows the results from different combinations of the **/n** switch working on these namespaces.

-   Windows.Foundation.Collections.IIterable
-   Windows.UI.DirectUI.Controls.Button
-   Windows.UI.DirectUI.Controls.ListView
-   Windows.UI.Immersive.Application.PlayTo.Target
-   Windows.Web.Syndication.RSS



| Switches                         | Result                                                                                                                                                                                                                                                       | Explanation                                                                                                                                                                                                                                                                                                                        |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **/n:-1** /**n:1**               | Windows.winmd                                                                                                                                                                                                                                                | The last /n switch overrides all previous –n switches.                                                                                                                                                                                                                                                                           |
| **/n:-1/n:Windows.UI:2**         | <dl> <dt>Windows.Foundation.winmd</dt> <dt>Windows.UI.winmd</dt> <dt>Windows.Web.Syndication.winmd</dt> </dl> | <dl> <dt>**Windows.Foundation** is always composed at –n:2.</dt> <dt>**Windows.UI** types are grouped.</dt> <dt>**Windows.Web.Syndication** is composed at n:-1.</dt> </dl>       |
| **/n:1/n:Windows.UI.DirectUI:3** | <dl> <dt>Windows.Foundation.winmd</dt> <dt>Windows.UI.DirectUI.winmd </dt> <dt>Windows.winmd</dt> </dl>       | <dl> <dt>**Windows.Foundation** is always composed at –n:2.</dt> <dt>**Windows.UI.DirectUI** is composed at level 3.</dt> <dt>All other types are composed at level 1.</dt> </dl> |



 

Here are the rules for handling multiple instances of the **/n** switch.

-   The most specific instance prevails. For example, if you specify **–n:A.B.C:4–n:A.B:5**, MDMERGE resolves A.B.C.D at level 4, because A.B.C is more specific than A.B. A.B.E.F resolves at depth 5, because it matches A.B but not A.B.C.
-   The last instance prevails. For example, if you specify **–n:5–n:2**, the types are composed at level 2.
-   Both of these rules apply. If you specify –n:A.B.C:4 –n:A.B.C:1, namespace A.B.C is composed at level 1.

## Examples

**mdmerge.exe -metadata\_dir $(SDK\_METADATA\_PATH) -i $(INTERNAL\_SDK\_METADATA\_PATH) -o $(OBJ\_PATH)\\$O\\SystemMetadata -v -n:-1 -n:Windows.Foundation:2**

## Requirements



| Requirement | Value |
|-------------------|--------------------------------|
| Client<br/> | Windows 8<br/>           |
| Server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> </dl>

 

 





