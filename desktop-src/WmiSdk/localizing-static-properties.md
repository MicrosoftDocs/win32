---
description: You can localize static properties by using partial value maps.
ms.assetid: 67e91454-c065-4ab2-a373-245c9392c71c
ms.tgt_platform: multiple
title: Localizing Static Properties
ms.topic: article
ms.date: 05/31/2018
---

# Localizing Static Properties

You can localize static properties by using partial value maps.

The following procedure describes how static properties can be localized using partial value maps with regular expressions.

**To use value maps to localize static properties**

1.  Create a master MOF file (Mastervm.mof).

    The following code example can be used to create a master MOF file (Mastervm.mof).

    ```syntax
    [Locale(0x409)]
    class Group1
    {
        [key] string ID;
        [DisplayName("Numbers"),
            ValueMap{0,1,2,3}:amended,
            Values{"Zero", "One", "Two", "Three"}:amended]
        Uint32 Numbers;
    };
    ```

2.  Create the language-neutral and language-specific versions of the MOF file.

    Type the following command at a command prompt to create the language-neutral and language-specific versions of the MOF file.

    ```syntax
    mofcomp -MOF:LnVm.mof -MFL:LsVm.mfl -Amendment:MS_409 MasterVm.mof
    ```

    The MOF compiler generates the language-specific and language-neutral MOF files, LnVm.mof and LsVm.mfl. The American English values for the [Numbers](numbers.md) property is placed in the .mfl file for the American English namespace.

    The following code example shows the contents of the LsVm.mfl file.

    ```syntax
    #pragma namespace("\\\\.\\root\\default")
    instance of __namespace{ name="ms_409";};
    #pragma namespace("\\\\.\\root\\default\\ms_409")

    [AMENDMENT, LOCALE(0x409)] 
    class Group1
    {
      [ValueMap{0, 1, 2, 3} : Amended,
          Values{"Zero", "One", "Two", "Three"} : Amended] 
      Uint32 Numbers;
    };
    ```

3.  Compile the two MOF files and store the class information in the CIM repository.

    Type the following command at a command prompt to compile the two MOF files.

    ```syntax
    Mofcomp LnVm.mof 
    Mofcomp LsVm.mfl
    ```

4.  Localize the MFL file for other locales.

    The following code example shows the contents of an MFL file for the French namespace.

    ```syntax
    #pragma namespace("\\\\.\\root\\default")
    instance of __namespace{ name="ms_40C";};
    #pragma namespace("\\\\.\\root\\default\\ms_40C")

    [AMENDMENT, LOCALE(0x40C)] 
    class Group1
    {
        [key] string ID;
        [ValueMap{0, 1, 2, 3} : Amended,
            Values{"Zero", "Un", "Deux", "Trois"} : Amended]
        Uint32 Numbers;
    };
    ```

The net result is that both the display name and the value of the [Numbers](numbers.md) property depend on the locale of the logged-on user. If the user specifies a locale that has not been provided, the default qualifier data comes from the English (ms\_409) namespace.

The implication of this design is that each string value is used as a lookup identifier, which cannot be localized. When defining this scheme, you must ensure that the value the provider puts in is locale-independent.

> [!Note]  
> WMI does not currently provide run-time support for mapping values to strings defined by qualifiers. Interpretation of the suggested syntax is the application's responsibility.

 

 

 



