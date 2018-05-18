---
Description: 'To start using administration Component Object Model (COM) objects, you first have to set up your development environment. You should install the fax service before beginning to use the administration objects.'
ms.assetid: 'dca56180-4309-4c45-9ffd-d6fad7a5f71f'
title: Setting up the Development Environment
---

# Setting up the Development Environment

To start using administration Component Object Model (COM) objects, you first have to set up your development environment. You should install the fax service before beginning to use the administration objects.

## To start using administration objects with C++

1.  Include the file Fxscomex.dll by using the following line of code:

    ```
    #import "fxscomex.dll"
    ```

    

    The file Fxscomex.dll contains the definitions of the fax service extended COM objects.

2.  Create a root object as described in [Creating the Root Object](-mfax-creating-the-root-object.md).
3.  Write your program.
4.  To apply your changes, you may have to call the **Save** method as described in [Saving and Refreshing Objects](-mfax-saving-and-refreshing-objects.md).

For more information about C++ programming for the fax service using the [\#import](http://msdn.microsoft.com/library/en-us/vclang/html/_predir_The_.23.import_Directive.asp) directive, see [Fax Extended COM Visual C++ Programming](-mfax-fax-extended-com-visual-c-programming.md).

## To start using administration objects with Visual Basic

1.  Start Microsoft Visual Basic and open (for example) a new **Standard EXE** project.
2.  On the **Project** menu, click **References**.
3.  Select **Microsoft Fax Service Extended COM Type Library** from the dialog box that appears. This library is defined in Fxscomex.dll, which is a file included with the fax service. Therefore, you need to have the fax service installed for access to this library. This will make all the administration COM objects available to you.
4.  Create a root object as described in [Creating the Root Object](-mfax-creating-the-root-object.md).
5.  Write your program. See [Monitoring Fax Activity](-mfax-monitoring-fax-activity.md) for an introductory example.
6.  To apply your changes, you may have to call the **Save** method as described in [Saving and Refreshing Objects](-mfax-saving-and-refreshing-objects.md).

If you are using Microsoft Visual Basic Scripting Edition (VBScript), and would like to use enumerations, see [Using Enumerations in Scripts](-mfax-using-enumerations-in-scripts.md).

> [!Note]  
> Many of the examples in this section are written in Visual Basic, but you can use any language to script with the administration objects. If, for example, you script with VBScript, you can use any text editor to create the scripts.

 

 

 



