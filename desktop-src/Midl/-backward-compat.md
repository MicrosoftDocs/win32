---
title: /backward_compat Switch
description: The /backward\_compat switch directs the MIDL compiler to turn off some advanced features when generating RPC/COM stubs.
ms.assetid: eec0ade7-30a0-44e4-92e9-fb03ff657723
ms.topic: article
ms.date: 05/31/2018
---

# /backward\_compat Switch

The /backward\_compat switch directs the MIDL compiler to turn off some advanced features when generating RPC/COM stubs.

``` syntax
midl /backward_compat { maybenull_sizeis | zeroout_alignmentgap | 
     BSTR_byvalue_escaping | string_defaultvalue | signed_wchar_t }
```

## Switch Options

*maybenull\_sizeis*<dl> Applies the [\[disable\_consistency\_check\]](disable-consistence-check.md) attribute to an entire MIDL compilation.  
</dl>

*zeroout\_alignmentgap*<dl> Turns off zeroing out gaps in the marshaled buffer.  
</dl>

*BSTR\_byvalue\_escaping*<dl> Directs the MIDL compiler to honor escape sequences such as â€˜\\nâ€™ or â€˜\\tâ€™ in BSTRs.  
</dl>

*string\_defaultvalue*<dl> Forces the MIDL compiler to coerce strings in [**\[defaultvalue\]**](defaultvalue.md) attributes into VARIANT.VT\_I4 type before coercing the value into the correct type.  
</dl>

*signed\_wchar\_t*<dl> Directs MIDL to treat the wchar\_t type as signed for compatibility with Visual Basic.  
</dl>

## Remarks

-   *maybenull\_sizeis*: See \[disable\_consistency\_check\].
-   *zeroout\_alignmentgap*: When IDLs are compiled with â€“target NT60 or higher, MIDL will create stubs that zero out any alignment gaps between members or a structure in the wire buffer. The command line switch */backward\_compat zeroout\_alignmentgap* directs MIDL to disable this feature.

    In the following example structure, the wire buffer contains a 7 byte alignment gap to align the hyper member to 8 after the char member. With â€“target NT60 or higher, MIDL will zero out that gap unless the switch is used.

    IDL file:

    ``` syntax
    typedef struct _structwithgaps{
        char c;
        // 7 byte gap to align the following hyper to 8 
        hyper h;
    } structwithgap;
    ```

    This switch can provide a slight performance improvement with potentially significant increases in disclosure risk.

-   *BSTR\_byvalue\_escaping*: By default, the MIDL compiler does not process escape sequences such as â€˜\\nâ€™ or â€˜\\tâ€™ in string constants for OLE Automation when converting a string constant to types VT\_LPSTR or VT\_LPWSTR. With this backward compatibility switch option, the escape sequences are evaluated.
-   *string\_defaultvalue*: Forces the MIDL compiler to coerce numeric strings in [**\[defaultvalue\]**](defaultvalue.md) attributes into VARIANT.VT\_I4 type before coercing the value into the correct type. This can lead to loss of precision in some cases, so this switch option is not recommended.
-   *signed\_wchar\_t*: Directs MIDL to treat the wchar\_t type as signed for compatibility with Visual Basic.

 

 




