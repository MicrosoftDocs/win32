---
title: helpfile attribute
description: The \ helpfile\ attribute sets the name of the Help file for a type library. All types in a library share the same Help file.
ms.assetid: caa248b1-a1a7-4c36-886a-079a66a01907
keywords:
- helpfile attribute MIDL
topic_type:
- apiref
api_name:
- helpfile
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# helpfile attribute

The **\[helpfile\]** attribute sets the name of the Help file for a type library. All types in a library share the same Help file.

``` syntax
[
    uuid(uuid-number), 
    helpfile("filename") 
    [, optional-attribute-list]
] 
library 
{
    library statements
};
```

## Parameters

<dl> <dt>

*uuid-number* 
</dt> <dd>

Specifies a universally unique identification number for the [**library**](library.md).

</dd> <dt>

*filename* 
</dt> <dd>

Specifies the name of the file containing the help text.

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that the MIDL compiler will apply to the [**library**](library.md).

</dd> <dt>

*library statements* 
</dt> <dd>

Specifies one or more MIDL statements that define the library interface.

</dd> </dl>

## Remarks

Use the **GetDocumentation** functions in the **ITypeLib** and **ITypeInfo** interfaces to retrieve the file name.

## Examples

``` syntax
[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676),
    helpfile("filename.hlp"),
    lcid(0x0409), 
    version(2.0)
]
library Hello
{
    /* Library definition statements here. */
};
```

## See also

<dl> <dt>

[**library**](library.md)
</dt> <dt>

[ODL File Syntax](df7aa86f-1453-4409-939e-788d469d611e)
</dt> <dt>

[ODL File Example](86d64a4f-08eb-422a-bb1d-dfa868094645)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 




