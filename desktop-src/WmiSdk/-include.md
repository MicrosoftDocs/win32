---
description: Includes the contents of one MOF file into another MOF file.
ms.assetid: 06765956-e4ee-467b-9b3b-d5da17b9cd82
ms.tgt_platform: multiple
title: '#include'
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# '#include'
/*   Title: MyMof.Mof                           */
/*   Title: MyMof2.Mof                               */

The \#include preprocessor command includes the contents of one MOF file into another MOF file. The following code example describes the syntax for the \#include command.

``` syntax
#include ("Moffile.mof")
```

In the previous example, Moffile.mof is the name of the MOF file to include.

The following example shows two MOF files. When you compile the first MOF file, the compiler automatically compiles the second MOF file (Mymof2.mof) in the location you place the \#include statement.

``` syntax
/*   Title: MyMof.Mof                           */
/*                                              */ 
/*   This MOF file shows how to include  */
/*   an MOF file in another MOF file             */

#pragma namespace("\\\\.\\root")            

#include ("mymof2.mof")

class myclass1 
{
    [key] string Description;
};


instance of myclass1
{
    Description = "Description of myclass1";
};
/*   End of MyMof.Mof                           */
```

The following MOF file is included in the previous example:

``` syntax
/*   Title: MyMof2.Mof                               */
/*                                                   */
/*   This MOF is included when MyMof.MOF is compiled */

class myclass2 
{
    [key] string Description;
};


instance of myclass2
{
    Description = "Description of myclass2";
    
};
```

## Related topics

<dl> <dt>

[Preprocessor Commands](preprocessor-commands.md)
</dt> </dl>

 

 



