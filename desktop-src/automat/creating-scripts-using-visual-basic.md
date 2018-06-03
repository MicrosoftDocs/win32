---
title: Creating Scripts Using Visual Basic
description: Visual Basic provides a complete programming environment for creating Windows applications with which you can manipulate the exposed ActiveX objects of other applications.
ms.assetid: 85ec41e1-0a71-4180-89cb-b97398d211e2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Scripts Using Visual Basic

Visual Basic provides a complete programming environment for creating Windows applications with which you can manipulate the exposed ActiveX objects of other applications. Internally, Visual Basic fully supports Automation dual interfaces.

For the syntax and semantics of the Automation features, see the Visual Basic Help file, Vb5.hlp. To see how the Visual Basic statements translate into ActiveX application programming interfaces (APIs), refer to [Information for Visual Basic Programmers](https://msdn.microsoft.com/windows/desktop/67307637-777A-47AE-A27C-0E681ACAC6E4).

> [!Note]  
> Automation does not require Visual Basic. It is presented here as an example of a programming tool that supports Automation and is convenient for packaging Automation scripts. Optionally, a different ActiveX client can be used for testing.

 

Exposed objects can be called directly from programs written with Visual Basic. The following figure shows how this was done for the sample program Hello.exe.

![](images/oa03-03.png)

### To access an exposed object

1.  Start Visual Basic. Initialization and release of OLE is handled automatically by Visual Basic.

2.  To select the type library of the object, click **Tools** on the **References** menu.

3.  Add code to declare a variable of the interface type. For example:

    ```C++
    Dim HelloObj As IHello
    ```

    

4.  Add code in event procedures to create an instance of the object and to manipulate the object using its properties and methods. For example:

    ```C++
    Sub Form_Load ( )
       Set HelloObj = New Hello.Hello
    End Sub
    Sub SetVisible_Click ( )
       HelloObj.Visible = True
    End Sub
    ```

    

5.  Click **Start** on the **Run** menu, and then trigger the event by clicking the form.

The following figure shows the interfaces you use when accessing exposed objects through Visual Basic.

 

 




