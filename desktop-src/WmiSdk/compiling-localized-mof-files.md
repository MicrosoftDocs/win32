---
description: You must compile your master MOF file to create the language-neutral and language-specific MOF files.
ms.assetid: ae2fa320-8294-4991-be30-403088c34b7a
ms.tgt_platform: multiple
title: Compiling Localized MOF Files
ms.topic: article
ms.date: 05/31/2018
---

# Compiling Localized MOF Files

You must compile your master MOF file to create the language-neutral and language-specific MOF files.

Type the following command at a command prompt to compile a master MOF file.

**mofcomp -MOF:Lnmof.mof -MFL:Lsmof.mfl -Amendment:MS\_409 Mastermof.mof**

When you run this command, the MOF compiler creates two MOF files from the original Mastermof.mof file. The MOF compiler produces a language-neutral version, Lnmof.mof, in which all language-specific items are removed. A second, language-specific version, Lsmof.mof, is also created; this file contains only items that were marked with the [**Amended**](qualifier-flavors.md) Qualifier Flavor in the Mastermof.mof file.

The following code example shows the contents of the language-neutral MOF file (Lnmof.mof) that is generated.

``` syntax
#pragma namespace("\\\\.\\root")

Instance of __Namespace
{
  Name = "TEST";
};
#pragma namespace("\\\\.\\root\\TEST")

[LOCALE(1033)] 
class myclass
{
  [key] string Name;
  uint64 Value;
  uint64 Timestamp;
};
```

The following code example shows the contents of the language-specific MOF file (Lsmof.mfl) that is generated.

``` syntax
#pragma namespace("\\\\.\\root\\TEST")
instance of __namespace{ name="ms_409";};
#pragma namespace("\\\\.\\root\\TEST\\ms_409")

[Description("Localized version of MyClass for American English") :
    Amended, LOCALE(0x409)] 

class myclass
{
    [DisplayName("User Name") : Amended,
    Description("The Name property contains the name of the user") : 
    Amended, key]
     string Name;

    [DisplayName("Time Stamp") : Amended,
    Description("This property shows when the object was created") : 
    Amended] 
     uint64 Timestamp;
};
```

Compiling a MOF file with the [**Amended**](qualifier-flavors.md) qualifier only generates separate language-neutral and language-specific MOF files; the CIM repository is not updated with the new class information. You must use the MOF compiler to compile the two MOF files that the first compilation produced before any class information is available to WMI.

When you compile a master MOF file, only qualifiers with the [**Amended**](qualifier-flavors.md) flavor are moved to the language-specific MOF file. Qualifiers that do not have the **Amended** flavor are not localized and only exist in the basic class definition in the language-neutral MOF file. Nonlocalized qualifiers can be used for default descriptions if localized descriptions are not available.

You can use the [pragma amendment](pragma-amendment.md) command instead of specifying [**Amended**](qualifier-flavors.md) as a switch to the MOF compiler. Either of these options are equivalent to requesting language-specific and language-neutral versions of a MOF file. If you use either the pragma amendment command or the **Amended** command-line option, you must specify the name of the output files using the **-MFL** and **-MOF** options at the command prompt.

> [!Note]  
> The language-neutral MOF file that the MOF compiler generates contains the decimal equivalent of the locale ID, even if this value was entered in hexadecimal. In the example above, the compiler has converted the value 0x409 to the decimal number 1033 for the Lnmof.mof output file.

 

 

 



