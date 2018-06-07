---
title: dllname(str) attribute
description: The \ dllname\ attribute defines the name of the DLL that contains the entry points for a module.
ms.assetid: dbf062ce-9dcc-4cc6-b7cd-cdc5945e399b
keywords:
- dllname(str) attribute MIDL
topic_type:
- apiref
api_name:
- dllname(str)
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# dllname(str) attribute

The **\[dllname\]** attribute defines the name of the DLL that contains the entry points for a module.

``` syntax
[
    uuid(uuid-number), 
    dllname("filename")
    [, optional-attribute-list]
]
module modulename
{
    elementlist
};
```

## Parameters

<dl> <dt>

*uuid-number* 
</dt> <dd>

Specifies a universally unique identification number for the [**module**](module.md).

</dd> <dt>

*filename* 
</dt> <dd>

Specifies a NULL-terminated string which contains the full path to the Dll file.

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Specifies a list of zero or more MIDL interface attributes.

</dd> <dt>

*modulename* 
</dt> <dd>

Specifies the name which other software components can use to refer to the module.

</dd> <dt>

*elementlist* 
</dt> <dd>

Specifies one or more module element definition statements.

</dd> </dl>

## Remarks

The **\[dllname\]** attribute is required on a module.

## Examples

``` syntax
[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676),
    helpstring("A meaningful comment"),   
    dllname("HANDY.DLL")
] 
module HandyStuff
{
    /* Module content definitions */
};
```

## See also

<dl> <dt>

[**module**](module.md)
</dt> <dt>

[**entry**](entry.md)
</dt> <dt>

[ODL File Syntax](https://msdn.microsoft.com/windows/desktop/df7aa86f-1453-4409-939e-788d469d611e)
</dt> <dt>

[ODL File Example](https://msdn.microsoft.com/windows/desktop/86d64a4f-08eb-422a-bb1d-dfa868094645)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 




