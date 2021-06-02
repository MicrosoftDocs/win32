---
description: Directs the MOF compiler to separate a MOF file into language-neutral and language-specific versions.
ms.assetid: c1aec33c-b936-4cca-8fcd-7bd088af7116
ms.tgt_platform: multiple
title: pragma amendment
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pragma
api_type: 
- NA
api_location: 
---

# pragma amendment

The **pragma amendment** preprocessor command directs the MOF compiler to separate a MOF file into language-neutral and language-specific versions. The language-specific MOF file moves amended qualifiers to a namespace for a specific locale. You then compile the language-specific and language-neutral MOF files to store class information in the WMI repository.

## Examples

The following example shows how to create a MOF file that contains amended qualifiers. You can then compile the MOF code with the following command:

**mofcomp** **-MOF:Lnmof.mof** **-MFL:Lsmof.mfl** **Mastermof.mof**

The command instructs the MOF compiler to produce two MOF files from the original Mastermof.mof file. The MOF compiler produces a language-neutral version of the MOF file, called Lnmof.mof, with all language-specific items removed. The compiler also creates a second, language-specific MOF file called Lsmof.mfl that contains only items that you must localize.

> [!Note]  
> When you are splitting a MOF file with the **amendment** qualifier or the **pragma amendment** command, you must specify the **-MOF** and **-MFL** options. Otherwise, the compiler does not generate any output files. You must then compile the two output files to make the class information available to WMI.

 


```mof
#pragma amendment ("MS_409")

[Description("Localized version of MyClass" for American English") :
    Amended, LOCALE(0x409)] 

Class myclass
{
     [DisplayName("User Name") : Amended,
     Description("The Name property contains the name of the user") : 
     Amended, key]
    string Name;

    uint64 Value; // non-localized value field

     [DisplayName("Time Stamp") : Amended,
     Description("This property shows when the object was created") : 
     Amended] 
    uint64 Timestamp;
};
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[Preprocessor Commands](preprocessor-commands.md)
</dt> </dl>

 

 




