---
title: disable_consistency_check Attribute
description: Directs RPC to not enforce correlation consistency checking.
ms.assetid: 33ba331d-56e5-4965-a844-7780ea81623d
ms.topic: article
ms.date: 05/31/2018
---

# disable\_consistency\_check Attribute

Directs RPC to not enforce correlation consistency checking.

``` syntax
interface interface-name
{
  return-type function-name(
        [[attribute-list,] disable_consistency_check] param-type param-name
}
```

For correlated parameters, RPC will enforce that a non-null buffer is passed when the correlation count variable is non-null.

## Example

``` syntax
HRESULT PassString( [in] DWORD Length, [in, unique, string, 
    size_is( Length )]LPWSTR MyString );
```

If *MyString* is **NULL**, RPC will reject the call unless Length is set to 0. Note that RPC will allow *Length* to be 0 while *MyString* is non-NULL, and RPC will treat *MyString* as a 0-length buffer allocation.

## Remarks

To disable this checking, the IDL can contain the \[disable\_consistency\_check\] attribute on a parameter, typedef, or pointer type. This will direct RPC to not enforce the consistency between the buffer pointer and the correlation variable for the buffer pointed to by the parameter or pointer.

To disable consistency checking for an entire MIDL compilation (and disable enforcement of the checking in all cases), the MIDL command line switch [/backward\_compat maybenull\_sizeis](-backward-compat.md) can be used. This requires that the target of the MIDL compilation be at least â€“target NT60.

 

 




