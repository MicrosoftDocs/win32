---
title: usesgetlasterror
description: Tells the caller that, if there is an error when calling that function, the caller can then call GetLastError to retrieve the error code.
ms.assetid: 875e3837-86ff-41cd-a45a-891f72983e07
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# usesgetlasterror

Tells the caller that, if there is an error when calling that function, the caller can then call GetLastError to retrieve the error code.

## Allowed on

Member of a module.

## Remarks

The usesgetlasterror attribute can be set on a module entry point, if that entry point uses the SetLastError function to return error codes. The attribute tells the caller that, if there is an error when calling that function, the caller can then call GetLastError to retrieve the error code.

## Example


```C++
[dllname("MyOwn.dll")] module MyModule
    {
    [entry("One"), usesgetlasterror, bindable, requestedit,
   propputref, defaultbind]
        void Func1 ([in]IUnknown * iParam1, [out] long * Param2) ;
    [entry("TwentyOne"), usesgetlasterror, hidden, vararg]
         SAFEARRAY (int) Func2 ([in, out] SAFEARRAY (variant) *varP) ;
. . .};
  
```



## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




