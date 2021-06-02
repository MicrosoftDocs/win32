---
description: Creating localized class definitions is a three-step process.
ms.assetid: e303b894-07c4-44e3-9c57-58b1db16ae9a
ms.tgt_platform: multiple
title: Creating Localized Class Definitions
ms.topic: article
ms.date: 05/31/2018
---

# Creating Localized Class Definitions

Creating localized class definitions is a three-step process. You start by writing MOF code that defines the classes, including all qualifiers that must be localized. This original file is called the "master MOF" file because it contains all of the qualifiers and properties that define the class.

Next, use the [MOF compiler](mofcomp.md) to create the language-neutral and language-specific versions of the MOF file. The MOF compiler places the basic class description in a new MOF file and creates a localized version of the MOF file that contains only the properties and qualifiers that must be localized. Although the language-specific and language-neutral versions of the MOF file can have the same file name, you should use a .mfl file name extension to indicate that the file contains localized information. You can localize the .mfl file to other locales, if necessary. Storing the class definitions in the CIM repository requires an additional step of using the MOF compiler to compile both the language-neutral and the language-specific MOF files.

The following steps describe how to create and store a localized class definition.

**To create and store a localized class definition**

1.  Create the master MOF file that defines the classes that you want localized.

    Save this MOF code in a file called Mastermof.mof.

    ```syntax
    #pragma namespace("\\\\.\\root")

    instance of __Namespace
    {
        Name = "TEST" ;
    } ;

    #pragma namespace("\\\\.\\root\\TEST")

    [Description("Localized version of MyClass for American English") 
        : Amended, LOCALE(0x409)] 

    class myclass
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

2.  Create language-neutral and language-specific versions of the MOF file by compiling the MasterMOF.mof file.

    Type the following command at a command prompt to compile the MasterMOF.mof file.

    **mofcomp -MOF:Lnmof.mof -MFL:Lsmof.mfl -Amendment:MS\_409 Mastermof.mof**

3.  Compile the language-neutral (Lnmof.mof) and language-specific (Lsmof.mfl) files and store the class information in the CIM repository.

    Type the following commands at a command prompt to store the class information in the CIM repository.

    **Mofcomp Lnmof.mof**

    **Mofcomp Lsmof.mfl**

    After you compile these files, you will have a language-neutral class definition in the root\\test namespace and a localized class definition in the root\\test\\ms\_409 namespace. For more information about compiling localized MOF files, see [Compiling Localized MOF files](compiling-localized-mof-files.md).

 

 



